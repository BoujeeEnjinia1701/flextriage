# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""FlexTriage Origami Bay: sizing and first-principles checks (FXT-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py   (writes docs/04-calcs/sizing_results.json)
Reads cad/src/model.py (PARAMS and the part lists of FT1, FT2 and FT3), the platform numbers in
docs/platform/platform_check.py (FXP-PLT-001, imported, not changed) and bom/bom.csv.
Every input is cited in FXT-CAL-001 (docs/04-calcs/01-sizing.md) with its source and the date checked
(2026-11-12), or marked as an assumption (A1 to A14). CONCEPT, NOT FOR FABRICATION.
"""
import csv
import io
import json
import math
import sys
sys.dont_write_bytecode = True  # keep docs/platform/ untouched (no __pycache__ there)
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src"), str(ROOT / "docs/platform")]
import model as M  # noqa: E402
import flex_parts as fx  # noqa: E402
import stem_check as _sc  # noqa: E402
_sc.Check.write = lambda self: "open"          # read the platform numbers without rewriting docs/platform/platform_results.csv
with redirect_stdout(io.StringIO()):
    import platform_check as PLT  # noqa: E402

G = 9.80665
P = M.PARAMS
R = {}

# ---- platform figures used here (FXP-PLT-001) ----------------------------------------------------------------
GSM = P["GSM"] / 1000.0                     # 0.70 kg/m2, FXP-S4FR
RHO_PETG = 1.27                             # g/cm3, ASSUMED as in FXP-PLT-001 section 5.3 (A1)
S4 = PLT.SEC["4 mm FR 700"]
EI_MD, EI_CD, Q = S4["ei_md"], S4["ei_cd"], S4["q"]
HC = 39.7                                   # MJ/kg, PP heat of combustion (FSRI, via FXP-PLT-001)
P_PUSH = 178.0                              # N, ANSI/BIFMA X5.6 force stability (via FXP-PLT-001)
CAP_CLIP = PLT.R["connector"]["cap_clip"]   # N per clip (two pegs), FXP-PLT-001 P9

# ---- assumptions (FXT-CAL-001 section 1) -----------------------------------------------------------------------
MU_BARE = (0.2, 0.35)                       # A2 hard plastic on a smooth floor (Engineering ToolBox: polyethylene on steel 0.2, polystyrene 0.3 to 0.35)
MU_FLOOR = (0.45, 0.6)                      # rubber (EPDM pad, fix F5) on wet and dry concrete, low ends (Engineering ToolBox 0.45 to 0.75 wet, 0.6 to 0.85 dry)
BAG_EMPTY = 0.25                            # A3 kg, empty sand bag
CARRY_BAG = 0.8                             # A4 kg, empty flat carry bag
PRINT_KG_M2 = 0.20                          # A5 kg/m2, printed film plus overlaminate
SEAT_H = 450.0                              # A6 mm, chair seat height for seated eye height
DRAUGHT_PA = (1.0, 5.0)                     # A7 Pa, pressure difference across a flap indoors or in a tent
FT2_FABRIC = (0.20, 0.45)                   # A8 kg/m2: FR knit drape (not wipeable) and FR PVC-coated polyester (wipeable)
STEP_TIMES = {                              # A9 seconds per action for one person, (fast, slow), no training
    "unbag and unfold a duo": (10, 25), "stand a duo in its feet": (10, 20), "push in one clip": (6, 15),
    "set a foot, shoe or jamb foot": (8, 20), "hang a flap leaf and drop two pins": (25, 60),
    "fit a split pin": (8, 20), "fill and lay a ballast bag": (40, 90), "lay out the plan with a tape": (120, 300),
    "final check walk round": (60, 180)}
STEP_TIMES["lay a pad"] = (3, 8)
STEP_TIMES["lay a filled ballast bag"] = (10, 20)
TEAM_EFF = (0.85, 0.70)                     # A10 share of two-person time that is useful (waiting, carrying)

PRINT_RATE = 20.0                           # A11 g of PETG per printer-hour (one desktop printer, to confirm)
SERVICE_USD_G = 0.10                        # A12 USD per g at a print service (sensitivity only)
HC_PET = 21.4                               # MJ/kg, gross heat of combustion of PET (UQ fire lab, INS03 PET fibre), used for PETG and polyester
BR_N42 = 1.3                                # A13 T, remanence of N42 NdFeB (to confirm from the supplier)
UPLIFT_CAP = PLT.R["connector"]["cap_clip"] # N, two pegs in one slot ({PLT} P9)

# ---- geometry of FT1 -------------------------------------------------------------------------------------------
pitch, nx, ny = P["PITCH"], P["N_X"], P["N_Y"]
L_bay, W_bay = nx * pitch / 1000, ny * pitch / 1000
zones = {nm: ((j1 - j0) * pitch / 1000) * W_bay for nm, j0, j1 in P["ZONES"]}
interior = L_bay * W_bay
footprint = (L_bay + 0.6) * (W_bay + 0.6)          # outriggers reach 300 mm outside every wall line
R["plan"] = dict(length_m=L_bay, width_m=W_bay, zones_m2={k: round(v, 2) for k, v in zones.items()}, interior_m2=round(interior, 2),
                 footprint_m2=round(footprint, 2), deck_floor_m2=20.0)

parts = M.components("FT1")
by = {}
for q in parts:
    by.setdefault(q["bom"], []).append(q)
n = {k: len(v) for k, v in by.items()}
duo_m2 = P["DUO_W"] * P["H_WALL"] * 1e-6
flap_m2 = P["FLAP_W"] * P["FLAP_H"] * 1e-6
wall_len = n[1] * P["DUO_W"] / 1000
tail_m2 = P["LEAF"] * P["H_WALL"] * 1e-6
panel_m2 = n[1] * duo_m2 + n[5] * flap_m2 + n[23] * tail_m2
R["panels"] = dict(duos=n[1], flaps=n[5], wall_length_m=wall_len, wall_m2=round(n[1] * duo_m2, 2), flap_m2=round(n[5] * flap_m2, 2),
                   tails=n[23], sheets=math.ceil(n[1] / 2) + math.ceil(n[5] / 2) + 1)


def petg_kg(qs):
    return sum(q["shape"].volume for q in qs) / 1000 * RHO_PETG / 1000


out_trig = 2 * (170 * 265e-6) * GSM                 # two folded outrigger blanks per foot
mass = {
    "duo panels": n[1] * duo_m2 * GSM,
    "corner tail leaves": n[23] * tail_m2 * GSM,
    "flap leaves": n[5] * flap_m2 * GSM,
    "clips (angle, angle tee)": petg_kg(by[2] + by[3]),
    "hinge, sleeve, strike and stop clips": petg_kg(by[4] + by[6] + by[7] + by[21]),
    "pins, washers, magnets, strikes": sum(cpm for cpm in [sum(q["shape"].volume for q in parts if q["kind"] == "fastener") * 7.9e-6,
                                                            sum(q["shape"].volume for q in by[9] + by[10]) * 7.5e-6]),
    "feet blocks and outriggers": petg_kg([q for q in by[11]]) - n[11] * 2 * 33.4 * RHO_PETG / 1000 + n[11] * out_trig
                                  + petg_kg(by[12]) - n[12] * 33.4 * RHO_PETG / 1000 + n[12] * out_trig / 2
                                  + petg_kg(by[20]) - n[20] * 2 * 33.4 * RHO_PETG / 1000 + n[20] * out_trig,
    "angle junction and jamb feet": petg_kg(by[13]) - n[13] * 33.4 * RHO_PETG / 1000 + n[13] * out_trig / 2,
    "EPDM pads and finger guards": sum(q["shape"].volume for q in by[19] + by[22]) * 1.15e-6,
    "prints and overlaminate": sum(q["shape"].volume / 0.15 for q in by[15]) * 1e-6 * PRINT_KG_M2,
    "empty ballast bags": n[14] * BAG_EMPTY,
    "carry bags": 3 * CARRY_BAG,
}
total = sum(mass.values())
R["mass_kg"] = {k: round(v, 2) for k, v in mass.items()}
R["mass_total_kg"] = round(total, 1)
R["mass_without_bags_kg"] = round(total - 3 * CARRY_BAG, 1)
hardware = total - mass["duo panels"] - mass["flap leaves"] - mass["carry bags"]
R["mass_hardware_kg"] = round(hardware, 1)
# what 12 kg (two bags, 1.6 kg of bag) could carry: sheet area at 0.70 kg/m2 with no hardware
room = 12.0 - 2 * CARRY_BAG
R["pack_12kg"] = dict(sheet_m2_if_no_hardware=round(room / GSM, 1), wall_m_at_1200_if_no_hardware=round(room / GSM / 1.2, 1),
                      wall_m_at_1800_if_no_hardware=round(room / GSM / 1.8, 1), ratio=round(total / 12.0, 2),
                      bags_at_12kg=math.ceil(total / 12.0), bags_at_20kg=math.ceil(total / 20.0))
R["pack_volume"] = dict(duo_stack_mm=n[1] * (2 * P["SHEET_T"] + 2), flap_stack_mm=n[5] * P["SHEET_T"],
                        feet_L=round((n[11] + n[12] + n[13] + n[20]) * 0.12 * 0.07 * 0.04 * 1000, 1))
petg_total = mass["clips (angle, angle tee)"] + mass["hinge, sleeve, strike and stop clips"] + \
    petg_kg(by[11] + by[12] + by[13] + by[20]) - (2 * n[11] + n[12] + n[13] + 2 * n[20]) * 33.4 * RHO_PETG / 1000
R["printing"] = dict(petg_kg=round(petg_total, 1), print_hours=round(petg_total * 1000 / PRINT_RATE), service_extra_usd=round(petg_total * 1000 * (SERVICE_USD_G - 0.020)))

# ---- P18 alternative (FXT-DEC-001 D3): same plan at 1,800 mm -------------------------------------------------------
duo18 = 1.2 * 1.8 * GSM
extra_clips = 0.5 * (mass["clips (angle, angle tee)"] + mass["hinge, sleeve, strike and stop clips"])   # three clip heights at 1,800 mm
R["P18"] = dict(mass_kg=round(total - mass["duo panels"] + n[1] * duo18 + extra_clips, 1),
                sheets=n[1] + math.ceil(n[5] / 2) + 1, sheet_cost=round((n[1] + math.ceil(n[5] / 2) + 1) * 44.99, 0))

# ---- platform D15 (pack): moulded, cored feet of 0.15 kg and clips of 0.04 kg (FXP-PLT-001 P17, ASSUMED targets) -------
n_feet = n[11] + n[12] + n[13] + n[20]
n_clips = n[2] + n[3] + n[4] + n[6] + n[7] + n[21]
feet_now = mass["feet blocks and outriggers"] + mass["angle junction and jamb feet"]
clips_now = mass["clips (angle, angle tee)"] + mass["hinge, sleeve, strike and stop clips"]
moulded = total - feet_now - clips_now + n_feet * (0.15 + out_trig) + n_clips * 0.04
R["pack_D15"] = dict(platform_U_bay_kg=round(PLT.R.get("pack", {}).get("total", 14.3), 1) if isinstance(PLT.R.get("pack"), dict) else 14.3,
                     printed_kg=round(total, 1), moulded_cored_kg=round(moulded, 1), feet=n_feet, clips=n_clips,
                     bags_at_15kg=math.ceil(total / 15.0), bags_at_15kg_moulded=math.ceil(moulded / 15.0))
# configurable zones: each further 2-pitch zone adds two wall duos, one stub, two flap leaves and their hardware
per_zone_kg = 3 * duo_m2 * GSM + flap_m2 * GSM + 3 * 0.47 + 4 * 0.067 + 2 * 0.035 + 0.05
R["zones_config"] = dict(per_zone_kg=round(per_zone_kg, 1), per_zone_m2=round(2 * pitch / 1000 * W_bay, 2),
                         two_zone_kg=round(total - per_zone_kg * 1.5, 1), four_zone_kg=round(total + per_zone_kg, 1))

# ---- cohort height: sight lines (ANSUR II summary, NCSU) ------------------------------------------------------------
eye = {"standing eye, women 5th": 1421, "standing eye, men 95th": 1753, "seated eye, women 5th": 698 + SEAT_H,
       "seated eye, men 95th": 860 + SEAT_H, "stature, men 95th": 1870}
top = P["H_WALL"] + M.Z0
R["sight"] = {k: dict(eye_mm=v, sees_over_1200=v > top, sees_over_1800=v > 1800 + M.Z0) for k, v in eye.items()}
# hidden ground behind a 1.2 m wall for a short standing observer 0.5 m from it (A14: stretcher top 250 mm, trolley 800 mm)
slope = (1421 - top) / 500.0
R["sight_hidden_m"] = {"stretcher top 250 mm": round((top - 250) / slope / 1000, 2), "trolley top 800 mm": round((top - 800) / slope / 1000, 2),
                       "head of a seated patient 1,150 mm": round(max(0.0, top - 1150) / slope / 1000, 2)}

# ---- self-weight stability (platform method, P2, P3 and P29; FXP-PLT-001 v0.2 rule S1: zigzag walls) -------------
HOT = 0.5                                   # stiffness at 40 to 50 C or under creep, as FXP-PLT-001 section 10
K_FREE = (0.425 + 0.25) / 0.25              # A16 SS-free over free-free plate coefficient for b/h = 0.5 (uniform compression, ASSUMED for self-weight)
h_cr = (7.837 * EI_MD / Q) ** (1 / 3)
leaf = (2 * math.pi ** 2 * math.sqrt(EI_MD * EI_CD) / P["LEAF"] ** 2) / (Q * P["H_WALL"])
strip = (h_cr / P["H_WALL"]) ** 3
flap_col = (h_cr / (P["FLAP_H"] - fx.clip_heights(P["FLAP_H"])[0])) ** 3      # hung from its lower sleeve: the leaf above it stands
R["self_weight"] = dict(h_cr_flat_mm=round(h_cr), load_factor_flat_P12=round(strip, 2), load_factor_flat_P12_hot=round(strip * HOT, 2),
                        load_factor_flat_P18=round((h_cr / 1800) ** 3, 2), platform_factor=2.0,
                        leaf_both_edges=round(leaf, 2), leaf_both_edges_hot=round(leaf * HOT, 2),
                        leaf_free_edge=round(strip * K_FREE, 2), leaf_free_edge_hot=round(strip * K_FREE * HOT, 2),
                        flap_hung=round(flap_col, 2), flap_hung_hot=round(flap_col * HOT, 2),
                        leaf_P18_both_edges=round(leaf * P["H_WALL"] / 1800, 2), leaf_P18_both_edges_hot=round(leaf * P["H_WALL"] / 1800 * HOT, 2))

# ---- tipping under the 178 N push (rigid wall piece, as FXP-PLT-001 P7) ---------------------------------------------
z_push = min(1372.0, P["H_WALL"] + M.Z0 - 102.0)
ZIG_OFF = (fx.CORE / 2 + P["LEAF"] / 2) * math.sin(math.radians(P["ZIG"])) / 1000   # m, leaf centres outside the joint line
duo_kg = duo_m2 * GSM
foot_kg = mass["feet blocks and outriggers"] / (n[11] + n[12] + n[20])
bag_kg = P["BAG_KG"]


def piece_moment(bags_per_stub, bag_jamb=1, stubs=2, duos=None):
    """Outward push on wall A at a stub joint (piece: wall A, its stubs on anchor feet). Tipping axis: the outside
    outrigger tips, 300 mm outside the wall line. The anchor feet (F4) make each stub's foot and bags lift with it.
    Restoring moments about that axis, N m. A rigid piece: valid for a push at or near a stub joint only (S6)."""
    arm0 = 0.3
    duos = nx if duos is None else duos
    m_wall = duos * duo_kg * (arm0 - ZIG_OFF) + (duos + 1) * foot_kg * arm0     # zigzag leaves lie outside the joint line
    m_stubs = stubs * duo_kg * (arm0 + W_bay / 4) + stubs * foot_kg * (arm0 + W_bay / 2)
    m_bags = stubs * bags_per_stub * bag_kg * (arm0 + W_bay / 2) + bag_jamb * bag_kg * 0.0   # the jamb bag lies on the axis side
    return G * (m_wall + m_stubs + m_bags)


R["tip"] = dict(z_push_mm=z_push, demand_Nm=round(P_PUSH * z_push / 1000, 1))
for b in (0, 1, 2):
    R["tip"][f"piece_A_{b}_bags_per_stub_N"] = round(piece_moment(b) / (z_push / 1000), 1)
need = (P_PUSH * z_push / 1000 - piece_moment(0)) / (G * 2 * (0.3 + W_bay / 2))
R["tip"]["ballast_needed_per_stub_kg"] = round(need, 1)
# single duo between two feet (the platform P6 case at P12): local mechanism with no help from its neighbours
R["tip"]["single_duo_N"] = [round((duo_kg * (0.3 - ZIG_OFF) + 2 * foot_kg * 0.3) * G / (z_push / 1000), 1),
                            round((duo_kg * (0.3 + ZIG_OFF) + 2 * foot_kg * 0.3) * G / (z_push / 1000), 1)]   # outward, inward
# free wall end at an entry or exit jamb (jamb foot with one outside outrigger and one bag), outward and inward
out_m = (duo_kg / 2 + 0.44) * G * 0.3 + bag_kg * G * 0.14
in_m = bag_kg * G * 0.195 + (duo_kg / 2 + 0.44) * G * 0.035
R["tip"]["free_wall_end_N"] = [round(out_m / (z_push / 1000), 1), round(in_m / (z_push / 1000), 1)]
# a 2-zone bay: each long wall piece carries one stub
R["tip"]["two_zone_one_stub_2_bags_N"] = round(piece_moment(2, stubs=1, duos=5) / (z_push / 1000), 1)
R["tip"]["two_zone_bags_needed_kg"] = round((P_PUSH * z_push / 1000 - piece_moment(0, stubs=1, duos=5)) / (G * (0.3 + W_bay / 2)), 1)
# anchor foot uplift: at tipping each anchor lifts its two bags and itself, carried by the two pegs of its clip arm
uplift = (2 * bag_kg + foot_kg) * G
R["anchor"] = dict(uplift_N=round(uplift), peg_capacity_N=round(UPLIFT_CAP), factor=round(UPLIFT_CAP / uplift, 2),
                   v01_capacity_N=201, v01_factor=round(201 / uplift, 2),
                   tee_shear_N=round((2 * bag_kg + foot_kg + duo_kg) * G), tee_capacity_N=round(2 * UPLIFT_CAP),
                   tee_factor=round(2 * UPLIFT_CAP / ((2 * bag_kg + foot_kg + duo_kg) * G), 2))
# stub pushed sideways: the tee or corner joint carries the overturning couple into the long wall in edge bearing
dz = fx.clip_heights(P["H_WALL"])[1] - fx.clip_heights(P["H_WALL"])[0]
couple = P_PUSH * z_push / dz
bear = couple / (fx.CLIP_H * 2 * S4["ts"])
R["stub_joint"] = dict(clip_force_N=round(couple), edge_bearing_MPa=round(bear, 1), pp_yield_MPa=24.0, clip_pullout_N=round(CAP_CLIP))
# sliding before tipping: the moving piece is the pushed wall with its stubs, feet and ballast
m_piece = (nx + 2) * duo_kg + tail_m2 * GSM + (nx + 3) * foot_kg + (2 * 2 + 1) * bag_kg + 0.8
R["slide"] = dict(piece_kg=round(m_piece, 1), slide_bare_N=[round(mu * m_piece * G) for mu in MU_BARE],
                  slide_pads_N=[round(mu * m_piece * G) for mu in MU_FLOOR])

# ---- deployment time ------------------------------------------------------------------------------------------------
counts = {"unbag and unfold a duo": n[1] + n[23], "stand a duo in its feet": n[1] + n[23], "lay a pad": n[19],
          "push in one clip": n[2] + n[3] + n[4] + n[6] + n[7] + n[21],
          "set a foot, shoe or jamb foot": n[11] + n[12] + n[13] + n[20], "hang a flap leaf and drop two pins": n[5],
          "fit a split pin": n[8], "fill and lay a ballast bag": n[14], "lay out the plan with a tape": 1, "final check walk round": 1}
t_fast = sum(counts[k] * STEP_TIMES[k][0] for k in counts) / 2 / TEAM_EFF[0] / 60
t_slow = sum(counts[k] * STEP_TIMES[k][1] for k in counts) / 2 / TEAM_EFF[1] / 60
# fix F6: flap sleeves and catches stay fitted on the leaves and hinge clips on the jamb panels in the bag, and the
# ballast bags are filled before the clock starts (site preparation); the timed task is panels, wall clips, feet and flaps
pre = dict(counts)
pre["push in one clip"] = n[2] + n[3] + n[4] + n[21]  # wall, hinge and stop clips; sleeves and strike holders ride on the leaves
pre["fill and lay a ballast bag"] = 0
pre["lay a filled ballast bag"] = n[14]                 # bags filled before the clock, laid in 10 to 20 s each
pre["lay a pad"] = 0                                    # pads bonded under the feet and shoes (F5)
t_fix_fast = sum(pre[k] * STEP_TIMES[k][0] for k in pre) / 2 / TEAM_EFF[0] / 60
t_fix_slow = sum(pre[k] * STEP_TIMES[k][1] for k in pre) / 2 / TEAM_EFF[1] / 60
one_zone = {"unbag and unfold a duo": 2, "stand a duo in its feet": 2, "push in one clip": 4 + 3, "set a foot, shoe or jamb foot": 3,
            "hang a flap leaf and drop two pins": 1, "fit a split pin": 2, "lay a filled ballast bag": 2}
R["deploy_min"] = dict(counts=counts, as_drawn=[round(t_fast, 1), round(t_slow, 1)], with_F6=[round(t_fix_fast, 1), round(t_fix_slow, 1)],
                       target=15.0, one_zone_min=[round(sum(one_zone[k] * STEP_TIMES[k][j] for k in one_zone) / 2 / TEAM_EFF[j] / 60, 1) for j in (0, 1)])

# ---- flaps: magnetic catch, opening force, draught, doorway clear width ----------------------------------------------
pull_contact = 6.44 * 4.448                     # N, K&J D82 to a thick steel plate
md, mt = P["MAGNET"]
Rm, Lm = md / 2, mt


def b_axis(z):
    """On-axis flux density of a disc magnet (T) at z mm from its face (standard cylinder formula), Br = BR_N42."""
    return BR_N42 / 2 * ((Lm + z) / math.hypot(Rm, Lm + z) - z / math.hypot(Rm, z))


gap = P["COVER"] + 0.5                          # printed cover plus 0.5 mm air to the strike
pull_gap = pull_contact * (b_axis(gap) / b_axis(0.0)) ** 2     # A13: pull scaled with B squared (first-order)
z5 = next(z for z in [i * 0.5 for i in range(1, 400)] if b_axis(z) < 5e-4)
flap_area = flap_m2
lever = (P["FLAP_W"] + fx.CORE / 2) / (820 + 150 + fx.CORE / 2)   # catch at the free edge, push at the push-plate centre
draught = [dp * flap_area / 2 for dp in DRAUGHT_PA]   # a uniform pressure on a hinged leaf: half the force at the free edge
s15, c15 = math.sin(math.radians(P["ZIG"])), math.cos(math.radians(P["ZIG"]))
anchor_reach = 60.0 * c15 + 35.0 * s15          # anchor foot block (120 x 70) turned 15 deg off the doorway line
end_jamb_reach = 35.0 * c15 + 60.0 * s15        # jamb foot at a free wall end, along the 15 deg leaf
door_clear_floor = pitch - 35.0 - anchor_reach  # angle jamb foot half-depth at an inner doorway's wall jamb
door_clear_end = pitch - end_jamb_reach - anchor_reach
door_clear_flaps = pitch - fx.CORE - (P["SHEET_T"] + fx.CORE / 2)
door_clear_bags = pitch - 35.0 - 165.0          # upstream approach: bags reach 165 mm into the doorway width
R["flap"] = dict(magnet_contact_N=round(pull_contact, 1), magnet_at_gap_N=round(pull_gap, 1), push_per_catch=round(lever, 2),
                 push_force_N=round(pull_gap * lever, 1), field_0p5mT_mm=z5, ada_max_N=22.2, catch_target_N=[3.0, 18.0],
                 draught_edge_N=[round(d, 2) for d in draught], door_clear_approach_mm=round(door_clear_bags),
                 leaf_kg=round(flap_area * GSM, 2), door_clear_floor_mm=round(door_clear_floor), door_clear_open_flaps_mm=round(door_clear_flaps),
                 ada_clear_mm=815, stretcher_w_mm=750, tent_exit_72in_mm=1829,
                 door_clear_end_mm=round(door_clear_end))

# ---- fire load -------------------------------------------------------------------------------------------------------
R["fire"] = dict(panel_m2=round(panel_m2, 2), MJ=round(panel_m2 * GSM * HC), MJ_per_m2_floor=round(panel_m2 * GSM * HC / footprint, 1),
                 MJ_P18=round((n[1] * 1.2 * 1.8 + n[5] * flap_m2) * GSM * HC),
                 MJ_PETG=round(petg_total * HC_PET), MJ_bags_and_pads=round((n[14] * BAG_EMPTY + 3 * CARRY_BAG) * HC_PET),
                 MJ_all=round(panel_m2 * GSM * HC + petg_total * HC_PET + (n[14] * BAG_EMPTY + 3 * CARRY_BAG) * HC_PET))

# ---- sign legibility (ANSI Z535 ratio of 25 ft per inch of letter height, favourable conditions) ---------------------
ratio = 25 * 12                                  # 300:1
signs = {"zone numeral 150 mm": 150, "zone word 60 mm": 60}
R["legibility_m"] = {k: [round(h * ratio / 1000 / 2, 1), round(h * ratio / 1000, 1)] for k, h in signs.items()}
R["legibility_need_m"] = round(math.hypot(3 * pitch / 1000, W_bay), 1)   # diagonal of the largest zone

# ---- cost ------------------------------------------------------------------------------------------------------------
bom = list(csv.DictReader((ROOT / "bom/bom.csv").open()))
cost = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in bom)
drivers = sorted(((float(r["qty"]) * float(r["unit_cost_usd"]), r["item"]) for r in bom), reverse=True)[:4]
printed = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in bom if "print" in r["supplier"].lower() and r["item"][:3] != "15 ")
R["cost"] = dict(bom_total=round(cost, 2), target=800.0, sheet_saving_volume=round(R["panels"]["sheets"] * (44.99 - 34.99), 2),
                 printed_parts=round(printed, 2), stretch=500.0, over=round(cost - 800.0, 2),
                 drivers=[(d[1], round(d[0], 2)) for d in drivers], per_m2_interior=round(cost / interior, 1),
                 per_deployment_50=round(cost / 50, 2), per_deployment_100=round(cost / 100, 2))

# ---- FT2 and FT3 first-order numbers (same plan) ------------------------------------------------------------------------
f2 = M.components("FT2")
post_len = sum(q["shape"].volume for q in f2 if q["name"].startswith("Aluminium post")) * 2.7e-6
rail_len = sum(q["shape"].volume for q in f2 if q["name"].startswith(("Top rail", "Door header"))) * 2.7e-6
base = sum(q["shape"].volume for q in f2 if q["name"].startswith(("Base plate", "Post socket"))) * 2.7e-6
screen_m2 = sum(q["shape"].volume for q in f2 if "screen" in q["name"] or "curtain" in q["name"]) / P["FT2_FABRIC_T"] * 1e-6
n_posts = len([q for q in f2 if q["name"].startswith("Aluminium post")])
ft2_mass = [round(post_len + rail_len + base + screen_m2 * w + 1.5, 1) for w in FT2_FABRIC]
R["FT2"] = dict(posts=n_posts, screen_m2=round(screen_m2, 1), mass_kg=ft2_mass, frame_kg=round(post_len + rail_len + base, 1),
                cost_benchmark_usd=round(n_posts / 2 * 179.99 + 16 * 50.0), fire_MJ=None)
f3 = M.components("FT3")
n3 = len([q for q in f3 if q["name"].startswith("Stanchion post")])
post_kg = 42 / 2.2046                              # Uline H-3736BL, 42 lb per post
tip3 = post_kg * G * (P["FT3_BASE_D"] / 2000) / (P["FT3_POST"][2] / 1000)
R["FT3"] = dict(posts=n3, mass_kg=round(n3 * post_kg, 0), tip_one_post_N=round(tip3, 1), cost_steel_usd=round(n3 * 54.50 + 4 * 10.25 + 40, 0),
                cost_waterfill_usd=round(n3 * 79.79 + 4 * 10.25 + 40, 0), belt_height_mm=P["FT3_POST"][2])

(ROOT / "docs/04-calcs/sizing_results.json").write_text(json.dumps(R, indent=1))

if __name__ == "__main__":
    print(json.dumps(R, indent=1))
