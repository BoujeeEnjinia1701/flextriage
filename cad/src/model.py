# SPDX-License-Identifier: CERN-OHL-P-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""FlexTriage Origami Bay. Parametric model (kit 1.9 interface, STANDARDS section 24), detail level D3.

Run from the repo root:  python .kit/cad_check.py --export
Every main dimension is in PARAMS; docs/04-calcs/sizing.py (FXT-CAL-001) and stem_check.py (FXT-STM-001) read it.
FT1 is built from the shared Flex platform parts in cad/src/flex_parts.py (FXP-PLT-001); that file is not edited here.

Units mm. Z up, floor at z = 0. x runs along the patient flow (entry at x = 0), y across the bay.

Options (FXT-OPT-001; the recommendation is proposed, awaiting Amish):
  FT1  Origami panel bay (team concept, iteration 2): a serpentine three-zone bay of FXP-S4FR P12 duo panels
       (1,200 mm high) joined by the platform clip-lock family (FXP-PLT-001 v0.2), standing in feet on rubber pads.
       Walls and stubs are zigzags (leaves at +-15 deg, 30 deg folds and angle clips, rule S1). Two long walls carry
       four stubs that leave a doorway at alternate sides, so patients move one way: entry, 1 intake, 2 assessment,
       3 treatment, exit. Each doorway has one leaf on pin hinges that closes on a magnetic catch. Printed zone signs
       on the panel faces.
  FT2  Tensioned fabric screen bay: the same plan drawn with flame-retardant (FR) PVC-coated polyester screens,
       1.8 m high, laced between aluminium posts on ballasted base plates, with 2.1 m door posts and headers
       carrying split magnetic curtains.
  FT3  Floor marking and retractable-belt stanchions: the same plan marked on the floor with vinyl tape and
       bounded by belt stanchions at 0.97 m; doorways are unhooked belts; zone signs on the posts.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from build123d import Box, Compound, Cylinder, Location, Plane, Polygon, Pos, Rot, chamfer, extrude, fillet, Axis

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]
import cad_parts as cp  # noqa: E402
from cad_parts import part  # noqa: E402
import flex_parts as fx  # noqa: E402

TITLE = "FlexTriage Origami Bay"
OPTIONS = {"FT1": "Origami panel bay (FR twinwall, clip-lock)", "FT2": "Tensioned fabric screens on a pole frame",
           "FT3": "Floor marking and belt stanchions"}
PRINCIPLES = {
    "FT1": "Pre-scored FR polypropylene duo panels clip into a serpentine three-zone bay; the plan shape and "
           "ballasted feet give stability, printed faces carry the zone cues, flap leaves close each doorway.",
    "FT2": "FR coated fabric is tensioned between ballasted aluminium posts; the light fabric allows 1.8 m "
           "screens and 2.1 m door headers with split magnetic curtains, at the cost of more parts to erect.",
    "FT3": "Coloured floor tape marks the zones and the path; retractable belts at 0.97 m between weighted "
           "posts bound the cohorts. Fast and durable, but no screen and no privacy.",
}
CHOSEN = "FT1"   # carried to the drawing, BOM and build plan. Proposed, awaiting Amish (FXT-DEC-001 D1); not decided
OPTION_VIEWS = {
    "FT1": dict(el=30, az=-35, scale="person", keep_context=True, ground_z=0.0),
    "FT2": dict(el=30, az=-35, scale="person", keep_context=True, ground_z=0.0),
    "FT3": dict(el=30, az=-35, scale="person", keep_context=True, ground_z=0.0),
}
# Pins pass through the bores of the hinge cores by design; the split pins sit under them.
ALLOWED_CONTACTS = [("pin", "(hinge)"), ("pin", "pin")]   # pins run in the 6.5 mm bores of the hinge cores

T = fx.SHEET[fx.GRADE]["t"]                    # 4 mm FXP-S4FR
ZIG = 15.0                                     # zigzag: leaves alternate 15 deg either side of the wall line (FXP-PLT-001 v0.2 rule S1)
PITCH = (1200.0 + fx.CORE) * math.cos(math.radians(ZIG))   # joint to joint along a wall: one folded duo plus the clip core, 1,170.7 mm
PARAMS = {
    # platform (FXP-PLT-001), read, not changed
    "GRADE": fx.GRADE, "SHEET_T": T, "GSM": fx.SHEET[fx.GRADE]["gsm"], "DUO_W": 1200.0, "LEAF": fx.LEAF,
    "CORE": fx.CORE, "CLIP_H": fx.CLIP_H, "FOOT_SEAT": fx.FOOT_SEAT, "OUTRIGGER": 600.0,
    "PAD": 2.0,                                 # EPDM non-slip pad under every foot, jamb foot and shoe (FXT-DEC-001 F5)
    # FT1 plan: a serpentine bay, 7 pitches long and 2 pitches wide
    "H_WALL": 1200.0,                           # P12 duo, zigzag (proposed; P18 is the alternative, FXT-DEC-001 D3)
    "ZIG": ZIG, "PITCH": PITCH, "N_X": 7, "N_Y": 2,
    "ZONES": (("1 Intake", 0, 2), ("2 Assessment", 2, 4), ("3 Treatment", 4, 7)),   # zone name, from and to joint index
    "DIVIDERS": ((2, "B"), (4, "A")),           # joint index, wall the stub hangs from (doorway at the other wall)
    "DOOR_CLEAR": PITCH - fx.CORE,              # axis to axis less the cores, before feet and flaps
    # flap leaves (doorways), pin hinges and magnetic catch
    "FLAP_W": PITCH - fx.CORE - 10.0, "FLAP_H": 990.0, "FLAP_Z": 114.1, "FLAP_GAP": 10.0,   # one leaf per doorway (F3)
    "CATCH_Z": 114.1 + 840.0,
    "PIN_D": 6.0, "BORE_D": 6.5, "MAGNET": (12.7, 3.17), "COVER": 2.0,   # 2 mm cover plus 0.5 mm air sets the catch force (S11)
    # ballast (site-filled sand bags, 25 lb class, not carried filled)
    "BAG": (330.0, 250.0, 65.0), "BAG_KG": 5.0,
    # FT2: tensioned fabric screens on posts
    "FT2_SCREEN_H": 1900.0, "FT2_DOOR_H": 2100.0, "FT2_POST": (38.0, 1.5), "FT2_RAIL": (25.0, 1.5),
    "FT2_BASE": (300.0, 300.0, 6.0), "FT2_FABRIC_T": 0.6,
    # FT3: belt stanchions and floor tape
    "FT3_POST": (63.5, 1.2, 970.0), "FT3_BASE_D": 355.0, "FT3_BELT": (50.0, 1.0, 920.0), "FT3_TAPE_W": 50.8,
}
P = PARAMS
H = P["H_WALL"]
Y_B = P["N_Y"] * PITCH                          # wall B joint line
Y_T = PITCH                                     # stub terminals
X_END = P["N_X"] * PITCH
Z0 = fx.FOOT_SEAT + P["PAD"]                    # panel bottom edge, seated in a foot or shoe on its 2 mm pad
ZC = [Z0 + z for z in fx.clip_heights(H)]       # clip centres: 160.5 and 1060.5

