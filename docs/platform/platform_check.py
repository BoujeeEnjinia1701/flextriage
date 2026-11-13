# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Design Molecule Labs with Helpful Engineering
"""Flex panel and connector platform: the numbers behind FXP-PLT-001 (docs/platform/flex-platform.md).

Licence: Apache-2.0 (software used with the hardware), following the Helpful Engineering licensing guide.
Design Molecule Labs with Helpful Engineering. CONCEPT, NOT FOR FABRICATION.

Run from anywhere:  python3 docs/platform/platform_check.py
Writes docs/platform/platform_results.csv (claim id, claim, check, verdict, closed_by) with the Check class
of .kit/stem_check.py, and prints the key numbers the specification quotes.

v0.2 (2026-11-12): revised after the independent review recorded in FXP-PLT-001 section 16 (P1 to P26
reworked, P27 to P40 added for the missed claims). Every input is either cited in SRC below (link, checked
2026-11-12) or marked ASSUMED. Figures are first-order screens for TRL 3; none replaces the TRL 4 tests listed
in FXP-PLT-001 section 14.
"""
from __future__ import annotations

import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / ".kit"))
from stem_check import Check, WITHIN, PLAUSIBLE, FIX, FAILS, G   # noqa: E402

SRC = {
    "interprofile": "Coroplast/Interprofile product data 11/18/08, https://www.acplasticsinc.com/media/documents/PD_CoroPlast_InterProfile.pdf",
    "aky35": "DS Smith Akyplac 3,5 mm 600 g/m2 data sheet 06/2020, https://pim.igepa.nl/Plaatmateriaal/Polypropyleen/Akyplac%C2%AE/FT%20Akyplac%20600%20GB%20-%2006.2020.pdf",
    "aky8": "Akyplac 8 mm 1500 g/m2 data sheet (raw PP: flexural modulus 1150 MPa, yield 24 MPa, elongation at yield 11 %, Izod 15 kJ/m2 at 23 C and 7 at -20 C, HDT 50 C at 1.8 MPa, not resistant to oxidising substances), https://pim.igepa.nl/Plaatmateriaal/Polypropyleen/Akyplac%C2%AE/Technische%20datasheet%20Akyplac%208%20mm.pdf",
    "akyprint5": "Akyprint UV 5 mm 1300 g/m2 data sheet 06/2020 (raw PP flexural modulus 1100 MPa, expansion 0.11 mm/m C), https://sunclear.fr/img/medias/bt/POLYPROPYLENE_ALVEOLAIRE__AKYPRINT_5MM_fiche_technique_130422.pdf",
    "fsri": "UL FSRI Materials and Products Database, polypropylene (heat of combustion 39.7 MJ/kg, density 886 kg/m3), https://materials.fsri.org/materialdetail/polypropylene-pp",
    "sitebox": "Sitebox flame retardant protection board spec (rib distance 3.2 to 3.5 mm), https://www.sitebox.ltd.uk/docs/PBTFD12/FLAME_RETARDANT_PROTECTION_BOARD_SPEC_SHEET.pdf",
    "intepro_fr": "IntePro FR line card Sept 2020 (NFPA 701-2019 TM1; TM1 for <= 700 gsm; average flaming drip under 2 s), https://polymershapes.com/wp-content/uploads/2025/08/intepro-fr-092920.pdf",
    "bifma": "ANSI/BIFMA X5.6 force stability 178 N, impact stability 22.7 kg bag, as quoted in SGS report SDHL2201000875FT, https://www.mwworkstation.com/Uploads/202303/t8_cubicle_workstation--bifma-sgs.pdf",
    "cmr": "780 CMR 1607.13 interior walls and partitions over 1829 mm, https://regulations.justia.com/states/massachusetts/780-cmr/chapter-16/section-1607/subsection-1607-13",
    "bcn3d": "BCN3D PETG TDS (yield 50.4 MPa, modulus 2020 MPa, strain at yield 5.9 %, HDT 70 C), https://www.bcn3d.com/wp-content/uploads/2019/09/TDS_BCN3D_Filaments_PETG.pdf",
    "bayer": "Bayer MaterialScience, Snap-Fit Joints for Plastics (cantilever strain, tapered arm factor 1.09, force; friction PP 0.25 to 0.30, x 1.5 PP on PP), https://cdn.sparkfun.com/assets/home_page_posts/1/4/1/0/Plastic_Snap_fit_design.pdf",
    "cplab": "CP Lab Safety PP chart, https://www.cplabsafety.com/content/chemical-charts/Polypropylene.pdf",
    "ineos": "INEOS PP chemical resistance guide, https://www.ineos.com/globalassets/ineos-group/businesses/ineos-olefins-and-polymers-usa/products/technical-information--patents/ineos-pp-chemical-resistance-guide.pdf",
    "curbell_petg": "Curbell Plastics, Disinfecting acrylic, polycarbonate and PETG sheet, https://www.curbellplastics.com/wp-content/uploads/2022/11/Disinfecting-Acrylic-Polycarbonate-and-PETG-Sheet.pdf",
    "medline": "MedlinePlus Genetics, colour vision deficiency, https://medlineplus.gov/genetics/condition/color-vision-deficiency/",
    "niosh": "CCOHS, NIOSH lifting equation load constant 23 kg, https://www.ccohs.ca/oshanswers/ergonomics/niosh/assessing.html",
    "iarc": "IARC Monographs volume 131 Q and A (antimony trioxide Group 2B, 1989; trivalent antimony Group 2A), https://www.iarc.who.int/wp-content/uploads/2022/04/Mono-131-QA.pdf",
}

c = Check(out=HERE / "platform_results.csv")
R = {}   # numbers quoted in the specification

# ---------------------------------------------------------------------------------------------------------
# 1. Sheet grades and section model
# ---------------------------------------------------------------------------------------------------------
RHO = 886.0                     # kg/m3, PP (FSRI)
E_RAW = (1100.0, 1150.0)        # MPa, raw PP flexural modulus (Akyprint 5 mm; Akyplac 8 mm)
SIGMA_Y = 24.0                  # MPa, PP tensile strength at yield, raw material (Akyplac 8 mm, ISO 527-2)
HOT = 0.5                       # ASSUMED stiffness factor for 40 to 50 C in a tent with creep over a deployment; the
                                # ISO 75 HDT of 50 C at 1.8 MPa (0.2 % strain criterion) implies about 900/1150 = 0.78
                                # for short-term load at 50 C, so 0.5 also covers creep (to assess, T1 hot)
