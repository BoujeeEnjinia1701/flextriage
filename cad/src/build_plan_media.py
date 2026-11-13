# SPDX-License-Identifier: CERN-OHL-P-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""FlexTriage Origami Bay: prototype build plan pictures (FXT-BLD-001, STANDARDS section 18), option FT1.

Run from the repo root, one picture group per process on a small machine:
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py (components("FT1") and its part functions), so pictures and model agree:
    docs/05-build-plan/overview.png        one of each component, pulled apart, numbered in build order
    cad/drawings/FXT-DWG-101 to 107        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import functools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Box, Compound, Pos, Rot  # noqa: E402
import model as M  # noqa: E402
import flex_parts as fx  # noqa: E402

OUT = ROOT / "docs/05-build-plan"
DWG = ROOT / "cad/drawings"
DATE = "2026-11-12"
PROJECT = "FlexTriage Origami Bay"
P = M.PARAMS
GREY = "#9CA3AF"


@functools.lru_cache(None)
def raw():
    return M.components("FT1")


def sel(*keys, exclude=()):
    return [q for q in raw() if any(k in q["name"] for k in keys) and not any(e in q["name"] for e in exclude)]


def grp(name, qs, color=None, bom=None, explode=(0, 0, 0)):
    return Part(name, Compound([q["shape"] for q in qs]), color or qs[0]["color"], bom if bom is not None else qs[0]["bom"], explode)


def near(x, y, r=700, zmax=None, keys=None):
    out = []
    for q in raw():
        if keys and not any(k in q["name"] for k in keys):
            continue
        c = q["shape"].bounding_box().center()
        if abs(c.X - x) < r and abs(c.Y - y) < r and (zmax is None or c.Z < zmax):
            out.append(Part(q["name"], q["shape"], q["color"], q["bom"]))
    return out


# ---------------------------------------------------------------------------------------------------------
def overview():
    t = M.T
    items = [
        ("EPDM pad (22)", M.cp.sheet(118, 68, 2, r_corner=3), "#151617", 19, (-2200, 0, -300)),
        ("Angle foot (8), tail foot (2), jamb foot (2)", M.angle_foot((195.0, 345.0)), M.C_FOOT, 11, (-1600, 0, -300)),
        ("Angle junction foot (4), angle jamb foot (2)", M.angle_foot((75.0, 195.0, 345.0), inside=False, junction=True), M.C_FOOT, 13, (-1100, 0, -300)),
        ("Anchor foot (4)", M.anchor_foot(285.0), M.C_FOOT, 20, (-600, 0, -300)),
        ("P12 duo panel (18), folded 30 deg", Rot(0, 0, 15) * M.duo(-30.0), M.C_SHEET, 1, (-2300, 600, 300)),
        ("Corner tail leaf (2)", M.tail_leaf(), M.C_SHEET, 23, (-800, 600, 300)),
        ("Angle clip (18) and angle tee (8)", Compound([M.joint_clip((15.0, 165.0)), Pos(0, 0, 140) * M.joint_clip((75.0, 195.0, 345.0))]), M.C_CLIP, 2, (-100, 0, 600)),
        ("Hinge end clip (4)", M.hinge_end(), M.C_CLIP, 4, (300, 0, 600)),
        ("Flap leaf (4)", M.flap_leaf(), M.C_SHEET, 5, (600, 600, 300)),
        ("Sleeve clip (8), pins (8)", Compound([M.sleeve(), Pos(0, 0, 200) * M.cp.clevis_pin(6, 200)]), M.C_CLIP, 6, (700, 0, 600)),
        ("Catch stop clip (4) with magnet", M.stop_clip((195.0, 345.0), 1), M.C_CLIP, 21, (1100, 0, 600)),
        ("Strike holder (4)", M.strike_holder(), M.C_CLIP, 7, (1500, 0, 600)),
        ("Ballast bag (10), filled on site", M.bag(), M.C_BAG, 14, (2200, 0, -300)),
    ]
    ps = [Part(n, s, c, b, e) for n, s, c, b, e in items]
    return bv.overview(ps, OUT / "overview.png", title=f"{PROJECT}: components of the three-zone bay in build order",
                       subtitle="One of each component, pulled apart and numbered in build order, with the count for one bay; plan, not yet built",
                       size=(12, 8), key=True, elev=22, azim=-55)