C_SHEET, C_CLIP, C_FOOT, C_PIN, C_BAG = "#ECEDE8", "#2E3A40", "#2E3A40", "#C9CDD1", "#B8AD8F"
C_INK, C_WHITE = fx.SAFETY["black"], fx.SAFETY["white"]


def _p(name, shape, mat, kind="made", bom=None, explode=(0, 0, 0), color=None, group="shell", note=""):
    return part(name, shape, mat, kind=kind, bom=bom, group=group, explode=explode, color=color, note=note)


def jxy(i, wall):
    """Joint i on wall A (y = 0), wall B (y = Y_B) or a stub terminal (y = Y_T)."""
    return (i * PITCH, {"A": 0.0, "B": Y_B, "T": Y_T}[wall])


def place(xy, heading, z=Z0):
    """Location of a panel that leaves the joint at xy along 'heading' (deg): print face on the right."""
    return Pos(xy[0], xy[1], z) * Rot(0, 0, heading) * Pos(fx.CORE / 2, -T / 2, 0)


# ---------------------------------------------------------------------------------------------------------
# FT1: shapes built once and placed as moved copies
# ---------------------------------------------------------------------------------------------------------
_CACHE = {}


def _once(key, fn):
    if key not in _CACHE:
        _CACHE[key] = fn()
    return _CACHE[key]


def duo(turn=0.0, detail="full"):
    """P12 duo in the platform panel frame (x 0..1,200, print face y = 0, back face y = T), folded at its 13.6 mm
    groove (x = 600) by 'turn' deg about the panel mid-plane: + turns the second leaf to the left of the first (towards
    the back face), - to the right (towards the print face). Zigzag walls fold every duo by 30 deg (FXP-PLT-001 rule S1,
    v0.2). The two leaves are cut 0.8 mm back from the fold line so that they do not overlap where the front skin bends;
    the skin itself is not modelled across the fold."""
    def f():
        full = fx.panel(P["DUO_W"], H, scores=[P["LEAF"]])
        g = 0.8
        left = full & Pos((P["LEAF"] - g) / 2 - 1, T / 2, H / 2) * Box(P["LEAF"] - g + 2, T + 2, H + 2)
        right = full & Pos(P["LEAF"] + g + (P["DUO_W"] - P["LEAF"] - g) / 2 + 1, T / 2, H / 2) * Box(P["DUO_W"] - P["LEAF"] - g + 2, T + 2, H + 2)
        return Compound([left, fold_loc(turn) * right])
    return _once(f"duo_{turn}", f)


def fold_loc(turn):
    """Location that carries a part on the second leaf of a duo (panel frame) through the fold."""
    return Pos(P["LEAF"], T / 2, 0) * Rot(0, 0, turn) * Pos(-P["LEAF"], -T / 2, 0)


def u(a):
    return math.cos(math.radians(a)), math.sin(math.radians(a))


def walk(xy, heading, turn):
    """Joint axis reached by a duo that leaves the joint at xy along 'heading' and folds by 'turn'."""
    r = fx.CORE / 2 + P["LEAF"]
    (c1, s1), (c2, s2) = u(heading), u(heading + turn)
    return (xy[0] + r * (c1 + c2), xy[1] + r * (s1 + s2))


def tail_leaf():
    """L12 single leaf (600 x 1,200 mm, no groove): the corner tail that turns each end-stub corner into a tee (F7)."""
    return _once("tail", lambda: fx.panel(P["LEAF"], H))


def flap_leaf():
    return _once("flap", lambda: fx.panel(P["FLAP_W"], P["FLAP_H"]))


def _bore(h=fx.CLIP_H + 2):
    return Cylinder(P["BORE_D"] / 2, h)


def hinge_end(detail="light"):
    """Hinge end clip for a terminal edge: a round core with the 6.5 mm bore and one standard slot arm (angle 0)."""
    def f():
        core = Cylinder(fx.CORE / 2, fx.CLIP_H) - _bore()
        return core + fx._arm(T, detail)
    return _once(f"hinge_end_{detail}", f)


def sleeve(detail="light"):
    """Flap sleeve clip: a round core with the bore and one slot arm that grips the flap leaf's hinge edge."""
    return hinge_end(detail)


def joint_clip(arms, detail="light"):
    """Clip at a joint whose panels leave along the given directions (deg), built from the platform slot arm
    (fx._arm, FXP-PLT-001 section 5.2) on a round 12 mm core. Two arms 150 deg apart are the platform angle clip; three
    arms are the FlexTriage angle tee (the zigzag wall's two leaves and a stub or tail between). The platform angle clip
    puts its 150 deg arm on a square core, so a panel edge seated at the core face overlaps the core corner by about
    0.9 mm (platform request 8); the round core removes that and keeps every slot, peg and stop where the platform has them."""
    a = tuple(sorted(round(x % 360, 3) for x in arms))

    def f():
        body = Cylinder(fx.CORE / 2, fx.CLIP_H)
        for x in a:
            body = body + Rot(0, 0, x) * fx._arm(T, detail)
        return body
    return _once(f"joint_{a}_{detail}", f)