GRADES = {                      # name: thickness mm, grammage g/m2 (cited), flute pitch mm (ASSUMED: 3.4 mm from the
    "4 mm FR 700": (4.0, 700, 3.4),        # cited 3.2 to 3.5 mm rib distance; pitch = thickness above 4 mm)
    "4 mm 750": (4.0, 750, 3.4),
    "5 mm 1000": (5.0, 1000, 5.0),
    "6 mm 1400": (6.0, 1400, 6.0),
    "8 mm 1800": (8.0, 1800, 8.0),
    "10 mm 2000": (10.0, 2000, 10.0),
}
CAL = {"3.5 mm 600": (3.5, 600, 3.4, 3.6, 1.3), "8 mm 1500": (8.0, 1500, 8.0, 41.0, 4.0)}   # Akyplac ISO 178: k_MD, k_CD in N/mm


def skin(h, gsm, p):
    """Skin (= rib, ASSUMED equal) thickness from grammage: 2 ts + ts (h - 2 ts)/p = gsm/rho."""
    a = gsm / RHO
    lo, hi = 0.0, h / 2
    for _ in range(60):
        ts = (lo + hi) / 2
        if 2 * ts + ts * (h - 2 * ts) / p > a:
            hi = ts
        else:
            lo = ts
    return ts


def i_md(h, gsm, p):
    """Second moment per unit width (mm4/mm) for bending along the flutes: two skins plus the ribs."""
    ts = skin(h, gsm, p)
    d = h - ts
    hc = h - 2 * ts
    return 2 * (ts ** 3 / 12 + ts * (d / 2) ** 2) + (ts / p) * hc ** 3 / 12, ts


EI_meas, E_eff = {}, []
for name, (h, gsm, p, kmd, kcd) in CAL.items():
    ei_md = kmd * 100 ** 3 / 48 / 40           # ISO 178 three-point bend, L 100 mm, b 40 mm: k = 48 EI / L^3
    ei_cd = kcd * 100 ** 3 / 48 / 40
    I, _ = i_md(h, gsm, p)
    EI_meas[name] = (ei_md, ei_cd, ei_cd / ei_md)
    E_eff.append(ei_md / I)
E_EFF = sum(E_eff) / len(E_eff)


def cd_ratio(h):
    (h1, r1), (h2, r2) = (3.5, EI_meas["3.5 mm 600"][2]), (8.0, EI_meas["8 mm 1500"][2])
    x = (math.log(h) - math.log(h1)) / (math.log(h2) - math.log(h1))
    return math.exp(math.log(r1) + x * (math.log(r2) - math.log(r1)))


def section(h, gsm, p):
    I, ts = i_md(h, gsm, p)
    ei_md = E_EFF * I
    ei_cd = ei_md * cd_ratio(h)
    return dict(h=h, gsm=gsm, p=p, ts=ts, ei_md=ei_md, ei_cd=ei_cd, q=gsm / 1000 * G * 1e-6)


SEC = {n: section(*v) for n, v in GRADES.items()}
s4 = SEC["4 mm FR 700"]
s4lo = section(4.0, 700 * 0.9, 3.4)            # grammage tolerance band: -10 % (Akyplac 600 +-60)
R["E_eff"], R["sections"] = E_EFF, SEC
model_err = max(abs(E_EFF * i_md(h, gsm, p)[0] / EI_meas[n][0] - 1) for n, (h, gsm, p, _, _) in CAL.items())
c.cited("P1", "Bending stiffness EI of corrugated PP twinwall per unit width can be estimated per flute direction from grammage",
        "Physics", "Strength of materials",
        "Sandwich section (two skins plus ribs, skins sized from grammage at 886 kg/m3) fitted to Akyplac ISO 178 three-point "
        "flexural rigidity (k = 48 EI / L^3, L 100 mm, b 40 mm); CD from the measured CD/MD ratio, log-interpolated in thickness",
        f"Fitted E_eff {E_EFF:.0f} MPa, above the raw resin (1100 to 1150 MPa), so the section model under-counts I or the skins are "
        f"oriented: EI is a fitted effective value, not a bound; within {model_err * 100:.0f} % of both data points. 4 mm FR 700: "
        f"EI_MD {s4['ei_md']:,.0f}, EI_CD {s4['ei_cd']:,.0f} N mm2/mm; at -10 % grammage {s4lo['ei_md']:,.0f} and {s4lo['ei_cd']:,.0f}. "
        "EI_CD at a 100 mm span is shear-dominated, so it under-states CD bending at 600 mm spans (conservative there); 4 to 10 mm "
        "values are interpolated, not measured", PLAUSIBLE,
        closed_by="T1: ISO 178 on the bought lot, both directions, at 100 and 400 mm spans, 23 and 50 C")

# ---------------------------------------------------------------------------------------------------------
# 2. Free height and leaf buckling (cold and hot)
# ---------------------------------------------------------------------------------------------------------
SF = 2.0   # ASSUMED load factor on self-weight buckling
for name, s in SEC.items():
    s["h_cr"] = (7.837 * s["ei_md"] / s["q"]) ** (1 / 3)          # Greenhill, fixed base, free top
    s["h_allow_flat"] = s["h_cr"] / SF ** (1 / 3)
    s["h_cr_hot"] = s["h_cr"] * HOT ** (1 / 3)
    s["h_allow_hot"] = s["h_cr_hot"] / SF ** (1 / 3)
    D1, D2 = s["ei_md"], s["ei_cd"]
    s["N_cr_leaf"] = math.pi ** 2 / 600 ** 2 * (2 * math.sqrt(D1 * D2) + 0.0)   # orthotropic, D3 = 0 lower bound
    s["N_base_1800"] = s["q"] * 1800
    s["leaf_margin"] = s["N_cr_leaf"] / (SF * s["N_base_1800"])          # margin with the load factor 2 included
    s["leaf_margin_hot"] = HOT * s["leaf_margin"]
