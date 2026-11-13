---
doc_id: FXT-PRS-001
title: FlexTriage Origami Bay product requirements and specifications
project: FlexTriage Origami Bay
doc_type: Product requirements
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First product requirements for the carried option FT1, traced to FXT-URS-001, with targets, tolerances and planned verification
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Statuses restated on FXP-PLT-001 v0.2 (zigzag walls); PR-028 self-weight added
---

# FlexTriage Origami Bay product requirements and specifications

Requirements for the carried option FT1 (origami panel bay); the choice between FT1, FT2 and FT3 is awaiting Amish (FXT-DEC-001 D1). Status "met on paper" means FXT-CAL-001 or a cited figure shows it; nothing is tested at TRL 3. Verification families are in FXT-VER-001 and the platform tests T1 to T8 in FXP-PLT-001.

Table 1. Product requirements and specifications.

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Deployment and assembly | Deployment time | Two untrained people shall deploy the three-zone bay from its bags, tool-free, within the target | 15 | maximum | min | Timed trial V1 at TRL 4 (the team's decision gate) | At risk (estimate 12 to 35 with F6) |
| PR-002 | UR-002 | Performance | Zones and flow | The bay shall have three zones in order with one entry, one exit and one doorway between zones, at alternate sides | 3 | 2 to 4 | zones | Inspection | Met by design |
| PR-003 | UR-003 | Performance | Boundary height and spacing | Walls shall be continuous boundaries at least the target high, zones at least 2.3 m wide on joint lines so 1 m spacing fits; standing staff see over | 1.2 | minimum | m | Inspection; sight-line check in V1 | Met by design |
| PR-004 | UR-004 | Usability | Zone cues | Process zones shall be marked by numeral, word and arrow on neutral colours; red, yellow and green only as triage category bands with the category word | 0 | none | colour-only cues | Inspection; legibility test T5 | Met by design (F1) |
| PR-005 | UR-004 | Usability | Sign placement and size | Visual characters shall sit at least the target above the floor and be legible across their zone | 1015 | minimum | mm | Analysis FXT-CAL-001 section 9; T5 | Met on paper (60 mm words, 9 m in poor light) |
| PR-006 | UR-005 | Safety | Stability at stubs | A long wall pushed with 178 N at 1,110 mm next to a stub joint shall not tip, with two 5 kg bags on each anchor foot (three in a two-zone bay) | 178 | minimum | N | Analysis FXT-CAL-001 section 5; tip test T7 | Met on paper (312 N) |
| PR-007 | UR-005 | Safety | Stability between stubs | A wall pushed anywhere shall not tip under the lateral criterion Amish sets (D7) | 178 | to set | N | Analysis; T7 | Not met (5 to 15 N) |
| PR-008 | UR-005 | Safety | No sliding | The pushed wall piece shall not slide under 178 N on a dry or wet floor, on EPDM pads | 178 | minimum | N | Analysis; friction test in T7 | At risk (177 to 236) |
| PR-009 | UR-006 | Maintenance | Cleanable surfaces | Every face, edge, hole and groove facing a zone shall be sealed and withstand the target wipes with 0.5 % hypochlorite and 70 % alcohol | 120 | minimum | wipes | T4, T6, V4 | To verify at TRL 4 |
| PR-010 | UR-007 | Safety | FR sheet | Sheet shall be bought with an NFPA 701 Test Method 1 report and at most the target grammage | 700 | maximum | g/m2 | Inspection of supplier report (C1); T8 | To verify at TRL 4 |
| PR-011 | UR-007 | Safety | Fire placement | The bay shall stand at least the target from heaters, flames and oxygen outlets (label) | 1 | minimum | m | Inspection | Met by design |
| PR-012 | UR-009 | Environment and durability | Floor | The bay shall fit a clear floor of the target length plus 1.5 m approach at each end, 3.0 m wide, enclosing at least 20 m2 | 9.1 | maximum | m | Analysis FXT-CAL-001 section 2 | At risk (8.8 x 2.9 m of floor; 19.2 m2 inside, under 20 m2; D4) |
| PR-013 | UR-010 | Usability | Doorway width | Every doorway shall leave at least the target clear at the floor | 815 | minimum | mm | Analysis section 7; V1 walk-through | Met on paper (1,054 to 1,069) |
| PR-014 | UR-014 | Usability | Leaf force | A leaf shall hold shut against a draught and open with no more than the target at its push plate | 22.2 | maximum | N | Catch force test V3 | At risk (estimate 15) |
| PR-015 | UR-008 | Logistics | Pack mass | A bay shall pack within the target mass | 12 | maximum | kg | Weighing at TRL 4 | Not met (43.1; D2) |
| PR-016 | UR-008 | Logistics | Bag mass | No single bag shall exceed the target | 23 | maximum | kg | Weighing | Met on paper (four bags about 10.8) |
| PR-017 | UR-012 | Environment and durability | Cycle life | Clips, folds and hinges shall survive the target deployments; each hinge 150,000 swings | 50 | minimum | deployments | T2, T3, V3 | To verify at TRL 4 |
| PR-018 | UR-013 | Cost | Bay cost | Parts at prototype quantities shall be reported against the value-engineering target | 800 | maximum | USD | BOM | Over target (USD 1,174.23) |
| PR-019 | UR-015 | Regulatory | Placement | The bay shall stand indoors or in a tent, off the host's exit routes, with a host floor of at least 12 x 4 m | 0 | none | blocked exits | Inspection; label | Met by design |
| PR-020 | UR-015 | Regulatory | Claims | All wording shall follow FXT-CLM-001 | 0 | none | banned claims | Inspection; `render.py --check` | Met by design |
| PR-021 | UR-016 | Environment and durability | Floors and temperature | The bay shall stand on a 1:50 slope and keep its self-weight margin from 5 to 40 C | 50 | minimum | slope 1 in | T7 hot soak and slope | To verify at TRL 4 |
| PR-022 | UR-011 | Usability | Privacy | Where privacy is required a screen at least the target high shall be provided | 1.8 | minimum | m | Inspection | Not met at P12 (D3) |
| PR-023 | UR-017 | Maintenance | Replaceable parts | Every made part shall be cut from the platform sheet or printed | 0 | none | special parts | Inspection | Met by design |
| PR-024 | UR-002 | Performance | Zone count | The plan shall extend by 2 pitches, one stub and one leaf per added zone | 4 | 2 to 4 | zones | Analysis section 2 | Met by design |
| PR-025 | UR-001 | Deployment and assembly | Right first time | Feet, junction feet, anchors and jamb feet shall fit only their joints, and each duo shall carry its fold direction, and be colour-keyed; clipped edges carry a witness line | 0 | none | wrong fits | V1 with untrained users | To verify at TRL 4 |
| PR-026 | UR-014 | Safety | Hinge and floor hazards | Hinge gaps shall be guarded and no outrigger or bag shall lie in a doorway's clear width | 0 | none | hazards | Inspection | Met by design (F8, F9) |
| PR-027 | UR-015 | Regulatory | Magnet label | Each catch shall carry a pacemaker label; the field falls below 0.5 mT within the target distance | 60 | maximum | mm | Analysis section 7 | Met on paper (54) |
| PR-028 | UR-005 | Safety | Self-weight | Every panel taller than 600 mm shall stand with both vertical edges supported (FXP-PLT-001 v0.2 rule S1: zigzag walls) at the platform load factor cold and above 1 hot | 2 | minimum | load factor | Analysis FXT-CAL-001 section 4; T7 hot soak | Met on paper (held leaf 9.4 cold, 4.7 hot; free-edge leaf about 4.7 and 2.3) |

## Assumptions

Assumptions A1 to A15 are listed in FXT-CAL-001 section 1. Targets remain proposals for review with an emergency medical team.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