def _replace_block(ft, block):
    """A platform foot (Compound) with its moulded block replaced by 'block' (same size and seat, other slot angles)."""
    keep = [s for s in ft.solids() if not (abs(s.bounding_box().max.Z - 40.0) < 0.5 and s.bounding_box().size.X > 100)]
    return Compound([block] + keep)


def _block(slots, junction=False):
    hx, hy = (60.0, 60.0) if junction else (60.0, 35.0)
    gap = T + fx.CLEAR
    blk = Pos(0, 0, 20) * Box(2 * hx, 2 * hy, 40)
    try:
        blk = chamfer(blk.edges().filter_by(Axis.Z), 4.0)
    except Exception:
        pass
    for a in slots:
        blk = blk - Rot(0, 0, a) * Pos(45.0, 0, fx.FOOT_SEAT + 15) * Box(90.0, gap, 30)
    return blk


def angle_foot(slots, inside=True, junction=False):
    """Foot for a zigzag wall joint (local x along the wall line, local -y outside the bay): the platform foot block
    with its slots on the panel directions (product accessory, platform request 8) and the platform outriggers.
    inside=False drops the inside outrigger (doorway wall jambs and stub joints: nothing in a doorway, F8)."""
    def f():
        ft = _replace_block(fx.foot("junction" if junction else "inline", P["OUTRIGGER"]), _block(slots, junction))
        if inside:
            return ft
        return Compound([s for s in ft.solids() if s.center().Y <= 1.0])
    return _once(f"afoot_{tuple(slots)}_{inside}_{junction}", f)


def tee_foot():
    """Platform inline foot (FXP-PLT-001 v0.2 'inline', the v0.1 'tee'): slots at 0 and 180 deg, outriggers at 90 and 270."""
    return _once("tee_foot", lambda: fx.foot("inline", P["OUTRIGGER"]))


def jamb_foot():
    """Jamb foot for the free end of a long wall at a doorway: the platform inline foot with its inside outrigger
    removed, so nothing lies across the doorway; the outside outrigger and its ballast bag stay (local +y is inside)."""
    return _once("jamb_foot", lambda: Compound([s for s in tee_foot().solids() if s.center().Y <= 1.0]))


def anchor_foot(sdir=270.0, detail="light"):
    """Anchor foot for a stub terminal (fix F4): the platform inline foot block (slot along local x, the stub's terminal
    leaf direction 'sdir') fused to a hinge end clip whose arm, along +x, takes the stub's terminal edge with its two
    through-pegs at the lower hole pair. The arm walls run down to the foot block, so the stub cannot lift out of the
    foot and the foot's ballast lifts with the stub. The platform outriggers are turned to lie square to the doorway
    (world x), so neither reaches into the doorway's clear width (F8) although the zigzag stub ends 15 deg off it.
    Local frame: floor contact at z = 0 (on its pad), joint axis on the Z axis; the bore stays clear below the clip."""
    def f():
        ft = tee_foot()
        blk = [s for s in ft.solids() if abs(s.bounding_box().max.Z - 40.0) < 0.5 and s.bounding_box().size.X > 100]
        rigs = [s for s in ft.solids() if s not in blk]
        turn = -((sdir % 180) - 90)
        clip = Pos(0, 0, ZC[0] - P["PAD"]) * hinge_end(detail)
        gap = T + fx.CLEAR
        z0, z1 = 40.0, ZC[0] - P["PAD"] - fx.CLIP_H / 2
        walls = None
        for sy in (-1, 1):
            w = Pos(fx.CORE / 2 + fx.SLOT_DEPTH / 2, sy * (gap / 2 + fx.WALL / 2), (z0 + z1) / 2) * Box(fx.SLOT_DEPTH, fx.WALL, z1 - z0 + 0.4)
            walls = w if walls is None else walls + w
        return Compound(blk + [Rot(0, 0, turn) * r for r in rigs] + [clip.fuse(walls)])
    return _once(f"anchor_{sdir % 180}_{detail}", f)


def _stop_block(d_sign, y0=4.0):
    bx0, bx1 = -13.1, -5.1
    y1 = 50.0
    zt, zb = fx.CLIP_H / 2, P["CATCH_Z"] - 20.0 - ZC[1]
    blk = Pos((bx0 + bx1) / 2, d_sign * (y0 + y1) / 2, (zt + zb) / 2) * Box(bx1 - bx0, y1 - y0, zt - zb)
    try:
        blk = chamfer(blk.edges().filter_by(Axis.Z), 1.0)
    except Exception:
        pass
    md = P["MAGNET"][0]
    pocket = Pos(-5.1 - P["COVER"] - 1.65, d_sign * 36.0, P["CATCH_Z"] - ZC[1]) * Rot(0, 90, 0) * Cylinder(md / 2 + 0.2, 3.3)
    return blk, pocket


def stop_clip(arms, d_sign, detail="light"):
    """Catch stop clip at the wall jamb of a doorway (fix F3), at the upper clip height, in the bay frame (x downstream).
    With two arms it is the platform angle clip of a zigzag wall joint; with one arm a round core with one slot arm for a
    wall's free end. Either carries a stop block on the upstream side (-x) that reaches along the doorway (y, sign d_sign)
    and holds a 12.7 x 3.2 mm N42 disc behind a 2 mm cover, facing the leaf's strike: the catch works in pull."""
    def f():
        if len(arms) == 2:
            body = joint_clip(arms, detail)
            blk, pocket = _stop_block(d_sign, 4.0)
        else:
            body = Cylinder(fx.CORE / 2, fx.CLIP_H) + Rot(0, 0, arms[0]) * fx._arm(T, detail)
            blk, pocket = _stop_block(d_sign, 2.5)
        return body.fuse(blk) - pocket
    return _once(f"stop_{tuple(arms)}_{d_sign}_{detail}", f)


