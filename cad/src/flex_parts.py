# SPDX-License-Identifier: CERN-OHL-P-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""Flex panel and connector platform parts (FXP-PLT-001, docs/platform/flex-platform.md).

Shared CAD helpers for FlexClean, FlexSleep and FlexTriage. Each product's cad/src/model.py imports this
file; the copy is identical in the three repos (STANDARDS section 25.8). Licence: CERN-OHL-P-2.0 (hardware
source), Design Molecule Labs with Helpful Engineering. CONCEPT, NOT FOR FABRICATION.

Conventions follow .kit/cad_parts.py: millimetres, parts built along +Z from the floor, real sheet
thicknesses, score grooves and edge breaks as real cuts, connectors as solids, placement with `at()`.
The kit library is build123d, so every helper returns a build123d Part (the same OCCT shape a CadQuery
Workplane wraps). `as_workplane(shape)` wraps one in a cadquery.Workplane when CadQuery is installed
(it is not in the kit's requirements; see FXP-PLT-001 decision D9).

The corrugated twinwall is modelled as a solid sheet with its score grooves, connector holes and sealed
edges; flutes are not modelled, their direction is carried in `panel_info()` and in the part note. A whole
bay of 12 P18 duos, 40 clips and 8 feet exports well under the 45 MB STEP limit (see the self-test below).

    import sys; sys.path.insert(0, ".kit"); sys.path.insert(0, "cad/src")
    from cad_parts import at
    from flex_parts import panel, clip, foot, print_zone, flex_part, clip_heights

    duo = panel(1200, 1800, scores=[600])                  # P18 duo, one fold groove at mid-width
    parts = [flex_part("Panel P18 (duo)", duo, "sheet", width=1200, height=1800)]
    for z in clip_heights(1800):
        parts.append(flex_part("Clip, corner", at(clip("corner"), (1200, 0, z)), "clip"))
"""
from __future__ import annotations

import math
from build123d import (Axis, Box, Cylinder, Pos, Rot, Part, Compound, Polygon, extrude, chamfer, fillet)

# ---------------------------------------------------------------------------------------------------------
# Platform constants (FXP-PLT-001 sections 2 to 5). Change them there first, then here.
# ---------------------------------------------------------------------------------------------------------
SHEET = {                         # grade: thickness mm, grammage g/m2, flute pitch mm (pitch assumed, to assess)
    "FXP-S4FR": dict(t=4.0, gsm=700, pitch=3.4, note="platform grade: 4 mm FR twinwall, max 700 g/m2 (NFPA 701 TM1 scope)"),
    "FXP-S4":   dict(t=4.0, gsm=750, pitch=3.4, note="4 mm standard twinwall (prototype boards only, not FR)"),
    "FXP-S5":   dict(t=5.0, gsm=1000, pitch=5.0, note="5 mm twinwall (option, FR availability to assess)"),
    "FXP-S10":  dict(t=10.0, gsm=2000, pitch=10.0, note="10 mm twinwall (option, FR availability to assess)"),
}
GRADE = "FXP-S4FR"
LEAF = 600.0                      # standard leaf width between vertical folds or joints
HEIGHTS = {"P12": 1200.0, "P18": 1800.0, "H06": 600.0}
GROOVE_PITCHES = 4                # fold groove width in flute pitches: flat-bottomed, 13.6 mm (rule F3, FXP-PLT-001 section 3)
SKIN = 0.26                       # skin thickness of the 4 mm FR grade, mm (platform_check.py estimate)
EDGE_SEAL = 2.0                   # sealed edge taper, mm each face (edge break)
HOLE_D = 8.0                      # hot-punched clip hole
HOLE_E = 12.5                     # hole centre from the panel edge
CLIP_H = 100.0                    # clip height along the joint
SLOT_DEPTH = 40.0                 # how far a panel edge enters a clip slot
TONGUE_T = 1.5                    # snap tongue thickness at the root (tapered, Bayer type 2)
TONGUE_T_TIP = 0.75               # snap tongue thickness at the free end
TONGUE_W = 14.0                   # snap tongue width
WALL = 2.5                        # clip slot wall
CLEAR = 0.5                       # slot clearance over the nominal sheet thickness (sheet +-5 %: 3.8 to 4.2 mm)
PEG_D = 7.0                       # through-peg diameter (1 mm under the hole)
SOCKET = 1.0                      # peg tip depth into the socket in the back slot wall (through-peg, fix F8)
CORE = 12.0                       # clip core block (square)
FOOT_SEAT = 10.5                  # panel bottom edge height when seated in a foot slot
PEG_DZ = 25.0                     # two snap tongues and pegs per slot, at z = +-PEG_DZ from the clip centre


def clip_heights(height: float) -> list[float]:
    """Clip centre heights for a vertical joint of a panel 'height' tall, on one shared grid so that P12 and
    P18 panels can share a joint (platform request 5): 150 mm and height - 150 mm always, plus 1050 mm on
    panels taller than 1200 mm. P12: 150, 1050. P18: 150, 1050, 1650. H06: 150, 450."""
    zs = [150.0, height - 150.0]
    if height > 1250:
        zs.insert(1, 1050.0)
    return [round(z, 1) for z in zs]


def _groove_w(grade: str = GRADE) -> float:
    return GROOVE_PITCHES * SHEET[grade]["pitch"]


# ---------------------------------------------------------------------------------------------------------
# Panel
# ---------------------------------------------------------------------------------------------------------
def panel(width: float, height: float, thickness: float | None = None, flute: str = "vertical", scores=(),
          grade: str = GRADE, holes: bool = True, edge: float = EDGE_SEAL, hole_edges=("left", "right")) -> Part:
    """A twinwall panel in the XZ plane: x 0..width, z 0..height, faces at y = 0 (print face) and y = t.

    scores: positions of fold lines. With flute="vertical" (the platform rule) a number is a vertical fold at
    that x, cut as a flat-bottomed groove (GROOVE_PITCHES flute pitches wide) through the back skin and ribs
    on the back face (y = t side), leaving the front skin as the hinge: it folds to 180 deg towards the back
    face for packing and to +-90 deg either way in use (rule F3). A tuple
    ("h", z) adds a horizontal crush score across the flutes at height z (both faces, shallow). Holes are the
    hot-punched clip holes on the chosen vertical edges at clip_heights(height). Edges carry the sealed-edge
    taper (an edge break)."""
    t = thickness or SHEET[grade]["t"]
    if flute not in ("vertical", "horizontal"):
        raise ValueError("flute must be 'vertical' or 'horizontal'")
    body = Pos(width / 2, t / 2, height / 2) * Box(width, t, height)
    if edge:
        try:   # sealed edge: chamfer the eight long edges of the thickness (the perimeter of both faces)
            body = chamfer(body.edges().filter_by(lambda e: e.length > 3 * t), min(edge, t / 2 - 0.2))
        except Exception:
            pass
    ts = SKIN if grade.startswith("FXP-S4") else SHEET[grade]["t"] * 0.07
    for s in scores:
        if isinstance(s, (tuple, list)) and s[0] == "h":
            z = float(s[1])   # crush score across the flutes: two shallow grooves
            for y0 in (0.0, t):
                g = Pos(width / 2, y0, z) * Rot(0, 90, 0) * Cylinder(t * 0.35, width + 2)
                body = body - g
            continue
        x = float(s)
        wg = _groove_w(grade)
        depth = t - ts
        # flat-bottomed groove along Z, opening on the back face (y = t), floor on the front skin (y = ts)
        body = body - Pos(x, ts + (t - ts + 0.5) / 2, height / 2) * Box(wg, t - ts + 0.5, height + 2)
    if holes:
        xs = []
        if "left" in hole_edges:
            xs.append(HOLE_E)
        if "right" in hole_edges:
            xs.append(width - HOLE_E)
        for x in xs:
            for z in clip_heights(height):
                for dz in (-PEG_DZ, PEG_DZ):
                    body = body - Pos(x, t / 2, z + dz) * Rot(90, 0, 0) * Cylinder(HOLE_D / 2, t + 2)
    return body


def panel_info(width: float, height: float, grade: str = GRADE, flute: str = "vertical") -> dict:
    """Mass and flute data for a panel (the solid CAD sheet overstates mass; use this instead)."""
    g = SHEET[grade]
    area = width * height * 1e-6
    return dict(grade=grade, flute=flute, thickness=g["t"], gsm=g["gsm"], area_m2=round(area, 3),
                mass_kg=round(area * g["gsm"] / 1000, 3), note=g["note"])


# ---------------------------------------------------------------------------------------------------------
# Clip-lock connector family (FXP-PLT-001 section 5)
# ---------------------------------------------------------------------------------------------------------
_DIRS = {"inline": (0, 180), "corner": (0, 90), "tee": (0, 90, 180), "angle": (0, 150)}


def _arm(t: float, detail: str = "full") -> Part:
    """One slot arm along +X from the core face: two walls with a gap t + CLEAR. The front wall carries a
    pair of tapered cantilever snap tongues (TONGUE_T at the root, TONGUE_T_TIP at the free end, at
    z = +-PEG_DZ, rooted 3 mm inside the slot mouth, free end towards the core) in windows. Each tongue
    carries a through-peg: round (PEG_D), with a 45 deg ramp on the mouth side over its whole height so the
    panel edge cams it out, and a straight retaining face on the core side. Home, the peg passes through both
    skins into a SOCKET-deep pocket in the back wall (fix F8). A pull lip on the outside releases it.
    detail="light" keeps the walls, the stop and plain round pegs (no tongues, windows, ramps or lips) for
    bay-level assemblies, where it cuts the STEP size of a clip by about 2.7 times; the outer envelope and
    the peg positions are the same."""
    gap = t + CLEAR
    L = SLOT_DEPTH
    x0, mouth = CORE / 2, CORE / 2 + SLOT_DEPTH
    y0 = -gap / 2                                   # slot face of the front wall
    w_front = Pos(x0 + L / 2, y0 - WALL / 2, 0) * Box(L, WALL, CLIP_H)
    w_back = Pos(x0 + L / 2, gap / 2 + WALL / 2, 0) * Box(L, WALL, CLIP_H)
    stop = Pos(x0 / 2, 0, 0) * Box(x0, gap + 2 * WALL, CLIP_H)   # root block up to the core face (panel stop; joins the arm at any angle)
    arm = w_front + w_back + stop
    xp = x0 + HOLE_E                                # peg on the hole centre when the panel edge meets the core
    root = mouth - 3.0                              # tongue root, 3 mm inside the mouth
    xa = xp - 5.0                                   # tongue free end
    h = gap + SOCKET                                # peg height: through both skins into the socket
    if detail == "light":
        for dz in (-PEG_DZ, PEG_DZ):
            arm = arm + Pos(xp, 0, dz) * Rot(90, 0, 0) * Cylinder(PEG_D / 2, gap + 0.2)
        return arm
    extra = []
    for dz in (-PEG_DZ, PEG_DZ):
        arm = arm - Pos((xa - 1.0 + root) / 2, y0 - WALL / 2, dz) * Box(root - xa + 1.0, WALL + 1, TONGUE_W + 2.4)
        arm = arm - Pos(xp, gap / 2 + (SOCKET + 0.2) / 2, dz) * Box(PEG_D + 1.4, SOCKET + 0.2, PEG_D + 1.4)
        tprof = Polygon((xa, y0), (root + 1.0, y0), (root + 1.0, y0 - TONGUE_T), (xa, y0 - TONGUE_T_TIP), align=None)
        tongue = extrude(tprof, TONGUE_W)
        tongue = Pos(0, 0, dz - tongue.bounding_box().center().Z) * tongue   # centre on dz whatever the winding
        run = h                                     # 45 deg ramp
        wedge = Polygon((xp - PEG_D / 2 - 0.5, y0), (xp + PEG_D / 2, y0), (xp + PEG_D / 2 - run, y0 + h),
                        (xp - PEG_D / 2 - 0.5, y0 + h), align=None)
        wedge = extrude(wedge, PEG_D + 2)
        wedge = Pos(0, 0, dz - wedge.bounding_box().center().Z) * wedge
        cyl = Pos(xp, y0 + h / 2, dz) * Rot(90, 0, 0) * Cylinder(PEG_D / 2, h)
        peg = Pos(0, -0.3, 0) * (wedge & cyl)          # sunk 0.3 mm into the tongue so the two fuse
        lip = Pos(xa + 2.0, y0 - TONGUE_T_TIP - 1.1, dz) * Box(4.0, 3.0, TONGUE_W - 2)   # 0.4 mm into the tongue
        extra.append((tongue + peg) + lip)
    for e in extra:
        arm = arm + e
    return arm


def snap_arm_length() -> float:
    """Free length of the snap tongue from its root to the peg (used by platform_check.py)."""
    return (CORE / 2 + SLOT_DEPTH - 3.0) - (CORE / 2 + HOLE_E)


def clip(kind: str = "inline", thickness: float | None = None, grade: str = GRADE, angle: float = 150.0,
         detail: str = "full") -> Part:
    """Clip-lock connector, centred on the joint line (the Z axis), z from -CLIP_H/2 to +CLIP_H/2.
    kind: 'inline' (slots at 0 and 180 deg), 'corner' (0 and 90 deg), 'tee' (0, 90 and 180 deg) or 'angle'
    (0 and `angle` deg, default 150: the 30 deg zigzag joint that counts as a supported edge under rule S1).
    detail: "full" (every snap feature, for part STEP files and drawings) or "light" (bay assemblies).
    Slot k points along angle a: a panel edge slides in from that direction until it meets the core, and its
    hole meets the peg. The slot is centred on the panel mid-plane: place a panel() at y = -t/2 (rotated
    about Z by the slot angle) so its edge sits in the slot."""
    if kind not in _DIRS:
        raise ValueError(f"kind must be one of {tuple(_DIRS)}")
    t = thickness or SHEET[grade]["t"]
    core = Box(CORE, CORE, CLIP_H)
    try:
        core = fillet(core.edges().filter_by(Axis.Z), 2.0)
    except Exception:
        pass
    body = core
    dirs = (0, angle) if kind == "angle" else _DIRS[kind]
    for a in dirs:
        body = body + Rot(0, 0, a) * _arm(t, detail)
    try:
        body = chamfer(body.edges().filter_by(Axis.Z).filter_by(lambda e: e.length > CLIP_H - 1), 0.5)
    except Exception:
        pass
    return body


FOOT_KINDS = {   # kind: (slot directions, outrigger directions), degrees about Z; outriggers avoid every slot
    "inline": ((0, 180), (90, 270)),
    "corner": ((0, 90), (45, 225)),
    "junction": ((0, 90, 180), (270,)),
    "cross": ((0, 90, 180, 270), (45, 135, 225, 315)),
}


def foot(kind: str = "inline", length: float = 600.0, thickness: float | None = None, grade: str = GRADE) -> Compound:
    """Standard foot: a moulded foot block with upward panel slots and outrigger beams folded from twinwall
    offcut (equilateral triangle section, 50 mm sides, apex up, on the floor) reaching length/2 from the joint
    line. Kinds (FOOT_KINDS): 'inline' (slots 0 and 180 deg, outriggers 90 and 270), 'corner' (slots 0 and 90,
    outriggers 45 and 225), 'junction' for tee joints (slots 0, 90, 180, outrigger 270) and 'cross' (four slots,
    diagonal outriggers). 'tee' is the v0.1 name of 'inline' and still works. Floor at z = 0; nothing goes
    below it. The joint line is the Z axis; a panel stands in a slot with its bottom edge at z = FOOT_SEAT
    (10.5 mm), centred on its slot line. Non-slip pads under the block are to assess (D17)."""
    kind = {"tee": "inline"}.get(kind, kind)
    if kind not in FOOT_KINDS:
        raise ValueError(f"kind must be one of {tuple(FOOT_KINDS)} (or 'tee')")
    slots, rigs = FOOT_KINDS[kind]
    t = thickness or SHEET[grade]["t"]
    gap = t + CLEAR
    hx, hy = (60.0, 35.0) if kind == "inline" else (60.0, 60.0)
    blk = Pos(0, 0, 20) * Box(2 * hx, 2 * hy, 40)
    try:
        blk = chamfer(blk.edges().filter_by(Axis.Z), 4.0)
    except Exception:
        pass
    for a in slots:
        blk = blk - Rot(0, 0, a) * Pos((hx + 4 - gap / 2) / 2 + gap / 4, 0, FOOT_SEAT + 15) * Box(hx + 4 + gap / 2, gap, 30)
    side = 50.0
    tri_h = side * math.sqrt(3) / 2
    beams = []
    for a in rigs:
        ca, sa = abs(math.cos(math.radians(a))), abs(math.sin(math.radians(a)))
        r0 = min(hx / ca if ca > 1e-6 else 1e9, hy / sa if sa > 1e-6 else 1e9) - 6.0
        L = max(length / 2 - r0, 50.0)
        outer = extrude(Polygon((-side / 2, 0), (side / 2, 0), (0, tri_h), align=None), L)
        inner = Pos(0, 0, -1) * extrude(Polygon((-side / 2 + 1.5, 0.9), (side / 2 - 1.5, 0.9), (0, tri_h - 1.7), align=None), L + 2)
        beam = Rot(90, 0, 0) * (outer - inner)          # apex up (+Z), running along -Y
        beam = Rot(0, 0, a - 270) * Pos(0, -r0, 0) * beam
        beams.append(beam)
    return Compound([blk] + beams)


def outrigger_flat(length: float = 600.0) -> tuple[float, float]:
    """Flat blank (width, length) of the folded outrigger: three 50 mm faces plus a 20 mm glue-free lap."""
    return 3 * 50.0 + 20.0, length


# ---------------------------------------------------------------------------------------------------------
# Print zones and part dicts
# ---------------------------------------------------------------------------------------------------------
SAFETY = {   # ISO 3864-4 safety colours as RAL references (FXP-PLT-001 section 11)
    "red": "#9B2423", "yellow": "#F9A900", "blue": "#005387", "green": "#237F52", "white": "#ECECE7", "black": "#2B2B2C",
}


def print_zone(width: float, height: float, x0: float = 0.0, z0: float = 0.0, depth: float = 0.15) -> Part:
    """A thin solid standing for a printed or laminated area on a panel's print face (y = 0), drawn just
    proud of it (y from -depth to 0) with a broken edge so it reads as a film, not a block."""
    z = Pos(x0 + width / 2, -depth / 2, z0 + height / 2) * Box(width, depth, height)
    try:
        z = chamfer(z.edges().filter_by(Axis.Y), min(2.0, width / 4, height / 4))
    except Exception:
        pass
    return z


def flex_part(name: str, shape, role: str, width: float = 0, height: float = 0, color: str | None = None,
              bom: int | None = None, group: str = "shell", explode=(0, 0, 0), grade: str = GRADE) -> dict:
    """A cad_parts.part() dict for a platform part. role: 'sheet' (twinwall panel or outrigger), 'clip'
    (connector or foot block, PETG prototype or moulded PP), or 'print' (printed zone)."""
    import sys
    from pathlib import Path
    kit = Path(__file__).resolve().parents[2] / ".kit"
    if str(kit) not in sys.path:
        sys.path.insert(0, str(kit))
    from cad_parts import part
    if role == "sheet":
        info = panel_info(width, height, grade) if width and height else {"note": SHEET[grade]["note"]}
        note = f"{SHEET[grade]['note']}; flutes vertical; mass {info.get('mass_kg', '-')} kg (gsm basis)"
        return part(name, shape, "hdpe_natural", kind="made", bom=bom, group=group, explode=explode,
                    color=color or "#E9ECEA", note=note)
    if role == "clip":
        return part(name, shape, "hdpe_black", kind="made", bom=bom, group=group, explode=explode,
                    color=color or "#2E3A40", note="clip-lock connector: PETG print (prototype), moulded PP (scale)")
    if role == "print":
        return part(name, shape, "label", kind="made", bom=bom, group=group, explode=explode,
                    color=color or SAFETY["green"], note="printed zone: UV-cured ink under clear overlaminate (to assess)")
    raise ValueError("role must be 'sheet', 'clip' or 'print'")


def as_workplane(shape):
    """Wrap a part in a cadquery.Workplane if CadQuery is installed (optional)."""
    import cadquery as cq   # noqa: not a kit requirement
    return cq.Workplane("XY").add(cq.Shape.cast(shape.wrapped))


def test_bay():
    """A U bay for the self-test: back wall and two returns of P18 duos (flat), corner clips at the shared
    heights, corner feet at the corners and inline feet at the free ends. Returns [(name, shape)]."""
    t = SHEET[GRADE]["t"]
    W = 1200.0
    z0 = FOOT_SEAT
    duo = panel(W, 1800, scores=[600])
    xr = CORE + W                                    # right corner joint line
    items = [("back wall", Pos(CORE / 2, -t / 2, z0) * duo),
             ("left return", Rot(0, 0, 90) * Pos(CORE / 2, -t / 2, z0) * duo),
             ("right return", Pos(xr, 0, 0) * Rot(0, 0, 90) * Pos(CORE / 2, -t / 2, z0) * duo)]
    for i, z in enumerate(clip_heights(1800)):
        d = "full" if i == 0 else "light"
        items.append((f"clip L {d}", Pos(0, 0, z0 + z) * clip("corner", detail=d)))
        items.append((f"clip R {d}", Pos(xr, 0, z0 + z) * Rot(0, 0, 90) * clip("corner", detail=d)))
    items += [("foot L", foot("corner")), ("foot R", Pos(xr, 0, 0) * Rot(0, 0, 90) * foot("corner")),
              ("foot end L", Pos(0, CORE / 2 + W, 0) * Rot(0, 0, 90) * foot("inline")),
              ("foot end R", Pos(xr, CORE / 2 + W, 0) * Rot(0, 0, 90) * foot("inline"))]
    return items


if __name__ == "__main__":
    # Self-test: build every part kind, check the floor plane and interference in a U bay, export STEP
    import sys, os, time
    from build123d import export_step
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/flex_parts_test.step"
    t0 = time.time()
    solo = {f"clip {k}": clip(k) for k in ("inline", "corner", "tee", "angle")}
    solo.update({f"foot {k}": foot(k) for k in FOOT_KINDS})
    solo["panel P18 duo"] = panel(1200, 1800, scores=[600])
    solo["panel P12 duo"] = panel(1200, 1200, scores=[600])
    solo["strip H06"] = panel(1200, 600)
    solo["print zone"] = print_zone(400, 300)
    for n, sh in solo.items():
        ok = all(sol.is_valid for sol in sh.solids())
        print(f"{n:16s} valid {ok}  solids {len(sh.solids())}  zmin {sh.bounding_box().min.Z:7.2f}")
    for k in FOOT_KINDS:
        assert foot(k).bounding_box().min.Z > -1e-6, f"foot {k} goes below the floor"
    bay = test_bay()
    zmin = min(sh.bounding_box().min.Z for _, sh in bay)
    hits = []
    for i in range(len(bay)):
        for j in range(i + 1, len(bay)):
            ni, nj = bay[i][0], bay[j][0]
            if ni.split()[0] == nj.split()[0] and ni.split()[0] != "back":
                if ni.startswith(("clip", "foot")) and nj.startswith(("clip", "foot")):
                    continue
            v = (bay[i][1] & bay[j][1]).volume
            if v > 1.0:
                hits.append((ni, nj, round(v, 1)))
    print(f"bay: {len(bay)} parts, lowest point z = {zmin:.2f} mm, interferences over 1 mm3: {hits or 'none'}")
    shared = sorted(set(clip_heights(1200)) & set(clip_heights(1800)))
    print(f"clip heights P12 {clip_heights(1200)}, P18 {clip_heights(1800)}, shared {shared}")
    big = [Pos(i * 1400, 4000, 0) * solo["panel P18 duo"] for i in range(12)]
    big += [Pos(i * 60, 6000, 900) * clip("tee", detail="light") for i in range(40)]
    big += [Pos(i * 300, 7000, 0) * solo["foot cross"] for i in range(8)]
    export_step(Compound([sh for _, sh in bay] + big), out)
    print(f"STEP {out}: {os.path.getsize(out) / 1e6:.2f} MB (U bay plus 12 duos, 40 light tee clips, 8 cross feet) in {time.time() - t0:.1f} s")