SHEETS = {
    101: ("duo", "P12 duo wall panel: making sketch",
          "4 mm flame-retardant PP twinwall (FXP-S4FR), 1,220 x 2,440 mm sheet, flutes along the 2,440 mm length; two per sheet",
          ["Cut a 1,200 x 1,200 mm blank with the flutes running up the panel",
           "Rout a flat-bottomed groove 13.6 mm wide on the back face at 600 mm, through the back skin and ribs, front skin whole",
           "Hot-punch eight 8 mm holes 12.5 mm from each side edge at 125, 175, 1,025, 1,075 mm",
           "Heat-seal every cut edge 2 mm deep, the groove shoulders and ends too (rules E1, E2)",
           "Print side is the front: zone signs at least 25 mm from holes",
           "Stands folded 30 deg at the groove (zigzag, rule S1); edges slide 40 mm into the clip slots until the pegs click",
           "Check: folds flat to 180 deg and 90 deg the other way without a crack in the front skin"]),
    102: ("flap", "Flap leaf: making sketch",
          "Same sheet grade, 1,149 x 990 mm, no groove; two per sheet",
          ["Cut a 1,149 x 990 mm blank, flutes running up the leaf",
           "Hot-punch eight 8 mm holes 12.5 mm from each side edge at 125, 175, 815, 865 mm",
           "Heat-seal all edges; apply the push plate and the dark edge band",
           "Hinge edge takes two sleeve clips; free edge takes the strike holder at the upper holes",
           "Hangs 114 mm above the floor and opens downstream only",
           "Check: swings 90 deg with no rub on the foot, the bag or the wall"]),
    103: ("clip", "Clip-lock connectors (platform): making sketch",
          "PETG print, 100 % infill at tongues and pegs, 0.2 mm layers; moulded PP at scale",
          ["Print the angle clips, angle tees and hinge end clips standing up (Z is the joint line); round 12 mm core",
           "Angle clip slots 150 deg apart; slot gap 4.5 mm, depth 40 mm, two 7 mm through-pegs per slot at 25 mm either side",
           "Hinge end and sleeve clips: ream the 6.5 mm bore after printing",
           "Remove all support from the tongue windows; the tongue must spring back freely",
           "Fits: panel edge slides in until it meets the core and both pegs drop into its holes",
           "Check: a firm hand tug does not pull the panel out; the pegs show through both skins"]),
    104: ("anchor", "Anchor foot (stub terminal): making sketch",
          "PETG print of the foot block, the slot arm and its two side walls in one piece; outriggers folded from FR twinwall offcut",
          ["Print the block, the arm walls and the hinge core as one part, slot upward",
           "Ream the 6.5 mm hinge bore; keep the bore clear below the clip",
           "Fold two triangular outrigger beams (50 mm sides) from 170 x 265 mm blanks; they lie square to the doorway",
           "Fits: the stub's end edge drops into the slot and the arm until the two pegs click into its lower holes",
           "Two filled bags sit on the upstream outrigger; when the wall leans they lift with the stub",
           "Check: lifting the stub end lifts the foot and both bags"]),
    105: ("stop", "Catch stop clip and strike holder: making sketch",
          "PETG print; N42 disc magnet 12.7 x 3.2 mm; stainless M8 washer as the strike",
          ["Print the stop clip (an angle clip with a block on the upstream side), magnet pocket 13.1 mm across, 3.3 mm deep",
           "Press the magnet into the pocket behind a 2 mm wall and seal the pocket opening with a bonded cap",
           "Print the strike holder; press the washer flush into its upstream wall",
           "Fits: the stop clip replaces the upper wall clip at the doorway's wall jamb",
           "The block face sits 0.5 mm from the strike when the leaf is shut",
           "Check: the leaf holds shut and opens with under 22 N at the push plate"]),
    106: ("foot", "Angle foot, angle junction foot and jamb foot: making sketch",
          "PETG print of the FXP-PLT-001 foot block with slots at the zigzag angles; outriggers folded from FR twinwall offcut",
          ["Print the 120 x 70 x 40 mm block (120 x 120 for junctions) with 4.5 mm slots at 150 deg (and the stub slot)",
           "Two outriggers at plain wall joints; only the outside one at doorway jambs, junctions and free ends",
           "Bond a 2 mm EPDM pad under every block",
           "Fits: panel bottom edges sit 12.5 mm above the floor in the slot",
           "Check: the bay stands without rocking on a flat floor"]),
}