def strike_holder(detail="light"):
    """Strike holder on the leaf's free edge: one standard slot arm, back along the leaf (local frame: free edge at
    x = 0, arm from x = 0 to -40); the upstream wall carries a flush stainless M8 washer as the strike."""
    return _once(f"strike_holder_{detail}", lambda: Pos(fx.CORE / 2, 0, 0) * Rot(0, 0, 180) * fx._arm(T, detail))


def _upright_foot(kind):
    """FXP-PLT-001 v0.2 builds every outrigger on the floor, so the v0.1 work-around is a no-op (platform request 3)."""
    return fx.foot(kind, P["OUTRIGGER"])


def bag():
    def f():
        bx, by, bz = P["BAG"]
        return cp.break_edges(Pos(0, 0, bz / 2) * Box(bx, by, bz), 14.0)
    return _once("bag", f)


def zone(w, h, x0, z0):
    return fx.print_zone(w, h, x0, z0)


# ---------------------------------------------------------------------------------------------------------
# FT1 plan (v0.2): zigzag walls (leaves at +-15 deg, folds and angle clips at 30 deg, fold vertices outside the bay),
# zigzag stubs, angle tees at stub and tail joints
# ---------------------------------------------------------------------------------------------------------
ANG = P["ZIG"]
# long walls: (wall, start joint, heading, turn) for every duo. Wall B runs from joint i to i + 1 heading +15 deg;
# wall A is placed from joint i + 1 back to i heading 195 deg, so both print faces look into the bay.
WALL_DUOS = [("B", i, ANG, -2 * ANG) for i in range(P["N_X"])] + [("A", i + 1, 180 + ANG, -2 * ANG) for i in range(P["N_X"])]
# stubs: name, start point, heading, turn, wall joint, terminal (the stub's print face looks upstream or downstream)
STUBS = [("left end", (0, "A"), 90 - ANG, 2 * ANG), ("divider 1", (2, "B"), 270 + ANG, -2 * ANG),
         ("divider 2", (4, "T"), 270 + ANG, -2 * ANG), ("right end", (7, "B"), 270 + ANG, -2 * ANG)]
TAILS = [("A0", (0, "A"), 180 + ANG), ("B7", (7, "B"), ANG)]
# doorways: name, stub terminal, stub direction from the terminal, leaf heading, wall jamb, d_sign (stop block side)
DOORS = [("entry", 0, 270 + ANG, 90, (0, "B")), ("door 1", 2, 90 - ANG, 270, (2, "A")),
         ("door 2", 4, 270 + ANG, 90, (4, "B")), ("exit", 7, 90 - ANG, 270, (7, "A"))]


def _ft1_joints():
    """{(wall, i): [panel directions leaving the joint]} for every wall joint, including stubs and corner tails."""
    j = {}
    for w, i, hd, tn in WALL_DUOS:
        j.setdefault((w, i), []).append(hd % 360)
        end = i + 1 if w == "B" else i - 1
        j.setdefault((w, end), []).append((hd + tn + 180) % 360)
    for nm, (i, w), hd, tn in STUBS:
        if w in ("A", "B"):
            j[(w, i)].append(hd % 360)
        else:
            j[("A", i)].append((hd + tn + 180) % 360)
    for nm, (i, w), hd in TAILS:
        j[(w, i)].append(hd % 360)
    return j


def duo_loc(xy, heading, z=Z0):
    return place(xy, heading, z)


