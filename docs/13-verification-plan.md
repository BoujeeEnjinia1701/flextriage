---
doc_id: FXT-VER-001
title: FlexTriage Origami Bay verification plan
project: FlexTriage Origami Bay
doc_type: Verification plan
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First verification plan, TRL 4 test families on paper only
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: PR-028 (self-weight, zigzag walls) added to V2; anchor clip pull-out named
---

# FlexTriage Origami Bay verification plan

Planned TRL 4 verification on paper. Nothing here is run at TRL 3. Method: STANDARDS section 25.7. The team's decision gate (two people deploy a functional three-zone bay in under 15 minutes with no training) is passed by V1; V2 and V5 must pass alongside it before any patient use. The platform's tests T1 to T8 (FXP-PLT-001) cover the shared sheet, clips and feet.

Table 1. Test families.

| Family | Method and observations | Evidence needed for the gate | Solutions | Requirements |
| --- | --- | --- | --- | --- |
| V1 Deployment and use | Three pairs of untrained people deploy from the bags with the picture card, timed by step; walk-through with a stretcher, a wheelchair and an ambulant patient; evacuation drill; sight-line check | Under 15 min, every part fitted to its own joint first time; stretcher turns; zones read correctly | FT1 (FT2 or FT3 if chosen) | PR-001, PR-002, PR-003, PR-012, PR-013, PR-019, PR-024, PR-025 |
| V2 Stability | BIFMA X5.6 style push of 178 N through a 203 mm disk at 1,110 mm, at a stub joint and between stubs, with and without bags, on dry and wet vinyl; 1:50 slope; hot soak at 40 to 50 C; anchor clip pull-out (platform T3) | No tip or slide at stub joints; force recorded between stubs against D7; folds hold 30 deg hot | FT1 | PR-006, PR-007, PR-008, PR-021, PR-028 |
| V3 Leaf and catch | Force gauge at the push plate; hold against a fan draught; 150,000 machine swings on one hinge | At most 22.2 N; holds shut; no wear-through | FT1 | PR-014, PR-017, PR-027 |
| V4 Cleaning | 120 wipes with 0.5 % hypochlorite and 70 % alcohol on faces, edges, holes, grooves, tape and prints; ATP or visual check after | No lifting, no liquid behind seals | FT1 | PR-009 |
| V5 Fire and materials | Supplier NFPA 701 TM1 and ASTM E84 reports for the bought lot; grammage weighed | Pass, at most 700 g/m2 | FT1 | PR-010, PR-011 |
| V6 Legibility and logistics | Signs read by members of a receiving team from each zone's far corner in poor light; bags weighed; parts replaced from spares | Misreading under one in ten; bags under 23 kg | FT1 | PR-004, PR-005, PR-015, PR-016, PR-018, PR-020, PR-022, PR-023, PR-026 |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
