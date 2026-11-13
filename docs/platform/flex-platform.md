---
doc_id: FXP-PLT-001
title: "Flex panel and connector platform"
project: "Flex platform (FlexClean, FlexSleep, FlexTriage)"
doc_type: Platform specification
version: "0.3"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First platform specification after Amish's decision of 2026-11-12 that FlexClean, FlexSleep and FlexTriage share one panel and connector platform; sheet grade, modules, clip-lock family, rules and the platform STEM check (platform_check.py, 26 rows); fixes F1 to F7 under the standing fix rule; decisions D1 to D13 proposed
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Independent review recorded (6 hold, 11 weak, 3 refuted of 20; 14 missed claims added as P27 to P40); FlexTriage platform requests 1 to 7 resolved or answered; through-peg clip with full-height ramp, angle clip, foot family, shared clip grid, 13.6 mm two-way fold groove, zigzag walls, seal rules E1 to E3, lot grammage cap, colour rule C6, ballast rule B1 (fixes F3 and F8 to F12); P9 and P17 now fail with a fix proposed; decisions D14 to D18 proposed
  - version: "0.3"
    date: 2026-11-12
    author: Amish Chadha
    change: Open requests R8 to R14 from FlexClean, FlexSleep and FlexTriage recorded (section 17.1); flex_parts.py unchanged, product-local parts stand until v0.3 of the parts

---

# Flex panel and connector platform

Status: CONCEPT, NOT FOR FABRICATION. Design Molecule Labs with Helpful Engineering. This document is carried as an identical copy in `docs/platform/` of FlexClean, FlexSleep and FlexTriage (STANDARDS section 25.8). Each product cites it as FXP-PLT-001 and adds only what is specific to the product. Calculations: `docs/platform/platform_check.py`, results in `docs/platform/platform_results.csv`; CAD helpers: `cad/src/flex_parts.py`. All sources were checked on 2026-11-12; links are in section 19.

Release limitation (STANDARDS 25.5b): no prototype built on this platform is used in patient care until its stability, fire performance, cleanability and the procedure it embeds are reviewed by qualified infection prevention and control (IPC) and safety staff. The platform supports IPC practice by giving care spaces physical boundaries and printed cues; it makes no claim that it prevents infection or transmission, and no panel is a barrier against a person, a fluid jet or airborne particles.

## 1. Purpose and scope

The three Helpful Engineering decks (FlexClean Origami Decon Station, FlexSleep Origami Patient Pod, FlexTriage Origami Bay, iteration 2) describe one kit of parts: pre-scored corrugated polypropylene panels (Coroplast type), tool-free clip-lock or snap connectors (the decks also say "PVC-lock joints"), printed colour and pictograms on wipe-clean faces, disinfection with bleach and alcohol, 50 or more deployment cycles and flat-pack storage. This specification defines that kit once:

- the sheet grade, its stiffness by flute direction and its fire performance;
- the fold and score geometry and the standard panel modules;
- one clip-lock connector family (inline, angle, corner, tee) and a foot family;
- edge sealing, print, disinfection compatibility and colour rules;
- the structural rules every layout must follow, with the numbers behind them;
- what each product may change and what it must not.

It does not design any of the three products. Layouts, accessories (bin hooks, gel bracket, magnetic flaps, ventilation bands, translucent upper panels) and product claims belong to each product's own documents.

Interpretation of "PVC-lock joints": the decks use the phrase in the feature tables of all three products without describing it. This specification reads it as the clip-lock connector family of section 5, which contains no PVC; a PVC tube frame is not part of the platform (decision D13).

## 2. Sheet

### 2.1 What the market offers

Corrugated PP twinwall is an extruded sheet of two skins joined by ribs; the flutes (channels) run in the extrusion direction. Stiffness, crush strength and the stated flexural rigidity are much higher along the flutes (machine direction, MD) than across them (cross direction, CD).

Table 1. Cited twinwall grades (thickness, grammage, sizes and special grades).

| Source | Thickness, grammage | Sizes | Notes |
| --- | --- | --- | --- |
| Coroplast/Interprofile product data (11/18/08) | 2 mm 490, 3 mm 600, 4 mm 750, 5 mm 1,000, 6 mm 1,400, 8 mm 1,800, 10 mm 2,000 g/m2 | not stated | FR grade at 3 and 4 mm: ASTM E84 flame spread under 25, smoke developed under 450 (NFPA 101 Class A interior finish); outdoor grade 2,500 h SAE J1960, "1 year in Miami, FL, without brittleness"; melting point about 165 C; water absorption 0.03 % |
| Coroplast graphic stock list | 2 to 10 mm | 48 x 96 in (1,219 x 2,438 mm) standard; 4 mm also 48 x 120, 50 x 100, 60 x 120 in | corona treated both sides for ink |
| Coroplast Print tolerances (May 2021) | thickness plus or minus 5 % | | squareness on sheets of 60 in and over: 5/8 in (16 mm) between diagonals; dyne level 46 minimum |
| DS Smith Akyplac 3.5 mm (06/2020) | 3.5 mm, 600 g/m2 | 2,000 x 3,000 mm | flexural rigidity (ISO 178, span 100 mm, sample 40 x 200 mm) 3.6 N/mm MD, 1.3 N/mm CD; flat crush 550 kPa; FR and UV "on request" |
| Akyplac 8 mm | 8 mm, 1,500 g/m2 | 2,000 x 3,000 mm | flexural rigidity 41.0 N/mm MD, 4.0 N/mm CD; raw PP yield 24 MPa (ISO 527-2); HDT 50 C at 1.8 MPa |
| Akyprint UV 5 mm (06/2020) | 5 mm, 1,300 g/m2 | 2,050 x 3,050 mm | raw PP flexural modulus 1,100 MPa; "UV treatment internal 18 months" |
| LaminaCorr Ultra FR | 2 to 10 mm; 700 g/m2 (4 mm) | 48 x 96 in; up to 100 in across the flutes | "passed the UL-94, NFPA 701-15 and ASTM E-84-18A" (UL 94 class not stated); anti-UV additive |
| IntePro FR line card (Sept 2020) | 4 mm, white with green tint | 96 in long | passes NFPA 701 (2019) Test Method 1; Test Method 1 applies to areal density of 700 g/m2 or less |
| Coroplast Firewall FRB SDS (5 May 2014) | white | | brominated flame retardant under 5 %, antimony trioxide under 3 %; combustion products include hydrogen bromide and antimony oxides |
| Sitebox and Safety Signs UK FR boards | 2 mm 250, 3 mm 350 to 380, 4 mm 600 to 700 g/m2; rib distance 3.2 to 3.5 mm | 2,400 x 1,200 mm | flame retardant to LPS 1207 only; no EN 13501-1 class stated |
| Correx (UK) | 2.0 to 3.5 mm, 250 to 700 g/m2 | 1.22 x 2.44 m and 1.2 x 2.2 m | FR approvals LPS 1207 and NFPA 701-2023 |

### 2.2 Platform grade (proposed, D1)

**FXP-S4FR: 4 mm flame-retardant PP twinwall, white, corona treated, UV stabilised, 48 x 96 in (1,219.2 x 2,438.4 mm) or 1.22 x 2.44 m with the flutes along the length, bought at a measured lot areal density of at most 700 g/m2 (nominal about 665 g/m2 or less, since suppliers state plus or minus 5 to 10 %) with the supplier's NFPA 701 Test Method 1 report and an ASTM E84 Class A report.** Masses and fire loads in this document use 700 g/m2, the upper bound. Reasons:

- Mass: a P18 duo panel (section 4) weighs at most 1.51 kg; the FlexTriage 12 kg two-bag target is already exceeded by one U bay at 4 mm (P17). 5 mm (1.0 kg/m2) and 10 mm (2.0 kg/m2) multiply the panel mass by 1.4 and 2.9.
- Fire: cited FR twinwall with an NFPA 701 result exists at 4 mm and 700 g/m2 (LaminaCorr Ultra FR, IntePro FR). The standard 4 mm board at 750 g/m2 lies outside the scope of Test Method 1, and a nominal 700 g/m2 board can exceed it within tolerance (P24, fix F5).
- Stiffness: no twinwall grade resists a hand push in plate bending (P4), so a thicker grade buys little; stability comes from folds, joints, plan shape and ballast (section 10).
- Availability: 48 x 96 in is the North American stock size and 1.22 x 2.44 m the UK size; 2.0 x 3.0 m European sheets cut the same modules at a lower yield (section 4).

Prototype panels for fit and fold trials may use standard 4 mm boards at 750 g/m2; any panel near people uses FXP-S4FR.

The FR chemistry of the cited grades is brominated with antimony trioxide (Coroplast Firewall SDS). A halogen-free FR twinwall would avoid hydrogen bromide and antimony oxides in smoke; availability is to assess (D11, P37).

### 2.3 Flute direction

Rule F0: flutes run vertically in every standing panel. The panel then works as a column in its stiff direction, vertical folds run parallel to the flutes (between ribs, section 3), and liquid that enters a flute drains to the sealed bottom edge rather than spreading sideways. Horizontal flutes are allowed only in parts that lie flat (foot outriggers, header strips).

## 3. Fold and score geometry

Two kinds of fold are used.