m12_cold = (s4["h_cr"] / 1200) ** 3
m12_hot = (s4["h_cr_hot"] / 1200) ** 3
R["p12_flat_margin"] = (m12_cold, m12_hot)
c.cited("P2", "Every platform panel above 600 mm stands only with both vertical edges supported (fold or angle joint of 30 deg or more, corner or tee)",
        "Physics", "Elastic stability",
        "Greenhill self-weight buckling h_cr = (7.837 EI / q)^(1/3), strip clamped at the base (an upper bound: a foot is not a clamp)",
        f"Flat 4 mm FR: h_cr {s4['h_cr']:.0f} mm cold, {s4['h_cr_hot']:.0f} mm hot (x {HOT} stiffness); a flat P12 strip has a load margin "
        f"of {m12_cold:.2f} cold and {m12_hot:.2f} hot, a flat P18 strip fails outright; 10 % lighter sheet lowers h_cr by about 3 %. "
        "Fixed by rule S1 for every panel above 600 mm (P12 included); the supported leaf is P3", WITHIN,
        closed_by="Fix F1 (rule S1, v0.2: P12 included, angle clip)")
c.cited("P3", "A 600 mm leaf supported on both vertical edges carries its own weight at 1800 mm without buckling, cold and hot",
        "Physics", "Elastic stability",
        "Orthotropic plate, uniform compression, long plate: N_cr = pi^2/b^2 (2 sqrt(D1 D2) + 2 D3), D3 = 0 as the lower bound "
        "(twinwall is soft in twist); against N = q H at the base",
        f"Margin {s4['leaf_margin']:.1f} cold and {s4['leaf_margin_hot']:.1f} hot, load factor 2 included, at D3 = 0 (v0.1 used k = 4 and gave 6.3; uniform base load is conservative). An edge "
        "at a 30 deg fold or angle clip is held laterally by the next leaf's in-plane stiffness x sin 30 = 0.5, which is far stiffer "
        "than the restraint buckling needs, but this is not computed here", PLAUSIBLE,
        closed_by="Rule S1; T1 hot and T7 bay test at 23 and 50 C")
R["free_height"] = {n: (round(s["h_cr"]), round(s["h_allow_flat"]), round(s["h_allow_hot"]), round(s["leaf_margin"], 1),
                        round(s["leaf_margin_hot"], 1)) for n, s in SEC.items()}

# ---------------------------------------------------------------------------------------------------------
# 3. Lateral push: BIFMA X5.6 force stability 178 N
# ---------------------------------------------------------------------------------------------------------
P_PUSH, Z_PUSH = 178.0, 1372.0
ALPHA = 0.0169      # centre deflection coefficient, SS rectangular plate a/b = 3, point load (Timoshenko and Woinowsky-Krieger)
DEFL_LIM = 25.0     # mm, ASSUMED serviceability limit for a hand push on a leaf
for name, s in SEC.items():
    D = math.sqrt(s["ei_md"] * s["ei_cd"])
    s["defl_plate_178"] = ALPHA * P_PUSH * 600 ** 2 / D
    s["P_allow_plate"] = DEFL_LIM * D / (ALPHA * 600 ** 2)
c.cited("P4", "Panels are boundaries, not barriers: a 600 mm leaf bows well past 25 mm under the 178 N BIFMA push", "Physics", "Plate bending",
        "w = alpha P b^2 / D (simply supported on four edges, a/b = 3, alpha 0.0169), D = sqrt(D_MD D_CD); a free top edge is worse",
        f"4 mm FR: {s4['defl_plate_178']:.0f} mm at 178 N (small-deflection theory; membrane action limits it); 25 mm at "
        f"{s4['P_allow_plate']:.1f} N. 10 mm: {SEC['10 mm 2000']['defl_plate_178']:.0f} mm. No twinwall grade resists a hand push in bending; "
        "the claim is dropped and stated as limit L1", FIX, closed_by="D5 Proposed, awaiting Amish: stated limit L1 in every product")
R["push"] = {n: (round(s["defl_plate_178"]), round(s["P_allow_plate"], 1)) for n, s in SEC.items()}
q_cmr = 0.24e-3
w_cmr = 0.01223 * q_cmr * 600 ** 4 / math.sqrt(s4["ei_md"] * s4["ei_cd"])
top = 1800 + 10.5
c.claim("P5", "Platform panels, standing in their feet, top out below 1829 mm, outside the scope of the IBC interior partition load (780 CMR 1607.13)",
        "Engineering and technology", "Building codes",
        f"Top = 1800 mm panel + 10.5 mm foot seat = {top:.1f} mm, margin {1829 - top:.1f} mm before tolerances (sheet length 0 to +1 in on "
        f"standard sheets is trimmed off). Outside the threshold removes one load case only; it is not evidence of strength (a 4 mm leaf "
        f"would deflect about {w_cmr:.0f} mm under 0.24 kN/m2); BIFMA and the authority having jurisdiction still apply",
        value=top, limit=1829, unit="mm", rule="below", margin=0.02, closed_by="Rule S2 (cut height tolerance 0 to -3 mm)")
R["w_cmr"] = w_cmr

# ---------------------------------------------------------------------------------------------------------
# 4. Tip-over, sliding and impact
# ---------------------------------------------------------------------------------------------------------
M_CLIP = 0.067      # kg per inline or corner clip (full detail CAD about 51.5 cm3 at an ASSUMED PETG 1270 kg/m3, solid)
M_FOOT = 0.46       # kg: foot block about 312 cm3 solid at 1270 kg/m3 (0.40) plus two outriggers of 0.7 kg/m2 twinwall (0.06)
A_FOOT = 300.0      # mm, outrigger reach
m_duo = 1.2 * 1.8 * 700 / 1000
R["m_duo"] = m_duo
z_push = min(Z_PUSH, 1810.5 - 102)
F_single = (m_duo + 2 * M_FOOT + 6 * M_CLIP) * G * A_FOOT / z_push
ballast_single = (P_PUSH * z_push / (G * A_FOOT) - (m_duo + 2 * M_FOOT)) / 2
c.cited("P6", "No platform layout relies on a single freestanding panel", "Physics", "Statics", "Overturning about the outrigger tip: F = W a / z",
        f"A flat P18 duo on two standard feet tips at {F_single:.1f} N against the 178 N BIFMA push; it would need {ballast_single:.0f} kg of "
        "ballast per foot. Fixed by rule S3 (L, U or closed plans only)", WITHIN, closed_by="Fix F2 (rule S3)")