def _shape(key):
    return {"duo": M.duo(-30.0), "flap": M.flap_leaf(), "clip": M.joint_clip((15.0, 165.0), "full"), "anchor": M.anchor_foot(75.0, "full"),
            "stop": M.stop_clip((195.0, 345.0), 1, "full"), "foot": M.angle_foot((195.0, 345.0))}[key]


def _where(key):
    q = {"duo": sel("P12 duo, wall A 3"), "flap": sel("Flap leaf, door 1"), "clip": sel("Clip-lock angle, B1 low"),
         "anchor": sel("Anchor foot, door 1"), "stop": sel("Catch stop clip (angle), door 1"), "foot": sel("Angle foot, A1")}[key]
    return Part(q[0]["name"], q[0]["shape"], q[0]["color"], q[0]["bom"])


def sheets(which=None):
    for no, (key, title, mat, notes) in SHEETS.items():
        if which and str(no) not in which:
            continue
        part = _where(key)
        c = part.shape.bounding_box().center()
        nb = near(c.X, c.Y, r=1300, keys=("P12 duo", "Flap leaf", "foot", "shoe"))
        nb = [p for p in nb if p.name != part.name][:14]
        print(bv.component_sheet(part, nb, PROJECT, f"FXT-DWG-{no}", title, mat, notes, DATE, view_shape=_shape(key)))


def panels_near(x, y, r=260, zmax=1300):
    """Panel pieces (duos, tails, leaves) cut to a box round a joint, so a close-up shows how the panels sit in it."""
    box = Pos(x, y, zmax / 2) * Box(2 * r, 2 * r, zmax)
    out = []
    for q in raw():
        if not any(k in q["name"] for k in ("P12 duo", "L12 corner tail", "Flap leaf")):
            continue
        c = q["shape"].bounding_box()
        if c.min.X > x + r or c.max.X < x - r or c.min.Y > y + r or c.max.Y < y - r:
            continue
        piece = q["shape"] & box
        if piece is not None and sum(v.volume for v in piece.solids()) > 1.0:
            out.append(Part(q["name"] + " (cut)", piece, q["color"], q["bom"]))
    return out


def joints(which=None):
    X2, PI = 2 * M.PITCH, M.PITCH
    J = {
        1: ("Joint 1: zigzag wall joint, two angle clips and an angle foot on its pad", near(PI, 0, 260, zmax=1300) + panels_near(PI, 0), None, 30, -60),
        2: ("Joint 2: divider stub in an angle tee and an angle junction foot at the long wall", near(X2, M.Y_B, 260, zmax=1300) + panels_near(X2, M.Y_B), None, 30, -60),
        3: ("Joint 3: anchor foot, lower hinge pin and the leaf's sleeve at a stub end", near(X2, PI, 260, zmax=420), None, 22, -125),
        4: ("Joint 4: magnetic catch at the wall jamb (seen from upstream, above)",
            [p for p in near(X2, 0, 120) if p.shape.bounding_box().center().Z > 880], None, 40, -150),
        5: ("Joint 5: corner tail: the end stub's corner made a tee, with its outside leaf", near(0, 0, 330, zmax=1300) + panels_near(0, 0, 330), None, 30, -55),
    }
    for k, (title, ps, cut, el, az) in J.items():
        if which and str(k) not in which:
            continue
        print(bv.joint(ps, OUT / f"joint-{k:02d}.png", title, subtitle="Close-up from the model; parts named", cut=cut, elev=el, azim=az))


