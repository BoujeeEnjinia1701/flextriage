# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""FlexTriage Origami Bay: STEM check calculations (FXT-STM-001, STANDARDS sections 20 and 25.6a).

Run from the repo root:  python docs/04-calcs/sizing.py      (writes sizing_results.json)
                         python docs/04-calcs/stem_check.py  (writes stem_results.csv, stem_results_options.csv and
                                                              refreshes the two tables in docs/01b-stem-check.md)
Rows S1 to S44 check the carried option FT1 (the team's origami panel bay, iteration 2, as made constructable here).
Rows X1 to X14 check FT2 (tensioned fabric screens), FT3 (floor marking and belt stanchions) and the P18 variant of FT1.
Platform claims (sheet, clips, folds, disinfection, fire grade) are checked once in FXP-PLT-001 (rows P1 to P26) and
are cited here, not repeated. Sources and dates checked (2026-11-12) are in FXT-STM-001 and FXT-CAL-001.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
from stem_check import Check, WITHIN, PLAUSIBLE, FIX, FAILS  # noqa: E402,F401
import model as M  # noqa: E402

P = M.PARAMS
R = json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())
CAL = "FXT-CAL-001"
PLT = "FXP-PLT-001"
c = Check(ROOT / "docs/04-calcs/stem_results.csv")
x = Check(ROOT / "docs/04-calcs/stem_results_options.csv")
pk, pl, sw, tp, fl = R["pack_12kg"], R["plan"], R["self_weight"], R["tip"], R["flap"]

# ---- mass, area and pack (the deck's 12 kg claim) -------------------------------------------------------------------
REV = "independent review 2026-11-12"
an, pr = R["anchor"], R["printing"]
c.cited("S1", "A 3-zone bay packs into 2 carry bags under 12 kg in total (team deck)", "Mathematics", "Orders of magnitude",
        f"Mass budget from the model at 0.70 kg/m2 ({PLT} D1, F5) and PETG at 1.27 g/cm3; 12 kg less two empty bags buys "
        f"{pk['sheet_m2_if_no_hardware']} m2 of sheet with no hardware ({pk['wall_m_at_1200_if_no_hardware']} m of 1.2 m wall)",
        f"FT1 needs {R['panels']['wall_m2']} m2 of wall, {R['panels']['flap_m2']} m2 of leaves and two tail leaves (sheet "
        f"{R['mass_kg']['duo panels'] + R['mass_kg']['flap leaves'] + R['mass_kg']['corner tail leaves']:.1f} kg) plus {R['mass_hardware_kg']} kg of clips, "
        f"feet, pins, pads and prints: {R['mass_total_kg']} kg with bags, {pk['ratio']} times the claim. The panels alone exceed 12 kg. "
        f"{pk['bags_at_12kg']} bags of 12 kg or {pk['bags_at_20kg']} of 20 kg; a two-zone bay is {R['zones_config']['two_zone_kg']} kg. The platform's own "
        f"zigzag U bay is {R['pack_D15']['platform_U_bay_kg']} kg ({PLT} P17, D15); with moulded cored feet (0.15 kg) and clips (0.04 kg), platform D15 (b), "
        f"this bay is still about {R['pack_D15']['moulded_cored_kg']} kg, so only a higher target in more bags fits it. At 800 g/m2 the "
        f"sheet would weigh {(R['mass_kg']['duo panels'] + R['mass_kg']['flap leaves'] + R['mass_kg']['corner tail leaves']) * 8 / 7:.1f} kg ({REV}: holds). "
        "Changing the pack target changes a user-facing claim", FIX, closed_by="Proposed, awaiting Amish: FXT-DEC-001 D2")
c.cited("S2", f"A functional 3-zone bay of about 20 m2 needs {R['panels']['duos']} P12 duos, {R['panels']['flaps']} flap leaves and 2 tail leaves "
        f"({R['panels']['sheets']} sheets of 1,220 x 2,440 mm)", "Mathematics", "Units and dimensional analysis",
        "Plan geometry from the model: two zigzag long walls of 7 duos, four zigzag stubs, four doorways with one leaf each, two corner tails",
        f"{R['panels']['wall_length_m']:.1f} m of wall; interior {pl['interior_m2']} m2 on joint lines, about 1 % less clear (zones "
        f"{', '.join(f'{k} {v}' for k, v in pl['zones_m2'].items())} m2)", WITHIN, closed_by=f"{CAL} section 2")
sh = R["sight_hidden_m"]
c.cited("S3", "A 1.2 m wall marks a boundary between cohorts; the plan keeps the 1 m spacing WHO asks for; it is not a privacy screen",
        "Biology", "Human physiology and biomechanics",
        "WHO AFRO triage stations: seats at least 1 m apart, 1 to 2 m between health worker and patient, one-way flow; ANSUR II eye heights (NCSU summary)",
        f"Zones are {pl['width_m']:.2f} m wide on joint lines, so the layout gives the spacing. Every standing adult (eye 1,421 to 1,753 mm) sees heads and upper bodies over a "
        f"{P['H_WALL'] + M.Z0:.0f} mm wall, but a short observer 0.5 m from it cannot see a patient on a floor stretcher for {sh['stretcher top 250 mm']} m "
        f"behind it, or a trolley top for {sh['trolley top 800 mm']} m ({REV}: weak, restated). A staff-position rule (stand at a doorway, not at a wall) "
        f"goes in the procedure; separation is never by airflow ({PLT} L1)", WITHIN, closed_by="FXT-CLM-001; PR-003; FXT-DEC-001 D3 (height)")
