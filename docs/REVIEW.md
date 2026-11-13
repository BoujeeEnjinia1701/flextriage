# FlexTriage Origami Bay review note

**Media completed, 2026-11-12.** The Blender Cycles renders queued by this session were rendered on Amish's Mac: `media/options.png`, `media/render-hero.png`, `render-studio.png`, `render-cutaway.png` and `render-exploded.png` were composed and captioned, `media/card.png` and `media/social-preview.png` were made with `cards.py`, and `image_qc.py` passes. `render.py --check` passes. `release_gate.py` fails only on `stem_check: open` (Plausible rows wait on TRL 4 evidence; design decisions await Amish). Amish approved the repo as public on 2026-11-12.

## Session 2026-11-12, second pass: brought up to FXP-PLT-001 v0.2

The shared Flex platform was revised to v0.2 by the platform engineer after its own independent review and the seven FlexTriage platform requests. `docs/platform/` and `cad/src/flex_parts.py` were read, not edited. This pass brings FlexTriage onto v0.2 under the same rules as the first pass (TRL 3 cap, no git writes).

### What changed

- **Zigzag walls and stubs (fix F10, platform rule S1).** Every duo now stands folded 30 deg at its 13.6 mm two-way groove; every plain wall joint is an angle clip turning 30 deg the other way; stubs and corner tails join the walls at angle tees; the fold vertices point out of the bay. No inline joint remains (rule S4). Joint pitch 1,212 to 1,170.7 mm; plan 8.19 x 2.34 m on joint lines. `cad/src/model.py` rewritten for this.
- **Clips and feet.** Platform clip API v0.2 (4.5 mm slot, through-pegs, `detail="light"` in the assembly). Angle clips and angle tees are drawn on a round 12 mm core with the platform's slot arms (platform request 8). Feet are the platform foot block with slots cut on the zigzag angles: angle feet (two outriggers) at plain joints, angle junction feet (120 x 120 mm, one outside outrigger) at stub and tail joints, angle jamb feet (one outside outrigger) at doorway wall jambs, platform inline feet at the tail ends and free wall ends. Shoes are gone. `_upright_foot()` is now a no-op, as the platform says. Anchor feet keep the platform block but turn their outriggers square to the doorway, since a zigzag stub ends 15 deg off the doorway line.
- **Groove.** The stubs' back-face groove is covered by a clear PP strip (platform rule E2); the long walls' grooves face out of the bay.
- **Model and media.** `python .kit/cad_check.py --export` passes D3 (FT1 181 parts, FT2 184, FT3 124; no interference; 41 MB of STEP). Drawings FXT-DWG-001, 002 and 101 to 106, 16 STL files, build plan pictures, concept media and `product_model.py` views are regenerated. The option and view scenes in `/home/claude/he5/renderq/flextriage` and its `views` folder were replaced (`flextriage__options_jobs.json`, `flextriage__jobs.json`).
- **Numbers and documents.** `sizing.py` and `stem_check.py` were rerun and the BOM was updated. These documents were updated: STM v0.3, CAL v0.2, PRC, OPT, PRS (PR-028 added), BLD, DEC, DDR 0001 to 0003, REG, FEA, RSK, MKT, PLN, VER and README. `python .kit/trace.py` reports 0 gaps.

### Key results now (FXT-CAL-001 v0.2)

