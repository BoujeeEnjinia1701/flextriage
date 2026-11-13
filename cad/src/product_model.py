# SPDX-License-Identifier: CERN-OHL-P-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""FlexTriage Origami Bay: product appearance model (kit 1.9), TRL 3, option FT1 (carried; choice awaiting Amish).

Built from components("FT1") in cad/src/model.py with every part used as it is, so every main dimension comes from
the model. Only scale context is added: standing 1.75 m mannequins from .kit/context_parts.py on the same floor
(z = 0) as the feet, one at the entry and one inside zone 2, and a cut copy at doorway 1 for the cutaway render.
APPEARANCE MODEL ONLY. CONCEPT, NOT FOR FABRICATION.
Groups: "shell" (panels, leaves, prints), "internal" (clips, feet, pins, bags), "context" (people), "cut" (doorway 1 cut).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Box, Pos, Rot  # noqa: E402
import model as M  # noqa: E402

TITLE = "FlexTriage Origami Bay: three-zone triage bay of FR twinwall panels"
_SHELL = ("P12 duo", "Flap leaf", "L12 corner", "Print zone")
X_D1 = 2 * M.PITCH

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 30, "az": -60, "args": ["--lens=35"],
     "note": "In a hall or tent beside two 1.75 m people, seen from the front left and above (about 30 deg elevation); "
             "bay 8.2 x 2.3 m with 1.2 m zigzag walls, entry at left, zones 1 intake, 2 assessment and 3 treatment, exit at right"},
    {"name": "studio", "groups": ["shell", "internal"], "explode": False, "el": 45, "az": -50, "args": [],
     "note": "Studio view from the front left and above (about 45 deg elevation): serpentine plan, divider stubs at alternate walls, "
             "one leaf per doorway, feet and site-filled bags"},
    {"name": "cutaway", "groups": ["cut"], "explode": False, "el": 28, "az": -55, "args": [],
     "note": "Doorway 1 cut open, seen from the front left (about 28 deg elevation): divider stub on its anchor foot with two bags, "
             "the leaf on two pin hinges, the stop clip and magnet at wall A"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 30, "az": -60, "args": [],
     "note": "Exploded view from the front left and above (about 30 deg elevation): walls pulled outward, stubs and leaves lifted, "
             "feet lowered"},
]


def product_parts():
    import context_parts
    out = []
    cutter = Pos(X_D1, -600 + 2.0, 700) * Box(2000, 1200, 1600)      # removes wall A in front of doorway 1
    for q in M.components("FT1"):
        d = dict(q)
        d["group"] = "shell" if any(k in q["name"] for k in _SHELL) else "internal"
        out.append(d)
        c = q["shape"].bounding_box().center()
        if abs(c.X - X_D1) < 900 and -400 < c.Y < M.PITCH + 500:
            try:
                h = q["shape"] - cutter if c.Y < 60 else q["shape"]
                if h.volume > 1e-3:
                    cc = dict(q)
                    cc["shape"], cc["group"], cc["name"] = h, "cut", q["name"] + " (cut)"
                    out.append(cc)
            except Exception:
                pass
    for nm, x, y, rz in (("Person at the entry (scale)", -900.0, 1800.0, -70), ("Person in zone 2 (scale)", 3600.0, 1300.0, 160)):
        man = Pos(x, y, 0) * Rot(0, 0, rz) * context_parts.mannequin(1750.0, "stand")
        out.append(dict(name=nm, shape=man, material="clay", material_name="skin", color="#9C9C9E", kind="context",
                        bom=None, group="context", explode=(0, 0, 0), note=""))
    return out


if __name__ == "__main__":
    from collections import Counter
    print(Counter(p["group"] for p in product_parts()))