c.cited("S4", "Zigzag P12 walls and stubs stand under their own weight, cold and hot", "Physics", "Elastic stability",
        f"Greenhill self-weight buckling of a flat strip ({PLT} P2): h_cr = (7.837 EI/q)^(1/3) = {sw['h_cr_flat_mm']} mm; a 600 mm leaf held on both "
        f"vertical edges by a 30 deg fold or angle clip, orthotropic formula with zero twisting stiffness ({PLT} P3); hot = half the 23 C stiffness "
        f"({PLT} section 10); platform load factor 2",
        f"As drawn in v0.1 (flat duos, inline joints) a P12 strip had factor {sw['load_factor_flat_P12']} cold and {sw['load_factor_flat_P12_hot']} hot, "
        f"failing hot ({PLT} v0.2 agrees, 0.87; platform request 1). Fixed with the platform's v0.2 rule S1: every wall and stub is a zigzag, leaves at "
        f"15 deg, folds and angle clips at 30 deg, inline joints only where a tee return meets them (rule S4). A held leaf is {sw['leaf_both_edges']} cold "
        f"and {sw['leaf_both_edges_hot']} hot; a leaf with one free edge (the wall ends at the entry and exit, the tails) about {sw['leaf_free_edge']} cold "
        f"and {sw['leaf_free_edge_hot']} hot (A16, an assumed plate coefficient); a flap leaf hung from its lower sleeve {sw['flap_hung']} cold and "
        f"{sw['flap_hung_hot']} hot. All exceed 2 cold and 1 hot; the free-edge figure rests on an assumed coefficient", PLAUSIBLE,
        closed_by=f"{PLT} rule S1 (F1, v0.2); FXT-DEC-001 F10 (standing instruction); T7 hot soak at TRL 4")
c.claim("S5", "A long wall pushed outward with 178 N at the BIFMA height next to a stub joint does not tip", "Physics", "Mechanics and statics",
        f"Rigid wall piece about the outside outrigger tips, as {PLT} P7; push at {tp['z_push_mm']:.0f} mm; unballasted {tp['piece_A_0_bags_per_stub_N']} N "
        f"(fails); two 5 kg bags on each stub's anchor foot, which now lifts with the stub ({REV}: refuted as first drawn, the stub lifted out of a plain foot "
        f"slot); anchor uplift {an['uplift_N']} N against {an['peg_capacity_N']} N for two through-pegs ({PLT} v0.2 P9; v0.1 used 201 N, factor "
        f"{an['v01_factor']}), factor {an['factor']}; the tee clips carry the stub's {an['tee_shear_N']} N of lift in shear against {an['tee_capacity_N']} N, "
        f"factor {an['tee_factor']}. {PLT} P9 now fails with a fix proposed (D14): demand on a clip in a bowing leaf is not bounded on paper",
        tp["piece_A_2_bags_per_stub_N"], 178.0, "N", rule="above",
        closed_by="FXT-DEC-001 F4 (standing instruction, 2026-10-23); T3 peg uplift, T7 tip test at TRL 4")
c.cited("S6", "A push anywhere along a long wall, away from a stub, does not tip the wall", "Physics", "Mechanics and statics",
        f"A lone zigzag P12 duo on two feet tips at {tp['single_duo_N'][0]} N outward and {tp['single_duo_N'][1]} N inward ({PLT} P6 method, leaves "
        f"78 mm outside the joint line); a free wall end at the entry or exit jamb at {tp['free_wall_end_N'][0]} N outward and {tp['free_wall_end_N'][1]} N "
        f"inward; a zigzag stiffens the wall up its height, not along it, so it still cannot carry a push sideways to the stubs (a 600 mm leaf bows past "
        f"25 mm at 5.8 N, {PLT} P4)",
        f"Fails: between stubs the walls tip at about 5 to 15 N against 178 N ({REV}: refuted). Buttresses every 1.2 m would each need about 20 kg of "
        "ballast; the honest options are a stated limit (boundaries that tip if leant on, as platform limit L1) with a lower lateral criterion, or a "
        "different structure. A scope and safety trade-off", FIX, closed_by="Proposed, awaiting Amish: FXT-DEC-001 D7; FXP-PLT-001 D5")
sj = R["stub_joint"]
c.claim("S7", "A tee joint carries a stub's overturning couple into the long wall in edge bearing", "Engineering and technology",
        "Joint design", f"Couple 178 N x {tp['z_push_mm']:.0f} mm over the 900 mm between clip heights: {sj['clip_force_N']} N per clip height, borne by "
        f"the pushed-side wall leaf's edge on the round core of the angle tee over 100 mm and both 0.26 mm skins; at a corner there is no panel beyond the joint, so the "
        f"couple fell on peg tension ({sj['clip_pullout_N']} N per clip, factor about 1, {REV}: refuted). Fixed: a 600 mm tail leaf outside each "
        f"end-stub corner makes it a tee (F7). Bearing stress in MPa against half of the PP yield of 24 MPa",
        sj["edge_bearing_MPa"], 12.0, "MPa", rule="below", closed_by="FXT-DEC-001 F7 (standing instruction); T3 and T7 at TRL 4")