ZIG = math.cos(math.radians(15))      # zigzag walls: leaves alternate +-15 deg off the wall line (30 deg joints, rule S1)
D_U = 2 * 1200 * ZIG                  # 2318 mm plan depth of a two-duo zigzag return
N_FEET_U, N_CLIPS_U, BALLAST = 7, 15, 5.0
R["U"] = dict(D=D_U, feet=N_FEET_U, clips=N_CLIPS_U)


def u_tip(ballast_far=0.0):
    m_ret = 2 * m_duo
    restoring = 2 * m_ret * G * D_U / 2 + 2 * ballast_far * G * D_U + N_FEET_U * M_FOOT * G * D_U / 2
    return restoring / z_push


F_U0, F_U5 = u_tip(0.0), u_tip(BALLAST)
need_b = max(0.0, (P_PUSH - F_U0) * z_push / (2 * G * D_U))
M_U = 6 * m_duo + N_FEET_U * M_FOOT + N_CLIPS_U * M_CLIP + 2 * BALLAST
R["tip"] = dict(single=F_single, ballast_single=ballast_single, U=F_U0, U5=F_U5, U_ballast=need_b, M_U=M_U)
c.cited("P7", "A zigzag U bay (2.3 m back and returns of P18 duos) with a 5 kg bag at each far return foot does not tip under the 178 N push",
        "Physics", "Statics",
        "Restoring moment of returns, feet and ballast about the back wall base line, push at 1372 mm; the U is taken as rigid",
        f"Unballasted {F_U0:.0f} N; ballast needed {need_b:.1f} kg per far foot; with 5 kg {F_U5:.0f} N. Not modelled: the push reaches the "
        "returns through a leaf that bows (P4) and clips (P9), so the rigid-U figure is an upper bound on what the bay resists before a "
        "joint lets go; BIFMA 5.1 also asks for no loss of serviceability", PLAUSIBLE,
        closed_by="Fix F2 (rule S3, zigzag walls in v0.2); T7 bay test")
MU_ASSUMED = 0.25
F_slide = MU_ASSUMED * M_U * G
mu_tip = F_U5 / (M_U * G)
R["slide"] = dict(F=F_slide, mu_tip=mu_tip)
c.cited("P27", "A bay slides on the floor before it tips under a push", "Physics", "Statics", "Sliding F = mu W against the tipping force of P7",
        f"Ballasted U bay {M_U:.1f} kg: slides at {F_slide:.0f} N if mu = {MU_ASSUMED} (ASSUMED; floor and pad friction not cited); it can only "
        f"tip if mu exceeds {mu_tip:.2f}. Sliding caps the tipping load, which helps, but a bay that slides moves zone lines",
        PLAUSIBLE, closed_by="D17 Proposed, awaiting Amish: accept sliding or add non-slip pads; T7 measures mu")
# BIFMA 5.2 impact: energy needed to tip the ballasted U backwards about the back wall base line
def lift(m, a, z):
    return m * G * (math.hypot(a, z) - z) / 1000
E_tip = lift(4 * m_duo, D_U / 2, 900) + lift(2 * BALLAST, D_U, 20) + lift(N_FEET_U * M_FOOT, D_U / 2, 20)
R["E_tip"] = E_tip
c.cited("P28", "The ballasted bay does not tip under the BIFMA X5.6 5.2 impact (22.7 kg bag, 610 mm horizontal swing)", "Physics", "Dynamics",
        "Energy to rotate the bay over its tipping line (raise of centres of mass) against the bag's energy",
        f"Tipping needs about {E_tip:.0f} J; the bag's energy depends on its pendulum length, which the report does not give (the reviewer's 34 J "
        "is not cited): to assess. Local damage to the struck leaf is not covered", PLAUSIBLE, closed_by="T7 impact case")
for v in (5.0, 10.0):
    qw = 0.5 * 1.225 * v ** 2
    R[f"wind_{v:.0f}"] = (qw, qw * 2.4 * 1.8 * 0.9)
Mrest = F_U5 * z_push / 1000
c.cited("P8", "The platform is for indoor use or use inside a tent", "Physics", "Fluid mechanics",
        "q = 0.5 rho v^2, Cp 1.0 ASSUMED, resultant at mid-height; no gust factor",
        f"10 m/s gives {R['wind_10'][0]:.0f} Pa and {R['wind_10'][1]:.0f} N m on a 2.4 x 1.8 m wall; the ballasted U restores {Mrest:.0f} N m, "
        "under 1.5 x the wind moment. Outdoor use fails; tent door gusts and fans are not checked", FIX,
        closed_by="D6 Proposed, awaiting Amish: indoor or in-tent only (stated limit L2)")

# ---------------------------------------------------------------------------------------------------------
# 5. Connector: through-peg bearing, demand band, peg shear, snap strain, forces
# ---------------------------------------------------------------------------------------------------------
HOLE_D, HOLE_E, PEG_D = 8.0, 12.5, 7.0
TAU_PP = SIGMA_Y / math.sqrt(3)
ts = s4["ts"]
e_clear = HOLE_E - HOLE_D / 2
near_only = PEG_D * ts * SIGMA_Y                                   # v0.1 peg: near skin only
F_bear = 2 * PEG_D * ts * SIGMA_Y                                  # v0.2 through-peg: both skins
F_tear = 2 * (2 * e_clear * ts * TAU_PP)
cap_peg = min(F_bear, F_tear)
cap_clip = 2 * cap_peg
# demand band per panel edge: (a) the v0.1 estimate T = P L/(4 delta) at 165 mm; (b) a string with edges held in-plane
T_a = P_PUSH * 1200 / (4 * 165.0)
EA = E_EFF * 2 * ts * 600                                          # ASSUMED effective width 600 mm
delta_m = 600 * (P_PUSH / (8 * EA)) ** (1 / 3)
T_b = P_PUSH * 600 / (4 * delta_m)
R["connector"] = dict(near_only=near_only, F_bear=F_bear, F_tear=F_tear, cap_peg=cap_peg, cap_clip=cap_clip, T_a=T_a, T_b=T_b,
                      delta_m=delta_m, ts=ts)
