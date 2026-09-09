Meeting Notes from 07.09.2026 (Welcome Meeting)

*Security*: 
* Referring to the additional datasets (different animals) that can be provided - some datasets are private and may not be granted to us.
* Code is OK to be public
* Raw data should not be published

*Seal Dataset*: 
* ~85 samples containing ~100 instances (some images have 2 flippers)
* No labels, only measurements! Labels were promised, but no guarantee to quantity and time of delivery.
* Three seal species distribution in the dataset: >30 grey, >20 harbour, few ringed seal.
* Anatomically species are similar, size might be different.
* Dataset is not uniform. Samples vary in intensity, scale, resolution, number of samples per image.

*Accuracy & Scale*:
* Coin is used for scale, but it should be made possible for the scale to be defined by user.
* 3 decimals are just format, not precision
* In manual measurements precision of up to square centimeter was OK (due to hard cases mostly).
* Scale is square millimeters
* Regarding "rapid" and "quick": no exact threshold, just not several minutes. As fast as possible but in general should be reasonably faster than a human performing same task.

*Overlaps & Fusion*:
* Fusion occurs on the image as partially or completely 3 categories: fused, not fused, partially.
* Overlaps are not critical as long as model manages to recognize them properly and it doesn't affect the bone measurements significantly.
* Fusion should be flagged on the image (not only binary flag but also localized)
* Fusion examples will be gathered - expected to receive by undetermined date

*Application (functional requirements)*:
* Output is the 1) segmentation map, 2) Measurements of bones in the required format matching Excel OR directly added to Excel
* Target device: tablet. Client wants to access it via web and be able to pause and continue work from other device if needed (use case: samples are initially skimmed from PC, then annotations are edited on a tabled with pen)
* Application should be integratable for museum servers (long term plan: add this app for museum's application catalogue, or otherwise make it accessible for larger groups)
* Application should either 1) connect to online version of the Excel sheet containing the dataset metrics or 2) take CSV-like local file and append new measurements. Copy-paste solution is not encouraged.
* Application should provide a way to manually edit the annotations (output of the model) and save the result - metrics adjusted accordingly. Citing "we want to click on the bone and manually adjust its borders".
* As example of the above-described editing functionality "Image J" was mentioned, but as noted by specialists it doesn't work with overlaps well. Some sort of smart "MS Paint".
  
*Organisational*:
* Client prefers to have access to the progress sheet and have meetings ad-hoc if consulting is needed.
* Developer team meetings will be held bi-weekly with weekly check-ins for progress report formation.