sl = R["slide"]
c.cited("S8", "The bay does not slide when bumped with 178 N next to a stub", "Physics", "Mechanics and statics",
        f"Friction mu W of the pushed piece ({sl['piece_kg']} kg with ballast); hard plastic feet mu 0.2 to 0.35, rubber on concrete 0.45 to 0.85 "
        "(Engineering ToolBox)",
        f"Bare PETG feet slide at {sl['slide_bare_N'][0]} to {sl['slide_bare_N'][1]} N (fails). Fixed with a 2 mm EPDM pad under every foot "
        f"(F5): {sl['slide_pads_N'][0]} to {sl['slide_pads_N'][1]} N, so the wet low end only just reaches 178 N; a single duo between stubs slides at a "
        f"few newtons, as S6 ({REV}: weak). Friction on wet clinical vinyl with hypochlorite to measure", PLAUSIBLE,
        closed_by="FXT-DEC-001 F5 (standing instruction); T7 at TRL 4")
dm = R["deploy_min"]
c.cited("S9", "Two people with no training deploy a functional 3-zone bay in under 15 minutes (team decision gate)", "Biology", "Ergonomics",
        "Step count from the model (20 panels, 46 clips, 22 feet, 22 pads, 4 leaves, 8 pins, 10 bags) x ASSUMED action times, two people at "
        "70 to 85 % useful time (A9, A10)",
        f"As first drawn {dm['as_drawn'][0]} to {dm['as_drawn'][1]} min: fails at both ends. With fix F6 (sleeves and strike holders stay on the leaves, "
        f"pads bonded under the feet, bags filled before the clock and laid in 10 to 20 s) {dm['with_F6'][0]} to {dm['with_F6'][1]} min: the fast end meets "
        f"15 min, the slow end does not ({REV}: weak). Error modes (wrong foot type, stub on the wrong wall) not counted. Only the timed trial can close it",
        PLAUSIBLE, closed_by="FXT-DEC-001 F6; decision gate test V1 at TRL 4")
c.cited("S10", "One zone goes from flat pack to standing in under 5 minutes (team deck)", "Biology", "Ergonomics",
        "Two duos, three feet, seven clips, one leaf on two pins and two filled bags at the A9 times",
        f"{dm['one_zone_min'][0]} to {dm['one_zone_min'][1]} min including the leaf and ballast ({REV}: weak, now counted); assumed times", PLAUSIBLE,
        closed_by="V1 at TRL 4")
c.cited("S11", "The magnetic catch holds a leaf shut against a draught and the leaf opens with no more than 22.2 N", "Physics", "Electromagnetism and circuits",
        f"N42 disc 12.7 x 3.2 mm: {fl['magnet_contact_N']} N to a thick steel plate at contact (K&J D82); pull scaled with B squared on the disc axis "
        f"(A13) to a {P['COVER'] + 0.5:.1f} mm gap; push plate at 956 mm from the hinge against the catch at {P['FLAP_W'] + 6:.0f} mm; ADA 404.2.9 22.2 N used as the push "
        "target (ADA itself excludes catch release)",
        f"First drawn as two leaves meeting edge to edge, the catch acted in shear and held about 2 N ({REV}: refuted). Fixed (F3): one leaf per doorway, "
        f"opening downstream only, closing on a stop block upstream with the magnet in pull on a stainless strike: about {fl['magnet_at_gap_N']} N at the catch, "
        f"{fl['push_force_N']} N at the push plate, against a draught need of {fl['draught_edge_N'][0]} to {fl['draught_edge_N'][1]} N. Thin-strike and "
        "gap losses are first order; measured hold to set the cover", PLAUSIBLE, closed_by="FXT-DEC-001 F3 (standing instruction); V3 at TRL 4")
c.claim("S12", "Each doorway passes a stretcher and a wheelchair", "Engineering and technology", "Standards practice",
        f"Clear width at the floor between the wall jamb's foot and the anchor foot, whose block sits 15 deg off the doorway line; ADA 404.2.3 clear width "
        f"815 mm; fabric stretcher 750 mm wide (CQC NATO); {fl['door_clear_end_mm']} mm at the entry and exit; {fl['door_clear_approach_mm']} mm in the "
        f"upstream approach beside the bags; {fl['door_clear_open_flaps_mm']} mm past the open leaf",
        fl["door_clear_floor_mm"], 815.0, "mm", rule="above", closed_by=f"{CAL} section 7; turning space in S32")
