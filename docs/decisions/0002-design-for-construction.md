---
doc_id: FXT-DDR-002
title: "0002: Design for construction of FT1"
project: FlexTriage Origami Bay
doc_type: Decision record
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First record of the changes that made FT1 constructable (STANDARDS section 18)
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Redrawn on FXP-PLT-001 v0.2, zigzag walls and stubs, angle clips and angle tees on round cores, angle feet, groove cover strip
---

# 0002: Design for construction of FT1

Status: made under STANDARDS section 18; reversible by Amish.

## Context

The deck shows panels, clips and flaps but not how a flap hangs, how a short panel joins a wall, what a corner stands on or how anything is made. A plan someone can build needs every part, joint and step defined from the platform's parts (FXP-PLT-001, `cad/src/flex_parts.py`).

## What was decided

- Plan: two long walls of seven P12 duos at a 1,170.7 mm pitch, four zigzag stubs at alternate sides leaving 1,054 to 1,069 mm clear doorways, three zones (5.48, 5.48 and 8.22 m2).
- Zigzag (FXP-PLT-001 v0.2 rule S1, adopted as F10): every duo stands folded 30 deg at its 13.6 mm groove and every wall joint turns 30 deg the other way, so each leaf stands 15 deg off its wall line with the fold vertices outside the bay; stubs zigzag the same way.
- Joints: angle clips at 150 and 1,050 mm above the panel's bottom edge on every plain wall joint; angle tees (the two wall slots 150 deg apart and a third slot for the stub or tail) where a stub meets a wall; a corner tail at each end-stub corner (F7). No inline joint remains (rule S4).
- Clip cores: the platform's angle clip carries its 150 deg arm on a square 12 mm core, so a panel edge seated at the core face overlaps the core corner by about 0.9 mm (found by the D3 interference check). FlexTriage draws its angle clips and angle tees on a round 12 mm core with the platform's slot arms unchanged, and asks the platform to do the same (platform request 8).
- Feet: angle feet (the platform foot block with its slots on the leaf directions) and two outriggers at plain wall joints; angle junction feet (120 x 120 mm block, one outside outrigger) at the stub and tail joints, and angle jamb feet (one outside outrigger) at doorway wall jambs, so no outrigger crosses a panel or a doorway; jamb feet at the free wall ends (F8); anchor feet at stub ends (F4), with their outriggers turned square to the doorway because the stub ends 15 deg off it.
- Flaps: one 1,149 x 990 mm leaf per doorway on two 6 mm stainless clevis pins through a hinge end clip on the stub and two sleeve clips on the leaf; a stop clip (an angle clip, or a single arm at a free wall end) with a sealed magnet at the wall jamb and a strike holder on the leaf (F3).
- Groove cover: a clear PP strip over each stub's back-face groove (platform rule E2); the long walls' grooves face out of the bay.
- Platform foot: v0.2 builds every outrigger on the floor, so the v0.1 work-around in the model is now a no-op (platform request 3). `flex_parts.py` itself is not edited.
- Making sketches FXT-DWG-101 to 106, STL for every printed part, a step-by-step build plan with joint close-ups (FXT-BLD-001).

## Consequences

181 parts at D3, no interference, BOM matching the model. The hinge pins are the only metal parts besides the magnets and strikes. Every made part is cut from the platform sheet or printed (PR-023).

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
