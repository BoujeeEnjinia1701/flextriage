---
doc_id: FXT-PRB-001
title: FlexTriage Origami Bay problem statement
project: FlexTriage Origami Bay
doc_type: Problem statement
version: "0.1"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First problem statement from the Helpful Engineering project update (iteration 2), with cited burning platform, users, personas, constraints and kill criteria
---

# FlexTriage Origami Bay problem statement

Triage in surge, mass casualty and outbreak response is routinely improvised with tape on floors, repurposed tarps and makeshift barriers. Cohorts mix, staff lose spatial cues and patients have no clear path. Emergency medical teams, outbreak coordinators and field hospital operators need a rapidly deployable, lightweight bay that gives intake, assessment and treatment defined zones, a one-way flow and cues anyone can read, without permanent construction. This statement draws on the Helpful Engineering project update for the FlexTriage Origami Bay (concept iteration 2) and is a proposal for review with a co-design partner. CONCEPT, NOT FOR FABRICATION.

Release limitation (STANDARDS 25.5b): no prototype is used in patient care until its stability, fire performance, cleanability and the procedure it embeds are reviewed by qualified infection prevention and control (IPC) and safety staff.

## Burning platform

- WHO's guidance for triage stations asks for seats at least 1 m apart, 1 to 2 m between the health worker and the patient, and "one-way into the station and one-way out of the station" ([WHO AFRO, Establishing COVID-19 triage stations](https://www.afro.who.int/sites/default/files/Covid-19/Techinical%20documents/Establishing%20COVID-19%20triage%20stations%20at%20healthcare%20facilities%20-%20Key%20instructions%20and%20tips.pdf), checked 2026-11-12). Tape and tarps give neither the spacing nor the one-way path reliably.
- CDC's triage guidance for non-US settings asks for waiting seats "separated by at least one meter", a separate well-ventilated area and "clear signs at the entrance" ([CDC](https://www.cdc.gov/covid/hcp/non-us-settings/sop-triage-prevent-transmission.html), checked 2026-11-12).
- WHO's minimum standards for emergency medical teams require teams to "establish a single-entry point for patient presentation" and "a dedicated triage system for mass casualty situations", with interpreters at triage and respect for cultural aspects such as separation of gender in waiting areas ([WHO EMT classification and minimum standards, 2021](https://extranet.who.int/emt/sites/default/files/BlueBook2021.pdf), checked 2026-11-12).
- Triage systems colour patients, not rooms: START uses green (minor), yellow (delayed), red (immediate) and black (expectant) ([CHEMM, US HHS](https://chemm.hhs.gov/startalgotext.htm)); SALT and the Model Uniform Core Criteria use "immediate/red, delayed/yellow, minimal/green, expectant/gray, dead/black" ([MUCC addendum](https://www.ems.gov/assets/MUCC_Addendum_EMR.pdf), both checked 2026-11-12). A bay whose process zones are painted the same colours invites misreading (FXT-STM-001 S19).

## Users and context

Table 1. Users and needs.

| User | Context | Need | Persona |
| --- | --- | --- | --- |
| Emergency medical team lead | Field hospital or surge site, tent or hall | A triage bay standing in minutes, with zones the whole team reads the same way | P1 |
| Triage nurse | Intake and assessment, gloved, many patients an hour | Clear path, room to work round a stretcher, line of sight to the next zone | P2 |
| Outbreak response coordinator | Respiratory outbreak, cohorts by symptoms | Physical separation of cohorts and one-way flow that supports IPC practice | P3 |
| Logistician | Ships and stores kits with other relief items | Flat pack, known mass and volume, few loose parts | P4 |
| Patient (ambulant, wheelchair, stretcher) | Frightened, may not read the local language | A path that is obvious without words, doorways wide enough | P5 |
| Volunteer setting up | No training, minimal tools | Pictures, parts that only fit one way | P6 |

### Personas

- **P1 Dr. Achieng, EMT lead.** Runs a Type 1 mobile team; sets triage up in a school hall within the first hour. Measures success in minutes to the first patient.
- **P2 Tomas, triage nurse.** Works START in a red-yellow-green tagging system; needs to see the next zone over the wall.
- **P3 Priya, outbreak coordinator.** Separates suspected respiratory cases at a district hospital's entrance; worried about cohorts mixing in queues.
- **P4 Yusuf, logistician.** Moves kits by pickup and by hand from the road to the tent; counts bags and kilograms.
- **P5 Mrs. Haddad, patient.** Arrives on a stretcher; her son walks beside her; neither reads the signs' language.
- **P6 Lena, volunteer.** Assembles the bay with one other person from a picture card.

### Stakeholders

Table 2. Stakeholders.

| Stakeholder | Interest | How they shape the design |
| --- | --- | --- |
| Helpful Engineering (project team) | Open, low-cost hardware for crisis settings | Source deck, decision gate, volunteer support |
| Design Molecule Labs | Constructable open design at TRL 3 | Kit standards, shared Flex platform (FXP-PLT-001) |
| Emergency response teams (WHO EMT, MSF, named in the deck as partners to explore) | Zone configuration and procedure | Validate zones, flow and colour scheme (to engage) |
| FEMA (named in the deck) | Viability input | Review of deployment cases (to engage) |
| Site fire safety officer | Fire load, exits, FR materials | Placement rules (FXT-REG-001) |
| IPC lead at the receiving site | Cohorting, cleaning, touch surfaces | Procedure review before any patient use |
| Materials test partner (named in the deck) | Panel structural assessment | Verification at TRL 4 (FXT-VER-001) |
| Funders (the deck cites the US rural health fund) | Cost per bay and per deployment | Value-engineering target |

## Constraints

- Shared Flex platform (Amish, 2026-11-12): FXP-S4FR 4 mm FR polypropylene twinwall, the clip-lock family, feet, print and colour rules, and the structural rules S1 to S4, L1 and L2 (FXP-PLT-001).
- Indoor or in-tent use only (FXP-PLT-001 L2, proposed).
- Value-engineering target USD 800 per three-zone bay; stretch under USD 500 at volume (team deck).
- Team targets: two people deploy a 3-zone bay in under 15 minutes without training; two carry bags under 12 kg in total; 50 or more deployment cycles; about 20 m2 of floor; tool-free connectors; magnetic flaps at zone transitions; 2 to 4 zones configurable.
- No medical device claim; claims follow STANDARDS 25.5b (FXT-CLM-001).

## Out of scope

- Airborne or droplet barriers: panels are boundaries, not barriers (FXP-PLT-001 L1); no claim on transmission.
- Outdoor use without a tent (FXP-PLT-001 L2).
- Filtration (the deck's iteration 1 filtration device; the CleanAir project covers air).
- Clinical triage protocols: the bay follows the receiving team's scheme.

## Prior work

- Team iteration 1: steel or aluminium tube frame with polycarbonate panels and bolted joints, dropped on weight and volume.
- Commercial options: pipe-and-drape kits, folding medical privacy screens and retractable-belt stanchions (FXT-MKT-001).
- Patents on folding partitions and corrugated board connectors (FXT-FTO-001).

## Kill criteria (project stop rules, not a product claim)

The project stops or changes course if any of these holds at TRL 4:

- Two untrained people cannot deploy a functional 3-zone bay in under 30 minutes (twice the team target) after the fixes in FXT-DEC-001.
- A wall bay tips at a stub joint under the 178 N push with the specified ballast.
- The bought sheet fails NFPA 701 Test Method 1.
- Printed cues are misread by more than one in ten users of the receiving team in the legibility test.
- Field partners judge a bay of about 40 kg in four bags unusable for their logistics.

## User research and co-design

Every target here is a proposal until tested with an emergency medical team: zone sizes, the flow, the colour scheme, the pack and who carries it.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