c.cited("S13", "The bay never narrows the host tent's or room's exits", "Engineering and technology", "Standards practice",
        "Minnesota State Fire Code tent sheet (MSFC 3103.12): 2 exits of 72 in (1,829 mm) for 10 to 199 occupants; egress paths kept clear and unobstructed",
        f"A placement rule, not physics ({REV}: weak): the bay needs {pl['length_m'] + 0.6:.1f} x {pl['width_m'] + 0.6:.1f} m plus 1.5 m of approach at the "
        "entry and exit, so a host tent or hall at least about 12 x 4 m clear of its exit routes; its own doorways are internal and narrower than a tent exit",
        WITHIN, closed_by="PR-019; FXT-REG-001 R4")
fi = R["fire"]
c.cited("S14", f"The bay adds about {fi['MJ_all']} MJ of fire load", "Chemistry", "Materials and polymer chemistry",
        f"{PLT} P23: 27.8 MJ/m2 of FXP-S4FR (PP 39.7 MJ/kg, FSRI); PET gross heat of combustion 21.4 MJ/kg (UQ fire laboratory) for the PETG parts "
        "and polyester bags",
        f"Sheet {fi['MJ']} MJ, PETG clips and feet {fi['MJ_PETG']} MJ (not FR rated), bags {fi['MJ_bags_and_pads']} MJ ({REV}: refuted at 851 MJ, now "
        f"counted); {fi['MJ_P18']} MJ of sheet at P18. True, so the FR sheet is mandatory, PETG parts are few and small, and the bay stays 1 m from "
        "heaters and flames", WITHIN, closed_by=f"{PLT} rule FR1; FXT-DEC-001 C9 (FR clip grade)")
c.cited("S15", "The bought sheet is the platform FR grade (NFPA 701 TM1, at most 700 g/m2)", "Engineering and technology", "Standards practice",
        f"{PLT} P24 and F5; the priced listing (cplast.net 48964WFR) says its FR board 'meets most city and state codes' and links a data sheet",
        "Grammage and an NFPA 701 TM1 and ASTM E84 report for the bought lot are not on the listing; at 800 g/m2 the sheet mass rises by 1/7 (S1)",
        PLAUSIBLE, closed_by=f"FXT-DEC-001 C1; {PLT} T8")
c.cited("S16", "Sheet, clips, pads, pins, strikes and the enclosed magnet tolerate 0.5 % hypochlorite and 70 % alcohol wipes", "Chemistry",
        "Materials and polymer chemistry", f"{PLT} P18 to P20 for PP and PETG; EPDM and stainless not on those charts; chloride pits zinc plating",
        f"Strikes and washers changed to stainless (A2 is weakly magnetic, so a ferritic grade may be needed, C7); a printed 2 mm cover is not a hermetic "
        f"seal, so the magnet pocket is sealed with a bonded cap ({REV}: weak); EPDM and the cap to the T4 coupons", PLAUSIBLE, closed_by=f"{PLT} T4")
c.cited("S17", "Every surface facing a care zone can be wiped", "Biology", "Microbiology",
        f"{PLT} v0.2 rules E1 (cut edges, groove shoulders and ends, holes sealed), E2 (groove face away from care zones, or covered by a flexible "
        f"clear PP strip) and E3 (clips off for cleaning); the 13.6 mm flat-bottomed groove is on every duo's back face",
        "Wall grooves face outside the bay (print faces in), so they meet E2 by layout. The four stubs face a zone on both sides: their groove is covered "
        "by a clear PP strip heat-staked or taped along both shoulders (F2, now platform rule E2; platform request 2 resolved). Strip lift under wiping is "
        f"unproven ({REV}: weak)", PLAUSIBLE, closed_by=f"FXT-DEC-001 F2; {PLT} E2; {PLT} T6")
c.cited("S18", "Hinges, catches, clip slots, pads and feet can be cleaned between uses", "Biology", "Microbiology",
        f"Clip slots have 0.25 mm clearance a side (4.5 mm slot, {PLT} v0.2); pin hinges, stop blocks and foot slots are crevices; pads sit at floor level",
        f"Cleanable only with the leaves lifted off their pins, clips removed ({PLT} rule E3) and pads bonded and edge-sealed (F5); disassembly time "
        "counted in turnaround",
        PLAUSIBLE, closed_by=f"V4 at TRL 4; {PLT} T6")
c.cited("S19", "Colour-coded zones are read the same way by every team", "Biology", "Human physiology and biomechanics",
        "START (CHEMM): red immediate, yellow delayed, green minor, black expectant; SALT and the Model Uniform Core Criteria: immediate red, delayed yellow, "
        "minimal green, expectant gray, dead black; ISO 3864-1: red prohibition and fire, yellow warning, blue mandatory, green safe condition",
        "The deck's 'green zone' and 'red zone' for process steps would read as triage categories and as ISO safe and fire colours (fails as drawn). Fixed "
        "(F1): process zones carry a numeral, a word and an arrow on neutral white and black; the way out of the bay is a neutral sign, not an ISO 7010 "
        f"emergency exit ({REV}: weak, corrected); red, yellow and green appear only as category bands with the category word ({PLT} C2, C4)", WITHIN,
        closed_by=f"FXT-DEC-001 F1 (standing instruction); {PLT} T5")