def steps(which=None):
    pads = sel("EPDM pad")
    feet = sel("Platform foot", "Angle foot", "Angle junction foot", "Angle jamb foot", "Jamb foot", "Anchor foot")
    tag = lambda q: q["name"].split(", ")[-1]
    wallB = sel("P12 duo, wall B") + [q for q in sel("Clip-lock") if tag(q).startswith("B")]
    wallA = sel("P12 duo, wall A") + [q for q in sel("Clip-lock") if tag(q).startswith("A")]
    stubs = sel("P12 duo, stub", "Groove cover", "L12 corner tail", "Hinge end clip")
    doors = sel("Flap leaf", "Flap sleeve", "Hinge pin", "Split pin", "M6 washer", "Catch stop", "Strike", "N42 disc", "Hinge finger")
    bags = sel("Ballast bag")
    signs = sel("Print zone")
    G = lambda n, qs, ex=(0, 0, 0): grp(n, qs, explode=ex)
    S = {
        1: ("Step 1: mark the plan on the floor and lay the 22 pads", [], [G("EPDM pads (22)", pads, (0, 0, 120))]),
        2: ("Step 2: set the angle, junction, anchor and jamb feet on the pads", [G("pads", pads)], [G("Feet and anchors (22)", feet, (0, 0, 200))]),
        3: ("Step 3: stand the seven wall B duos, folded 30 deg, in their feet and clip each joint", [G("pads", pads), G("feet", feet)],
            [G("Wall B duos and clips", wallB, (0, 600, 0))]),
        4: ("Step 4: stand the seven wall A duos and clip each joint", [G("pads", pads), G("feet", feet), G("wall B", wallB)],
            [G("Wall A duos and clips", wallA, (0, -600, 0))]),
        5: ("Step 5: stand the four zigzag stubs and two corner tails; fit the angle tees and hinge end clips",
            [G("pads", pads), G("feet", feet), G("wall B", wallB), G("wall A", wallA)], [G("Stubs, tails, hinge clips", stubs, (0, 0, 500))]),
        6: ("Step 6: hang the four leaves on their pins; fit the stop clips and finger guards",
            [G("pads", pads), G("feet", feet), G("wall B", wallB), G("wall A", wallA), G("stubs", stubs)], [G("Leaves and catch parts", doors, (0, 0, 500))]),
        7: ("Step 7: lay the filled ballast bags on the anchor and jamb feet; walk round and check",
            [G("pads", pads), G("feet", feet), G("wall B", wallB), G("wall A", wallA), G("stubs", stubs), G("doors", doors), G("signs", signs)],
            [G("Ballast bags (10)", bags, (0, 0, 400))]),
    }
    for k, (title, done, new) in S.items():
        if which and str(k) not in which:
            continue
        print(bv.step(done, new, OUT / f"step-{k:02d}.png", title, size=(10, 6), elev=38, azim=-62, label_done=False))


if __name__ == "__main__":
    cmd, args = (sys.argv[1] if len(sys.argv) > 1 else "all"), sys.argv[2:]
    if cmd in ("overview", "all"):
        print(overview())
    if cmd in ("sheets", "all"):
        sheets(args)
    if cmd in ("joints", "all"):
        joints(args)
    if cmd in ("steps", "all"):
        steps(args)
