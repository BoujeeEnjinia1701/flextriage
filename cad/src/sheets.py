# SPDX-License-Identifier: CERN-OHL-P-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""FlexTriage Origami Bay: drawing set and STL export for option FT1 (carried in the drawing set; choice awaiting Amish).

Run from the repo root, one sheet per process on a small machine:  python cad/src/sheets.py [ga|door|stl]
    cad/drawings/FXT-DWG-001   general arrangement, three-zone serpentine bay of P12 duos
    cad/drawings/FXT-DWG-002   doorway detail: hinge clips, flap leaves, pins, magnetic catch, jamb feet
    cad/stl/*.stl              one of each made part, for printing the clips and feet
Making sketches for each made part (FXT-DWG-101 onward) are drawn by cad/src/build_plan_media.py.
Sheets are generated from cad/src/model.py and never edited by hand; figures come from FXT-CAL-001.
CONCEPT, NOT FOR FABRICATION.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
from build123d import Box, Compound, Pos, export_stl  # noqa: E402
from drawing import Sheet, project_views  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
DATE = "2026-11-12"
DWG = ROOT / "cad/drawings"
R = json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())
PROJECT = "FlexTriage Origami Bay"
MAT = "FXP-S4FR 4 mm FR PP twinwall (FXP-PLT-001); PETG printed clips and feet; stainless pins; see bom/bom.csv"
SKIP = ("Print zone", "EPDM pad", "Split pin", "washer (ISO", "M6 washer")


def body(skip=SKIP):
    return [q for q in M.components("FT1") if q["kind"] != "context" and not any(s in q["name"] for s in skip)]


def ga():
    parts = body(SKIP + ("Hinge pin", "magnet", "strike"))
    work = DWG / "_views_ga"
    views = project_views(Compound(children=[q["shape"] for q in parts]), work, center_lines=False)
    s = Sheet(project=PROJECT, title="Three-zone triage bay of P12 duo panels (option FT1): general arrangement",
              dwg_no="FXT-DWG-001", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None, material=MAT,
              revisions=[("P1", "Preliminary GA from the TRL 3 model (FXT-CAL-001)", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale; seen from the front left and above")
    pl = R["plan"]
    s.add_notes("Key dimensions (mm) and data", [
        f"Bay {pl['length_m'] * 1000:.0f} x {pl['width_m'] * 1000:.0f} on joint lines; walls {P['H_WALL']:.0f} high on 12.5 mm seats",
        f"Joint pitch {P['PITCH']:.1f} (duo plus 12 clip core, folded 30 deg: zigzag walls)",
        f"Zones: 1 intake {pl['zones_m2']['1 Intake']}, 2 assessment {pl['zones_m2']['2 Assessment']}, 3 treatment {pl['zones_m2']['3 Treatment']} m2",
        "18 P12 duos, all folded 30 deg: 7 per long wall, 4 zigzag stubs (doorways at alternate sides)",
        f"4 doorways, one leaf each, {P['FLAP_W']:.0f} x {P['FLAP_H']:.0f}, pin hinges, magnetic catch",
        f"Clear doorway {R['flap']['door_clear_floor_mm']} at the floor",
        "8 angle feet, 6 angle junction and jamb feet, 4 anchor feet, 2 jamb feet, 2 tail feet, all on 2 mm EPDM pads",
        "2 corner tails (600) outside the end-stub corners",
        "10 site-filled 5 kg sand bags: 2 per anchor foot, 1 per jamb foot",
        f"Floor needed {pl['length_m'] + 0.6:.1f} x {pl['width_m'] + 0.6:.1f} m; indoor or in-tent only",
        f"Mass {R['mass_total_kg']} kg with bags; parts USD {R['cost']['bom_total']:.2f}",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "FXT-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/FXT-DWG-001.svg, .pdf, .png")


def door():
    x0 = 2 * P["PITCH"]
    parts = []
    for q in body(("Print zone", "EPDM pad", "Ballast bag", "P12 duo", "Hinge pin", "magnet", "strike")):
        c = q["shape"].bounding_box().center()
        if abs(c.X - x0) < 700 and -300 < c.Y < P["PITCH"] + 400:
            parts.append(q["shape"])
    work = DWG / "_views_door"
    views = project_views(Compound(children=parts), work, center_lines=False)
    s = Sheet(project=PROJECT, title="Triage bay doorway 1 (option FT1): leaf, pin hinges and magnetic catch",
              dwg_no="FXT-DWG-002", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None, material=MAT,
              revisions=[("P1", "Preliminary doorway detail from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"], dims=True)
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Doorway 1 cut from the bay; not to scale")
    s.add_notes("Doorway hardware", [
        "Hinge jamb (stub end): anchor foot with its clip, hinge end clip above",
        f"One leaf {P['FLAP_W']:.0f} x {P['FLAP_H']:.0f}, bottom {P['FLAP_Z']:.0f} above the floor, opens downstream",
        "Sleeve clips on the leaf ride on 6 mm stainless pins",
        "Lower hinge bears on an M6 washer; split pins under both",
        f"Catch at {P['CATCH_Z']:.0f}: stop clip on the wall jamb, N42 disc behind 2 mm",
        f"Strike: stainless M8 washer in the holder; about {R['flap']['magnet_at_gap_N']} N hold, {R['flap']['push_force_N']} N push",
        "EPDM finger guards over the hinge gap",
        f"Clear width {R['flap']['door_clear_floor_mm']} at the floor (ADA 815, stretcher 750)",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "FXT-DWG-002")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/FXT-DWG-002.svg, .pdf, .png")


def stl():
    out = ROOT / "cad/stl"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.stl"):
        old.unlink()
    shapes = {"clip-angle": M.joint_clip((15.0, 165.0), "full"), "clip-angle-tee-75": M.joint_clip((75.0, 195.0, 345.0), "full"),
              "clip-angle-tee-105": M.joint_clip((105.0, 195.0, 345.0), "full"),
              "hinge-end-clip": M.hinge_end("full"), "flap-sleeve-clip": M.sleeve("full"), "anchor-foot-75": M.anchor_foot(75.0, "full"),
              "anchor-foot-285": M.anchor_foot(285.0, "full"),
              "catch-stop-clip-angle": M.stop_clip((195.0, 345.0), 1, "full"), "catch-stop-clip-end": M.stop_clip((195.0,), 1, "full"),
              "strike-holder": M.strike_holder("full"), "platform-foot-inline": M.tee_foot(), "jamb-foot": M.jamb_foot(),
              "angle-foot": M.angle_foot((195.0, 345.0)), "angle-jamb-foot": M.angle_foot((195.0, 345.0), inside=False),
              "angle-junction-foot-75": M.angle_foot((75.0, 195.0, 345.0), inside=False, junction=True),
              "angle-junction-foot-105": M.angle_foot((105.0, 195.0, 345.0), inside=False, junction=True)}
    for nm, sh in shapes.items():
        export_stl(sh, str(out / f"fxt-{nm}.stl"), tolerance=0.05, angular_tolerance=0.2)
    print("wrote", len(list(out.glob("*.stl"))), "STL files to cad/stl/")


if __name__ == "__main__":
    fns = {"ga": ga, "door": door, "stl": stl}
    for w in sys.argv[1:] or list(fns):
        fns[w]()