lg = R["legibility_m"]
c.claim("S20", "Zone words can be read from anywhere in their own zone", "Biology", "Human physiology and biomechanics",
        f"ANSI Z535 ratio (25 ft per inch of letter height), halved for poor light; 60 mm words and 150 mm numerals in a band 1,015 to 1,195 mm above the "
        f"floor (ADA 703.5.6); distance in m against the largest zone's diagonal ({REV}: weak, restated per zone)",
        lg["zone word 60 mm"][0], R["legibility_need_m"], "m", rule="above",
        closed_by=f"Numerals {lg['zone numeral 150 mm'][0]} to {lg['zone numeral 150 mm'][1]} m; {CAL} section 9")
c.cited("S21", "Cues are understood across languages and cultures", "Biology", "Human physiology and biomechanics",
        "ISO 7010 aims at safety information that 'relies as little as possible on the use of words'; WHO EMT minimum standards ask for interpreters at "
        "triage and respect for cultural aspects such as separation of gender in waiting areas",
        "Numerals, arrows and symbols carry most of it; words in the local languages; colour meanings vary by culture: to assess with the field partner",
        PLAUSIBLE, closed_by=f"{PLT} T5 with users at TRL 4")
c.cited("S22", "The 3-zone bay fits the deck's 20 m2 of floor", "Mathematics", "Units and dimensional analysis",
        "Zone areas from the plan; outriggers reach 300 mm outside every wall line; approach at entry and exit",
        f"Interior {pl['interior_m2']} m2 on joint lines (the zigzag walls shorten the pitch to {P['PITCH']:.0f} mm), a little under 20 m2, and the bay needs {pl['length_m'] + 0.6:.1f} x {pl['width_m'] + 0.6:.1f} m ({pl['footprint_m2']} m2) of clear floor "
        f"plus about 1.5 m of approach at each end ({REV}: weak, the claim fails as stated). Restating the site requirement is a user-facing change", FIX,
        closed_by="Proposed, awaiting Amish: FXT-DEC-001 D4")
co = R["cost"]
c.cited("S23", f"The prototype bay's parts cost about USD {co['bom_total']:.0f}, against the USD 800 value-engineering target", "Mathematics",
        "Orders of magnitude", "Priced BOM (bom/bom.csv), cited prices checked 2026-11-12; printed parts at filament cost",
        f"USD {co['bom_total']:.2f}, USD {co['over']:.2f} over the target (a value-engineering target, not a limit, STANDARDS 18); drivers sheet USD "
        f"{co['drivers'][0][1]:.0f} and freight USD {co['drivers'][1][1]:.0f}. A print service at USD 0.10/g would add about USD {pr['service_extra_usd']}; "
        f"{pr['petg_kg']} kg of PETG is about {pr['print_hours']} printer-hours at 20 g/h (A11). At the 1,100-sheet price the sheet falls by USD "
        f"{co['sheet_saving_volume']:.0f}; under USD 500 is not shown ({REV}: refuted as 'plausible', restated as a number)", WITHIN,
        closed_by="FXT-MKT-001; value engineering in FXT-DEC-001")
c.cited("S24", "Panels, clips, hinges and catches survive 50 or more deployments", "Engineering and technology", "Fatigue",
        f"{PLT} P13, P14 (hinge strain 4.0 %, snap strain 1.4 %); about 200 passages a day per doorway ASSUMED: 2,800 swings in a two-week use, "
        "140,000 in 50 uses",
        f"Clips and folds as the platform; the leaf's stainless pin in a printed bore and the catch see 150,000 cycles over the life ({REV}: weak, raised)",
        PLAUSIBLE, closed_by=f"{PLT} T2, T3; V3 at 150,000 cycles at TRL 4")
c.cited("S25", "The bay is for use indoors or inside a tent", "Physics", "Fluid mechanics", f"{PLT} P8 and limit L2 (10 m/s exceeds the ballasted restoring moment)",
        "Inherited from the platform; lower walls lower the wind moment but do not change the limit", WITHIN, closed_by=f"{PLT} D6 (proposed, awaiting Amish)")
c.cited("S26", "The bay supports IPC cohorting practice; it makes no claim on airborne or droplet transmission", "Biology", "Epidemiology",
        f"{PLT} L1 and STANDARDS 25.5b; WHO AFRO and CDC rely on distance, PPE and ventilation, not partitions",
        "Claims limited to physical separation, one-way flow and cues (FXT-CLM-001)", WITHIN, closed_by="FXT-CLM-001")
c.cited("S27", "The bay stands on uneven field floors (team risk)", "Physics", "Mechanics and statics",
        "Feet seat each panel 12.5 mm above the floor on a 2 mm pad; a duo spans 1.17 m between feet",
        "A floor step larger than the pad's give racks the joint; slope and step tolerance are to measure", PLAUSIBLE, closed_by="T7 on a 1:50 slope at TRL 4")
c.cited("S28", "Ballast bags lie clear of the leaf's swing and the doorway's clear width", "Biology", "Human physiology and biomechanics",
        "Leaves open downstream only; bags stacked on the upstream outrigger of each anchor foot (F8); jamb feet keep only their outside outrigger",
        f"First drawn, a leaf swept 3.5 mm over a bag ({REV}: refuted). Now no bag lies under a swing; bags reach 165 mm into the upstream approach, leaving "
        f"{fl['door_clear_approach_mm']} mm; bags and feet are marked on the floor", WITHIN, closed_by="FXT-DEC-001 F3, F8 (standing instruction)")