def option_ft1():  # noqa: C901
    out = []
    joints = _ft1_joints()
    turns = {}
    # ---- panels: zigzag wall duos and stubs
    for w, i, hd, tn in WALL_DUOS:
        k = i + 1 if w == "B" else i
        out.append(_p(f"P12 duo, wall {w} {k}", duo_loc(jxy(i, w), hd) * duo(tn), "hdpe_natural", "made", 1,
                      (0, 260 if w == "B" else -260, 0), C_SHEET,
                      note="FXP-S4FR 4 mm FR twinwall, 1,200 x 1,200 mm, 13.6 mm groove at 600 mm folded 30 deg, flutes vertical"))
        turns[(w, i)] = (hd, tn)
    for nm, (i, w), hd, tn in STUBS:
        loc = duo_loc(jxy(i, w), hd)
        out.append(_p(f"P12 duo, stub {nm}", loc * duo(tn), "hdpe_natural", "made", 1, (0, 0, 220), C_SHEET,
                      note="zigzag stub folded 30 deg; groove on the back face covered by a clear PP strip (rule E2)"))
        halves = [Pos(P["LEAF"] - 7.0, T + 0.15, H / 2) * Box(11.0, 0.3, H - 20),
                  fold_loc(tn) * Pos(P["LEAF"] + 7.0, T + 0.15, H / 2) * Box(11.0, 0.3, H - 20)]
        out.append(_p(f"Groove cover strip, stub {nm}", loc * Compound(halves), "label", "bought", 16, (0, 0, 220), "#E4F0F2"))
    for nm, (i, w), hd in TAILS:
        out.append(_p(f"L12 corner tail leaf, {nm}", duo_loc(jxy(i, w), hd) * tail_leaf(), "hdpe_natural", "made", 23, (0, 0, 220), C_SHEET,
                      note="600 x 1,200 mm leaf outside the bay; turns the end-stub corner into a tee (F7)"))
    # ---- clips at wall joints: angle clips (platform) and angle tees; the upper clip at a doorway's wall jamb is the stop clip
    jambs = {(jw, ji): (dn, -1 if jw == "B" else 1) for dn, _, _, _, (ji, jw) in DOORS}
    for (w, i), dirs in sorted(joints.items()):
        if len(dirs) == 1:
            continue
        kind = "angle" if len(dirs) == 2 else "angle tee"
        for n, zc in enumerate(ZC):
            if n == 1 and (w, i) in jambs:
                continue
            out.append(_p(f"Clip-lock {kind}, {w}{i} {'low' if n == 0 else 'high'}", Pos(*jxy(i, w), zc) * joint_clip(dirs), "hdpe_black", "made",
                          2 if kind == "angle" else 3, (0, 0, 0), C_CLIP))
    # ---- feet on 2 mm EPDM pads (floor z = 0)
    zp = P["PAD"]
    pad = cp.sheet(118.0, 68.0, zp, r_corner=3.0, edge=0.3)
    pad_sq = cp.sheet(118.0, 118.0, zp, r_corner=3.0, edge=0.3)
    for (w, i), dirs in sorted(joints.items()):
        x, y = jxy(i, w)
        nm = f"{w}{i}"
        if len(dirs) == 1:        # free wall end at the entry or exit: jamb foot along the wall leaf, outside outrigger only
            r = (dirs[0] + 180) % 360 if w == "B" else dirs[0] - 180
            out.append(_p(f"EPDM pad, {nm}", Pos(x, y, 0) * Rot(0, 0, r) * pad, "epdm", "bought", 19, (0, 0, -160), "#151617"))
            out.append(_p(f"Jamb foot, {nm}", Pos(x, y, zp) * Rot(0, 0, r) * jamb_foot(), "hdpe_black", "made", 12, (0, 0, -120), C_FOOT,
                          note="platform inline foot with the outside outrigger only"))
            continue
        rot = 0 if w == "A" else 180                     # local x along the wall line, local -y outside the bay
        slots = tuple(sorted(round((a - rot) % 360, 3) for a in dirs))
        if len(dirs) == 3:
            out.append(_p(f"EPDM pad, {nm}", Pos(x, y, 0) * Rot(0, 0, rot) * pad_sq, "epdm", "bought", 19, (0, 0, -160), "#151617"))
            out.append(_p(f"Angle junction foot, {nm}", Pos(x, y, zp) * Rot(0, 0, rot) * angle_foot(slots, inside=False, junction=True),
                          "hdpe_black", "made", 13, (0, 0, -120), C_FOOT, note="angle-tee block, one outside outrigger"))
        elif (w, i) in jambs:
            out.append(_p(f"EPDM pad, {nm}", Pos(x, y, 0) * Rot(0, 0, rot) * pad, "epdm", "bought", 19, (0, 0, -160), "#151617"))
            out.append(_p(f"Angle jamb foot, {nm}", Pos(x, y, zp) * Rot(0, 0, rot) * angle_foot(slots, inside=False), "hdpe_black", "made", 13,
                          (0, 0, -120), C_FOOT, note="angle block, outside outrigger only (nothing in the doorway, F8)"))
        else:
            out.append(_p(f"EPDM pad, {nm}", Pos(x, y, 0) * Rot(0, 0, rot) * pad, "epdm", "bought", 19, (0, 0, -160), "#151617"))
            out.append(_p(f"Angle foot, {nm}", Pos(x, y, zp) * Rot(0, 0, rot) * angle_foot(slots), "hdpe_black", "made", 11, (0, 0, -120), C_FOOT,
                          note="platform foot block with slots at the zigzag angle, two outriggers"))
    for nm, (i, w), hd in TAILS:
        ex, ey = jxy(i, w)[0] + (fx.CORE / 2 + P["LEAF"]) * u(hd)[0], jxy(i, w)[1] + (fx.CORE / 2 + P["LEAF"]) * u(hd)[1]
        out.append(_p(f"EPDM pad, tail {nm}", Pos(ex, ey, 0) * Rot(0, 0, hd) * pad, "epdm", "bought", 19, (0, 0, -160), "#151617"))
        out.append(_p(f"Platform foot, tail {nm}", Pos(ex, ey, zp) * Rot(0, 0, hd) * tee_foot(), "hdpe_black", "made", 11, (0, 0, -120), C_FOOT,
                      note="FXP-PLT-001 inline foot at the tail's free end"))
    # ---- doorways: one leaf hinged at the stub terminal, opening downstream (+x), closing on a stop at the wall jamb
    zf = P["FLAP_Z"]
    zcl = fx.clip_heights(P["FLAP_H"])
    for dn, ti, sdir, hd, (ji, jw) in DOORS:
        txy, jxy_ = jxy(ti, "T"), jxy(ji, jw)
        d_sign = 1 if jxy_[1] < txy[1] else -1          # stop block points from the wall jamb toward the terminal
        out.append(_p(f"EPDM pad, terminal {dn}", Pos(txy[0], txy[1], 0) * Rot(0, 0, sdir) * pad, "epdm", "bought", 19, (0, 0, -160), "#151617"))
        out.append(_p(f"Anchor foot, {dn} (hinge)", Pos(txy[0], txy[1], zp) * Rot(0, 0, sdir) * anchor_foot(sdir), "hdpe_black", "made", 20,
                      (0, 0, -120), C_FOOT, note="platform foot fused to a hinge end clip: the stub cannot lift out (F4)"))
        out.append(_p(f"Hinge end clip, {dn} high (hinge)", Pos(txy[0], txy[1], ZC[1]) * Rot(0, 0, sdir) * hinge_end(), "hdpe_black", "made", 4,
                      (0, 0, 0), C_CLIP))
        lloc = Pos(txy[0], txy[1], zf) * Rot(0, 0, hd) * Pos(fx.CORE / 2, -T / 2, 0)
        out.append(_p(f"Flap leaf, {dn}", lloc * flap_leaf(), "hdpe_natural", "made", 5, (0, 0, 160), C_SHEET,
                      note=f"FXP-S4FR, {P['FLAP_W']:.0f} x {P['FLAP_H']:.0f} mm, opens downstream only"))
        for n, zc in enumerate(zcl):
            out.append(_p(f"Flap sleeve clip, {dn} {'low' if n == 0 else 'high'} (hinge)", Pos(txy[0], txy[1], zf + zc) * Rot(0, 0, hd) * sleeve(),
                          "hdpe_black", "made", 6, (0, 0, 160), C_CLIP))
        zj_lo_bot, zj_lo_top = ZC[0] - fx.CLIP_H / 2, ZC[0] + fx.CLIP_H / 2
        zs_lo_top = zf + zcl[0] + fx.CLIP_H / 2
        zj_hi_top, zs_hi_bot = ZC[1] + fx.CLIP_H / 2, zf + zcl[1] - fx.CLIP_H / 2
        out.append(_p(f"M6 washer (ISO 7089, A2), {dn} lower hinge", Pos(txy[0], txy[1], zj_lo_top) * cp.washer(6), "stainless", "fastener"))
        for zhead, grip, lab in ((zs_lo_top, zs_lo_top - zj_lo_bot, "lower"), (zj_hi_top, zj_hi_top - zs_hi_bot, "upper")):
            out.append(_p(f"Hinge pin 6 mm (ISO 2341 B), {dn} {lab}", Pos(txy[0], txy[1], zhead) * cp.clevis_pin(6, grip), "stainless", "fastener", 8))
            out.append(_p(f"Split pin (ISO 1234), {dn} {lab} hinge pin", Pos(txy[0], txy[1], zhead - grip - 6.0) * Rot(0, 0, hd + 90) * cp.split_pin(6),
                          "stainless", "fastener"))
        for side in (-1, 1):   # finger guards across the hinge gap, both faces, mostly on the leaf side of the axis
            guard = Pos(txy[0], txy[1], (zj_lo_top + zs_hi_bot) / 2 + 40) * Rot(0, 0, hd) * Pos(12.0, side * (T / 2 + 5.4), 0) * Box(40.0, 0.8, 520.0)
            out.append(_p(f"Hinge finger guard, {dn} {'upstream' if side < 0 else 'downstream'}", cp.break_edges(guard, 0.3), "epdm", "bought", 22,
                          (0, 0, 160), "#2B2B2C"))
        edge = Pos(txy[0], txy[1], P["CATCH_Z"]) * Rot(0, 0, hd) * Pos(fx.CORE / 2 + P["FLAP_W"], 0, 0)
        hold = edge * (Rot(180, 0, 0) if hd == 90 else Rot(0, 0, 0)) * strike_holder()   # tongue lips always downstream
        sc = (jxy_[0], jxy_[1] + d_sign * 36.0)
        hold = hold - Pos(sc[0] - 4.6 + 0.85, sc[1], P["CATCH_Z"]) * Rot(0, 90, 0) * Cylinder(8.1, 1.7)
        out.append(_p(f"Strike holder, {dn}", hold, "hdpe_black", "made", 7, (0, 0, 160), C_CLIP))
        out.append(_p(f"Strike washer M8 (ISO 7089, A2), {dn}", Pos(sc[0] - 4.6, sc[1], P["CATCH_Z"]) * Rot(0, 90, 0) * cp.washer(8), "stainless",
                      "bought", 10, (0, 0, 160)))
        jdirs = joints[(jw, ji)]
        jkind = "angle" if len(jdirs) == 2 else "end"
        out.append(_p(f"Catch stop clip ({jkind}), {dn}", Pos(jxy_[0], jxy_[1], ZC[1]) * stop_clip(tuple(sorted(jdirs)), d_sign), "hdpe_black", "made", 21,
                      (0, 0, 0), C_CLIP, note="stop block upstream of the leaf with the magnet behind 2 mm (F3)"))
        md, mt = P["MAGNET"]
        mag = cp.break_edges(Cylinder(md / 2, mt), 0.3)
        out.append(_p(f"N42 disc magnet 12.7 x 3.2 mm, {dn}", Pos(jxy_[0] - 5.1 - P["COVER"] - mt / 2 - 0.05, jxy_[1] + d_sign * 36.0, P["CATCH_Z"]) * Rot(0, 90, 0) * mag,
                      "zinc_plated", "bought", 9, (0, 0, 0)))
    # ---- ballast bags (site-filled, sealed bags, rule B1): two stacked on the upstream outrigger of each anchor foot, clear
    #      of the leaf's swing (F8), and one on the outside outrigger of each jamb foot
    tri_h = 50.0 * math.sqrt(3) / 2 + 0.3 + zp
    for dn, ti, sdir, hd, _ in DOORS:
        x, y = jxy(ti, "T")
        for k in range(2):     # on the upstream outrigger, which lies along -x (anchor_foot)
            out.append(_p(f"Ballast bag, {dn} terminal {k + 1}", Pos(x - 160.0, y, tri_h + k * (P["BAG"][2] + 0.2)) * Rot(0, 0, 90) * bag(),
                          "canvas", "bought", 14, (0, 0, 120), C_BAG))
    for (w, i), dirs in sorted(joints.items()):
        if len(dirs) != 1:
            continue
        x, y = jxy(i, w)
        d = 90 + ANG if w == "B" else 270 + ANG     # outside, square to the wall leaf
        out.append(_p(f"Ballast bag, jamb {w}{i}", Pos(x + 160 * u(d)[0], y + 160 * u(d)[1], tri_h) * Rot(0, 0, d - 90) * bag(), "canvas", "bought", 14,
                      (0, 0, 120), C_BAG))
    # ---- printed zones (FXP-PLT-001 sections 7 and 12, rules C1, C5, C6; F1: process zones by numeral and word on neutral;
    #      visual characters at least 1,015 mm above the floor, ADA 703.5.6). (wall or stub, joint, leaf 1 or 2, x0 on the panel)
    zs = 1015.0 - Z0
    wall_loc = {(w, i): (jxy(i, w), hd, tn) for w, i, hd, tn in WALL_DUOS}
    stub_loc = {nm: (jxy(i, w), hd, tn) for nm, (i, w), hd, tn in STUBS}

    def on(ref, x0, w=520, h=180, z0=zs):
        xy, hd, tn = ref
        loc = duo_loc(xy, hd)
        pz = zone(w, h, x0, z0)
        return loc * (fold_loc(tn) * pz if x0 >= P["LEAF"] else pz)

    signs = [("Zone sign 1 Intake", wall_loc[("B", 1)], 40), ("Zone sign 2 Assessment", wall_loc[("B", 2)], 640),
             ("Zone sign 3 Treatment", wall_loc[("A", 6)], 40), ("Direction sign to 2", stub_loc["divider 1"], 40),
             ("Direction sign to 3", stub_loc["divider 2"], 40), ("Way out sign", stub_loc["right end"], 640)]
    for nm, ref, x0 in signs:
        out.append(_p(f"Print zone, {nm}", on(ref, x0), "label", "made", 15, (0, 0, 0), C_INK))
    for j, (cat, col) in enumerate((("immediate", fx.SAFETY["red"]), ("delayed", fx.SAFETY["yellow"]), ("minor", fx.SAFETY["green"]))):
        out.append(_p(f"Print zone, triage category band {cat}", on(wall_loc[("B", 5)], (40, 300, 640)[j], w=240), "label", "made", 15,
                      (0, 0, 0), col))
    for dn, ti, sdir, hd, _ in DOORS:
        x, y = jxy(ti, "T")
        lloc = Pos(x, y, zf) * Rot(0, 0, hd) * Pos(fx.CORE / 2, -T / 2, 0)
        out.append(_p(f"Print zone, push plate {dn}", lloc * zone(300, 160, 800, 700), "label", "made", 15, (0, 0, 160), C_INK))
        out.append(_p(f"Print zone, contrast edge band {dn}", lloc * zone(P["FLAP_W"] - 80, 60, 40, 30), "label", "made", 15, (0, 0, 160), C_INK))
    return out