c.cited("P9", "Clips hold the panel edges under the 178 N BIFMA push (no separation)", "Engineering and technology", "Joint design",
        "Bearing d t sigma_y per skin, tear-out 2 e t tau; demand from a bowed leaf as a string T = P L / (4 delta)",
        f"v0.1 peg (3.7 mm) reached the near skin only: {near_only:.0f} N per peg, refuted. v0.2 through-peg (fix F8) bears on both skins: "
        f"{cap_peg:.0f} N per peg, {cap_clip:.0f} N per clip. Demand is not bounded on paper: {T_a / 2:.0f} N per clip if two of three clips "
        f"share the v0.1 estimate ({T_a:.0f} N per edge, delta 165 mm is a BIFMA stop, not a sag), up to {T_b:.0f} N per edge if the leaf "
        f"acts as a string with held edges (delta {delta_m:.0f} mm). Thin FR skins may crumple before full bearing", FIX,
        closed_by="Fix F8 (through-peg); D14 Proposed, awaiting Amish: holding principle settled by T3 and T7")
c.claim("P10", "The PETG through-peg does not shear before the panel hole yields", "Engineering and technology", "Joint design",
        "Peg shear pi d^2 / 4 x 50.4 / sqrt 3 MPa (BCN3D), derated x 0.3 for layers across the peg (ASSUMED); the peg is printed with the tongue lying flat",
        value=0.3 * math.pi / 4 * PEG_D ** 2 * 50.4 / math.sqrt(3), limit=cap_peg, unit="N", rule="above")
L_arm, h_root, gap = 24.5, 1.5, 4.5
y_peg = gap + 1.0
K_ROOT = 2.0        # ASSUMED stress concentration at the tongue root with a 0.5 mm root radius (reviewer range 1.5 to 2.5)
eps = y_peg * h_root / (1.09 * L_arm ** 2)                        # Bayer tapered arm (to half thickness)
R["snap"] = dict(eps=eps, eps_root=K_ROOT * eps)
c.claim("P11", "The tapered snap tongue deflects by the full through-peg height (5.5 mm) below half the PETG strain at yield, root factor included",
        "Engineering and technology", "Snap-fit design",
        f"Bayer tapered arm eps = y h / (1.09 l^2), l 24.5 mm, h 1.5 to 0.75 mm, x {K_ROOT} at the root (ASSUMED). At rest the peg sits in its "
        "socket and the tongue is unstrained (no creep); slot gap 4.5 mm takes sheet of 3.8 to 4.2 mm (+-5 %)",
        value=K_ROOT * eps * 100, limit=5.9 / 2, unit="% strain", rule="below", margin=0.2,
        closed_by="Moulded PP strain limit to assess (D4); T3 cycles; print the tongue lying flat")
F_def = 14.0 * h_root ** 2 * 2020 * eps / (6 * L_arm)
mu = 0.30 * 1.5
F_ins = F_def * (mu + 1) / (1 - mu)
R["snap"].update(F_def=F_def, F_ins=F_ins)
c.cited("P12", "Clipping and release are tool-free with gloved hands: push the panel home; release with two fingertips on the two lips while the other hand pulls",
        "Biology", "Human factors",
        "Bayer: P = b h^2 E eps / (6 l); insertion over a 45 deg ramp that covers the whole peg height, P (mu + 1)/(1 - mu), mu 0.45 (PP on PP x 1.5)",
        f"Deflection {F_def:.1f} N per tongue; insertion about {2 * F_ins:.0f} N per slot pushed through the panel edge; release {F_def:.1f} N "
        "per lip over 5.5 mm. The v0.1 peg (1.2 mm lead-in on a 3.7 mm peg) could not cam and was refuted; no cited hand-force limit is used, "
        "and the two-handed method is stated", PLAUSIBLE, closed_by="Fix F9 (full-height ramp); T5 with gloved users")

# ---------------------------------------------------------------------------------------------------------
# 6. Hinge
# ---------------------------------------------------------------------------------------------------------
R_fold = 4.0 - ts / 2                                  # skin radius when two leaves close back to back
need_w = math.pi * R_fold
W_GROOVE = 4 * 3.4
eps_h = ts / (2 * R_fold)
eps_h2 = ts / (2 * W_GROOVE / (math.pi / 2))
R["hinge"] = dict(R=R_fold, need_w=need_w, w=W_GROOVE, eps=eps_h, eps_90=eps_h2)
c.cited("P13", "The flat-bottomed fold groove (front skin only) folds 180 deg for flat-pack and +-90 deg either way in use",
        "Engineering and technology", "Hinge strain",
        "Back to back the skin wraps a radius R = t - t_s/2 and needs pi R of free skin; strain t_s/(2R)",
        f"R {R_fold:.2f} mm needs {need_w:.1f} mm of free skin: the v0.1 groove (10.2 mm) stopped at about 150 deg; v0.2 groove {W_GROOVE:.1f} mm "
        f"(4 pitches, flat-bottomed) gives {eps_h * 100:.1f} % at 180 deg and {eps_h2 * 100:.1f} % at 90 deg the other way. Raw PP elongation "
        "at yield is 11 % (Akyplac); FR fillers and cross orientation lower it: to assess. Routing depth tolerance to assess", PLAUSIBLE,
        closed_by="Fix F3 (groove 4 pitches, flat bottom, two-way); T2 at 5, 23 and 50 C")
c.cited("P14", "Folds and clip joints survive 50 to 100 deployment cycles with at least 80 % of their first retention", "Engineering and technology", "Fatigue",
        "Low-cycle fatigue of PP and PETG at the strains of P11 and P13; hole wear in a 0.26 mm skin",
        f"Hinge {eps_h * 100:.1f} % per fold, tongue {K_ROOT * eps * 100:.1f} % at the root per cycle; no data for scored FR twinwall or printed "
        "PETG tongues; holes ovalise with each cycle; the 80 % retention target is ASSUMED: to assess", PLAUSIBLE,
        closed_by="T2 and T3 (with hole wear and retention per cycle) at TRL 4")