c.cited("S29", "Smoke from the FR sheet in a fire is no worse than other FR plastics in a care space", "Biology", "Toxicology",
        f"{PLT} section 2.2 and D11: brominated FR with antimony trioxide; combustion products include hydrogen bromide and antimony oxides",
        "To assess with the halogen-free FR question (platform D11)", PLAUSIBLE, closed_by=f"{PLT} D11")
zc = R["zones_config"]
c.cited("S30", "The bay configures to 2 to 4 zones and each configuration stands next to its stubs", "Mathematics", "Units and dimensional analysis",
        "Each further zone adds 2 pitches: two wall duos, one stub, one leaf and their hardware; rigid-piece tipping as S5",
        f"Two-zone about {zc['two_zone_kg']} kg, four-zone about {zc['four_zone_kg']} kg; in a two-zone bay each wall carries one stub and tips at "
        f"{tp['two_zone_one_stub_2_bags_N']} N with two bags, so it needs {tp['two_zone_bags_needed_kg']} kg (three bags) at that stub ({REV}: weak)", WITHIN,
        closed_by=f"{CAL} section 5; configuration rule in PR-006")
# ---- claims the independent review found missing (2026-11-12) -------------------------------------------------------
c.cited("S31", "The bay is not an impact barrier", "Physics", "Mechanics and statics",
        "A 150 kg trolley at 1 m/s carries 75 J (ASSUMED case); the energy to tip one wall piece is about 27 J and one duo about 1 J",
        "A trolley or a falling person knocks walls over; stated in the claims register and on the zone signs ('boundary, do not lean')", WITHIN,
        closed_by="FXT-CLM-001; D7")
c.cited("S32", "A stretcher can be turned through the serpentine doorways", "Biology", "Ergonomics",
        "Zone clear width about 2.35 m; a 2.1 m stretcher with a bearer at each end about 2.9 m long (ASSUMED); doorways 1.2 m wide at alternate sides",
        "Not shown on paper: the swept path through a 90 deg turn in a 2.35 m zone is tight; a swept-path drawing and a mock-up walk-through decide it",
        PLAUSIBLE, closed_by="V1 mock-up walk-through at TRL 4")
c.cited("S33", "People can leave the bay quickly in an emergency", "Engineering and technology", "Standards practice",
        "Each zone has two doorways; leaves open downstream with a push of about 16 N (S11) and are pulled the other way; walls are 1.2 m high",
        "Forward evacuation passes 1 to 3 leaves; backward needs a pull. Leaves lift off their pins in seconds for a mass move; evacuation drill in V1",
        PLAUSIBLE, closed_by="V1 at TRL 4; FXT-RSK-001")
c.cited("S34", "The hinge side of a leaf does not trap fingers", "Biology", "Human physiology and biomechanics",
        "Leaf and stub edges each sit 6 mm from the pin axis, so the hinge gap opens and closes between about 0 and 12 mm as the leaf swings",
        "That range traps fingers as drawn first. Fixed: a flexible EPDM finger guard bonded across the hinge gap on both faces (F9)", WITHIN,
        closed_by="FXT-DEC-001 F9 (standing instruction)")
c.cited("S35", "Passing a doorway needs no hand contact", "Biology", "Microbiology",
        "Leaves open with about 16 N (S11) on a push plate 820 to 1,120 mm from the hinge, 814 to 974 mm above the floor",
        "A hip, forearm or trolley can push the plate; returning upstream needs a pull by hand, so the leaf edge is a touch surface cleaned with the "
        "high-touch surfaces", PLAUSIBLE, closed_by="V1 at TRL 4")
c.cited("S36", "Ballast does not bring soil or wet bags onto a clinical floor", "Biology", "Microbiology",
        "Site sand or soil can carry spores and dirt; coated polyester sits at floor level",
        "Bags filled with clean sand off the clinical floor, closed and wiped; a sealed, wipeable bag or a water bag to source (C8)", PLAUSIBLE,
        closed_by="FXT-DEC-001 C8")
c.cited("S37", "Signs and doorways are usable by people with low vision and by wheelchair users", "Biology", "Human physiology and biomechanics",
        "ADA 703.5.6: visual characters at least 40 in (1,015 mm) above the floor; 703.5.1 contrast; doorway clear width S12",
        "Signs moved to a band 1,015 to 1,195 mm with dark characters on light; leaves carry a dark edge band on white walls; feet and bags marked on the "
        "floor; the 43 mm outriggers along every wall line remain a trip edge for low vision", PLAUSIBLE, closed_by="T5 and V1 at TRL 4")
c.cited("S38", "PP sheet and PETG clips keep their stiffness and grip in a hot tent", "Chemistry", "Materials and polymer chemistry",
        "PETG glass transition about 81 C (MakeItFrom); PP stiffness at 50 C ASSUMED half (A15); black clips in sun-heated tents",
        "Self-weight factor of S4 falls to about 0.86 for a flat strip; snap tongues and pegs creep under sustained load; maximum use temperature to set",
        PLAUSIBLE, closed_by=f"Hot soak in T7; {PLT} T3 at 40 and 50 C")