- **Fold groove (parallel to the flutes, every vertical fold; v0.2).** A flat-bottomed groove 4 flute pitches wide (13.6 mm for 4 mm board) is cut from the back face through the back skin and the ribs, leaving the front skin whole as the hinge. Its two shoulders and its two ends are heat-sealed like any cut edge (rule E1). The fold closes to 180 deg towards the back face for packing, and opens to 90 deg either way in use, so a duo can turn left or right in a plan (platform request 7). The front (print) face is continuous across the fold; artwork may cross it, text may not (rule C5). CAD: `panel(..., scores=[x])`. The routing depth tolerance that keeps the front skin whole is to assess (T2).
- **Crush score (across the flutes, flat parts only).** A creasing rule crushes the section; Curbell's conversion guide gives a creasing rule for 4 mm cross-flute creases of 0.912 to 0.918 in, 6 pt or 4 pt, and notes that twinwall needs a wider rule than paperboard. Used for the foot outriggers and header strips, never in a standing panel (a crushed band across the flutes is a hinge across the column).

Hinge geometry and strain (P13): the front skin is about 0.26 mm thick (estimated from 700 g/m2, section 15). Folded flat, the two leaves meet back to back and the skin wraps a radius of about t minus t_s/2 = 3.87 mm, which needs pi x 3.87 = 12.2 mm of free skin. The v0.1 groove (3 pitches, 10.2 mm, V-shaped) could not reach it and would have stopped at about 150 deg or crushed its shoulders (independent review). The 13.6 mm flat-bottomed groove (fix F3) gives a skin strain of 3.4 % at 180 deg and 1.5 % at 90 deg the other way. Raw PP elongation at yield is 11 % (Akyplac); FR fillers and the cross-flute direction lower it, by an amount to assess.

Hinge fatigue over 50 to 100 cycles: moulded PP living hinges survive more than a million cycles when moulded thin and flexed while warm (PlasticsToday), but an extruded skin is not oriented across the fold and there is no cited fatigue data for scored FR twinwall. 50 to 100 cycles are to assess (P14, test T2 at 5, 23 and 50 C).

## 4. Standard panel modules and heights

Leaf width is 600 mm. A "duo" is two leaves on one sheet joined by a fold groove at mid-width; it packs flat at 600 mm wide. Heights are 1,200 and 1,800 mm, with a 600 mm header strip from the offcut.

Table 2. Standard modules (FXP-S4FR, flutes vertical; masses at 700 g/m2).

| Module | Size (W x H, mm) | Folds | Mass | Clip heights (mm) | Cut from |
| --- | --- | --- | --- | --- | --- |
| P18 duo | 1,200 x 1,800 | 1 groove at 600 | 1.51 kg | 150, 1,050, 1,650 | 48 x 96 in sheet with the H06 strip |
| P12 duo | 1,200 x 1,200 | 1 groove at 600 | 1.01 kg | 150, 1,050 | two per 48 x 96 in sheet |
| H06 header or sign strip | 1,200 x 600 | none, or crush scores for a channel | 0.50 kg | 150, 450 | offcut of a P18 sheet |
| L18 and L12 single leaves | 600 x 1,800, 600 x 1,200 | none | 0.76, 0.50 kg | as P18, P12 | 2,000 x 3,000 sheets only |

Clip heights sit on one shared grid (v0.2, fix F12): 150 mm and H minus 150 mm on every panel, plus 1,050 mm on panels taller than 1,200 mm. A P12 and a P18 standing side by side therefore share their clips at 150 and 1,050 mm (platform request 5; P40).

Sheet yield: a 48 x 96 in sheet is 1,219.2 x 2,438.4 mm, which leaves a width trim of 9.6 mm per side, about 8.0 mm after the minus 1/8 in width tolerance (P15). Squareness (up to 5/8 in between diagonals on sheets of 60 in and over) is set by cutting to a square datum, not by the trim. Yield is 96.9 % for a P18 duo plus H06 strip and for two P12 duos, and 89.4 % for a 2,000 x 3,000 mm sheet cut into a P18 duo, a P12 duo, an L18 and an L12.

Standing in its feet, a P18 tops out at 1,810.5 mm (panel plus the 10.5 mm foot seat), 18.5 mm under the 1,829 mm (6 ft) threshold above which the IBC interior partition load of 0.24 kN/m2 applies (780 CMR 1607.13; P5, rule S2). Panels are cut to height with a tolerance of 0 to minus 3 mm. Staying under the threshold removes one load case; it is not evidence of strength, and BIFMA targets and the authority having jurisdiction still apply.

## 5. Clip-lock connector family

### 5.1 Concept

One clip body serves every joint: a 12 mm square core on the joint line with slot arms that each take one panel edge, each arm ending in a stop block at the core face. The family (v0.2) has four members and a foot family:

- **Inline** (slots at 0 and 180 deg): joins two panels in line. An inline joint is an unsupported edge (rule S1), so it is used only on panels up to 600 mm tall or where a tee return meets the same joint.
- **Angle** (0 and 150 deg; v0.2): the zigzag joint. Its 30 deg turn makes the joint a supported edge under rule S1. Mirrored, it turns the other way.
- **Corner** (0 and 90 deg).
- **Tee** (0, 90 and 180 deg).
- **Foot** family (section 5.4).

Clips are 100 mm tall and sit at the shared heights of section 4, so any clip fits any module (`clip_heights()` in `flex_parts.py`).

### 5.2 Dimensions and holding features

Table 3. Clip dimensions (4 mm sheet; v0.2).

| Feature | Value |
| --- | --- |
| Clip height | 100 mm |
| Core | 12 x 12 mm, 2 mm fillets; stop block to the core face in every arm |
| Slot depth (panel edge to core) | 40 mm |
| Slot gap | 4.5 mm (sheet plus 0.5 mm; takes sheet of 3.8 to 4.2 mm, P35) |
| Slot wall | 2.5 mm |
| Snap tongues | two per slot, at plus and minus 25 mm from the clip centre; 14 mm wide, tapered from 1.5 mm at the root to 0.75 mm at the free end, 24.5 mm free length, rooted 3 mm inside the slot mouth |
| Through-peg (fix F8) | 7 mm round, 5.5 mm tall: through both skins of the panel into a 1.0 mm socket in the back slot wall |
| Lead-in (fix F9) | 45 deg ramp on the mouth side over the whole peg height; straight retaining face on the core side |
| Release | a pull lip on each tongue; two fingertips pull both lips while the other hand pulls the panel |
| Panel holes | 8 mm, hot-punched and fused (rule E1), 12.5 mm from the edge, two per clip position |

How it holds: the panel edge slides into the slot and rides up the ramp, which lifts the tongue; at full depth the peg drops through both skins of the panel into the socket. Home, the tongue is unstrained (no creep), and the peg is held at both ends, by the tongue and by the socket. Pull-out is resisted by the peg bearing on both skins; shear along the joint by the slot walls and the peg.

Numbers (P9 to P12, v0.2): the v0.1 peg (3.7 mm tall in a 4.2 mm slot) reached only the near skin and held about 44 N per peg, so P9 was refuted by the review. The through-peg bears on both skins: about 88 N per peg (bearing; tear-out 123 N), 176 N per clip. Demand under the 178 N BIFMA push is not bounded on paper: about 162 N per clip by the v0.1 estimate, up to about 1,160 N per panel edge if the bowed leaf works as a string with held edges. Thin FR skins may also crumple before they reach full bearing. The holding principle therefore waits for the pull-out and bay tests (T3, T7) and decision D14. The peg shears at about 336 N even with a 0.3 derate for printed layers. Tongue strain is 1.26 % (Bayer tapered arm), 2.5 % with an assumed root factor of 2, against half the PETG strain at yield (2.95 %). Deflection force is about 5.5 N per tongue; insertion about 29 N per slot through the panel edge; release 5.5 N per lip.

### 5.3 Materials

- Prototype: PETG print (BCN3D PETG: yield 50.4 MPa, modulus 2,020 MPa, strain at yield 5.9 %, HDT 70 C), printed with the tongues lying flat so the layers run along them, 100 % infill at tongues and pegs.
- At scale: injection-moulded PP copolymer, so sheet and clip are one polymer family for chemical resistance and recycling. The moulding grade, its strain limit and cored clips and feet are to assess (D4).
- Full-detail CAD volume about 51.5 cm3 for inline, corner and angle clips and 70.3 cm3 for a tee; at an assumed PETG density of 1,270 kg/m3 an inline clip prints at about 67 g solid.

### 5.4 Foot family and outrigger (v0.2)

The foot is a moulded block (120 x 70 x 40 mm for an inline joint, 120 x 120 x 40 mm for the others) with 4.5 mm slots on the joint's panel lines and outrigger beams that reach 300 mm from the joint line. Each outrigger is folded from twinwall offcut into a triangular beam with 50 mm sides, apex up, standing on the floor (blank 170 mm wide, crush scored across the flutes). The v0.1 helper built the +y outrigger apex-down below the floor (platform request 3); v0.2 builds every outrigger on the floor. Outriggers point only into free directions, so none crosses a panel (platform request 4):

| Kind | Slots | Outriggers | Use |
| --- | --- | --- | --- |
| inline (v0.1 name "tee", still accepted) | 0, 180 deg | 90, 270 deg | inline joints and free wall ends |
| corner | 0, 90 deg | 45, 225 deg (diagonals) | corners |
| junction | 0, 90, 180 deg | 270 deg | tee joints |
| cross | 0, 90, 180, 270 deg | four diagonals | four-way joints |

A ballast tray on the foot takes a 5 kg bag of sand or gravel, filled on site; water only double-bagged in a lipped tray (rule B1, P39). The panel's bottom edge sits 10.5 mm above the floor. Non-slip pads under the block are to assess (D17, P27). The block is solid in CAD (about 0.40 kg in PETG); coring is to assess (D4).

## 6. Edge protection and cleanability

