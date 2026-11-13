---
doc_id: FXT-CAL-001
title: FlexTriage Origami Bay sizing and first-principles checks
project: FlexTriage Origami Bay
doc_type: Calculation note
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First sizing note for option FT1 on FXP-PLT-001 (plan, mass and pack, self-weight, tipping and sliding, deployment time, doorways and catch, fire load, cues, cost) with FT2 and FT3 first-order numbers, after the independent review
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Brought up to FXP-PLT-001 v0.2 (zigzag walls and stubs under rule S1, angle clips, 4.5 mm slots, through-peg clip at 176 N, foot family, 13.6 mm groove, pack D15); every number recomputed
---

# FlexTriage Origami Bay sizing and first-principles checks

Result: the carried bay (FT1), now built with zigzag walls and stubs as FXP-PLT-001 v0.2 requires, encloses 19.2 m2 in three zones, uses 18 P12 duos, four leaves and two tails from 12 FR sheets, and weighs **43.1 kg** with its hardware and bags, 3.6 times the deck's 12 kg. Every wall and stub leaf now stands under its own weight hot and cold. Next to a stub joint a wall resists **312 N** against the 178 N push with two 5 kg bags on each anchor foot; between stubs a wall tips at **about 5 to 15 N**. Two people deploy it in an estimated **12 to 35 minutes**. Each doorway leaves **1,054 to 1,069 mm** clear; a leaf opens with about **15 N**. Fire load about **1,279 MJ**. Parts **USD 1,174.23** against the USD 800 value-engineering target. All numbers come from `docs/04-calcs/sizing.py` (results in `sizing_results.json`), which reads the model (`cad/src/model.py`), the platform numbers (`docs/platform/platform_check.py`, FXP-PLT-001 v0.2, read only) and the BOM. These are first-order screens for TRL 3; FXT-VER-001 lists the tests that close them. CONCEPT, NOT FOR FABRICATION.

## 1. Inputs and assumptions

Cited inputs: FXP-PLT-001 v0.2 (sheet 0.70 kg/m2, EI_MD 2,621 and EI_CD 766 N mm2/mm, skin 0.26 mm, through-peg clip 88 N per peg and 176 N per clip, rule S1 zigzag walls, BIFMA X5.6 push 178 N at 1,372 mm or 102 mm below the top, PP 39.7 MJ/kg, pack P17); ANSUR II eye heights (NCSU summary); ADA 404.2.3, 404.2.9 and 703.5.6; K&J D82 pull 6.44 lb; Engineering ToolBox friction; UQ PET heat of combustion 21.4 MJ/kg; ACGIH 0.5 mT for pacemakers (UCSD summary); BOM prices (bom/bom.csv). All checked 2026-11-12; links in FXT-STM-001.

Table 1. Assumptions.

| # | Assumption | Value | Used in |
| --- | --- | --- | --- |
| A1 | PETG density (as FXP-PLT-001) | 1.27 g/cm3 | Section 3 |
| A2 | Friction of hard plastic feet on a floor; EPDM pads on concrete | 0.20 to 0.35; 0.45 to 0.60 (low ends of the cited ranges) | Section 5 |
| A3 | Empty sand bag | 0.25 kg | Section 3 |
| A4 | Empty flat carry bag | 0.8 kg | Section 3 |
| A5 | Printed film and overlaminate | 0.20 kg/m2 | Section 3 |
| A6 | Chair seat height for seated eye height | 450 mm | Section 9 |
| A7 | Pressure difference across a leaf indoors or in a tent | 1 to 5 Pa | Section 7 |
| A8 | FT2 fabric: FR knit drape and FR PVC-coated polyester | 0.20 and 0.45 kg/m2 | Section 11 |
| A9 | Action times for one person, fast and slow | Table 4 | Section 6 |
| A10 | Useful share of two-person time | 85 % and 70 % | Section 6 |
| A11 | Print rate of one desktop printer | 20 g of PETG per hour | Section 10 |
| A12 | Print service price (sensitivity only) | USD 0.10/g | Section 10 |
| A13 | N42 remanence; catch pull scales with the square of the on-axis field | 1.3 T | Section 7 |
| A14 | Stretcher top on the floor; trolley top | 250 mm; 800 mm | Section 9 |
| A15 | PP stiffness at 40 to 50 C or under sustained load (as FXP-PLT-001 section 10) | half of the 23 C value | Section 4 |
| A16 | Buckling of a leaf with one free vertical edge, as a multiple of a free strip (simply supported and free plate, b/h = 0.5, uniform compression coefficient used for self-weight) | 2.7 | Section 4 |
| A17 | Moulded, cored feet and clips (FXP-PLT-001 D15 option b targets) | 0.15 kg and 0.04 kg | Section 3 |