# ---------------------------------------------------------------------------------------------------------
# 7. Sheet, mass, pack, carry
# ---------------------------------------------------------------------------------------------------------
SW, SL = 48 * 25.4, 96 * 25.4
trim_w = (SW - 1200) / 2
trim_min = trim_w - 3.2 / 2
yields = {"48 x 96 in: P18 duo + H06": (1.2 * 1.8 + 1.2 * 0.6) / (SW * SL * 1e-6),
          "48 x 96 in: two P12 duos": (2 * 1.2 * 1.2) / (SW * SL * 1e-6),
          "2000 x 3000: P18 + P12 duos, L18 + L12 leaves": (1.2 * 1.79 + 1.2 * 1.19 + 0.6 * 1.79 + 0.6 * 1.19) / 6.0}
R["yield"], R["trim"] = yields, (trim_w, trim_min)
c.claim("P15", "Standard modules cut from a 48 x 96 in (1219.2 x 2438.4 mm) sheet with under 5 % waste", "Mathematics", "Geometry",
        f"Area of modules / sheet area; width trim {trim_w:.1f} mm per side nominal, about {trim_min:.1f} mm after the -1/8 in width tolerance; "
        "squareness is set by cutting to a square datum, not by the trim",
        value=yields["48 x 96 in: P18 duo + H06"] * 100, limit=95.0, unit="% yield", rule="above")
c.claim("P16", "One person carries a folded P18 duo under the arm, held horizontal", "Biology", "Human factors",
        "Mass against the NIOSH load constant (23 kg) as a ceiling only: NIOSH is a two-handed lifting method; a 1.8 m fold cannot be "
        "carried hanging from one hand (its end would reach the floor); wind area 1.08 m2 outdoors",
        value=m_duo, limit=23.0, unit="kg", rule="below")
pack = 6 * m_duo + N_FEET_U * M_FOOT + N_CLIPS_U * M_CLIP + 1.0
R["pack"] = dict(total=pack, duos=6 * m_duo, feet=N_FEET_U * M_FOOT, clips=N_CLIPS_U * M_CLIP, bags=1.0)
light = 6 * m_duo + N_FEET_U * 0.15 + N_CLIPS_U * 0.04 + 1.0
R["pack_light"] = light
c.cited("P17", "A 12 kg two-bag pack (FlexTriage deck target) holds a 2.3 x 2.3 m zigzag U bay of P18 duos", "Mathematics", "Mass budget",
        "Sum of panel, foot, clip and bag masses (ballast filled on site)",
        f"6 duos {6 * m_duo:.2f} kg + {N_FEET_U} feet {N_FEET_U * M_FOOT:.2f} kg + {N_CLIPS_U} clips {N_CLIPS_U * M_CLIP:.2f} kg + bags 1.0 kg "
        f"= {pack:.1f} kg, {100 * (pack / 12 - 1):.0f} % over 12 kg (the v0.1 row counted 6 feet and read Plausible: refuted). Cored feet of "
        f"0.15 kg and clips of 0.04 kg (ASSUMED targets) would give {light:.1f} kg", FIX,
        closed_by="D15 Proposed, awaiting Amish: pack target, bag count or lighter moulded feet and clips")
pack_duo = 0.6 * 1.8 * (2 * 4.0 + 2.0)
R["pack_duo_L"] = pack_duo

# ---------------------------------------------------------------------------------------------------------
# 8. Disinfection, print, cleanability
# ---------------------------------------------------------------------------------------------------------
c.cited("P18", "PP sheet tolerates 0.5 % sodium hypochlorite, 70 % alcohol and 3 to 7.5 % hydrogen peroxide at the label contact time",
        "Chemistry", "Polymer chemical resistance",
        "CP Lab: NaOCl < 20 % A, ethanol A, isopropyl A2 (satisfactory to 48 C), H2O2 10 % A; INEOS: NaOCl conc. S at 21 C, O at 60 C; H2O2 30 % S/O",
        "Resin immersion data only: the Akyplac sheet itself says PP is not resistant to oxidising substances, and oxidisers attack UV "
        "stabilisers; the FR additive, print and tent temperatures of 40 to 50 C are not covered", PLAUSIBLE,
        closed_by="T4 at 23 and 45 C with 0.5 % NaOCl, 70 % alcohol, a named quat and accelerated H2O2 at label contact times")
c.cited("P19", "PP sheet tolerates quaternary ammonium disinfectants", "Chemistry", "Polymer chemical resistance",
        "Neither chart lists quats; CP Lab rates detergents A", "Uncited: to assess with a named quat product's maker list", PLAUSIBLE,
        closed_by="T4")
c.cited("P20", "PETG prototype clips tolerate 0.5 % sodium hypochlorite, 70 % isopropanol and 3 to 5 % hydrogen peroxide", "Chemistry",
        "Polymer chemical resistance",
        "Curbell (Vivak, flat unstressed sheet): diluted bleach (5 tablespoons per gallon, about 2 % household bleach, 0.10 to 0.16 % NaOCl), "
        "IPA 70 %, H2O2 3 to 5 % compatible; quats not listed",
        "0.5 % NaOCl is about 3 to 5 times the tested strength and printed parts trap fluid between layers: to assess. The v0.2 tongue is "
        "unstrained at rest, which lowers the stress-cracking risk", PLAUSIBLE, closed_by="T4 on printed clips; moulded PP clips at scale fall under P18")
c.cited("P21", "Printed pictograms stay legible after repeated disinfectant wipes", "Chemistry", "Coatings",
        "No wipe data for UV inks on twinwall; Fujifilm Uvijet KX lists Coroplast as variable, full resistance 24 h after cure",
        "To assess (no evidence either way). Proposed protection: clear PP overlaminate (D3)", PLAUSIBLE,
        closed_by="T4: 120 wipes, 30 min dry per agent, legibility scored")
