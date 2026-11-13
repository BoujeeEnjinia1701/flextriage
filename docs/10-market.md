---
doc_id: FXT-MKT-001
title: FlexTriage Origami Bay market and viability
project: FlexTriage Origami Bay
doc_type: Market and viability
version: "0.2"
status: Draft
date: 2026-11-12
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-12
    author: Amish Chadha
    change: First market and viability note with cited benchmark prices
  - version: "0.2"
    date: 2026-11-12
    author: Amish Chadha
    change: Costs restated after the v0.2 parts changes (BOM USD 1,174.23)
---

# FlexTriage Origami Bay market and viability

A three-zone origami bay costs about USD 1,174 in parts at prototype quantities, about USD 23.48 a deployment over 50 deployments. The nearest commercial ways to mark out triage zones are crowd-control stanchions (cheap per post but heavy, with no screen) and pipe and drape (privacy, but heavier and dearer per bay). The bay's niche is emergency medical teams and clinics that need a fast, wipeable, clearly signed one-way flow and can carry about 42 kg. Prices are cited with the date checked; none is a quote.

Table 1. Market segments and benchmarks.

| Segment | Target users and region | Competitive benchmark (cited price, checked 2026-11-12) | Estimated cost per bay (USD) | Value proposition |
| --- | --- | --- | --- | --- |
| Emergency medical teams and field hospitals | EMT logisticians, worldwide | Retractable-belt stanchions: Uline H-3736BL, USD 54.50 each at 5 or more, 42 lb ([Uline](https://www.uline.com/Product/Detail/H-3736BL/Crowd-Control/Uline-Black-Crowd-Control-Posts-with-Retractable-Belt-Black-10)); Global Industrial 40 in post, USD 44.95 on clearance ([Global Industrial](https://www.globalindustrial.com/p/crowd-control-stanchion-40-in-black-post-blue-belt-7-1-2-ft-l)) | 1,174.23 (FT1); 844 to 1,198 for an FT3 stanchion bay | Continuous, printed, wipeable walls with doorways and one-way leaves, about a sixth of the mass of steel stanchions |
| Clinics adding an outbreak triage area | Clinic managers, IPC leads | Water-fillable stanchion, Montour, USD 79.79 ([Zoro](https://www.zoro.com/montour-line-stanchion-belt-barrier-waterfillable-base-yellow-post-11ftblkrd-belt-p400wf-yw-brd-110/i/G401030986)); floor marking tape 2 in x 108 ft, USD 10.25 ([Zoro](https://www.zoro.com/global-industrial-floor-marking-tape-vinyl-yellow-2-in-w-x-108-ft-l-670651yl/i/G111892461)) | 1,174.23 | Defined zones and signs in one kit; tape grafted on for the path (D1) |
| Privacy at assessment and treatment | Clinics, shelters | Medline foldable FR vinyl privacy screen, 3 panels, 69 x 87 in, USD 210.79 ([Staples](https://www.staples.com/medline-foldable-flame-retardant-vinyl-privacy-screen-with-casters-3-panel-69-x-87in-mds80450/product_829862)); pipe and drape kit 8 ft x 10 ft, USD 179.99 ([Urquid Linen](https://www.urquidlinen.com/products/pipe-and-drape-kit-8-tall-x-10-wide)) with IFR drape panels ([Urquid Linen](https://www.urquidlinen.com/products/ifr-poly-knit-drapery-panels-118-wide-2-colors)) | About 2,060 for an FT2 screen bay at commercial prices | FT1 gives no privacy to a standing adult; a P18 privacy screen at the beds is D3 |

Table 2. Cost per deployment (FXT-CAL-001 section 11).

| Item | FT1 origami bay | FT3 stanchion bay | FT2 screen bay |
| --- | --- | --- | --- |
| First cost (USD) | 1,174.23 | 844 to 1,198 | About 2,060 |
| Mass (kg) | 41.6 | About 267 (steel posts) | 54 to 65 |
| Over 50 deployments (USD each) | 23.48 | 17 to 24 | About 41 |
| Over 100 deployments (USD each) | 11.74 | 8 to 12 | About 21 |
| Interior area (USD per m2) | 61.2 | n/a (open plan) | n/a |

## Open route

Open hardware under CERN-OHL-P-2.0: anyone may make and sell the bay. Who would build it: sign shops (FR twinwall cutting and printing is their daily work), makerspaces and print farms for the clips and feet, and emergency medical team logistics bases that keep bays in stock. Where the cost falls: FR sheet bought by the pallet (USD 34.99 against 44.99 a sheet, about USD 120 a bay), freight shared across bays, and moulded clips and feet once the design is frozen (D6). The platform shares clips, feet and sheet with FlexClean and FlexSleep, so a stock of parts serves all three.

## Sources

All checked 2026-11-12: Uline H-3736BL; Global Industrial 40 in stanchion; Montour water-fillable stanchion and Global Industrial floor tape on Zoro; Medline privacy screen on Staples; Urquid Linen pipe and drape kit and IFR drape; cplast.net 48964WFR FR sheet; MatterHackers PETG; K&J Magnetics D82; Walmart ABCCANOPY sand bags (links in `bom/bom.csv` and FXT-STM-001).

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