## 2. Plan, areas and panel count

Walls and stubs are zigzags (FXP-PLT-001 v0.2 rule S1): every leaf stands 15 deg off its wall line, each duo is folded 30 deg at its groove and each wall joint is an angle clip turning 30 deg. The fold vertices point out of the bay, 157 mm outside the joint line, so the zones keep their full width. Joint pitch (1,200 + 12) x cos 15 deg = 1,170.7 mm. Seven pitches long (8,195 mm), two wide (2,341 mm). Zones: 1 intake 5.48 m2 (2 pitches), 2 assessment 5.48 m2 (2 pitches), 3 treatment 8.22 m2 (3 pitches); interior 19.19 m2 on joint lines, a little under the deck's 20 m2. The outriggers reach 300 mm outside every wall line, so the bay needs 8.8 x 2.9 m (25.9 m2) of clear floor plus about 1.5 m of approach at the entry and the exit (PR-012). Each added zone adds two pitches, two wall duos, one stub and one leaf: a two-zone bay about 34.7 kg, a four-zone bay about 48.7 kg (PR-024). The plan gives three zones in order with doorways at alternate sides (PR-002).

Joints: 18 angle clips at the plain wall joints and the lower clip of the two doorway wall jambs; 8 angle tees (the two zigzag leaves 150 deg apart and a stub or corner tail between) at the two divider joints and the two end-stub corners. No inline joint remains (rule S4).

Panels: 14 wall duos, 4 stub duos (21.6 m of wall, 25.9 m2), 4 leaves of 1,149 x 990 mm (4.6 m2), 2 tail leaves of 600 x 1,200 mm; 9 + 2 + 1 = 12 sheets of 1,220 x 2,440 mm.

## 3. Mass and pack

Table 2. Mass budget (sheet by grammage, printed parts by CAD volume at 1.27 g/cm3).

| Item | kg |
| --- | --- |
| 18 duo panels | 18.14 |
| 2 corner tail leaves | 1.01 |
| 4 flap leaves | 3.18 |
| Clips (18 angle, 8 angle tee) | 1.97 |
| Hinge, sleeve, strike and stop clips | 1.15 |
| Pins, washers, magnets, strikes | 0.43 |
| Angle and tail feet, anchor feet and jamb feet with outriggers | 7.68 |
| Angle junction and jamb feet (one outrigger each) | 3.78 |
| EPDM pads and finger guards | 0.61 |
| Prints and overlaminate | 0.23 |
| Empty ballast bags (10) | 2.50 |
| Carry bags (3) | 2.40 |
| **Total** | **43.1** |

The deck's 12 kg in two bags is 3.6 times too low: 12 kg less two bags buys 14.9 m2 of sheet with no hardware, 12.4 m of 1.2 m wall, against 21.6 m plus leaves and tails (PR-015, FXT-STM-001 S1). The platform's own zigzag U bay of six P18 duos is 14.3 kg (FXP-PLT-001 P17); this bay has three times its panels and three times its feet. With moulded, cored feet of 0.15 kg and clips of 0.04 kg (A17, platform D15 option b) it would still weigh about 35.0 kg. A bay packs into four bags of about 10.8 kg or three of about 14.4 kg (platform D15 option a asks for bags of about 15 kg), each under the 23 kg NIOSH load constant quoted as a ceiling (PR-016). Pack: folded duos stack about 180 mm thick at 600 x 1,200 mm; leaves 16 mm at 1,149 x 990 mm; feet about 7.4 L. Ballast is filled on site and never carried filled. At 800 g/m2 instead of 700 the sheet mass rises by 1/7 (C1).

## 4. Self-weight of the walls

