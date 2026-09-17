# User Requirement Specification

## 2.1 User Requirements

NRM requires a system capable of processing pectoral flipper radiographs to automatically identify and segment three clinically relevant bones (the metacarpal, phalange M1, and phalange M2), and quantify each bone's cross-sectional area with sub-millimeter precision, calibrated against the scale reference present in each individual image. The system must support a human-in-the-loop review and correction workflow, allowing a qualified operator to verify and adjust generated measurements prior to approval, before the finalized data is exported and integrated into NRM's existing Excel-based record-keeping system. Age estimation itself remains outside the system's scope, it is performed independently by NRM using the area and fusion status values this tool outputs.

## 2.2 System Requirements

### Summary table

| ID | Requirement | Priority |
|----|-------------|----------|
| FR1 | Identify metacarpal, phalange M1, phalange M2 | Must |
| FR2 | Exclude radius, ulna, claws, navicular bones, other non-target structures | Must |
| FR3 | Detect overlapping bones | Must |
| FR4 | Correctly split area on overlap (no double counting) | Must |
| FR5 | Auto-propose a measurement before review | Must |
| FR6 | Allow manual correction of the boundary | Must |
| FR7 | Detect fusion / non-fusion, record as its own field | Should |
| FR8 | Exclude the gap in an unfused bone from area | Should |
| FR9 | Accept and process a batch of images | Should |
| FR10 | Step through processed images one at a time | Should |
| FR11 | Report area in mm to 3 decimals using the image's own scale | Must |
| FR12 | Export approved measurements to Excel | Must |
| FR13 | Map values to predefined Excel columns | Should |
| FR14 | Add new data without overwriting existing Excel data | Desirable |
| NFR1 | Accuracy vs. manual measurement | TBD — blocked on ground truth |
| NFR2 | Speed per image | TBD — blocked on hardware/GPU decision |
| NFR3 | Robustness on bad input (no scale marker, rotated image) | Target: flag, don't guess |
| NFR4 | Reviewer can act on one image in a small, fixed number of steps | — |
| NFR5 | Runs on whatever stack the team locks in (Technical Components, still TBD) | — |
| NFR6 | Export never corrupts or drops existing Excel rows/columns | — |

### Functional requirements, written out

**FR1 (Must).** The system shall identify and segment the metacarpal, phalange M1, and phalange M2 in a given flipper radiograph.

**FR2 (Must).** The system shall exclude radius, ulna, claws, navicular bones, and other non-target structures from the segmentation output.

**FR3 (Must).** The system shall detect when two or more relevant bones overlap in the image.

**FR4 (Must).** When bones overlap, the system shall assign each pixel/region to the correct bone and shall not count overlapping regions twice or attribute them to the wrong bone.

**FR5 (Must).** The system shall automatically generate a proposed area measurement for each identified bone before any human review.

**FR6 (Must).** The system shall let the reviewer manually adjust the proposed bone boundary, and shall recompute the area from the corrected boundary.

**FR7 (Should).** The system shall classify each relevant bone as fused or not fused, and shall record fusion status as a separate output field from the area measurement.

**FR8 (Should).** When a bone is not fused, the system shall exclude the gap between the unfused parts from the area calculation.

**FR9 (Should).** The system shall accept a batch of radiographs in one upload and process them sequentially without requiring re-upload per image.

**FR10 (Should).** The system shall let the reviewer step through processed images one at a time, in sequence, without leaving the review screen.

**FR11 (Must).** The system shall report each bone's area in mm, to 3 decimal places, using the scale reference present in that specific image (not a fixed pixel-to-mm ratio).

**FR12 (Must).** The system shall export approved measurements to an Excel-compatible file.

**FR13 (Should).** The system shall map each exported value to the correct predefined column in NRM's existing Excel template.

**FR14 (Desirable).** The system shall add new measurements to an existing NRM Excel file without deleting or overwriting the data already in it.

### Non-functional requirements, written out

**NFR1 — Accuracy.** Measured bone area shall be within [TBD, needs a target once we have ground truth to compare against] of a manual measurement on the same image. Owner: Validation, blocked on NRM providing labeled/verified images. 

**NFR2 — Speed.** The system shall produce a proposed measurement for one radiograph within [TBD] seconds of upload, so batch review stays practical for NRM's ~80+ image set.

**NFR3 — Robustness.** The system shall not fail silently on irregular input, for example an image with no visible scale marker (we already found one, B202600073_KS) or a rotated/uncropped image. It should flag these for manual attention instead of producing a false measurement.

**NFR4 — Usability.** A reviewer shall be able to accept, correct, or reject one image's measurement in a small, fixed number of actions, so reviewing a full batch doesn't become the bottleneck.

**NFR5 — Portability.** The system shall run on whatever environment the team locks in under Technical Components (still TBD) without requiring NRM to install specialized hardware or software beyond that.

**NFR6 — Data integrity.** The export step (FR12–FR14) shall never corrupt or drop existing rows/columns in NRM's Excel file.

### Open items 

- NFR1 and NFR2 need real numbers — depends on what ground truth/labels NRM sends back and what hardware/GPU the team decides to use.
  
- Needs the approval + corrections pass with Linnea/Elsa per the team's own timeline (item 1d in Flippers.pdf).
