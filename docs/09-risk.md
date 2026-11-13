---
doc_id: FXT-RSK-001
title: FlexTriage Origami Bay risk register and hazard analysis
project: FlexTriage Origami Bay
doc_type: Risk register
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First risk register, preliminary hazard analysis and design FMEA for option FT1
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Restated on FXP-PLT-001 v0.2, zigzag walls, through-peg clip, open platform items
---

# FlexTriage Origami Bay risk register and hazard analysis

The largest risks are walls that tip onto a patient when leant on between stubs, fire in a tent full of patients, and a false sense that a boundary controls infection. Controls are a stated limit and label, the FR grade with placement rules, honest claims and IPC review before use. Likelihood and impact 1 (low) to 5 (high).

## Project risk register

Table 1. Project risks.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | Deployment over 15 min | Many joints (26 clips, 22 feet, 8 pins, 18 folds set to 30 deg) | Team gate not met | 3 | 4 | Test lead | Deployment kit (F6); colour keys; timed V1 |
| P2 | Pack target not accepted | 43.1 kg against 12 kg | Concept rejected by logistics | 4 | 3 | Project lead | D2: four bags of about 12 kg |
| P3 | Cost over target | Sheet, freight, prints | Fewer bays funded | 4 | 3 | Project lead | Value engineering; volume sheet price; moulding (D6) |
| P4 | Platform changes still open | Angle clip core (request 8), clip holding (platform D14), pack (D15) shared across FlexClean, FlexSleep, FlexTriage | Parts change after the build | 3 | 3 | Platform owner | Platform requests 8 to 10; D10 |
| P5 | Print capacity | 672 printer-hours a bay | Prototype schedule slips | 4 | 2 | Mechanical lead | Makerspace pool; print service |
| P6 | Overclaiming by users or partners | Bays read as "isolation" | Misuse, regulatory exposure | 3 | 4 | Project lead | FXT-CLM-001 wording on signs and materials |
| P7 | Decision on D1 delayed | Three options within 10 % | Schedule | 3 | 2 | Project lead | Decision request in FXT-PLN-001 |

## Preliminary hazard analysis

Table 2. Hazards. Severity and likelihood 1 to 5.

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Wall tips onto a person | Lean or bump between stubs (5 to 15 N) | Bruising; a fall for a frail patient | 3 | 3 | Stated limit L1 and "boundary, do not lean" on signs; place patients away from walls; D7 | Medium |
| H2 | Whole wall piece tips | 178 N push at a stub joint without bags | As H1, larger | 3 | 2 | Anchor feet with two bags (F4); "bags before leaves" stop | Low |
| H3 | Fire spread | Combustible sheet and prints (1,279 MJ) near a heat source | Burns, smoke in a crowded tent | 5 | 2 | FR grade with report (C1); 1 m from heaters, flames, oxygen; off exit routes; FR prints sought (C9) | Medium |
| H4 | Blocked escape | Serpentine path and leaves | Delay in an emergency | 4 | 2 | Two doorways per zone, leaves push open forward and lift off pins; bay off host exits; drill in V1 | Low |
| H5 | Trip | Outriggers 43 mm high along wall lines; bags | Fall | 3 | 3 | Nothing in doorways (F8); contrast floor marks; outriggers on the outside where possible | Medium |
| H6 | Finger pinch | Hinge gap 0 to 12 mm; leaf closing on the stop | Finger injury | 2 | 2 | Finger guards (F9); slow magnet close | Low |
| H7 | Pacemaker interference | Magnets in the catches | Device mode change | 4 | 1 | 0.5 mT at about 54 mm; label on every stop block | Low |
| H8 | Cross-contamination via surfaces | Unsealed edges, groove, leaf edge, bag covers | Pathogen carry-over | 4 | 3 | Sealed edges and groove shoulders (FXP-PLT-001 E1); groove cover strip (F2, rule E2); wipe plan; wipeable bags (C8); IPC review | Medium |
| H9 | Wrong reading of zones | Colour-coded zones | Patient sent the wrong way | 3 | 2 | Numeral, word and arrow on neutral colours (F1) | Low |
| H10 | False sense of protection | Bay seen as isolation | Exposure | 4 | 3 | Claims register; release limitation | Medium |
| H11 | Strain injury | Carrying bags | Back injury | 2 | 2 | Bags under 23 kg (D2) | Low |

## Design FMEA (first pass, P3)

Table 3. Failure modes. RPN = severity x occurrence x detection (each 1 to 10).

| # | Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Long wall between stubs | Stand as a boundary | Tips when leant on | Wall on a patient | Low lateral stiffness (S6) | 7 | 6 | 3 | 126 | D7 criterion; label; T7 |
| F2 | Clip snap tongues | Hold panel edges | Tongue cracks or creeps after reuse | Joint opens, wall falls | Print layer weakness, fatigue | 6 | 4 | 5 | 120 | Full infill at tongues; witness line (PR-025); T2 over 50 deployments |
| F3 | Anchor foot pegs | Hold stub to its ballast | Pegs pull out (103 N against 176 N on paper, demand not bounded, platform P9) | Stub tips | Thin FR skins crumple before full bearing | 7 | 4 | 5 | 140 | T3 pull-out; clips at 300 mm on anchor joints if under 200 N per clip (D10) |
| F4 | EPDM pads | Stop sliding | Slip on wet disinfected vinyl | Wall slides under a push | Residue, water (177 N low end) | 5 | 4 | 5 | 100 | C3 friction test; pads replaced each deployment if worn |
| F5 | Magnet catch | Hold the leaf shut | Too weak (thin or weakly magnetic strike) or too strong | Leaf swings or needs more than 22 N | A2 strike grade, cover thickness | 4 | 5 | 3 | 60 | C7; V3 force test; cover set by measurement |
| F6 | Hinge pins and sleeves | Carry the leaf | Bore wear, pin lost | Leaf drops | 150,000 swings; split pin missing | 5 | 3 | 3 | 45 | V3 cycle test; spare pins in the kit |
| F7 | Groove cover strip | Seal the stub's back face | Strip or tape lifts | Uncleanable crevice | Wiping, folding | 6 | 5 | 4 | 120 | T6 wipe test; replace tape at each deployment |
| F8 | Sheet in heat | Stand under own weight | Creep or buckling above 40 C | Wall sags | PP stiffness falls (A15); a fold relaxes from 30 deg | 6 | 2 | 4 | 48 | Zigzag walls (F10); angled foot slots hold the fold; hot soak in T7 |
| F9 | Ballast bags | Weigh the anchors | Bags forgotten or split | Stub tips (H2) | Deployment haste | 7 | 4 | 3 | 84 | Bags before leaves (build plan stop); bag pockets marked |
| F10 | Signs | Show zones | Peeled or wrong order | Wrong flow | Wiping, set-up error | 4 | 3 | 2 | 24 | Overlaminate; numerals keyed to feet colours |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