Open flutes and crevices cannot be wiped (P22). The review found three the v0.1 rule missed: the open back-face groove (13.6 mm wide along the full height, with flute ends at top and bottom), the half-flute troughs on cut edges parallel to the flutes, and the clip slots. Rules (fix F4, v0.2):

- **E1:** every cut edge is heat-sealed (flute ends fused closed over about 2 mm, modelled as an edge break), including the two groove shoulders and the groove ends; every clip hole is hot-punched so the skins fuse round the hole.
- **E2 (platform request 2):** a groove face looks away from care zones where the layout allows. Where it faces a care zone, the groove is covered by a flexible clear PP strip heat-staked or taped along both shoulders. Tape lift is a known failure mode (FlexTriage FMEA), so the strip and its fixing are part of test T6.
- **E3:** clips come off the panels for cleaning between deployments; slots are never cleaned in place.

Seal integrity under repeated wiping is unproven (T6). The alternative of a U-profile edge trim is decision D8; a PVC profile, as the decks' "PVC-lock" wording hints, would add chlorine to the fire products.

## 7. Print

Print and pictograms go on the front face only. Two methods are possible:

- **Direct UV-cured inkjet on the corona-treated face.** Fujifilm's Uvijet KX data sheet lists Coroplast with the note "media quality varies, test before production", expects adhesion at 42 dyn/cm or above (Coroplast ships at 46 minimum), and reaches full chemical and scuff resistance only 24 hours after curing. No cited data covers UV inks under repeated hypochlorite or alcohol wipes.
- **Print under a clear overlaminate film** bonded to the face. This puts a known film between the ink and the disinfectant; the film's own compatibility, edge lift and fire behaviour are to assess.

Recommendation (D3): print under a clear PP overlaminate for the TRL 4 coupons, with direct UV print as the comparison. Legibility after disinfection is plausible but unproven (P21) and is the purpose of test T4.

## 8. Disinfection compatibility

Table 4. Compatibility of sheet, connector and print with the four disinfectant families (v0.2 after the review; all "to assess" until T4).

| Agent (use strength) | PP twinwall sheet | PETG prototype clip | Moulded PP clip | Print |
| --- | --- | --- | --- | --- |
| Sodium hypochlorite 0.5 % | CP Lab: under 20 % "A"; INEOS: concentrated S at 21 C, O at 60 C; but Akyplac's own sheet says PP is "not resistant to substances with an oxidizing effect" | Curbell tested about 0.10 to 0.16 % NaOCl (5 tablespoons of household bleach per gallon) on flat unstressed sheet: 0.5 % to assess | as sheet | to assess (T4) |
| Alcohol 70 % (ethanol or isopropanol) | CP Lab: ethanol A; isopropyl A2 (satisfactory to 48 C); INEOS S | Compatible, isopropyl 70 % (Curbell) | as sheet | to assess (T4) |
| Quaternary ammonium | Not listed on either chart; detergents A (CP Lab): uncited, to assess | Not listed: to assess | to assess | to assess (T4) |
| Hydrogen peroxide (3 to 7.5 %, accelerated) | 10 % A (CP Lab); 30 % S at 21 C, O at 60 C (INEOS); PP excellent with AHP (Virox) | Compatible at 3 to 5 % (Curbell) | as sheet | to assess (T4) |

The charts rate resin immersion, not the FR additive, UV stabilisers (which oxidisers attack), print, staining or stress cracking. Printed PETG traps fluid between layers. Wet chlorine is rated severe for PP (CP Lab "chlorine water D"); panels are not stored wet with bleach. T4 runs each agent at its label contact time at 23 and 45 C, with mixed products (quat plus alcohol) as sold.

## 9. Fire performance

PP is combustible (P23), and the FR grade does not reduce its fire load; it delays ignition and flame spread, and PP still melts and drips (P38). Its heat of combustion is 39.7 MJ/kg (FSRI), so FXP-S4FR carries 27.8 MJ/m2, a P18 duo 60 MJ and a six-duo U bay 360 MJ of fire load. Solid 3.3 mm PP reached a peak heat release rate of 1,340 to 1,680 kW/m2 in the cone calorimeter at 25 kW/m2 (FSRI); twinwall is thinner and hollow, so ignition is faster. A non-FR twinwall partition round a sleeping patient is not acceptable. Smoke from the cited FR grades contains hydrogen bromide and antimony oxides (SDS); IARC places antimony trioxide in Group 2B (1989) and trivalent antimony in Group 2A (volume 131), so smoke toxicity in patient spaces is to assess (P37, D11).

Targets (rule FR1): FR grade only, for every panel used near people.

| Benchmark | What it is | Platform target |
| --- | --- | --- |
| NFPA 701 (2019 or later), Test Method 1 | Flame propagation of curtains, draperies and similar; TM1 for areal density of 700 g/m2 or less; pass criteria include an average flaming drip under 2 s (IntePro) | Pass, supplier report on the bought lot, measured lot areal density at most 700 g/m2 (fix F5; P24, P38) |
| NFPA 286 | Room-corner fire test for interior finish, which shows melting and dripping that a tunnel test can miss | Proposed as the first benchmark for a 1.8 m partition (D18); availability of reports to assess |
| ASTM E84 | Tunnel test for interior finish; Class A is flame spread 25 or less, smoke developed 450 or less | Class A (Interprofile FR grade reaches it at 3 and 4 mm) |
| UL 94 | Small-flame plastics rating (V-0, V-1, V-2, HB; VTM for thin films) | V-0 or VTM-0 as a target; LaminaCorr states a UL 94 pass without the class: to assess |
| EN 13501-1 | European reaction-to-fire class A1 to F with smoke s1 to s3 and droplets d0 to d2 (EN 13823 SBI, EN ISO 11925-2) | No cited classification for FR twinwall; FR solid PP film 0.35 to 0.70 mm reached B-s2,d0 on a metal frame with an 80 mm air gap (Efectis EFR-25-000397). Target to be set after supplier quotes (D2; P25) |

Health care context: NFPA 101 sections 18.7.5 and 19.7.5 with 10.3.1 require curtains, including cubicle and privacy curtains, in health care occupancies to pass NFPA 701 (as summarised by the Minnesota Department of Health, rev. June 2024). A freestanding panel round a bed is not a curtain in the code's terms, but it does the same job, so the platform uses the curtain test as its minimum. Whether a deployment authority treats the panels as furnishings, decorations or interior finish is to assess for each site; decorations in some codes may instead show a heat release rate of 100 kW or less in NFPA 289.

What this means for each product:

- **FlexSleep** (panels round a sleeping, possibly immobile patient): the most demanding case. FR grade with NFPA 701 TM1 and ASTM E84 Class A reports before any use; no heat sources, lamps or chargers fixed to panels; frosted or mesh upper panels need their own fire report, because a non-FR mesh would undo the grade; egress from the open end kept clear.
- **FlexClean** (doffing corridor with alcohol-based hand rub at the panel 4 to 5 transition): the hand rub is a flammable liquid beside a combustible wall. The gel bracket keeps the dispenser off the panel face and away from any ignition source; dispenser rules for health care settings are to assess in the FlexClean regulatory register.
- **FlexTriage** (several bays and the largest panel area per room): the largest fire load (360 MJ for one six-duo U bay); bay layouts keep exit routes clear of panels and are reviewed with the site's fire safety staff.

## 10. Structural rules

The numbers come from `platform_check.py` (section 15). Twinwall is stiff only along its flutes and only in its own plane; as a plate it is floppy. The rules turn that into a structure the way a folded box does. "Hot" means 40 to 50 C in a tent: stiffness is taken at 0.5 of the 23 C value to cover heat and creep over a deployment (assumed; the ISO 75 heat deflection temperature of 50 C at 1.8 MPa alone implies about 0.78 for a short load).

- **S1 (fix F1, v0.2): every vertical edge of a panel taller than 600 mm, P12 included, is supported:** a fold or angle joint that turns by at least 30 deg, a corner or a tee. Straight walls are built as zigzags: leaves alternate 15 deg either side of the wall line, with the duo folds and angle clips at 30 deg. A flat 4 mm FR panel buckles under its own weight at about 1,440 mm with a clamped base, 1,144 mm hot (P2); a flat P12 strip has a load margin of 1.73 cold but 0.87 hot, which is why v0.2 extends S1 to P12 (platform request 1). A 600 mm leaf supported on both vertical edges keeps a margin of 3.1 cold and 1.6 hot with a load factor of 2 included, using the orthotropic buckling formula with zero twisting stiffness (P3; v0.1 used k = 4 and overstated it).
- **S2: panel height at most 1,800 mm, top at most 1,810.5 mm in its feet** (section 4; P5).
- **S3 (fix F2): no single freestanding panel; the minimum layout is an L, a U or a closed plan, with a 5 kg ballast bag on each foot at the far end of a return.** A flat P18 duo on two feet tips at about 6 N against the 178 N BIFMA X5.6 force stability push at 1,372 mm, and would need 40 kg of ballast per foot (P6). A zigzag U of P18 duos (about 2.3 x 2.3 m in plan) tips at about 77 N without ballast; with 5 kg at each far return foot it holds about 242 N if the U acts rigidly (P7). It does not: the push reaches the returns through a bowing leaf and clips (P4, P9), so 242 N is an upper bound and T7 decides.
- **S4 (v0.2): inline (180 deg) joints only on panels up to 600 mm tall, or where a tee return meets the same joint.** This replaces the v0.1 rule of a 1,200 mm unsupported run, which the platform's own U bay broke (platform request 1).
- **Sliding (P27):** the ballasted U bay (about 23.3 kg) slides at about 57 N if floor friction is 0.25 (assumed); it can tip only if friction exceeds about 1.06. Sliding caps the tipping load, but a bay that slides moves its zone lines (D17).
- **Impact (P28):** tipping the ballasted U over its back wall base line needs about 295 J. The BIFMA X5.6 5.2 bag energy depends on a pendulum length the cited report does not give, so the margin is to assess (T7).
- **L1 (stated limit, D5): panels are boundaries, not barriers.** A 600 mm leaf would bow about 760 mm (small-deflection theory, four edges held) under the 178 N push, and reaches 25 mm at about 6 N; 10 mm board still bows about 90 mm; a free top edge is worse (P4). The BIFMA criteria the platform targets are no tipping, no separation of components and no loss of serviceability, not stiffness. Staff and patients must not lean on panels; each product says so on the panel.
- **L2 (stated limit, D6): indoor use or use inside a tent only.** A 10 m/s wind gives 61 Pa and about 238 N m of overturning moment on a 2.4 x 1.8 m wall; the ballasted U restores about 333 N m, less than 1.5 times that (P8). Tent door gusts and fans are not checked.
- **Thermal expansion (P31):** a 2.4 m wall grows about 7.9 mm over a 30 C swing (0.11 mm/(m C), Akyprint); a zigzag takes it with a fold angle change of about 0.7 deg.

