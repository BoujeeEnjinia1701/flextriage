# SPDX-License-Identifier: CERN-OHL-P-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""FlexTriage Origami Bay: concept media from the TRL 3 model (option FT1, carried; proposed, awaiting Amish).

Run from the repo root:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process. Geometry comes from
cad/src/model.py; figures come from FXT-CAL-001 (docs/04-calcs/sizing_results.json). Uses the pieces of
.kit/concept.py render_all one at a time, with a 1.75 m person for scale. CONCEPT, NOT FOR FABRICATION.
"""
import csv
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
import concept as K  # noqa: E402
from concept import Part  # noqa: E402
import model as M  # noqa: E402

PROJECT, TITLE, DWG, DATE = "FlexTriage Origami Bay", "Three-zone triage bay of FR twinwall panels (option FT1, proposed)", "FXT-DWG-010", "2026-11-12"
MD = ROOT / "media"
RES = ROOT / "docs/04-calcs/sizing_results.json"
SMALL = ("pin", "washer", "Split", "magnet", "pad", "guard", "Groove")


def parts(small=False, window=None):
    out = []
    for q in M.components(M.CHOSEN):
        if not small and any(s in q["name"] for s in SMALL):
            continue
        if window:
            c = q["shape"].bounding_box().center()
            (x0, x1), (y0, y1) = window
            if not (x0 <= c.X <= x1 and y0 <= c.Y <= y1):
                continue
        out.append(Part(q["name"], q["shape"], q["color"], q["bom"], tuple(q["explode"])))
    return out


def hero():
    ps = K.with_scale_figure(parts())
    return K._render(ps, MD / "hero.png", title=PROJECT, size=(10, 6.5), elev=34, azim=-62,
                     note="Option FT1 (carried; choice proposed, awaiting Amish). Seen from the front left and above, 34 deg elevation; "
                          "grey figure 1.75 m. Bay 8.2 x 2.3 m, zigzag, walls 1.2 m; entry at left, exit at right; zones 1 intake, 2 assessment, "
                          "3 treatment. CONCEPT, NOT FOR FABRICATION")


def cutaway():
    ps = parts(window=((2 * M.PITCH - 1500, 2 * M.PITCH + 1500), (-400, M.Y_B + 400)))
    ps = [p for p in ps if p.shape.bounding_box().center().Y > 150]
    return K._render(ps, MD / "cutaway.png", azim=-55, elev=28, size=(9, 7), title=f"{PROJECT}: cutaway at doorway 1",
                     note="Wall A removed in front; seen from the front left, 28 deg elevation. Divider 1 stands on its anchor foot with two bags; "
                          "the leaf hangs on pins from the stub end and closes on the stop clip at wall A (removed here with the wall). CONCEPT, NOT FOR FABRICATION")


def bom_names():
    out = {}
    for r in csv.DictReader((ROOT / "bom/bom.csv").open()):
        n, _, rest = r["item"].partition(" ")
        out[int(n)] = rest.split(",")[0]
    return out


def exploded():
    names = bom_names()
    ps = []
    for p in parts(window=((M.PITCH - 100, 3 * M.PITCH + 100), (-400, M.Y_B + 400))):
        if p.bom is None:
            continue
        ps.append(Part(names.get(p.bom, p.name), p.shape, p.color, p.bom, p.explode))
    return K._render(ps, MD / "exploded.png", offsets=True, labels=True, size=(11, 8), elev=30, azim=-60,
                     title=f"{PROJECT}: exploded view of zone 2 and doorway 1",
                     note="Seen from the front left and above, 30 deg elevation; numbers match bom/bom.csv. Walls pulled outward, "
                          "stub and leaf lifted, feet lowered")


def flow():
    r = json.loads(RES.read_text())
    z = r["plan"]["zones_m2"]
    fl = r["flap"]
    stages = [("Entry, push leaf", f"{fl['door_clear_floor_mm']} mm clear"),
              ("1 Intake", f"{z['1 Intake']} m2"),
              ("Doorway 1", f"push {fl['push_force_N']} N"),
              ("2 Assessment", f"{z['2 Assessment']} m2"),
              ("Doorway 2", "one way"),
              ("3 Treatment", f"{z['3 Treatment']} m2"),
              ("Exit, push leaf", "way-out sign")]
    return K.flow_diagram(stages, MD / "flow.png",
                          f"{PROJECT}: one-way patient flow through the serpentine bay (estimates, FXT-CAL-001); "
                          "leaves open downstream only; staff return by pulling", "")


def web():
    return K.export_web_model(parts(), "media", title=f"{PROJECT}: {TITLE}")


def blueprint():
    from build123d import Compound
    from drawing import Sheet, project_views
    r = json.loads(RES.read_text())
    ps = parts()
    shown = K.with_scale_figure(parts())
    views = project_views(Compound(children=[p.shape for p in ps]), MD / "_views", center_lines=False)
    views["iso"] = project_views(Compound(children=[p.shape for p in shown]), MD / "_views_fig", center_lines=False)["iso"]
    pl = r["plan"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P1", author="Amish Chadha", date=DATE, theme="blueprint",
              material="Detailed TRL 3 model for concept communication",
              revisions=[("P1", "Concept sheet from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 118, label="Isometric view", sublabel="Not to scale; grey is a 1.75 m person")
    s.add_notes("Key figures (estimates, FXT-CAL-001)", [
        f"Bay {pl['length_m']:.2f} x {pl['width_m']:.2f} m, walls 1.2 m; interior {pl['interior_m2']} m2",
        f"Three zones {pl['zones_m2']['1 Intake']}, {pl['zones_m2']['2 Assessment']}, {pl['zones_m2']['3 Treatment']} m2; one-way flow",
        f"18 P12 duos, 4 leaves, 2 tails from {r['panels']['sheets']} FR sheets",
        f"Mass {r['mass_total_kg']} kg with bags (deck target 12 kg: not met)",
        f"Tips at {r['tip']['piece_A_2_bags_per_stub_N']:.0f} N next to a stub with 2 bags; walls between stubs are boundaries only",
        f"Leaf push about {r['flap']['push_force_N']} N; doorway {r['flap']['door_clear_floor_mm']} mm clear",
        f"Deploy {r['deploy_min']['with_F6'][0]} to {r['deploy_min']['with_F6'][1]} min for two people (estimate)",
        f"Parts USD {r['cost']['bom_total']:.0f} (target USD 800); indoor or in-tent only"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w_ in sys.argv[1:] or list(fns):
        print(w_, "->", fns[w_]())