# ---------------------------------------------------------------------------------------------------------
# FT2: tensioned fabric screens on a pole frame (same plan)
# ---------------------------------------------------------------------------------------------------------
def option_ft2():
    out = []
    od, t = P["FT2_POST"]
    rod, rt = P["FT2_RAIL"]
    bx, by, bt = P["FT2_BASE"]
    sh, dh = P["FT2_SCREEN_H"], P["FT2_DOOR_H"]
    xs = [0.0, 2 * PITCH, 4 * PITCH, 5.5 * PITCH, X_END]
    door_posts = {(2 * PITCH, 0.0), (X_END, 0.0), (0.0, Y_B), (4 * PITCH, Y_B)}
    posts = [(x, 0.0) for x in xs] + [(x, Y_B) for x in xs] + [(0.0, Y_T), (2 * PITCH, Y_T), (4 * PITCH, Y_T), (X_END, Y_T)]
    base_plate = cp.sheet(bx, by, bt, holes=[(sx * 110, sy * 110, 9) for sx in (-1, 1) for sy in (-1, 1)], r_corner=12)
    bolt_hole = Pos(0, 0, 118) * Rot(0, 90, 0) * Cylinder(4.5, od + 20)
    socket = cp.round_tube(od + 6, 2.0, 160) - bolt_hole
    for k, (x, y) in enumerate(posts):
        tall = (x, y) in door_posts or y == Y_T
        L = (dh if tall else sh) + 60
        out.append(_p(f"Base plate {k + 1}, aluminium 6 mm", Pos(x, y, 0) * base_plate, "aluminium", "made", 21, (0, 0, -100)))
        out.append(_p(f"Post socket {k + 1}", Pos(x, y, bt) * socket, "aluminium", "made", 21, (0, 0, -100)))
        post = cp.round_tube(od, t, L - 2) - Pos(0, 0, 116) * Rot(0, 90, 0) * Cylinder(4.5, od + 20)
        out.append(_p(f"Aluminium post {k + 1}, {od:.0f} x {t} mm", Pos(x, y, bt + 2) * post, "aluminium", "bought", 22))
        for n, s in cp.hex_bolt_set(8, od + 6):
            out.append(_p(f"{n}, post {k + 1} locking bolt", Pos(x, y, bt + 118) * Rot(0, 90, 0) * Pos(0, 0, (od + 6) / 2) * s, "zinc_plated", "fastener"))
        off = (0, -330) if y == 0.0 else ((0, 330) if y == Y_B else ((-330 if x > X_END / 2 else 330), 0))
        out.append(_p(f"Ballast bag, post {k + 1}", Pos(x + off[0], y + off[1], 0) * bag(), "canvas", "bought", 14, (0, 0, 100), C_BAG))
    runs = []
    for y in (0.0, Y_B):
        for a, b in zip(xs[:-1], xs[1:]):
            runs.append(((a, y), (b, y)))
    for x in (0.0, 2 * PITCH, 4 * PITCH, X_END):
        y0 = 0.0 if x in (0.0, 4 * PITCH) else Y_B
        runs.append(((x, y0), (x, Y_T)))
    for k, ((x0, y0), (x1, y1)) in enumerate(runs):
        L = math.hypot(x1 - x0, y1 - y0)
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        loc = Pos(x0, y0, 0) * Rot(0, 0, ang)
        out.append(_p(f"Top rail {k + 1}", loc * Pos(od / 2 + 2, 0, sh) * Rot(0, 90, 0) * cp.round_tube(rod, rt, L - od - 4), "aluminium", "bought", 23))
        for e, xe in (("a", od / 2 + 12), ("b", L - od / 2 - 12)):
            ring = Cylinder(rod / 2 + 4, 20) - Cylinder(rod / 2 + 0.3, 22)
            out.append(_p(f"Rail clamp {k + 1}{e}, printed", loc * Pos(xe, 0, sh) * Rot(0, 90, 0) * ring, "hdpe_black", "made", 24))
        scr = cp.sheet(L - od - 80, sh - 120, P["FT2_FABRIC_T"], holes=[(-(L - od - 80) / 2 + 30 + j * 300, (sh - 120) / 2 - 25, 10)
                                                                     for j in range(int((L - od - 140) // 300) + 1)], r_corner=20, edge=0.2)
        out.append(_p(f"FR coated fabric screen {k + 1}", loc * Pos(L / 2, 0, 50 + (sh - 120) / 2) * Rot(90, 0, 0) * scr, "canvas", "bought", 25,
                      color="#DCE7EA"))
        ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pts = [(x0 + u * ca, y0 + u * sa, 28.0) for u in (od / 2 + 30, L / 2, L - od / 2 - 30)]
        out.append(_p(f"Bottom tension cord {k + 1}", cp.rope(pts, 4.0), "rope", "bought", 26))
    doors = [((2 * PITCH, 0.0), (2 * PITCH, Y_T)), ((4 * PITCH, Y_T), (4 * PITCH, Y_B)), ((0.0, Y_T), (0.0, Y_B)), ((X_END, 0.0), (X_END, Y_T))]
    for k, ((x0, y0), (x1, y1)) in enumerate(doors):
        L = math.hypot(x1 - x0, y1 - y0)
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        loc = Pos(x0, y0, 0) * Rot(0, 0, ang)
        out.append(_p(f"Door header {k + 1}", loc * Pos(od / 2 + 2, 0, dh) * Rot(0, 90, 0) * cp.round_tube(rod, rt, L - od - 4), "aluminium", "bought", 23))
        half = (L - od - 30) / 2
        for s, x0c in (("a", od / 2 + 10), ("b", od / 2 + 20 + half)):
            cur = cp.sheet(half, dh - 80, P["FT2_FABRIC_T"], r_corner=20, edge=0.2)
            out.append(_p(f"Split magnetic curtain {k + 1}{s}", loc * Pos(x0c + half / 2, 0, 40 + (dh - 80) / 2) * Rot(90, 0, 0) * cur, "canvas", "bought", 27,
                          color="#C9D8DC"))
    return out


# ---------------------------------------------------------------------------------------------------------
# FT3: floor marking and retractable-belt stanchions (same plan)
# ---------------------------------------------------------------------------------------------------------
def option_ft3():
    out = []
    pd, pt, ph = P["FT3_POST"]
    bd = P["FT3_BASE_D"]
    bw, btk, bz = P["FT3_BELT"]
    xs = [0.0, 2 * PITCH, 4 * PITCH, 5.5 * PITCH, X_END]
    posts = [(x, 0.0) for x in xs] + [(x, Y_B) for x in xs] + [(0.0, Y_T), (2 * PITCH, Y_T), (4 * PITCH, Y_T), (X_END, Y_T)]
    base = cp.break_edges(Pos(0, 0, 15) * Cylinder(bd / 2, 30), 6.0) - Pos(0, 0, 7.5) * Cylinder(22, 15.2) - Pos(0, 0, 22) * Cylinder(5.5, 20)
    head = cp.break_edges(Pos(0, 0, 40) * Box(90, 90, 80), 8.0)
    for k, (x, y) in enumerate(posts):
        out.append(_p(f"Stanchion base {k + 1}, cast", Pos(x, y, 0) * base, "matte_black", "bought", 31))
        out.append(_p(f"Stanchion post {k + 1}", Pos(x, y, 30) * cp.round_tube(pd, pt, ph - 110), "painted_steel", "bought", 31, color="#1F2937"))
        out.append(_p(f"Belt cassette head {k + 1}", Pos(x, y, ph - 80) * head, "matte_black", "bought", 31))
        for n, s in cp.hex_bolt_set(10, 15):
            out.append(_p(f"{n}, stanchion {k + 1}", Pos(x, y, 30) * s, "zinc_plated", "fastener"))
    belts = []
    for y in (0.0, Y_B):
        for a, b in zip(xs[:-1], xs[1:]):
            belts.append(((a, y), (b, y)))
    for x in (0.0, 2 * PITCH, 4 * PITCH, X_END):
        y0 = 0.0 if x in (0.0, 4 * PITCH) else Y_B
        belts.append(((x, y0), (x, Y_T)))
    for k, ((x0, y0), (x1, y1)) in enumerate(belts):
        L = math.hypot(x1 - x0, y1 - y0)
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        belt = cp.break_edges(Pos(L / 2, 0, bz) * Box(L - 100, btk, bw), 0.3)
        out.append(_p(f"Retractable belt {k + 1}", Pos(x0, y0, 0) * Rot(0, 0, ang) * belt, "rope", "bought", 31, color="#1D4E89"))
    # floor tape: zone boundaries, the path and arrows (vinyl, 2 in), sitting on the floor
    tw = P["FT3_TAPE_W"]
    lines = [((0, -300), (X_END, -300)), ((0, Y_B + 300), (X_END, Y_B + 300)), ((2 * PITCH + 300, 0), (2 * PITCH + 300, Y_B)),
             ((4 * PITCH + 300, 0), (4 * PITCH + 300, Y_B))]
    for k, ((x0, y0), (x1, y1)) in enumerate(lines):
        L = math.hypot(x1 - x0, y1 - y0)
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        out.append(_p(f"Floor tape line {k + 1}", Pos(x0, y0, 0) * Rot(0, 0, ang) * Pos(L / 2, 0, 0) * cp.sheet(L, tw, 0.15, r_corner=2, edge=0),
                      "label", "bought", 32, color="#F9A900" if k < 2 else "#ECECE7"))
    path = [(600, 1800), (1800, 600), (3300, 600), (4400, 1800), (6200, 1800), (7800, 600)]
    for k, (x, y) in enumerate(path):
        arrow = extrude(Polygon((0, -120), (250, 0), (0, 120), align=None), 0.15)
        out.append(_p(f"Floor tape arrow {k + 1}", Pos(x, y, 0) * arrow, "label", "bought", 32, color="#ECECE7"))
    for k, (x, y) in enumerate([(PITCH, 0.0), (3 * PITCH, Y_B), (5.5 * PITCH, 0.0), (X_END, Y_T)]):
        s = cp.sheet(300, 220, 3.0, r_corner=6)
        out.append(_p(f"Post-top zone sign {k + 1}", Pos(x, y + (60 if y < Y_T else -60), ph + 40) * Rot(90, 0, 0) * s, "hdpe_natural", "bought", 33,
                      color="#ECECE7"))
    return out


def components(option="FT1"):
    return {"FT1": option_ft1, "FT2": option_ft2, "FT3": option_ft3}[option]()


if __name__ == "__main__":
    from collections import Counter
    for k in OPTIONS:
        ps = components(k)
        real = [q for q in ps if q["kind"] != "context"]
        print(k, len(real), "parts", Counter(q["kind"] for q in real))