Table 5. Stiffness, free height and push response by grade (vertical flutes; EI per mm of width, fitted effective values, not bounds).

| Grade | Skin (mm) | EI_MD (N mm2/mm) | EI_CD (N mm2/mm) | Flat free height allowed, cold / hot (mm) | Leaf margin at 1,800 mm, cold / hot | Leaf deflection at 178 N (mm) | Push for 25 mm (N) | Mass (kg/m2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 mm FR 700 (FXP-S4FR) | 0.26 | 2,621 | 766 | 1,144 / 908 | 3.1 / 1.6 | 764 | 5.8 | 0.70 |
| 4 mm 750 | 0.28 | 2,782 | 813 | 1,140 / 905 | 3.1 / 1.6 | 720 | 6.2 | 0.75 |
| 5 mm 1,000 | 0.40 | 5,883 | 1,208 | 1,330 / 1,055 | 4.1 / 2.1 | 406 | 11.0 | 1.00 |
| 6 mm 1,400 | 0.56 | 11,540 | 1,775 | 1,488 / 1,181 | 5.0 / 2.5 | 239 | 18.6 | 1.40 |
| 8 mm 1,800 | 0.72 | 26,559 | 2,591 | 1,807 / 1,434 | 7.2 / 3.6 | 131 | 34.1 | 1.80 |
| 10 mm 2,000 | 0.79 | 47,062 | 3,225 | 2,111 / 1,675 | 9.6 / 4.8 | 88 | 50.6 | 2.00 |

At 10 % under nominal grammage, the 4 mm FR grade's EI falls to about 2,390 and 700 N mm2/mm (P1). EI_CD comes from a 100 mm span test that shear dominates, so it understates CD bending at 600 mm spans; the values are conservative there.

Design load: ANSI/BIFMA X5.6 force stability, 178 N (40 lbf) through a 203 mm disk at 1,372 mm or 102 mm below the top, whichever is lower; the product may tilt up to 10 deg but must not tip over, and components must not separate; 5.2 impact stability uses a 22.7 kg bag swung through 610 mm (as quoted in an SGS test report).

## 11. Packing

- Mass: 0.70 kg/m2 (FXP-S4FR, lot maximum); P18 duo 1.51 kg, P12 duo 1.01 kg, H06 strip 0.50 kg; clip about 67 g (PETG, solid); foot about 0.46 kg with outriggers.
- Pack: a P18 duo folds to 600 x 1,800 mm and about 10 mm thick, 10.8 L. Three folded duos stack to about 30 mm, inside the 10 cm the FlexSleep deck allows.
- Carry (P16): one person carries a folded duo horizontally under the arm (1.51 kg). The NIOSH load constant of 23 kg is quoted only as a ceiling: it belongs to a two-handed lifting method. A 1.8 m fold cannot hang from one hand, and its 1.08 m2 catches wind outdoors.
- Pack mass (P17, refuted in review and now "Fails, fix proposed"): a zigzag U bay needs 6 P18 duos (9.07 kg), 7 feet (3.22 kg), 15 clips (1.01 kg) and about 1 kg of bags: 14.3 kg, 19 % over the FlexTriage 12 kg two-bag target. Cored moulded feet of 0.15 kg and clips of 0.04 kg (assumed targets) would bring it to about 11.7 kg. Ballast is filled on site and never carried. Decision D15.
- Bag: 0.62 x 1.82 m flat bag; folds across the flutes to shorten it are not allowed (section 3).

## 12. Colour and pictogram rules

- **C1 (fix F6): colour is never the only code.** About 1 in 12 men and 1 in 200 women of Northern European ancestry have red-green colour vision deficiency (MedlinePlus). Every zone colour also carries a word, a shape and a pattern band; red and green zones are never adjacent without a white band at least 100 mm wide. Effectiveness is unproven (P26, test T5).
- **C2: safety colours keep their ISO 3864 meanings.** ISO 3864-1 (2011) sets red for prohibition and fire equipment, yellow for warning, blue for mandatory action and green for safe condition, with white or black contrast; ISO 3864-4 (2011) gives the colorimetric values. The RAL matches (3001, 1003, 5005, 6032) come from a Wikipedia summary; the standard's own values, and the ISO 3864-1 sign-size distance factor, are to be read from the purchased standards (D16).
- **C3: safety signs are ISO 7010 graphical symbols** (built on ISO 3864) where a registered symbol exists; custom pictograms follow ISO 3864-3 design principles. Doffing sequences and their pictograms cite WHO and CDC PPE guidance and are reviewed by an IPC specialist before use (STANDARDS 25.5b).
- **C4: triage colours follow the scheme the receiving team uses.** START uses green (minor), yellow (delayed), red (immediate) and black (expectant) (CHEMM, US HHS).
- **C5: print zones** sit at least 25 mm from clip holes; folds may be crossed by continuous artwork, never by text.
- **C6 (fix F10, v0.2): triage and zone colours never take a safety-sign form.** Triage red, yellow and green appear only as zone bands carrying the category word and the C1 shape, never as the background of a sign; ISO 7010 signs on the same panel keep their own shapes, borders and contrast colours. This resolves the clash between triage red and green and ISO 3864 fire-equipment red and safe-condition green in one bay (P36).

## 13. What each product may change and what it must not

Each product may:

- choose its own layout from the standard modules, within rules S1 to S4;
- choose print content, zone colours and pictograms within section 12;
- add accessories that clip to the standard hole pattern or to an H06 strip (bin hooks, gel bracket, magnetic flap frames, labels), each with its own mass, fire and cleaning check;
- add a product material (FlexSleep translucent upper panel, ventilation perforations in a lower band) if the product's own STEM check covers its stiffness, sealing and fire performance and the perforations stay at least 50 mm from folds, holes and edges;
- use `clip(detail="light")` in bay assemblies to keep the STEP size down.

Each product must not:

- change the sheet grade, its flute direction or its lot grammage cap without a new fire report and an update of this document;
- exceed 1,800 mm in panel height or stand a single panel on its own;
- change the clip grid, the clip slot or the peg, or mix clip generations (v0.1 and v0.2 pegs) in one bay;
- leave cut edges, groove shoulders or holes unsealed;
- use colour as the only code, or use a safety colour or sign form for a non-safety meaning;
- claim barrier, airborne or isolation performance, or any wording banned by STANDARDS 25.5b; it carries the release limitation;
- use the platform outdoors (limit L2) unless Amish decides otherwise and an outdoor case is checked.

Platform changes are made here first and copied unchanged to all three repos.

## 14. Planned TRL 4 tests (paper only)

These are listed so that each product's verification plan (VER) can cite them; none has been run, and no prototype exists.

| Test | What it measures | Closes |
| --- | --- | --- |
| T1 | ISO 178 flexural rigidity of the bought FXP-S4FR lot, MD and CD, at 100 and 400 mm spans, 23 and 50 C; lot grammage | P1, P3, P29 |
| T2 | Fold groove: 100 cycles 0 to 180 deg back and 0 to 90 deg front, at 5, 23 and 50 C; skin cracking, fold accuracy, routing depth | P13, P14, P30 |
| T3 | Clip pull-out per panel edge (through-peg, both skins), and retention per cycle over 100 release cycles, with hole wear and ovalisation, at 5, 23 and 50 C | P9, P11, P14 |
| T4 | 120 wipes with a 30 min dry for each agent of section 8 at label contact times, 23 and 45 C, on sheet, clip, sealed edge, groove strip and print coupons | P18 to P21 |
| T5 | Clip use with gloved hands; zone legibility with colour-deficient observers; sharp-edge and pinch check | P12, P26, P34, P36 |
| T6 | Edge, groove and hole seal integrity after T4 (dye ingress), groove strip lift | P22 |
| T7 | BIFMA X5.6 5.1 force stability and 5.2 impact on an L, a U and a closed bay, with and without ballast and pads; floor friction | P7, P27, P28, L1 |
| T8 | NFPA 701 TM1, ASTM E84 and NFPA 286 reports for the bought lot; drip behaviour; EN 13501-1 class if quoted | P24, P25, P38 |

## 15. Platform STEM check summary

Method: STANDARDS sections 20 and 25.6a (structures). EI per flute direction comes from a sandwich section (two skins and ribs, skin thickness solved from grammage at 886 kg/m3, flute pitch assumed 3.4 mm for 4 mm board from the cited 3.2 to 3.5 mm rib distance) fitted to the two Akyplac ISO 178 data points through three-point bending, k = 48 EI / L^3 (L = 100 mm, b = 40 mm). The fitted effective modulus is 1,249 MPa, above the raw resin's 1,100 to 1,150 MPa, so the section model under-counts I or the skins are oriented; EI is a fitted effective value, not a bound, and the model reproduces both data points within 7 %. CD stiffness uses the measured CD/MD ratio (0.36 at 3.5 mm, 0.10 at 8 mm), interpolated in log thickness. Free height uses Greenhill's self-weight buckling, h_cr = (7.837 EI/q)^(1/3); leaf buckling the orthotropic formula N_cr = pi^2/b^2 (2 sqrt(D1 D2) + 2 D3) with D3 = 0; leaf deflection w = alpha P b^2/D with alpha = 0.0169 for a simply supported plate of aspect 3 (Timoshenko and Woinowsky-Krieger); hot cases use 0.5 of the 23 C stiffness (assumed). These are first-order screens.

Verdicts (v0.2): 40 rows; 11 within known science (most closed by fixes or rules), 25 plausible and waiting for TRL 4 evidence, 4 fail with a fix proposed that waits for Amish (P4 stated limit L1, D5; P8 indoor only, D6; P9 clip holding, D14; P17 pack mass, D15); none fails outright. `platform_check` state: open. v0.1 had 26 rows (14 within, 10 plausible, 2 fail with a fix proposed); the independent review of section 16 moved several rows from within to plausible and added 14 rows.

Table 6. Platform STEM check (generated from `docs/platform/platform_results.csv`).

<!-- PLT_TABLE -->
| # | Claim | Check | Verdict | Closed by |
| --- | --- | --- | --- | --- |
| P1 | Bending stiffness EI of corrugated PP twinwall per unit width can be estimated per flute direction from grammage | Fitted E_eff 1249 MPa, above the raw resin (1100 to 1150 MPa), so the section model under-counts I or the skins are oriented: EI is a fitted effective value, not a bound; within 7 % of both data points. 4 mm FR 700: EI_MD 2,621, EI_CD 766 N mm2/mm; at -10 % grammage 2,390 and 699. EI_CD at a 100 mm span is shear-dominated, so it under-states CD bending at 600 mm spans (conservative there); 4 to 10 mm values are interpolated, not measured | Plausible, to confirm at TRL 3 | T1: ISO 178 on the bought lot, both directions, at 100 and 400 mm spans, 23 and 50 C |
| P2 | Every platform panel above 600 mm stands only with both vertical edges supported (fold or angle joint of 30 deg or more, corner or tee) | Flat 4 mm FR: h_cr 1441 mm cold, 1144 mm hot (x 0.5 stiffness); a flat P12 strip has a load margin of 1.73 cold and 0.87 hot, a flat P18 strip fails outright; 10 % lighter sheet lowers h_cr by about 3 %. Fixed by rule S1 for every panel above 600 mm (P12 included); the supported leaf is P3 | Within known science | Fix F1 (rule S1, v0.2: P12 included, angle clip) |
| P3 | A 600 mm leaf supported on both vertical edges carries its own weight at 1800 mm without buckling, cold and hot | Margin 3.1 cold and 1.6 hot, load factor 2 included, at D3 = 0 (v0.1 used k = 4 and gave 6.3; uniform base load is conservative). An edge at a 30 deg fold or angle clip is held laterally by the next leaf's in-plane stiffness x sin 30 = 0.5, which is far stiffer than the restraint buckling needs, but this is not computed here | Plausible, to confirm at TRL 3 | Rule S1; T1 hot and T7 bay test at 23 and 50 C |
| P4 | Panels are boundaries, not barriers: a 600 mm leaf bows well past 25 mm under the 178 N BIFMA push | 4 mm FR: 764 mm at 178 N (small-deflection theory; membrane action limits it); 25 mm at 5.8 N. 10 mm: 88 mm. No twinwall grade resists a hand push in bending; the claim is dropped and stated as limit L1 | Fails, fix proposed | D5 Proposed, awaiting Amish: stated limit L1 in every product |
| P5 | Platform panels, standing in their feet, top out below 1829 mm, outside the scope of the IBC interior partition load (780 CMR 1607.13) | 1810.5 mm <= 1829 mm | Plausible, to confirm at TRL 3 | Rule S2 (cut height tolerance 0 to -3 mm) |
| P6 | No platform layout relies on a single freestanding panel | A flat P18 duo on two standard feet tips at 6.1 N against the 178 N BIFMA push; it would need 40 kg of ballast per foot. Fixed by rule S3 (L, U or closed plans only) | Within known science | Fix F2 (rule S3) |
| P7 | A zigzag U bay (2.3 m back and returns of P18 duos) with a 5 kg bag at each far return foot does not tip under the 178 N push | Unballasted 77 N; ballast needed 3.1 kg per far foot; with 5 kg 242 N. Not modelled: the push reaches the returns through a leaf that bows (P4) and clips (P9), so the rigid-U figure is an upper bound on what the bay resists before a joint lets go; BIFMA 5.1 also asks for no loss of serviceability | Plausible, to confirm at TRL 3 | Fix F2 (rule S3, zigzag walls in v0.2); T7 bay test |
| P27 | A bay slides on the floor before it tips under a push | Ballasted U bay 23.3 kg: slides at 57 N if mu = 0.25 (ASSUMED; floor and pad friction not cited); it can only tip if mu exceeds 1.06. Sliding caps the tipping load, which helps, but a bay that slides moves zone lines | Plausible, to confirm at TRL 3 | D17 Proposed, awaiting Amish: accept sliding or add non-slip pads; T7 measures mu |
| P28 | The ballasted bay does not tip under the BIFMA X5.6 5.2 impact (22.7 kg bag, 610 mm horizontal swing) | Tipping needs about 295 J; the bag's energy depends on its pendulum length, which the report does not give (the reviewer's 34 J is not cited): to assess. Local damage to the struck leaf is not covered | Plausible, to confirm at TRL 3 | T7 impact case |
| P8 | The platform is for indoor use or use inside a tent | 10 m/s gives 61 Pa and 238 N m on a 2.4 x 1.8 m wall; the ballasted U restores 333 N m, under 1.5 x the wind moment. Outdoor use fails; tent door gusts and fans are not checked | Fails, fix proposed | D6 Proposed, awaiting Amish: indoor or in-tent only (stated limit L2) |
| P9 | Clips hold the panel edges under the 178 N BIFMA push (no separation) | v0.1 peg (3.7 mm) reached the near skin only: 44 N per peg, refuted. v0.2 through-peg (fix F8) bears on both skins: 88 N per peg, 176 N per clip. Demand is not bounded on paper: 162 N per clip if two of three clips share the v0.1 estimate (324 N per edge, delta 165 mm is a BIFMA stop, not a sag), up to 1158 N per edge if the leaf acts as a string with held edges (delta 23 mm). Thin FR skins may crumple before full bearing | Fails, fix proposed | Fix F8 (through-peg); D14 Proposed, awaiting Amish: holding principle settled by T3 and T7 |
| P10 | The PETG through-peg does not shear before the panel hole yields | 335.952 N >= 87.82 N | Within known science |  |
| P11 | The tapered snap tongue deflects by the full through-peg height (5.5 mm) below half the PETG strain at yield, root factor included | 2.52188 % strain <= 2.95 % strain | Plausible, to confirm at TRL 3 | Moulded PP strain limit to assess (D4); T3 cycles; print the tongue lying flat |
| P12 | Clipping and release are tool-free with gloved hands: push the panel home; release with two fingertips on the two lips while the other hand pulls | Deflection 5.5 N per tongue; insertion about 29 N per slot pushed through the panel edge; release 5.5 N per lip over 5.5 mm. The v0.1 peg (1.2 mm lead-in on a 3.7 mm peg) could not cam and was refuted; no cited hand-force limit is used, and the two-handed method is stated | Plausible, to confirm at TRL 3 | Fix F9 (full-height ramp); T5 with gloved users |
| P13 | The flat-bottomed fold groove (front skin only) folds 180 deg for flat-pack and +-90 deg either way in use | R 3.87 mm needs 12.2 mm of free skin: the v0.1 groove (10.2 mm) stopped at about 150 deg; v0.2 groove 13.6 mm (4 pitches, flat-bottomed) gives 3.4 % at 180 deg and 1.5 % at 90 deg the other way. Raw PP elongation at yield is 11 % (Akyplac); FR fillers and cross orientation lower it: to assess. Routing depth tolerance to assess | Plausible, to confirm at TRL 3 | Fix F3 (groove 4 pitches, flat bottom, two-way); T2 at 5, 23 and 50 C |
| P14 | Folds and clip joints survive 50 to 100 deployment cycles with at least 80 % of their first retention | Hinge 3.4 % per fold, tongue 2.5 % at the root per cycle; no data for scored FR twinwall or printed PETG tongues; holes ovalise with each cycle; the 80 % retention target is ASSUMED: to assess | Plausible, to confirm at TRL 3 | T2 and T3 (with hole wear and retention per cycle) at TRL 4 |
| P15 | Standard modules cut from a 48 x 96 in (1219.2 x 2438.4 mm) sheet with under 5 % waste | 96.8752 % yield >= 95 % yield | Within known science |  |
| P16 | One person carries a folded P18 duo under the arm, held horizontal | 1.512 kg <= 23 kg | Within known science |  |
| P17 | A 12 kg two-bag pack (FlexTriage deck target) holds a 2.3 x 2.3 m zigzag U bay of P18 duos | 6 duos 9.07 kg + 7 feet 3.22 kg + 15 clips 1.01 kg + bags 1.0 kg = 14.3 kg, 19 % over 12 kg (the v0.1 row counted 6 feet and read Plausible: refuted). Cored feet of 0.15 kg and clips of 0.04 kg (ASSUMED targets) would give 11.7 kg | Fails, fix proposed | D15 Proposed, awaiting Amish: pack target, bag count or lighter moulded feet and clips |
| P18 | PP sheet tolerates 0.5 % sodium hypochlorite, 70 % alcohol and 3 to 7.5 % hydrogen peroxide at the label contact time | Resin immersion data only: the Akyplac sheet itself says PP is not resistant to oxidising substances, and oxidisers attack UV stabilisers; the FR additive, print and tent temperatures of 40 to 50 C are not covered | Plausible, to confirm at TRL 3 | T4 at 23 and 45 C with 0.5 % NaOCl, 70 % alcohol, a named quat and accelerated H2O2 at label contact times |
| P19 | PP sheet tolerates quaternary ammonium disinfectants | Uncited: to assess with a named quat product's maker list | Plausible, to confirm at TRL 3 | T4 |
| P20 | PETG prototype clips tolerate 0.5 % sodium hypochlorite, 70 % isopropanol and 3 to 5 % hydrogen peroxide | 0.5 % NaOCl is about 3 to 5 times the tested strength and printed parts trap fluid between layers: to assess. The v0.2 tongue is unstrained at rest, which lowers the stress-cracking risk | Plausible, to confirm at TRL 3 | T4 on printed clips; moulded PP clips at scale fall under P18 |
| P21 | Printed pictograms stay legible after repeated disinfectant wipes | To assess (no evidence either way). Proposed protection: clear PP overlaminate (D3) | Plausible, to confirm at TRL 3 | T4: 120 wipes, 30 min dry per agent, legibility scored |
| P22 | Sealed panel edges, fold grooves and clip holes can be wiped clean between uses | Fixed by rule E1 v0.2 (every cut edge heat-sealed, including the two groove shoulders and the groove ends; hot-punched fused holes), rule E2 (groove face away from care zones or covered by a flexible PP strip) and rule E3 (clips come off for cleaning); seal integrity unproven | Plausible, to confirm at TRL 3 | Fix F4 (rules E1 to E3); T6 dye ingress after T4 |
| P23 | Twinwall panels are combustible and add fire load to a care space; the FR grade does not reduce that fire load | 27.8 MJ/m2; 60 MJ per P18 duo; 360 MJ per six-duo U bay. FR delays ignition and spread; PP still melts and drips (P39) | Within known science | Rule FR1: FR grade only near people |
| P24 | The platform FR grade is bought at a measured lot areal density of at most 700 g/m2 (NFPA 701 TM1 scope) | 700 g/m2 (lot maximum) <= 700 g/m2 (lot maximum) | Within known science | Fix F5 v0.2 (lot maximum, not nominal); D18 Proposed, awaiting Amish: benchmark hierarchy (NFPA 286 or ASTM E84 first, NFPA 701 second) |
| P25 | An FR twinwall grade can reach a European reaction-to-fire class (EN 13501-1) | No twinwall classification found; the FR solid film report (B-s2,d0 on a metal frame with an air gap) is a different product and mounting and is not evidence: to assess | Plausible, to confirm at TRL 3 | D2: target class set by Amish after supplier quotes |
| P26 | Zone colours are read correctly by staff with red-green colour vision deficiency | Colour alone fails; fixed by rule C1 (text, shape and pattern with every colour); legibility unproven | Plausible, to confirm at TRL 3 | Fix F6 (rule C1); T5 with colour-deficient observers |
| P29 | Panels, folds and clips keep their function at 40 to 50 C inside a tent | Hot: flat P12 margin 0.87 (rule S1 covers it), leaf margin 1.6, U bay tip unchanged (weight, not stiffness); fold set angles may relax; PETG clips stay below their HDT but near it in sun | Plausible, to confirm at TRL 3 | T1, T2, T7 at 50 C |
| P30 | Folds and clips do not crack in cold use (5 C and below) | Toughness halves by -20 C; no data at 5 C for scored skins or printed tongues: to assess; platform use below 5 C is not claimed | Plausible, to confirm at TRL 3 | T2 and T3 at 5 C |
| P31 | Thermal expansion of a 2.4 m wall is taken up without bowing off its feet | 7.9 mm over a 30 C swing on 2.4 m; the zigzag takes it with a fold angle change of about 0.7 deg; slot clearance 0.15 to 0.35 mm per side does not need to | Within known science | Rule S1 (zigzag walls) |
| P32 | Panels keep their properties over a stated service life | Indoor use only (L2); no service life is claimed; sunlit tent walls and the effect of brominated FR on UV stabilisers: to assess | Plausible, to confirm at TRL 3 | D6; supplier data for the FR plus UV grade |
| P33 | Static charge on PP panels is acceptable near medical electronics and oxygen use | Standard PP is highly insulating; dust pick-up and discharge near oxygen-enriched areas: to assess with the site; anti-static FR availability to assess | Plausible, to confirm at TRL 3 | Site review; supplier data |
| P34 | Edges, grooves and folds do not cut or pinch fingers | Sealed edges are rounded; routed shoulders are sealed by rule E1; pinch at a closing fold only during packing (hands on the leaf faces). Sharp-edge test (UL 1439 type) planned | Plausible, to confirm at TRL 3 | T5 sharp-edge and pinch check |
| P35 | Sheet of 3.8 to 4.2 mm (+-5 %) fits the 4.5 mm clip slot and the through-peg engages at both extremes | 4.2 mm sheet vs slot <= 4.5 mm sheet vs slot | Within known science | Fix F8 (CLEAR 0.5 mm) |
| P36 | Zone colours and safety signs do not conflict | Triage red and green collide with fire-equipment red and safe-condition green in one bay. Fixed by rule C6 (triage colours only as zone bands carrying the category word, never as sign backgrounds; safety signs keep ISO shapes and borders). ISO 3864-4 colour values and the sign-size distance factor are not yet read from the standards (the reviewer's z = 60 is unverified): to assess | Plausible, to confirm at TRL 3 | Fix F10 (rule C6); D16 Proposed, awaiting Amish: buy ISO 3864-1 and -4 |
| P37 | Smoke from FR panels is no worse than the platform accepts for patient spaces | Corrosive and toxic smoke products are certain; their size relative to plain PP smoke is not quantified: to assess | Plausible, to confirm at TRL 3 | D11 Proposed, awaiting Amish: halogen-free FR search |
| P38 | The FR grade does not shed burning drips | Supplier pass reports cover the NFPA criterion only; d-class and drip in a room-corner test (NFPA 286): to assess | Plausible, to confirm at TRL 3 | T8; D18 |
| P39 | Ballast bags do not create a slip or lifting hazard | Fixed by rule B1: sand or gravel in a sealed bag inside the foot tray; water only double-bagged in a lipped tray | Within known science | Fix F11 (rule B1) |
| P40 | Mixed P12 and P18 panels share joints | v0.1 heights (150, H/2, H - 150) gave no common middle clip; v0.2 grid 150 and 1050 for P12, plus 1650 for P18, shares two of three | Within known science | Fix F12 (clip_heights v0.2) |

## 16. Independent review

Method: on 2026-11-12 a separate Claude process, which did not see this document's reasoning, was given `platform_results.csv`, `platform_check.py` and the cited sources and asked to refute every "Within known science" and "Plausible" verdict. It fetched most sources, re-ran the key numbers and reported in `/tmp/claude-0/review-platform.md` (not kept in the repo). Of 20 verdicts tested it found 6 holding, 11 weak and 3 refuted (P9 clip holding, P12 one-hand clipping, P17 12 kg pack); it confirmed the self-declared fails P4 and P8 and listed 14 missed claims. Every finding was checked against this document's own numbers before acting on it.

What changed:

- **Refuted, confirmed and fixed or sent to Amish.** P9: the 3.7 mm peg in a 4.2 mm slot never reached the far skin (44 N per peg, not 100 N); fixed by the through-peg (F8, 88 N per peg, 176 N per clip), but demand is not bounded on paper, so the holding principle goes to Amish (D14). P12: a 1.2 mm lead-in on a 3.7 mm peg cannot cam the tongue; fixed by a 45 deg ramp over the whole peg height (F9) and a stated two-handed method. P17: the mass budget counted 6 feet where the U uses 7; corrected to 14.3 kg, 19 % over 12 kg, "Fails, fix proposed" (D15).
- **Weak, confirmed and reworked.** P1 ("lower bound" wording dropped; grammage band added; CD span dependence stated). P3 (orthotropic formula with zero twisting stiffness: margin 3.1, not 6.3; edge restraint stated). P5 (top height 1,810.5 mm including the foot; "not evidence of strength"). P7 (rigid-U assumption stated; sliding P27 and impact P28 added; full BIFMA criteria quoted). P10 (print derate 0.3). P11 (tapered tongue, root factor 2, slot 4.5 mm for the sheet tolerance, PETG HDT). P13 (the v0.1 groove was too narrow to fold flat: 12.2 mm of free skin needed, 13.6 mm flat-bottomed groove adopted, F3). P14 (hole wear and a retention target). P15 (true inch sizes: 9.6 mm trim, 8.0 mm after tolerance). P16 (NIOSH is two-handed; carry posture stated). P18 (isopropyl "A2" means satisfactory to 48 C, not 22 C; Akyplac's oxidiser caveat; downgraded to plausible). P20 (Curbell's bleach strength is about 0.10 to 0.16 % NaOCl, so 0.5 % on PETG is to assess). P21 (to assess). P22 (groove, half-flute troughs and slots added; rules E1 to E3). P23 (FR does not reduce fire load). P24 (lot maximum, not nominal). P25 (the FR film report is no longer cited as support).
- **Missed claims added as rows:** heat and creep at 40 to 50 C (P29), cold (P30), thermal expansion (P31), UV ageing and service life (P32), static (P33), sharp edges and pinch (P34), sheet thickness tolerance in the slot (P35), colour and sign conflicts (P36), smoke products (P37), flaming drips (P38), ballast bag hazards (P39), plus sliding (P27) and BIFMA impact (P28). Connector fatigue and disinfectant strength were folded into P14 and P18 and tests T3 and T4.
- **Not adopted as stated.** The reviewer reported that the next NFPA 701 edition limits Test Method 1 for wall, ceiling and floor coverings and interior finish, and that ASTM E84 warns about materials that drip; both source pages could not be opened from this session (permission not granted), so they are recorded as unverified and handled by decision D18 instead of a rule. The reviewer's 34 J for the BIFMA impact bag and z = 60 for ISO 3864 sign size are uncited and are not used. The reviewer could not open the Justia and Interprofile pages; both were read on 2026-11-12 for v0.1. IARC places antimony trioxide in Group 2B (1989), not a newer group; trivalent antimony is Group 2A (volume 131).

Rows the reviewer upheld (P2, P6, P10, P19, P23, P26) are unchanged in substance.

## 17. Platform requests from products

FlexTriage built a full bay on v0.1 and raised seven requests (`docs/REVIEW.md`, "Platform requests"). Resolution in v0.2:

| # | Request | Resolution |
| --- | --- | --- |
| 1 | S1 and S4 contradict the platform's own U bay (2.4 m straight runs); a flat P12 strip has a margin of about 0.86 hot | Resolved. S1 now covers P12, straight walls are zigzags with 30 deg folds and the new angle clip, S4 limits inline joints to panels up to 600 mm or joints with a tee return, P7 is recomputed for a zigzag U; hot stiffness is in P2, P3 and P29 (the platform finds 0.87, matching FlexTriage) |
| 2 | The back-face groove is an open crevice | Resolved by rules E1 (groove shoulders and ends sealed) and E2 (groove face away from care zones, or a flexible PP strip); strip lift is in T6 |
| 3 | `foot()` built the +y outrigger apex-down below the floor | Fixed in `flex_parts.py`: every outrigger stands on the floor, apex up; the self-test asserts z min = 0 for every foot. FlexTriage's `_upright_foot()` work-around becomes a no-op and can be removed |
| 4 | Cross-foot outriggers collide with the panel at corners and tees | Fixed: foot kinds inline, corner, junction and cross, with outriggers only in free directions (section 5.4); the bay self-test finds no interference |
| 5 | Mixed P12 and P18 joints impossible with the v0.1 hole pattern | Fixed: shared clip grid 150 and 1,050 mm, plus 1,650 mm on P18 (F12, P40). Holes in panels cut to the v0.1 pattern (900 mm) do not match |
| 6 | P9 refuted; FlexTriage's anchor uplift margin (103 N against 201 N) depends on it | Partly resolved. The through-peg gives 88 N per peg and 176 N per clip on paper (both skins), below the 201 N FlexTriage used; FlexTriage must recheck its anchor margin with 176 N per clip and T3 settles it (D14) |
| 7 | The fold works one way only | Resolved: the 13.6 mm flat-bottomed groove folds 180 deg back for packing and 90 deg either way in use (F3, P13) |

### 17.1 Open requests after v0.2 (raised by all three products, 2026-11-12)

FlexClean, FlexSleep and FlexTriage were each built on v0.2 and each worked around the same gaps with product-local parts. These are open for v0.3 of `flex_parts.py`; until then each product keeps its own part, recorded in its REVIEW.

| # | Request | Raised by | Product workaround now | Proposed platform change |
| --- | --- | --- | --- | --- |
| R8 | The angle clip's square core meets the panel about 0.9 mm before the stop, so holes miss the pegs at 150 deg | FlexClean, FlexSleep, FlexTriage | Angle clip drawn on a round core in each product | Adopt the round core in `clip(kind="angle")` |
| R9 | No foot for an angled joint, an angled junction or an angled tee, and none for a folded corner | FlexClean, FlexSleep, FlexTriage | Product feet built from the platform block and slot arm | Add `foot(kind="angle", angle=...)` and an angled junction |
| R10 | Rule S1 has no numbered rule for free edges (doorway jambs, tails, open wall ends); flat-panel figures carry no safety factor (1.73 cold, 0.87 hot) | FlexClean, FlexSleep, FlexTriage | FlexSleep stiffens free ends with aluminium channels; FlexTriage estimates 4.7 cold and 2.3 hot with an assumed coefficient | A free-edge rule with a stated safety factor, checked at T7 |
| R11 | The outrigger has no modelled connection to its foot block | FlexSleep | Pinned outriggers | Model the pin or a moulded hinge |
| R12 | Corner, junction and cross feet weigh about 0.71 kg, not the 0.46 kg the pack masses assume | FlexClean | Product masses use 0.71 kg | Correct the pack-mass table (P17) |
| R13 | Joints leave an 11.6 mm full-height gap between and beyond the clips | FlexSleep | Clear PP strips over the gaps | A joint cover strip as a platform part |
| R14 | The fire section should carry the hand-rub dispenser rules (at most 102 mm projection, 1,067 to 1,219 mm operating height, corridor width where dispensers are in a corridor) | FlexClean | Applied in FlexClean | Add to section 9 |

## 18. Decisions

Decided by Amish: the shared Flex platform for FlexClean, FlexSleep and FlexTriage (2026-11-12); the standing fix rule (2026-10-23).

Table 7. Platform decisions (v0.2).

| ID | Decision | Status | Options and reasons |
| --- | --- | --- | --- |
| F1 | Rule S1: every vertical edge of a panel above 600 mm (P12 included, v0.2) supported by a fold or angle joint turning 30 deg or more, a corner or a tee; straight walls as zigzags | Decided under Amish's standing instruction of 2026-10-23 (fix rule) | Flat panels buckle under their own weight (P2); a flat P12 fails hot (0.87) |
| F2 | Rule S3: no single freestanding panel; L, U or closed plans; 5 kg ballast at far return feet | Decided under the standing instruction (fix rule) | A single duo tips at 6 N (P6); the ballasted zigzag U holds about 242 N if rigid (P7) |
| F3 | Fold groove 4 pitches (13.6 mm), flat-bottomed, two-way | Decided under the standing instruction (fix rule) | The v0.1 groove could not fold flat (P13); request 7 |
| F4 | Rules E1 to E3: sealed edges, groove shoulders, groove ends and holes; groove face away from care zones or stripped; clips off for cleaning | Decided under the standing instruction (fix rule) | Open flutes and crevices cannot be wiped (P22); request 2 |
| F5 | FR grade bought at a measured lot maximum of 700 g/m2 with an NFPA 701 TM1 report | Decided under the standing instruction (fix rule) | 750 g/m2, or 700 nominal plus tolerance, lies outside TM1 scope (P24) |
| F6 | Rule C1: colour never the only code | Decided under the standing instruction (fix rule) | Red-green deficiency about 1 in 12 men (P26) |
| F7 | Two pegs per clip slot | Decided under the standing instruction (fix rule) | One peg could not carry the v0.1 demand (P9) |
| F8 | Through-peg into a back-wall socket; slot gap 4.5 mm | Decided under the standing instruction (fix rule) | The v0.1 peg reached only the near skin (P9, review); sheet tolerance (P35) |
| F9 | 45 deg ramp over the whole peg height; tapered tongue | Decided under the standing instruction (fix rule) | The v0.1 lead-in could not cam (P12, review); root strain (P11) |
| F10 | Rule C6: triage and zone colours never take a safety-sign form | Decided under the standing instruction (fix rule) | Triage red and green clash with ISO 3864 meanings (P36) |
| F11 | Rule B1: sand or gravel ballast in sealed bags; water only double-bagged in a lipped tray | Decided under the standing instruction (fix rule) | Leaking water is a slip hazard (P39) |
| F12 | Shared clip grid: 150 and 1,050 mm, plus 1,650 mm above 1,200 mm | Decided under the standing instruction (fix rule) | Mixed P12 and P18 joints (P40, request 5) |
| D1 | Platform sheet FXP-S4FR: 4 mm FR twinwall, lot maximum 700 g/m2, 48 x 96 in or 1.22 x 2.44 m, flutes along the length | Proposed, awaiting Amish | Alternatives 5 mm (1.4 x mass) or 10 mm (2.9 x mass); stiffness gain does not change the rules (P4) |
| D2 | EN 13501-1 target class | Proposed, awaiting Amish | No twinwall classification found (P25); set after supplier quotes |
| D3 | Print under a clear PP overlaminate, direct UV print as the comparison | Proposed, awaiting Amish | No wipe data for UV inks on twinwall (P21) |
| D4 | Clips and feet moulded in PP copolymer at scale, cored; PETG for prototypes | Proposed, awaiting Amish | One polymer family; mass (P17); moulding grade strain limit to assess (P11) |
| D5 | Stated limit L1: panels are boundaries, not barriers; "do not lean" on every product | Proposed, awaiting Amish | No grade resists a hand push in bending (P4); changes what products may promise |
| D6 | Stated limit L2: indoor or in-tent use only | Proposed, awaiting Amish | Wind at 10 m/s exceeds the ballasted restoring moment with margin (P8) |
| D7 | Modules: 600 mm leaf, P12 and P18 duos, H06 strip | Proposed, awaiting Amish | 96.9 % sheet yield (P15) |
| D8 | Edge seal method: heat seal (recommended) or U-profile trim (PP, or PVC as the decks hint) | Proposed, awaiting Amish | Heat seal adds no mass or crevice; trim protects print edges; PVC adds chlorine to the fire products |
| D9 | CAD helpers in build123d (the kit library) with an optional CadQuery wrapper | Proposed, awaiting Amish | CadQuery is not installed in the kit environment; `.kit/cad_parts.py` and `cad_check.py` read build123d shapes |
| D10 | Base sheet 48 x 96 in (or 1.22 x 2.44 m); 2,000 x 3,000 mm allowed at 89 % yield | Proposed, awaiting Amish | Stock size in North America and the UK |
| D11 | FR chemistry: accept brominated FR with antimony trioxide now, look for a halogen-free FR twinwall | Proposed, awaiting Amish | Smoke products include hydrogen bromide and antimony oxides (P37) |
| D12 | 5 kg site-filled ballast bag on far return feet as the standard | Proposed, awaiting Amish | 3.1 kg needed for the zigzag U (P7); 5 kg gives margin |
| D13 | "PVC-lock joints" read as the clip-lock family; no PVC tube frame | Proposed, awaiting Amish | The decks name the feature without describing it |
| D14 | Clip holding principle: keep the through-peg clip and let T3 and T7 decide; options if it falls short: (a) clips at a 300 mm pitch on every joint, (b) a moulded collar at each hole, (c) state "joints may release before the bay tips" as a limit | Proposed, awaiting Amish | Capacity 176 N per clip against a demand of 162 to about 1,160 N per edge on paper (P9); recommendation: (a) for FlexTriage anchor joints if T3 confirms under 200 N per clip |
| D15 | Pack target: (a) raise the FlexTriage target to about 15 kg in three bags, (b) keep 12 kg and require moulded cored feet (0.15 kg) and clips (0.04 kg), or (c) fewer duos per bag set | Proposed, awaiting Amish | 14.3 kg now, about 11.7 kg with (b) (P17); recommendation: (a) for prototypes, (b) as the volume target |
| D16 | Buy ISO 3864-1 and ISO 3864-4 (and ISO 7010) to set colour values and sign sizes | Proposed, awaiting Amish | Values now rest on a Wikipedia summary (C2, P36) |
| D17 | Sliding: accept that a bay slides before it tips, or add non-slip pads to every foot | Proposed, awaiting Amish | Slides at about 57 N at an assumed friction of 0.25; tips only above about 1.06 (P27); pads raise the tipping risk while keeping zone lines |
| D18 | Fire benchmark order: NFPA 286 room-corner or ASTM E84 Class A first for a 1.8 m partition, NFPA 701 TM1 second, confirmed with the authority having jurisdiction | Proposed, awaiting Amish | Reviewer reports a TM1 scope change and an E84 drip caveat (unverified, section 16); P38 |

## 19. Sources (all checked 2026-11-12)

1. Coroplast/Interprofile product data, 11/18/08. https://www.acplasticsinc.com/media/documents/PD_CoroPlast_InterProfile.pdf
2. Coroplast graphic stock sheet sizes. https://www.coroplast.com/?p=534
3. Coroplast Print tolerances, May 2021. https://www.coroplast.com/wp-content/uploads/Coroplast-Print-05252021.pdf
4. Coroplast Firewall FRB SDS, rev. 5 May 2014 (Polymershapes). https://www.polymershapes.com/wp-content/uploads/2020/04/Polymershapes_Coroplast_SafetyDataSheet-Fluted-SDS-FR-20140505.pdf
5. IntePro FR line card, Sept 2020. https://polymershapes.com/wp-content/uploads/2025/08/intepro-fr-092920.pdf
6. LaminaCorr Ultra FR (Global Plastic Sheeting). https://www.globalplasticsheeting.com/laminacorr-ultra-fire-retardant-corrugated-plastic-sheets
7. DS Smith Akyplac 3.5 mm 600 g/m2, 06/2020. https://pim.igepa.nl/Plaatmateriaal/Polypropyleen/Akyplac%C2%AE/FT%20Akyplac%20600%20GB%20-%2006.2020.pdf
8. Akyplac 8 mm 1500 g/m2. https://pim.igepa.nl/Plaatmateriaal/Polypropyleen/Akyplac%C2%AE/Technische%20datasheet%20Akyplac%208%20mm.pdf
9. Akyprint UV 5 mm, 06/2020. https://sunclear.fr/img/medias/bt/POLYPROPYLENE_ALVEOLAIRE__AKYPRINT_5MM_fiche_technique_130422.pdf
10. Sitebox flame retardant protection board. https://www.sitebox.ltd.uk/docs/PBTFD12/FLAME_RETARDANT_PROTECTION_BOARD_SPEC_SHEET.pdf
11. Safety Signs UK FR product data. https://www.safetysigns.uk.com/files/dbd709a2-bfdf-4d42-89de-ad98010a1e9d/FR%20Product%20Data%20Sheet.pdf
12. Correx data sheet (Temprotech). https://temprotech.com/userfiles/file/Data%20Sheets/TPTData-Correx.pdf
13. Curbell Plastics, fluted boards conversion guide. https://www.curbellplastics.com/wp-content/uploads/2022/11/Fluted-Boards-Conversion-Guide.pdf
14. PlasticsToday, Polypropylene part design part 2: living hinges. https://www.plasticstoday.com/materials/design-polypropylene-part-design-part-2-living-hinges
15. Bayer MaterialScience, Snap-fit joints for plastics. https://cdn.sparkfun.com/assets/home_page_posts/1/4/1/0/Plastic_Snap_fit_design.pdf
16. BCN3D PETG technical data sheet. https://www.bcn3d.com/wp-content/uploads/2019/09/TDS_BCN3D_Filaments_PETG.pdf
17. CP Lab Safety polypropylene chemical compatibility chart. https://www.cplabsafety.com/content/chemical-charts/Polypropylene.pdf
18. INEOS polypropylene chemical resistance guide. https://www.ineos.com/globalassets/ineos-group/businesses/ineos-olefins-and-polymers-usa/products/technical-information--patents/ineos-pp-chemical-resistance-guide.pdf
19. Curbell Plastics, Disinfecting acrylic, polycarbonate and PETG sheet. https://www.curbellplastics.com/wp-content/uploads/2022/11/Disinfecting-Acrylic-Polycarbonate-and-PETG-Sheet.pdf
20. Virox, AHP general materials compatibility. https://virox.com/resource/ahp-general-materials-compatibility/
21. PDI material compatibility brochure. https://pdihc.com/wp-content/uploads/2024/03/PDI-Compatibility-Brochure_UPDATE-0126_09238824_web.pdf
22. Fujifilm Uvijet KX ink data sheet. https://asset.fujifilm.com/www/ca/files/2020-02/68c6f4205153ee95cc42516d8947a074/Uvijet-KX-Ink-data-sheet.pdf
23. UL FSRI Materials and Products Database, polypropylene. https://materials.fsri.org/materialdetail/polypropylene-pp
24. Minnesota Department of Health, furnishings, mattresses and decorations in health care (rev. June 2024). https://www.health.mn.gov/facilities/regulation/engineering/lsciffurnishings24.pdf
25. Scottish Government, Building standards technical handbook 2022, annex 2.B reaction to fire (EN 13501-1). https://gov.scot/publications/building-standards-technical-handbook-2022-domestic/2-fire/annex-2-b-reaction-fire
26. Efectis classification report EFR-25-000397, Akyplen FR PP film B-s2,d0 (Sunclear). https://www.sunclear.fr/img/medias/bt/POLYPROPYLENES_FILM_PRYPLON_PV%20B-s2%2Cd0%20Akyplen%200.35-0.70%20mm%20Efectis%20-%20Au%2010-02-2025.pdf
27. SGS test report SDHL2201000875FT quoting ANSI/BIFMA X5.6 and X5.5. https://www.mwworkstation.com/Uploads/202303/t8_cubicle_workstation--bifma-sgs.pdf
28. 780 CMR 1607.13 interior walls and partitions (Justia). https://regulations.justia.com/states/massachusetts/780-cmr/chapter-16/section-1607/subsection-1607-13
29. CCOHS, NIOSH lifting equation. https://www.ccohs.ca/oshanswers/ergonomics/niosh/assessing.html
30. MedlinePlus Genetics, colour vision deficiency. https://medlineplus.gov/genetics/condition/color-vision-deficiency/
31. Wikipedia, ISO 3864 (summary of parts 1 to 4 and safety colours). https://en.wikipedia.org/wiki/ISO_3864
32. CHEMM (US HHS), START adult triage algorithm. https://chemm.hhs.gov/startalgotext.htm
33. IARC, Monographs volume 131 questions and answers (antimony compounds). https://www.iarc.who.int/wp-content/uploads/2022/04/Mono-131-QA.pdf
34. S. Timoshenko and S. Woinowsky-Krieger, Theory of Plates and Shells, 2nd ed. (New York: McGraw-Hill, 1959), coefficients for a simply supported rectangular plate under a central load.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