c.cited("S39", "Folds and clips survive cold use", "Chemistry", "Materials and polymer chemistry", "PP turns brittle towards 0 C; folds strain the 0.26 mm skin by 4 %",
        "Minimum use temperature to set; fold and clip only when the panels are at room temperature", PLAUSIBLE, closed_by=f"{PLT} T2 at 5 C")
c.cited("S40", "The sheet tolerates UV inside a tent", "Chemistry", "Materials and polymer chemistry",
        "Interprofile outdoor grade 2,500 h SAE J1960; LaminaCorr Ultra FR lists an anti-UV additive; the priced FR board's UV grade not stated",
        "UV grade to confirm with the supplier (C1)", PLAUSIBLE, closed_by="FXT-DEC-001 C1")
c.claim("S41", "The catch magnet's field falls below the 0.5 mT ACGIH limit for pacemakers close to the stop block", "Physics", "Electromagnetism and circuits",
        f"On-axis field of a 12.7 x 3.2 mm disc, Br {1.3} T ASSUMED (A13); ACGIH 0.5 mT for implanted cardiac pacemakers (UCSD summary); distance in mm",
        fl["field_0p5mT_mm"], 60.0, "mm", rule="below", closed_by="Label on each stop block: 'magnet, keep pacemakers 10 cm away'")
c.cited("S42", "A user can tell when a clip is fully home", "Biology", "Ergonomics",
        f"{PLT} P9 (v0.2) assumes both through-pegs engaged through both skins; a half-engaged clip looks like a full one",
        "A printed witness line 40 mm from each clipped edge disappears into the clip mouth when the clip is home; the peg tips show in the back-wall "
        "sockets; a tug test in the build plan", PLAUSIBLE,
        closed_by="T5 at TRL 4")
c.cited("S43", "Untrained people assemble it right first time", "Biology", "Ergonomics",
        "Six foot types, 46 clips, stubs on alternate walls, duos that fold one way, leaves that hang one way",
        "Feet colour-keyed and slotted so each fits only its joint; fold direction printed on each duo's back; a pictorial card in each bag; error "
        "modes in the FMEA",
        PLAUSIBLE, closed_by="V1 with untrained users at TRL 4")
c.cited("S44", "Printed parts can be made in the prototype time", "Engineering and technology", "Manufacturing tolerances",
        f"{pr['petg_kg']} kg of PETG at 20 g per printer-hour (A11)", f"About {pr['print_hours']} printer-hours: weeks on one printer, so a print farm or "
        "a makerspace pool for the prototype and moulding at scale", WITHIN, closed_by="FXT-BLD-001; FXT-PLN-001")

# ---- other options and the P18 variant -----------------------------------------------------------------------------
f2, f3 = R["FT2"], R["FT3"]
x.cited("X1", "FT2: fabric screens give visual privacy in assessment and treatment", "Biology", "Human physiology and biomechanics",
        "ANSUR II standing eye height 1,753 mm (men 95th), about 1,780 mm in shoes",
        "First drawn with the fabric top at 1,730 mm, a tall man saw over it (independent review 2026-11-12: refuted). Screens now 1.9 m with the fabric "
        "top at 1,830 mm", WITHIN)
x.cited("X2", f"FT2: the screen bay packs within the deck's 12 kg", "Mathematics", "Orders of magnitude",
        f"Aluminium posts, rails and 6 mm aluminium base plates from the model ({f2['frame_kg']} kg); fabric 0.20 to 0.45 kg/m2 ASSUMED (A8) on {f2['screen_m2']} m2",
        f"{f2['mass_kg'][0]} to {f2['mass_kg'][1]} kg: heavier than FT1 because it is 1.8 m tall and its frame is metal", FIX,
        closed_by="Same decision as S1 (FXT-DEC-001 D2); option not carried")
x.cited("X3", "FT2: 2.1 m door headers give headroom and carry split magnetic curtains that need no hand", "Biology", "Human physiology and biomechanics",
        "ANSUR II stature 1,870 mm (men 95th)", "Clearance about 217 mm under the rail; the curtain closes by gravity and magnets but touches the face and "
        "shoulders of everyone who passes, so it is body contact, not hands-free in the IPC sense", WITHIN)
x.cited("X4", "FT2: the fabric meets NFPA 701 and can be disinfected", "Chemistry", "Materials and polymer chemistry",
        "IFR knit drape listing 'will pass NFPA 701' (Urquid Linen); PVC-coated polyester is wipeable but its FR report is to source",
        "Knit drape is laundered, not wiped; the wipeable coated fabric adds mass (X2) and needs its own fire report", PLAUSIBLE)
x.cited("X5", "FT2: a screen bay costs about the deck's USD 800", "Mathematics", "Orders of magnitude",
        "Pipe-and-drape kit USD 179.99 per two 8 ft uprights, two bases and a crossbar (Urquid Linen); FR drape about USD 50 a panel",
        f"About USD {f2['cost_benchmark_usd']} for {f2['posts']} posts and 16 panels at commercial prices; a DIY frame would cost less (to assess)",
        FIX, closed_by="Option not carried")
