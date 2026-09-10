*Requirement Specification — Seal Flipper Age Tool*

*Problem:*
- NRM currently measures flipper bones by hand using ImageJ. It's slow and ImageJ doesn't handle overlapping bones well. We want to build a tool that speeds this up and handles overlap properly.

*Scope:*
- Bones needed: phalanges, metacarpal 1, metacarpal 2
- Also check for clavicular bone presence
- Other bones not required

*Functional requirements:*
- Identify relevant bones in the radiograph
- Measure bone area (not length/diameter - too much variation between individuals)
- Detect fusion status: fused, not fused, partially fused - and localize it, not just flag it
- Handle overlapping bones without messing up the measurement
- Report area in mm², 3 decimal format (this is a formatting requirement, not literal micron-level precision)
- Let the user click a bone and manually correct its boundary if needed
- Export approved measurements to Excel - either connect to their online sheet or output a CSV-like file, no copy-paste
- Support uploading and processing multiple images at once

*Non-functional requirements:*
- Should be faster than doing it by hand, not taking several minutes per image
- Needs to work on tablet and web, ideally usable on museum servers
- Should support switching devices mid-task (e.g. start on PC, continue on tablet)
- Dataset is not uniform - brightness, scale and resolution vary across the ~85 samples (~100 instances)

*Out of scope:*
- Calculating the seal's actual age (NRM does this separately using our measurements)
- Other animal datasets that are private

*Risk Assessment & Draft Strategies*

* Data Availability (No Labels): The dataset lacks ground-truth image masks, bottlenecking supervised learning.
  * *Draft Strategy:* (1) Test CV-based preprocessing (e.g., morphological operations) to generate pseudo-masks. (2) Manually annotate a small subset (e.g., via iPad) and validate with NRM experts to establish a baseline.
* Frontend Complexity (Interactive UI): Building a custom "Smart MS Paint" UI for manual boundary corrections from scratch is highly time-consuming.
  * *Draft Strategy:* Integrate existing touch-optimized web canvas libraries (e.g., Fabric.js) using HTML5 Pointer Events APIs to leverage native stylus inputs (like Apple Pencil).
* Data Integration (No Copy-Paste Rule): Direct API integration with museum servers may face strict IT security blocks.
  * *Draft Strategy:* Prepare a dual-path approach: Path A (Programmatic API or file ingestion to strictly avoid copy-paste) and Path B (A "Smart Clipboard" fallback that formats data with tab-separations `\t` for one-click error-free pasting, pending client approval).