c.cited("P22", "Sealed panel edges, fold grooves and clip holes can be wiped clean between uses", "Biology", "Infection prevention practice",
        "Open flute ends, cut edges parallel to the flutes (open half-flute troughs), the open back-face groove and clip slots are crevices",
        "Fixed by rule E1 v0.2 (every cut edge heat-sealed, including the two groove shoulders and the groove ends; hot-punched fused holes), "
        "rule E2 (groove face away from care zones or covered by a flexible PP strip) and rule E3 (clips come off for cleaning); seal "
        "integrity unproven", PLAUSIBLE, closed_by="Fix F4 (rules E1 to E3); T6 dye ingress after T4")

# ---------------------------------------------------------------------------------------------------------
# 9. Fire
# ---------------------------------------------------------------------------------------------------------
HC = 39.7
R["fire"] = dict(per_m2=0.7 * HC, per_duo=m_duo * HC, U_bay=6 * m_duo * HC)
c.cited("P23", "Twinwall panels are combustible and add fire load to a care space; the FR grade does not reduce that fire load", "Chemistry", "Combustion",
        "Heat of combustion 39.7 MJ/kg (FSRI PP)",
        f"{0.7 * HC:.1f} MJ/m2; {m_duo * HC:.0f} MJ per P18 duo; {6 * m_duo * HC:.0f} MJ per six-duo U bay. FR delays ignition and spread; "
        "PP still melts and drips (P39)", WITHIN, closed_by="Rule FR1: FR grade only near people")
c.claim("P24", "The platform FR grade is bought at a measured lot areal density of at most 700 g/m2 (NFPA 701 TM1 scope)", "Engineering and technology",
        "Fire testing", "NFPA 701 TM1 applies to areal density <= 700 g/m2 (IntePro); grammage tolerance +-5 to +-10 %, so the nominal is at most "
        "about 665 g/m2 and the lot is weighed",
        value=700, limit=700, unit="g/m2 (lot maximum)", rule="below",
        closed_by="Fix F5 v0.2 (lot maximum, not nominal); D18 Proposed, awaiting Amish: benchmark hierarchy (NFPA 286 or ASTM E84 first, NFPA 701 second)")
c.cited("P25", "An FR twinwall grade can reach a European reaction-to-fire class (EN 13501-1)", "Engineering and technology", "Fire testing",
        "UK FR boards cite LPS 1207 only", "No twinwall classification found; the FR solid film report (B-s2,d0 on a metal frame with an air gap) is a "
        "different product and mounting and is not evidence: to assess", PLAUSIBLE, closed_by="D2: target class set by Amish after supplier quotes")

# ---------------------------------------------------------------------------------------------------------
# 10. Colour
# ---------------------------------------------------------------------------------------------------------
c.cited("P26", "Zone colours are read correctly by staff with red-green colour vision deficiency", "Biology", "Human vision",
        "Red-green deficiency about 1 in 12 men and 1 in 200 women of Northern European ancestry (MedlinePlus)",
        "Colour alone fails; fixed by rule C1 (text, shape and pattern with every colour); legibility unproven", PLAUSIBLE,
        closed_by="Fix F6 (rule C1); T5 with colour-deficient observers")

# ---------------------------------------------------------------------------------------------------------
# 11. Claims the v0.1 check missed (independent review, 2026-11-12)
# ---------------------------------------------------------------------------------------------------------
c.cited("P29", "Panels, folds and clips keep their function at 40 to 50 C inside a tent", "Physics", "Polymer creep",
        f"Akyplac HDT 50 C at 1.8 MPa and 92 C at 0.45 MPa; PETG HDT 70 C (BCN3D); stiffness x {HOT} ASSUMED hot with creep",
        f"Hot: flat P12 margin {m12_hot:.2f} (rule S1 covers it), leaf margin {s4['leaf_margin_hot']:.1f}, U bay tip unchanged (weight, not "
        "stiffness); fold set angles may relax; PETG clips stay below their HDT but near it in sun", PLAUSIBLE, closed_by="T1, T2, T7 at 50 C")
c.cited("P30", "Folds and clips do not crack in cold use (5 C and below)", "Physics", "Fracture",
        "Akyplac Izod (ISO 180) 15 kJ/m2 at 23 C, 7 kJ/m2 at -20 C", "Toughness halves by -20 C; no data at 5 C for scored skins or printed tongues: "
        "to assess; platform use below 5 C is not claimed", PLAUSIBLE, closed_by="T2 and T3 at 5 C")
dL = 0.11 * 2.4 * 30
dth = math.degrees(dL / (4 * 600 * math.sin(math.radians(15))))
c.cited("P31", "Thermal expansion of a 2.4 m wall is taken up without bowing off its feet", "Physics", "Thermal expansion",
        "Akyprint 0.11 mm/(m C); zigzag wall with leaves at 15 deg", f"{dL:.1f} mm over a 30 C swing on 2.4 m; the zigzag takes it with a fold angle "
        f"change of about {dth:.1f} deg; slot clearance 0.15 to 0.35 mm per side does not need to", WITHIN, closed_by="Rule S1 (zigzag walls)")
c.cited("P32", "Panels keep their properties over a stated service life", "Chemistry", "Weathering",
        "Akyprint 'UV treatment internal 18 months'; Interprofile outdoor grade 2,500 h SAE J1960, about 1 year in Miami",
        "Indoor use only (L2); no service life is claimed; sunlit tent walls and the effect of brominated FR on UV stabilisers: to assess",
        PLAUSIBLE, closed_by="D6; supplier data for the FR plus UV grade")
c.cited("P33", "Static charge on PP panels is acceptable near medical electronics and oxygen use", "Physics", "Electrostatics",
        "Akyplac: anti-static on request; Interprofile antistatic grade 1e9 to 1e12 ohm/sq", "Standard PP is highly insulating; dust pick-up and "
        "discharge near oxygen-enriched areas: to assess with the site; anti-static FR availability to assess", PLAUSIBLE,
        closed_by="Site review; supplier data")
c.cited("P34", "Edges, grooves and folds do not cut or pinch fingers", "Biology", "Human factors",
        "Sealed (fused) edges; 0.26 mm skins at routed shoulders; folds close fully only when packing", "Sealed edges are rounded; routed shoulders "
        "are sealed by rule E1; pinch at a closing fold only during packing (hands on the leaf faces). Sharp-edge test (UL 1439 type) planned",
        PLAUSIBLE, closed_by="T5 sharp-edge and pinch check")