x.cited("X6", "FT2: the post frame resists the 178 N push", "Physics", "Mechanics and statics",
        "Posts on 300 mm aluminium base plates, push at 1,372 mm; the bag sits beside the plate, not on it",
        "One post tips at about 3 N, 8 N with the bag on the plate (independent review 2026-11-12); like FT1 it stands only where its frame is braced",
        FIX, closed_by="Option not carried; same decision as D7")
x.cited("X7", "FT3: a belt stanchion resists the 178 N push", "Physics", "Mechanics and statics",
        f"Uline H-3736BL: 42 lb post on a 14 in base; tipping about the base rim, push at the belt height",
        f"{f3['tip_one_post_N']} N per post (fails); belts carry no moment. A stanchion line marks a boundary, it does not stand a bump; that is a "
        "scope change", FIX, closed_by="Option not carried; stated limit if Amish chooses FT3")
x.cited("X8", f"FT3: the stanchion bay is portable", "Mathematics", "Orders of magnitude", "Uline H-3736BL 42 lb per post; water-fillable posts (Montour) empty mass not stated",
        f"{f3['posts']} steel posts weigh about {f3['mass_kg']:.0f} kg; water-fillable posts would be light empty but their mass is to assess", FIX,
        closed_by="Option not carried")
x.cited("X9", "FT3: belts at 0.97 m separate cohorts", "Biology", "Human physiology and biomechanics", "Belt height 40 in post (Uline, Global Industrial)",
        "A belt guides walking patients and marks the boundary; people can duck under, stretchers cannot be screened, no privacy", WITHIN)
x.cited("X10", "FT3: deploys in under 15 minutes", "Biology", "Ergonomics", "14 posts and 12 belts at 30 to 60 s each; 22 m of floor tape at 2 to 4 m a minute (A9); "
        "two people at 70 to 85 % useful time as FT1",
        "About 11 to 26 min; tape is the slow part, and moving 267 kg of steel posts is not counted", PLAUSIBLE)
x.cited("X11", "FT3: floor tape and post signs stay legible", "Chemistry", "Materials and polymer chemistry",
        "Vinyl floor tape 5 to 6 mil (Global Industrial listing)", "Trafficked floor tape soils and lifts under wet mopping; signs on posts read like FT1's",
        PLAUSIBLE)
x.cited("X12", "FT3: adds little fire load", "Chemistry", "Materials and polymer chemistry", "Steel posts, cast bases, nylon belts and vinyl tape",
        "Only the belts and tape burn, well under FT1's panels", WITHIN)
x.cited("X13", "FT3: a stanchion bay costs about USD 850 to 1,200 against the USD 800 target", "Mathematics", "Orders of magnitude",
        "Uline USD 54.50 a post (5 or more cartons); Montour water-fill USD 79.79; tape USD 10.25 a roll",
        f"USD {f3['cost_steel_usd']:.0f} with steel posts, USD {f3['cost_waterfill_usd']:.0f} with water-fill posts; over the target either way", WITHIN)
p18 = R["P18"]
p18 = R["P18"]
x.cited("X14", "FT1 at P18 (1.8 m walls, privacy variant)", "Mathematics", "Orders of magnitude",
        f"Same zigzag plan with P18 duos ({PLT} module, clips at 150, 1,050 and 1,650 mm); flat-strip factor {R['self_weight']['load_factor_flat_P18']} "
        f"({PLT} P2); held leaf ({PLT} P3)",
        f"{p18['mass_kg']} kg and {p18['sheets']} sheets (USD {p18['sheet_cost']:.0f} of sheet). With v0.2 zigzag walls a held 600 mm leaf at 1,800 mm is "
        f"{R['self_weight']['leaf_P18_both_edges']} cold and {R['self_weight']['leaf_P18_both_edges_hot']} hot ({PLT} P3 gives 3.1 and 1.6 after its load "
        "factor of 2), so P18 now stands structurally; it fails the pack target, like S1, and needs a lateral criterion, like S6", FIX,
        closed_by="FXT-DEC-001 D3; not carried")


def table(rows):
    out = ["| # | Claim (number and unit) | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |",
           "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in sorted(rows, key=lambda r: int(r["id"][1:])):
        out.append(f"| {r['id']} | {r['claim']} | {r['field']} | {r['branch']} | {r['law']} | {r['check']} | {r['verdict']} | {r['closed_by'] or 'Open'} |")
    return "\n".join(out)


def inject(doc, tag, text):
    s = doc.read_text(encoding="utf-8")
    a, b = f"<!-- {tag} -->", f"<!-- /{tag} -->"
    if a in s and b in s:
        i, j = s.index(a) + len(a), s.index(b)
        doc.write_text(s[:i] + "\n" + text + "\n" + s[j:], encoding="utf-8")


if __name__ == "__main__":
    state = c.write()
    x.write()
    doc = ROOT / "docs/01b-stem-check.md"
    if doc.exists():
        inject(doc, "STM_TABLE", table(c.rows))
        inject(doc, "STM_OPTIONS", table(x.rows))
        print("refreshed tables in docs/01b-stem-check.md")
    print("FT1 state:", state)
