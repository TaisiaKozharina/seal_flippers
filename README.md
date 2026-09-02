# Seal Flipper Radiograph Image Analysis

![Seal waving its flipper](http://images.stockcake.com/public/d/c/d/dcd6c96e-dfde-40f6-a964-00384a609c69_medium/seal-waves-hello-stockcake.jpg)

## Overview

This project aims to develop an image-analysis system for estimating seal age from pectoral flipper radiography. The project is carried out in collaboration with the **Museum X** and focuses on:

- Grey seal (*Halichoerus grypus*)
- Harbour seal (*Phoca vitulina*)
- Ringed seal (*Pusa hispida*)

The system will automatically identify, segment, and measure relevant bones while allowing a human operator to review and correct the results.

## Objectives

The model should be able to:

- Identify and segment **metacarpal bones, Phalange M1, and Phalange M2**.
- Exclude irrelevant structures such as the radius, ulna, claws, and navicular bones.
- Handle overlapping bones and secondary ossification centres.
- Detect bone fusion/non-fusion where technically feasible.
- Calculate bone area using the radiograph's spatial scale.
- Report measurements in **mm² to 3 decimal places**.
- Allow manual correction and approval of measurements.
- Process radiographs in batches.
- Export approved results to an Excel-compatible format.

## Workflow (approximate)

```text
Data
    ↓
Preprocessing
    ↓
Bone detection and/or segmentation
    ↓
Area measurement
    ↓
Human review & correction
    ↓
Approved measurements
    ↓
Export
```

The system is intended as a **human-in-the-loop tool**. Automatically generated measurements must be reviewable and correctable by the user.

## Dataset

Currently **80+ radiographs** are available. Some images contain two flippers and may be cropped during preprocessing. The dataset contains different scale configurations, which will be defined with Museum X staff.
Raw radiographs and other restricted project data should **not be committed to the repository** unless explicitly permitted.


## Evaluation

Performance will be assessed using both image-segmentation and measurement metrics, including:

- Some metric 1
- Some metric 2
- Some metric 3

The final goal is not only accurate segmentation, but **accurate and reproducible bone-area measurements**.

## Repository Structure

```text
├── data/          # Local/project data
├── src/           # Image processing and ML
├── who/           # User interface
├── knows/     # Experiments
├── lorem/         # Tests
└── ipsum/          # Methodology and annotation guidelines
```

## Status

**🚧 Early development**

The model, annotation methodology, and application architecture are currently being developed.
