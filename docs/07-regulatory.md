---
doc_id: FXT-REG-001
title: FlexTriage Origami Bay regulatory register
project: FlexTriage Origami Bay
doc_type: Regulatory register
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First regulatory register for the carried option FT1, with the shared platform standards cited from FXP-PLT-001
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Numbers restated on FXP-PLT-001 v0.2 (zigzag walls)
---

# FlexTriage Origami Bay regulatory register

The rules that apply where the bay stands, what the design does about each, and what is still to assess. Standards shared across the Flex platform are researched once in FXP-PLT-001 (section on fire and section on loads) and cited here. This is an engineering register, not legal advice; the host's fire safety officer and the authority having jurisdiction decide on site. Links checked 2026-11-12.

Table 1. Register.

| # | Area | Rule or standard | What it asks | Applies to the bay | Design response | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | Fire, materials | NFPA 701 (2019 or later), Test Method 1 (FXP-PLT-001) | Flame propagation of curtains, draperies and similar; TM1 for areal density of 700 g/m2 or less | Panels and leaves (the platform uses the curtain test as its minimum) | Grade FXP-S4FR, at most 700 g/m2, bought with the lot's report (C1) | To verify on the bought lot (T8) |
| R2 | Fire, materials | ASTM E84 Class A interior finish (FXP-PLT-001) | Flame spread under 25, smoke developed under 450 | Panels | Supplier report asked for with the lot | To verify (T8) |
| R3 | Fire, health care | NFPA 101 sections 18.7.5 and 19.7.5 with 10.3.1, as summarised by the Minnesota Department of Health, rev. June 2024 ([PDF](https://www.health.mn.gov/facilities/regulation/engineering/lsciffurnishings24.pdf)) | Curtains in health care occupancies pass NFPA 701 | A bay in a clinic or hospital; a panel is not a curtain in the code's terms but does the same job | As R1 | To assess with the host |
| R4 | Fire, tents | International Fire Code chapter 31 as applied by the Minnesota State Fire Marshal ([PDF](https://dps.mn.gov/divisions/sfm/fire-code/Documents/Fire-Code-Information-Sheets/Temporary-tents-membrane-structures-igloos.pdf)) | Tents and their contents: flame-resistance certification, means of egress kept clear, no open flames | A bay inside a field tent | FR sheet with its report; bay off exit routes (PR-019); 1 m from heaters and flames (PR-011); label | Met by design; host check |
| R5 | Fire, prints | No FR rating for PETG prints (288 MJ of the 1,279 MJ total) | Not a code requirement as such; adds fuel | Clips and feet | FR print grade to source (C9) | To assess |
| R6 | Fire, Europe | EN 13501-1 reaction to fire class (FXP-PLT-001) | Class from the bought lot's report where quoted | Sales in Europe | Ask the supplier | To assess |
| R7 | Egress | Host building or tent egress rules (R4; NFPA 101 means of egress) | Exit routes and widths kept clear | Placement | Off exit routes; 1.5 m approach at each end; leaves lift off pins for a mass move (S33) | Met by design; V1 drill |
| R8 | Accessibility | 2010 ADA Standards 404.2.3 clear width 32 in (815 mm) and 404.2.9 opening force 5 lbf (22.2 N), which excludes latch release ([404.2](https://www.corada.com/documents/2010ADAStandards/404-2)) | Doorway width and force | Bay doorways (used as a benchmark; the bay is not a building) | 1,054 to 1,069 mm clear; push about 15 N on paper | Met on paper; V3 |
| R9 | Accessibility, signs | 2010 ADA Standards 703.5 visual characters: 40 in (1,015 mm) above the floor minimum, contrast ([703.5](https://www.corada.com/documents/2010ADAStandards/703-5)) | Sign height and contrast | Zone signs | Band 1,015 to 1,195 mm, dark on light (F1) | Met by design; T5 |
| R10 | Safety signs | ISO 3864-1:2011 safety colours ([ISO](https://www.iso.org/standard/51021.html)); ISO 7010 registered signs ([summary](https://en.wikipedia.org/wiki/ISO_7010)) | Red prohibition and fire, yellow warning, blue mandatory, green safe condition; emergency exit signs reserved | Zone colours and the way-out sign | Process zones neutral; way-out sign neutral, not an ISO 7010 emergency exit (F1) | Met by design |
| R11 | Sign legibility | ANSI Z535 viewing distance ratio as quoted ([page](https://www.safetysign.com/determine-correct-viewing-distances)) | Letter height for the viewing distance | Zone signs | 60 mm words legible at about 9 m in poor light against 4.4 m needed | Met on paper |
| R12 | Triage colours | START (CHEMM) and SALT with the Model Uniform Core Criteria ([CHEMM](https://chemm.hhs.gov/startalgotext.htm), [MUCC](https://www.ems.gov/assets/MUCC_Addendum_EMR.pdf)) | Colours name patient categories | Bay cues | Category colours only as bands with the category word (F1) | Met by design |
| R13 | Stability | ANSI/BIFMA X5.6 force stability, 178 N at 1,372 mm or 102 mm below the top (FXP-PLT-001, used as a benchmark) | No tip, no separation | Walls | Met at stub joints on paper (312 N); not met between stubs (5 to 15 N, D7) | Partly met; T7 |
| R14 | Magnetic fields | ACGIH TLV for static fields, 0.5 mT for pacemaker wearers, as summarised by UC San Diego ([page](https://blink.ucsd.edu/safety/radiation/magnet/limits.html)) | Keep wearers out of fields above 0.5 mT | Catches | Field below 0.5 mT at about 54 mm; label on every stop block (PR-027) | Met on paper |
| R15 | Medical device | Medical device rules (US FDA, EU MDR) | Apply to products with a medical purpose | The bay makes no diagnostic, therapeutic or infection claim (FXT-CLM-001) | Claims register; release limitation | Classification of a clinic partition in each market to assess |
| R16 | Health and safety at work | Manual handling: one-person lift limit of 23 kg (NIOSH recommended weight limit, as cited in FXP-PLT-001 via CCOHS) | Bag mass | Carry bags | Four bags of about 10.4 kg (D2) | Met on paper |
| R17 | Intellectual property | Patents (FXT-FTO-001) | Freedom to operate | Whole bay | Desk screen; attorney opinion (C10) | To assess |

## Notes

- The bay is a temporary furnishing inside a building or a tent; it is not a structure and makes no structural, fire-separation or infection-control rating claim.
- Local fire rules vary; the host's fire safety officer approves placement before use.
- Release limitation: no prototype is used in patient care until its stability, fire performance, cleanability and the procedure it embeds are reviewed by qualified IPC and safety staff.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