Greenhill self-weight buckling of a flat strip (FXP-PLT-001 P2): h_cr = (7.837 EI_MD / q)^(1/3) = 1,441 mm. A flat P12 strip has a load factor of (1,441/1,200)^3 = 1.73 cold and 0.87 hot (A15), so the v0.1 flat walls failed hot, as the platform now also finds. With zigzag walls every leaf is held on both vertical edges by a 30 deg fold or angle clip (FXP-PLT-001 P3, orthotropic formula with no twisting stiffness): **9.43 cold and 4.72 hot** at 600 x 1,200 mm, against the platform's load factor of 2 (PR-028). The leaves with one free edge (the long walls' free ends at the entry and exit, and the corner tails) are about 4.68 cold and 2.34 hot by A16; a flap leaf, which stands above its lower sleeve, about 5.05 cold and 2.52 hot. At P18 a flat run fails outright (0.51); a held P18 leaf is 6.29 cold and 3.14 hot (the platform's 3.1 and 1.6 include its load factor of 2), so a P18 zigzag bay would stand (D3).

## 5. Stability: tipping and sliding

Push: 178 N at 1,110.5 mm (102 mm below the 1,212.5 mm wall top), 197.7 N m. Rigid wall piece (one long wall with its two stubs on anchor feet), tipping about the outside outrigger tips 300 mm outside the joint line. Restoring moments from the wall (its leaves lie 78 mm outside the joint line, so a lever of 0.22 m), its feet (0.3 m), the stubs (0.89 m) and the bags on each anchor foot (1.47 m):

Table 3. Tipping and sliding.

| Case | Result |
| --- | --- |
| No ballast | tips at 52.1 N |
| One 5 kg bag per anchor foot | 182 N |
| Two bags per anchor foot (as built) | **312 N** (PR-006) |
| Ballast needed per stub for 178 N | 4.8 kg |
| Two-zone bay, one stub per wall, two bags | 161 N; needs 11.3 kg, so three bags at that stub |
| Anchor uplift at tipping | 103 N against 176 N for two through-pegs (factor **1.71**; 1.96 with the v0.1 figure of 201 N) |
| Lift of a stub carried into the wall by its two angle-tee clips | 113 N in shear against 351 N (factor 3.12) |
| One zigzag duo alone between two feet | 4.5 N outward, 5.9 N inward |
| Free wall end at the entry or exit jamb | 8.7 N outward, 8.9 N inward |
| Stub couple per clip height at an angle tee | 220 N, edge bearing 4.2 MPa against 24 MPa yield |
| Sliding of the pushed piece (40.2 kg) | bare PETG 79 to 138 N; EPDM pads 177 to 236 N (PR-008) |

The rigid-piece result holds only for a push at or near a stub joint. A zigzag stiffens a wall up its height, not along it: a 600 mm leaf bows past 25 mm at 5.8 N (FXP-PLT-001 P4), so a wall cannot carry a mid-span push to the stubs, and between stubs the walls tip at about 5 to 15 N (PR-007, decision D7). The walls are boundaries, not barriers (FXP-PLT-001 L1). The anchor margin rests on the platform's through-peg capacity, which FXP-PLT-001 P9 now gives as "Fails, fix proposed" because the demand on a clip in a bowing leaf is not bounded on paper (platform D14); pull-out test T3 settles it.

## 6. Deployment time

Table 4. Step count from the model and assumed action times (A9), two people at 70 to 85 % useful time (A10).

| Action | Count | Fast (s) | Slow (s) |
| --- | --- | --- | --- |
| Unbag and unfold a panel | 20 | 10 | 25 |
| Stand a panel in its feet | 20 | 10 | 20 |
| Lay a pad (bonded under F6) | 22 | 3 | 8 |
| Push in one clip | 46 (30 with F6) | 6 | 15 |
| Set a foot, junction, anchor or jamb foot | 22 | 8 | 20 |
| Hang a leaf and drop two pins | 4 | 25 | 60 |
| Fit a split pin | 8 | 8 | 20 |
| Fill and lay a ballast bag (laid only under F6) | 10 | 40 (10) | 90 (20) |
| Lay out the plan with a tape | 1 | 120 | 300 |
| Final check walk round | 1 | 60 | 180 |

As first drawn 16.3 to 47.5 min; with fix F6 (sleeves and strike holders on the leaves, pads bonded, bags filled before the clock) **12.0 to 34.9 min** against the 15 minute target (PR-001, at risk). One zone (two duos, three feet, seven clips, one leaf, two bags) 1.6 to 4.7 min, inside the deck's 5 minutes. Setting each duo's fold to 30 deg is not timed separately; the feet's angled slots set it. Error modes are not counted (PR-025).

## 7. Doorways, leaves and the catch

Each stub ends 15 deg off the doorway line, so its anchor foot block (120 x 70 mm) reaches 67 mm into the doorway; the angle jamb foot at an inner doorway's wall jamb reaches 35 mm, and the jamb foot at a free wall end 49 mm. Clear width at the floor: 1,170.7 - 35 - 67 = **1,069 mm** at the inner doorways and **1,054 mm** at the entry and exit, above the 815 mm ADA clear width and a 750 mm stretcher; 971 mm in the upstream approach beside the bags; 1,149 mm past the open leaf (PR-013). The anchor foot's outriggers are turned square to the doorway so none reaches into it (F8). Leaf 1,149 x 990 mm, 0.80 kg. Catch: K&J D82 pulls 28.6 N on a thick plate at contact; behind a 2 mm cover with 0.5 mm of air (2.5 mm gap) the on-axis field falls to 0.67 of contact (A13), so about **12.9 N**; at the push plate (956 mm from the hinge against the catch at 1,155 mm) **15.3 N**, under the 22.2 N target, and above the 0.6 to 2.8 N a draught of 1 to 5 Pa needs at the free edge (PR-014). Thin-strike losses are not modelled; the cover is set by test V3. The field falls below 0.5 mT at 54 mm from the magnet face (PR-027).

## 8. Fire load

Sheet 31.9 m2 at 27.8 MJ/m2: 887 MJ; PETG parts 13.4 kg at 21.4 MJ/kg: 288 MJ (not FR rated); bags 105 MJ; **about 1,279 MJ**. A P18 bay's sheet alone would carry 1,207 MJ. FR sheet with an NFPA 701 TM1 report is mandatory (PR-010) and the bay stands 1 m from heat sources (PR-011).

## 9. Cohort boundary and cues

Every standing adult in ANSUR II (standing eye 1,421 mm women 5th to 1,753 mm men 95th) sees over a 1,212.5 mm wall; a seated 5th percentile woman (1,148 mm with a 450 mm seat) does not. For a short observer 0.5 m from the wall the ground is hidden for 2.31 m behind it for a floor stretcher (250 mm), 0.99 m for a trolley top: staff supervise from doorways (PR-003). Signs: 150 mm numerals and 60 mm words in a band 1,015 to 1,195 mm above the floor (ADA 703.5.6; PR-005), each on one leaf so no text crosses a fold (FXP-PLT-001 C5); by the ANSI Z535 ratio (25 ft per inch, halved in poor light) words read at 9 to 18 m and numerals at 22.5 to 45 m, against 4.2 m for the largest zone's diagonal. Process zones carry no safety or triage colour, and triage colours never take a safety-sign form (PR-004; FXP-PLT-001 C6).

## 10. Cost

BOM total **USD 1,174.23**, USD 374.23 over the USD 800 value-engineering target (PR-018). Drivers: duo sheet USD 405.00, freight USD 150.00 (estimate), leaves USD 90.00, feet with two outriggers USD 81.00; printed PETG parts USD 276.78 at filament cost (the angle junction feet are 120 x 120 mm blocks). A print service at USD 0.10/g would add about USD 1,076 (A12); the 13.4 kg of PETG is about 672 printer-hours at 20 g/h (A11). At the 1,100-sheet price (USD 34.99) the sheet falls by USD 120. Cost per deployment USD 23.48 over 50 uses, USD 11.74 over 100.

## 11. FT2 and FT3 first-order numbers

FT2 (same plan, 1.9 m screens): 14 aluminium posts, rails and 6 mm aluminium base plates 42.9 kg, fabric 43.9 m2, total 53.2 to 64.1 kg (A8); about USD 2,060 at commercial pipe-and-drape prices (seven kits at USD 179.99 and 16 FR panels at about USD 50). FT3: 14 steel stanchions at 42 lb (19.1 kg) each, about 267 kg; one tips at 34.2 N (19.1 kg on a 178 mm base radius, push at 970 mm); USD 844 with steel posts and tape, USD 1,198 with water-fill posts.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
