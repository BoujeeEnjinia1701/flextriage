---
doc_id: FXT-DEC-001
title: FlexTriage Origami Bay design decisions register
project: FlexTriage Origami Bay
doc_type: Design decisions register
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First register; D1 to D9 proposed, awaiting Amish; F1 to F9 made under the standing instruction of 2026-10-23
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Brought up to FXP-PLT-001 v0.2; D5 closed by the platform (zigzag walls, adopted here as F10); D2 aligned with platform D15; D3 restated now that a P18 zigzag stands; D10 (clip holding, platform D14) added
---

# FlexTriage Origami Bay design decisions register

Every design decision for this repo, in one place. Nothing below is recorded as Amish's decision unless he made it: the open decisions are **proposed, awaiting Amish**. The STEM fixes F1 to F10 were made under his standing instruction of 2026-10-23 (STANDARDS section 20) and he can reverse them. The shared Flex platform (FXP-PLT-001, now v0.2) was decided by Amish on 2026-11-12; its own decisions D1 to D18 are proposed and awaiting him and are not restated here, except where they decide something in this bay (D2 and platform D15, D10 and platform D14).

## Open decisions (proposed, awaiting Amish)

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| D1 | Concept choice | FT1 origami panel bay (176 of 260); FT3 floor marking and belt stanchions (169); FT2 fabric screens on a pole frame (159) | All three are within 10 %, so all come to Amish without a pick. Engineering view: FT1 gives the clearest zones and the shared platform; FT3 is quickest, most durable and least combustible; FT2 alone gives privacy. FT1 is carried in the drawings, BOM and build plan so a constructable design exists. Graft FT3's floor tape for the path and the 1 m spacing onto whichever is chosen | Everything | FXT-OPT-001, FXT-DDR-001 |
| D2 | Pack target (STM S1; platform D15) | (a) keep "two bags under 12 kg" (not met: 43.1 kg; the platform's own U bay is 14.3 kg); (b) three bags of about 15 kg, platform D15 (a); (c) four bags of about 11 kg; moulded, cored feet and clips (platform D15 (b)) bring the bay only to about 35 kg | (b) for the prototype, the same three-bag kit at about 12 kg each once moulded parts exist | PR-015, PR-016, carry bags | FXT-CAL-001 section 3; FXP-PLT-001 P17 |
| D3 | Wall height | (a) P12, 1.2 m (as drawn; no privacy to a standing adult); (b) P18, 1.8 m zigzag (53.7 kg, 21 sheets; under platform v0.2 a held P18 leaf stands at 3.1 cold and 1.6 hot, so it is now a weight and cost question, not a structural one); (c) P12 walls with P18 privacy screens round the assessment and treatment places, now possible because P12 and P18 share the clip grid at 150 and 1,050 mm (platform request 5) | (c), drawn after D1 | PR-022, mass, cost | STM X14; FXP-PLT-001 P3, P40 |
| D4 | Floor statement (STM S22) | (a) keep "20 m2" (true of the interior only); (b) state "needs 8.8 x 2.9 m of clear floor plus 1.5 m at entry and exit; 19.2 m2 inside" | (b) | PR-012, README, label | FXT-CAL-001 section 2 |
| D6 | Making the clips and feet | (a) PETG prints (672 printer-hours, 13.4 kg, about USD 1,076 more at a print service); (b) moulded PP clips and feet at volume | (a) for TRL 4; (b) costed at P6 | Cost, deployment | FXT-CAL-001 section 11 |
| D7 | Lateral criterion between stubs (STM S6) | (a) state limit L1 (boundaries, not barriers) with a lower criterion of 5 to 15 N between stubs, label "do not lean"; (b) buttresses every 1.2 m (about 20 kg of ballast each); (c) a different structure | (a), because (b) makes the bay unportable; the criterion is a safety trade-off for Amish | PR-007, label, RSK H1 | FXP-PLT-001 L1, P6 |
| D8 | Two-zone variant | (a) two bags at the single stub (tips below 178 N); (b) three bags | (b) | PR-006, BOM per variant | STM S30 |
| D9 | Ballast on clinical floors | (a) coated sand bags filled on site (as drawn); (b) water bags, only double-bagged in a lipped tray (platform rule B1); (c) weights in sealed boxes | (a) with sealed, wipeable bag covers (C8), or (c) | BOM 14 | STM S36; FXP-PLT-001 B1 |
| D10 | Clip holding at the anchor feet (platform D14) | (a) keep the through-peg clip and let T3 decide (anchor uplift 103 N against 176 N, factor 1.71); (b) clips at a 300 mm pitch on anchor joints; (c) a moulded collar at each hole; (d) state "joints may release before the bay tips" | (a), with (b) ready if T3 shows under 200 N per clip, as platform D14 recommends for FlexTriage anchor joints | BOM 20, PR-006 | STM S5; FXP-PLT-001 P9, D14 |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| C1 | The FR sheet lot's NFPA 701 Test Method 1 report, grammage (at most 700 g/m2) and UV stabiliser | Fire, mass, outdoor tents | PR-010; FXP-PLT-001 |
| C2 | PP sheet resistance to 0.5 % hypochlorite and 70 % alcohol on the print overlaminate | Cleanability | PR-009 |
| C3 | Friction of EPDM pads on wet clinical vinyl with disinfectant residue | Sliding margin (177 N wet low end) | STM S8 |
| C4 | Printed clip tongue life over 50 deployments | Reuse | PR-017; FXP-PLT-001 T2 |
| C5 | Print time and print pool for 672 printer-hours | Schedule | STM S44 |
| C6 | Magnet supplier pull data for the batch | Catch force | STM S11 |
| C7 | Strike washer grade: A2 stainless is weakly magnetic, so a ferritic 430 disc may be needed | Catch force | BOM 10 |
| C8 | A ballast bag cover that can be wiped and sealed | Cleanability | STM S36 |
| C9 | An FR grade of PETG or PP for the prints (prints are not FR now, 288 MJ of the 1,279 MJ) | Fire | STM S14 |
| C10 | Freedom to operate by a patent attorney | Desk reading only | FXT-FTO-001 |

## Value engineering

Value-engineering target: USD 800 per three-zone bay (a hypothetical control target, not a limit); stretch under USD 500 at volume. Estimated cost of the constructable design: USD 1,174.23 at prototype quantities, USD 374.23 over the target. Main cost drivers: the 18 wall duos (USD 405, nine sheets), freight for the sheets (USD 150, estimate), the four leaves (USD 90) and the ten feet with two outriggers (USD 81.00). Printed parts at filament cost total USD 276.78; at a print service they would cost about USD 1,076 more. Savings worth trying: sheet at the 1,100-sheet price (USD 34.99 against 44.99, about USD 120 a bay), freight shared across several bays, moulded clips and feet at volume (D6), and carry bags already owned. At 50 deployments the bay costs about USD 23.48 a deployment.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-11-12 | Repo shape (one public repo), licences (CERN-OHL-P-2.0, Apache-2.0, CC-BY-4.0), no archive, the credits list | Amish | `project.yaml`, STANDARDS 25 |
| 2026-11-12 | Built on the shared Flex platform (FXP-PLT-001) | Amish | FXP-PLT-001 |
| 2026-11-12 | F1: process zones by numeral, word and arrow on neutral colours; triage colours only as category bands with the word; signs 1,015 to 1,195 mm above the floor; neutral way-out sign | Under Amish's standing instruction of 2026-10-23 | FXT-DDR-003 |
| 2026-11-12 | F2: back-face groove on each stub covered (filler and tape in v0.1; a clear PP strip under platform rule E2 now) | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F3: one leaf per doorway, opening downstream, closing on a stop with a pull-mode magnetic catch | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F4: anchor feet pegging the stub ends, two 5 kg bags each | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F5: EPDM pads under every foot | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F6: deployment kit (pre-fitted leaf hardware, bonded pads, pre-filled bags) | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F7: corner tails making the end-stub corners tees | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F8: nothing in a doorway (jamb feet with the outside outrigger only, anchor outriggers square to the doorway, bags upstream) | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F9: finger guards over the hinge gap | Under the standing instruction | FXT-DDR-003 |
| 2026-11-12 | F10: zigzag walls and stubs (each duo folded 30 deg, angle clips and angle tees) to meet FXP-PLT-001 v0.2 rule S1; closes STM S4 and the old D5 | Under the standing instruction (the platform's own fix F1) | FXT-DDR-003 |
| 2026-11-12 | D5 (platform rules S1 and S4 for straight runs) closed: resolved by FXP-PLT-001 v0.2 (platform request 1) | Platform revision; no FlexTriage decision left | FXP-PLT-001 section 17 |
| 2026-11-12 | Design for construction of FT1 (hinge pins and sleeves, stop and strike, angle tees and angle feet on the zigzag, round clip cores, making sketches) | Under STANDARDS section 18 | FXT-DDR-002 |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
