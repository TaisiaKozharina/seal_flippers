Requirement Specification — Seal Flipper Age Tool

*Problem:*
*NRM currently measures flipper bones by hand using ImageJ. It's slow and ImageJ doesn't handle overlapping bones well. We want to build a tool that speeds this up and handles overlap properly.

*Scope:*
- Bones needed: phalanges, metacarpal 1, metacarpal 2
- Also check for clavicular bone presence
- Other bones not required

Functional requirements:
- Identify relevant bones in the radiograph
- Measure bone area (not length/diameter - too much variation between individuals)
- Detect fusion status: fused, not fused, partially fused - and localize it, not just a flag
- Handle overlapping bones without messing up the measurement
- Report area in mm², 3 decimal format (this is a formatting requirement, not literal micron-level precision)
- Let the user click a bone and manually correct its boundary if needed
- Export approved measurements to Excel - either connect to their online sheet or output a CSV-like file, no copy-paste
- Support uploading and processing multiple images at once

Non-functional requirements:
- Should be faster than doing it by hand, not taking several minutes per image
- Needs to work on tablet and web, ideally usable on museum servers
- Should support switching devices mid-task (e.g. start on PC, continue on tablet)
- Dataset is not uniform - brightness, scale and resolution vary across the ~85 samples (~100 instances)

Out of scope:
- Calculating the seal's actual age (NRM does this separately using our measurements)
- Other animal datasets that are private