c.claim("P35", "Sheet of 3.8 to 4.2 mm (+-5 %) fits the 4.5 mm clip slot and the through-peg engages at both extremes", "Engineering and technology",
        "Tolerances", "Slot gap 4.5 mm; peg passes both skins into a 1.0 mm socket whatever the sheet position", value=4.2, limit=4.5,
        unit="mm sheet vs slot", rule="below", closed_by="Fix F8 (CLEAR 0.5 mm)")
c.cited("P36", "Zone colours and safety signs do not conflict", "Biology", "Human vision",
        "ISO 3864-1 reserves red, yellow, blue and green for safety meanings; START triage uses red, yellow, green and black (CHEMM)",
        "Triage red and green collide with fire-equipment red and safe-condition green in one bay. Fixed by rule C6 (triage colours only as "
        "zone bands carrying the category word, never as sign backgrounds; safety signs keep ISO shapes and borders). ISO 3864-4 colour values "
        "and the sign-size distance factor are not yet read from the standards (the reviewer's z = 60 is unverified): to assess",
        PLAUSIBLE, closed_by="Fix F10 (rule C6); D16 Proposed, awaiting Amish: buy ISO 3864-1 and -4")
c.cited("P37", "Smoke from FR panels is no worse than the platform accepts for patient spaces", "Chemistry", "Combustion products",
        "Coroplast Firewall SDS: brominated FR < 5 %, antimony trioxide < 3 %; smoke includes hydrogen bromide and antimony oxides; IARC: "
        "antimony trioxide Group 2B (1989), trivalent antimony Group 2A (volume 131)",
        "Corrosive and toxic smoke products are certain; their size relative to plain PP smoke is not quantified: to assess", PLAUSIBLE,
        closed_by="D11 Proposed, awaiting Amish: halogen-free FR search")
c.cited("P38", "The FR grade does not shed burning drips", "Engineering and technology", "Fire testing",
        "NFPA 701 TM1 pass criterion includes average flaming drip under 2 s (IntePro); EN 13501-1 d-class not found for twinwall",
        "Supplier pass reports cover the NFPA criterion only; d-class and drip in a room-corner test (NFPA 286): to assess", PLAUSIBLE,
        closed_by="T8; D18")
c.cited("P39", "Ballast bags do not create a slip or lifting hazard", "Biology", "Human factors",
        "A 5 kg bag is far under the NIOSH load constant (23 kg); water bags can leak onto clinical floors",
        "Fixed by rule B1: sand or gravel in a sealed bag inside the foot tray; water only double-bagged in a lipped tray", WITHIN,
        closed_by="Fix F11 (rule B1)")
c.cited("P40", "Mixed P12 and P18 panels share joints", "Mathematics", "Geometry", "Shared clip grid",
        "v0.1 heights (150, H/2, H - 150) gave no common middle clip; v0.2 grid 150 and 1050 for P12, plus 1650 for P18, shares two of three",
        WITHIN, closed_by="Fix F12 (clip_heights v0.2)")

state = c.write()

if __name__ == "__main__":
    print(f"E_eff {E_EFF:.0f} MPa; calibration EI_MD/EI_CD: " + ", ".join(f"{n}: {v[0]:,.0f}/{v[1]:,.0f}" for n, v in EI_meas.items()))
    print("grade | ts | EI_MD | EI_CD | flat allowed cold/hot | leaf margin cold/hot | defl 178 N | P for 25 mm | kg/m2")
    for n, s in SEC.items():
        print(f"{n:12s} | {s['ts']:.2f} | {s['ei_md']:8,.0f} | {s['ei_cd']:7,.0f} | {s['h_allow_flat']:5.0f}/{s['h_allow_hot']:5.0f} | "
              f"{s['leaf_margin']:5.1f}/{s['leaf_margin_hot']:4.1f} | {s['defl_plate_178']:5.0f} | {s['P_allow_plate']:5.1f} | {s['gsm'] / 1000:.2f}")
    t = R["tip"]
    print(f"tip: single duo {t['single']:.1f} N (ballast {t['ballast_single']:.0f} kg per foot); U {t['U']:.0f} N, with 5 kg {t['U5']:.0f} N, "
          f"needs {t['U_ballast']:.1f} kg; bay mass {t['M_U']:.1f} kg; slide {R['slide']['F']:.0f} N at mu 0.25, tip needs mu > {R['slide']['mu_tip']:.2f}; E_tip {R['E_tip']:.0f} J")
    k = R["connector"]
    print(f"connector: near skin only {k['near_only']:.0f} N/peg; through-peg bearing {k['F_bear']:.0f}, tear-out {k['F_tear']:.0f}, per clip "
          f"{k['cap_clip']:.0f} N; demand {k['T_a']:.0f} to {k['T_b']:.0f} N per edge (string sag {k['delta_m']:.0f} mm)")
    sn = R["snap"]
    print(f"snap: eps {sn['eps'] * 100:.2f} % (root {sn['eps_root'] * 100:.2f} %), deflection {sn['F_def']:.1f} N, insertion {sn['F_ins']:.1f} N per tongue")
    h = R["hinge"]
    print(f"hinge: R {h['R']:.2f} mm, free skin needed {h['need_w']:.1f} mm, groove {h['w']:.1f} mm, strain {h['eps'] * 100:.1f} % (90 deg other way {h['eps_90'] * 100:.1f} %)")
    print("yield: " + "; ".join(f"{k}: {v * 100:.1f} %" for k, v in R["yield"].items()) + f"; trim {R['trim'][0]:.1f} / {R['trim'][1]:.1f} mm")
    print(f"pack: {R['pack']}; light {R['pack_light']:.1f} kg; duo {m_duo:.2f} kg, {R['pack_duo_L']:.1f} L; fire {R['fire']}")
    print(f"P12 flat margin cold/hot {R['p12_flat_margin'][0]:.2f}/{R['p12_flat_margin'][1]:.2f}; wind 10 m/s {R['wind_10']}; top margin {1829 - top:.1f} mm")