- Plan: zones 5.48, 5.48 and 8.22 m2, interior **19.19 m2** (under the deck's 20 m2; it was 20.57 with flat walls). Needs 8.8 x 2.9 m of floor plus 1.5 m of approach at each end.
- Self-weight: the v0.1 flat walls stood at 1.73 cold and **0.87 hot**, which fails. Held zigzag leaves stand at **9.43 cold and 4.72 hot**. A leaf with one free edge (wall ends, tails) is about 4.68 and 2.34 (assumed plate coefficient, A16). A hung flap is 5.05 and 2.52.
- Stability at a stub joint (178 N at 1,110.5 mm): **312 N** with two bags per anchor foot (325 N before; the zigzag puts the wall's weight 78 mm outside the joint line); 52.1 N unballasted. Between stubs the walls still tip at about **5 to 15 N**: a zigzag stiffens a wall up its height, not along it. A lone duo tips at 4.5 N outward and 5.9 N inward.
- Anchor margin: uplift 103 N against **176 N** for two through-pegs. That is a factor of **1.71**, down from 1.95 with the v0.1 figure of 201 N. The stub's lift into the wall goes through the two angle-tee clips: 113 N against 351 N (factor 3.12). Platform P9 is now "Fails, fix proposed" (demand on a clip in a bowing leaf is not bounded on paper), so the margin waits for pull-out test T3 (platform D14, FlexTriage D10).
- Sliding: 177 to 236 N on EPDM pads (unchanged).
- Pack: **43.1 kg** (41.6 before; the junction feet are larger blocks), 3.6 times the deck's 12 kg. The platform's own zigzag U bay is 14.3 kg (P17). With moulded, cored feet and clips (platform D15 option b) this bay would still be about 35.0 kg. Three bags of about 14.4 kg (platform D15 option a) or four of about 10.8 kg.
- Doorways: **1,069 mm** clear at the inner doorways and **1,054 mm** at the entry and exit (1,115 before); 971 mm beside the bags; 1,149 mm past the open leaf. The leaf is now 1,149 x 990 mm. Catch 12.9 N, push **15.3 N** against 22.2 N.
- Deployment 12.0 to 34.9 min with the deployment kit (unchanged count; fold setting not timed separately). Fire load **1,279 MJ**. PETG 13.4 kg, about 672 printer-hours.
- BOM: **USD 1,174.23** against the USD 800 target, USD 374.23 over (USD 1,143.13 before). USD 23.48 per deployment over 50 uses.

### STEM check (FXT-STM-001 v0.3)

- FT1: 18 within, 23 plausible, **3 fail with a fix that goes to Amish**: S1 pack, S6 between stubs, S22 floor.
- S4 (straight runs) is closed by F10 and now reads plausible pending the hot soak.
- Options and variants: 5 within, 3 plausible, 6 fail. X14 (P18) now stands structurally as a zigzag and fails only on the pack.
- The first-pass independent review (17 held, 17 weak, 10 refuted of 44; 24 missed claims) stays recorded. No new independent review was run for this pass. The changed rows are S1, S4, S5, S6, S7, S12, S17, S18, S22, S27, S42, S43 and X14.

### Requirements not met or at risk

- Not met: PR-007 stability between stubs (5 to 15 N; D7), PR-015 pack mass (43.1 kg; D2), PR-022 privacy at P12 (D3).
- Over target: PR-018 cost (USD 1,174.23).
- At risk: PR-001 deployment (12 to 35 min), PR-008 sliding (wet low end 177 N), PR-012 floor (19.2 m2 inside; D4), PR-014 leaf force (estimate 15 N).
- To verify at TRL 4: PR-009, PR-010, PR-017, PR-021, PR-025.
- New PR-028 (self-weight) is met on paper.

### Decisions proposed and awaiting Amish (FXT-DEC-001 v0.2)

- **D1 concept:** FT1 176, FT3 169, FT2 159 of 260; all within 10 %, all to Amish. FT1 is carried only so a constructable design exists.
- **D2 pack**, now aligned with platform D15: recommend three bags of about 15 kg for the prototype.
- **D3 wall height:** a P18 zigzag now stands, so this is a weight and cost choice. Recommend P12 walls with P18 screens at the beds, now possible on the shared clip grid.
- **D4 floor statement.**
- **D6 prints or moulding.**
- **D7 lateral criterion between stubs.**
- **D8 three bags in a two-zone bay.**
- **D9 ballast on clinical floors** (platform rule B1).
- **D10 (new) clip holding at the anchor feet** (platform D14): keep the through-peg clip and let T3 decide, with clips at a 300 mm pitch ready.
- **Closed:** D5 (platform rules S1 and S4), resolved by the platform and adopted here as F10.
- **To confirm when parts are bought:** C1 to C10 as before.

### Platform requests (FXP-PLT-001; not edited here)

| # | Request | Status after v0.2 |
| --- | --- | --- |
| 1 | S1 and S4 forbade straight P12 runs; a flat P12 strip is about 0.86 hot | **Resolved.** Zigzag walls and angle clips adopted (F10); FlexTriage finds 0.87 hot for the flat strip, as the platform does |
| 2 | Back-face groove is an open crevice | **Resolved** by rules E1 and E2; the stubs' grooves carry a clear PP cover strip, the walls' grooves face outside |
| 3 | `foot()` built the +y outrigger below the floor | **Resolved**; `_upright_foot()` is a no-op |
| 4 | Cross-foot outriggers collided with panels at corners and tees | **Resolved** for the platform's own kinds; FlexTriage's angle joints need feet the family does not have (request 9) |
| 5 | Mixed P12 and P18 joints impossible | **Resolved** by the shared clip grid; used in D3 option (c) |
| 6 | P9 refuted; anchor uplift margin depends on it | **Partly resolved, still open.** 176 N per clip on paper gives a factor of 1.71; P9 now fails with a fix proposed; T3 and platform D14 decide (FlexTriage D10) |
| 7 | The fold worked one way only | **Resolved** by the two-way 13.6 mm groove; the walls fold towards the print face and the stubs towards the back face |
| 8 (new) | The angle clip's 150 deg arm sits on a square core, so a panel edge seated at the core face overlaps the core corner by about 0.9 mm (147 mm3 per clip in the D3 interference check) | **Open.** Ask: a round (or chamfered) core for the angle clip. FlexTriage draws its angle clips and angle tees on a round 12 mm core with the platform's arms unchanged |
| 9 (new) | The foot and clip family has no part for a zigzag joint: no foot with slots 150 deg apart and no tee whose wall slots are 150 deg apart | **Open.** Ask: an angle foot (inline block with 150 deg slots), an angle junction foot and an angle tee clip in the family. FlexTriage builds them from the platform block and arm as product accessories |
| 10 (new) | Rule S1 says every vertical edge of a panel over 600 mm is supported, but layouts need free edges: doorway jambs, corner tails and the platform's own U returns | **Open.** Ask: a free-edge rule with a number. FlexTriage estimates about 4.7 cold and 2.3 hot for a 600 mm leaf with one free edge (assumed coefficient, A16) |

### Build plan findings (design for construction, FXT-DDR-002 v0.2)

- The feet's angled slots set each duo's 30 deg fold, so no fold has to be measured on site.
- Anchor outriggers are turned square to the doorway.
- Divider 2 now folds the other way, so its bags lie upstream and clear of its leaf.
- Each duo carries a printed fold direction.

### Safety concerns

- **Walls tip when leant on between stubs** (H1, FMEA RPN 126).
- **Anchor peg pull-out** (RPN 140, the top item; margin now 1.71 on a capacity the platform no longer bounds).
- **Clip tongue fatigue and groove strip lift** (RPN 120 each).
- **Fire load** of about 1,279 MJ in a tent, with non-FR prints.
- **Trip edges** from the outriggers.
- **Pacemaker label** needed at each catch.
- **False sense of protection**, handled through the claims register.
- The release limitation is in every document.

### Checks and kit notes

- `python .kit/cad_check.py --export`: PASS (D3).
- `python .kit/trace.py`: 0 gaps.
- `python .kit/render.py --check`: fails only on `media/options.png`, which needs the Blender renders of the exported option scenes. The storefront warning lists `media/render-hero.png`, `media/card.png` and `media/social-preview.png`, also Blender-dependent.
- After the Mac renders: run `python .kit/options.py --compose=<dir>`, caption the views with `.kit/photo_caption.py`, then run `python .kit/cards.py .` and `python .kit/image_qc.py`.
- Twinwall is modelled as solid 4 mm sheet; masses use the platform's 0.70 kg/m2 (`cad/fidelity.json` shows 158.5 kg for FT1 at solid density; FXT-CAL-001 gives 43.1 kg).
- No git command that writes was run; committing and pushing are left to Amish.

### Appearance model

`product_model.py` uses the FT1 parts as modelled, with two mannequins. There are no appearance deviations from `model.py`. Proposed, awaiting Amish: none.

### Recommended next step

1. Amish decides D1, D2, D7 and D10.
2. The platform owner answers requests 8 to 10.
3. On paper the design is then ready for TRL 4, once the portfolio cap allows: one bay built to FXT-BLD-001, clip pull-out (T3) at the anchor joints, timed deployments with untrained pairs (the team's decision gate), push tests at and between stubs, a hot soak of the zigzag walls, and the sheet's fire report (FXT-VER-001).

## Session 2026-11-12, first pass: P0 to P3 (TRL 3) under kit 1.9.1-he

- STEM check first, then an independent review by a separate process (17 held, 17 weak, 10 refuted of 44 rows; 24 missed claims added as S31 to S44).
- Three options modelled at D3, scored and sent to Amish (all within 10 %).
- All pipeline documents written, drawings and pictures made, and nine fixes F1 to F9 made under the standing instruction.
- Platform requests 1 to 7 raised; the platform answered them in v0.2 (table above).
- First-pass figures, all superseded by this pass: 41.6 kg, 325 N at a stub joint, anchor factor 1.95, USD 1,143.13, doorways 1,115 mm, interior 20.57 m2.
