# Technical Specification Draft; NRM Seal Flipper Tool

## System overview

The tool runs as one pipeline, from upload to Excel. A user checks and fixes every result before it is exported.

<img width="1344" height="650" alt="Image" src="https://github.com/user-attachments/assets/27162d3e-467a-485c-9fbb-35104ea6cfbe" />

The top row runs on NRM's computer by itself. The bottom row is where the user comes in: when they fix an outline on the iPad, the area is worked out again.

## Components

The tool has nine parts. Each one takes the output of the one before it. Parts 3 to 6 are the ML part; we have not picked the method yet.

| # | Part | What it does | In | Out | Meets requirement |
| --- | --- | --- | --- | --- | --- |
| 1 | Batch upload | Loads many X-rays at once and gives each one a case ID in the same format | Image files | Image + case ID + side  | Upload many images at once |
| 2 | Scale detection | Finds the scale marker in the image and works out mm per pixel | Image | mm per pixel | Area uses each X-ray's own scale |
| 3 | Bone segmentation | Draws the outline of each bone | Image | Mask per bone | Find the bones automatically |
| 4 | Naming of bones | Labels bones as metacarpal, M1, M2 and drops the rest (radius, ulna, claws, navicular) | Masks | Named masks | Measure only metacarpal, M1, M2 |
| 5 | Overlap handling | Splits the area correctly where two bones cross | Named masks | Cleaned masks | Overlap edges are not taken as bone edges |
| 6 | Fusion check | Marks each bone fused or not fused. A bone with a separate epiphysis (the unfused end piece) is not fused | Named masks | Fused yes/no per bone | Fusion status per bone |
| 7 | Area measurement | Counts mask pixels and converts to mm². For an unfused bone: bone area + epiphysis area, so the gap is not counted | Masks + mm per pixel | Area in mm², 3 decimals | Area in mm², 3 decimals, gap not counted |
| 8 | Review and correct | Shows the X-ray next to the result on the iPad, so the user can fix outlines by drawing | Image + masks + numbers | Corrected masks | User can check and fix outlines |
| 9 | Approve and export | Only approved results go into NRM's Excel template | Approved results | Excel file | Approve step, export to NRM's Excel |


## Data and file formats

| Data | Format | Notes |
| --- | --- | --- |
| X-ray images | Image files from NRM, around 165 counted in the first batch (final number not confirmed) | 6 folders: Ringed, Grey, Harbour seal, Harbour porpoise (2), Borås |
| Case ID | One format after normalizing, e.g. species + ID + side | Needed so results match NRM's Excel rows |
| Labels | Made in CVAT, exported as COCO (JSON) with polygon outlines | The file uses MC, P1, P2, P3, epiphysis, carpal, radius\_ulna, other\_bone. P1 and P2 need to be renamed to M1 and M2 to match NRM. Each outline also has flipper (1.1 or 1.2) and digit fields |
| Model output | Mask image where each pixel value is a bone class | One mask per image |
| iPad corrections | Corrected mask (PNG) sent back to the computer | Already works in the demo app |
| Final results | Excel, in NRM's template columns | Area in mm² (3 decimals) + fused yes/no per bone |
| Test set | A fixed set of images kept aside | Never used for training, so test scores stay honest |

## User interface draft

This is a rough draft of the steps a user goes through: open the app, upload a batch of images, let the model run, check and fix the results, then export to Excel.

<img width="1344" height="1092" alt="Image" src="https://github.com/user-attachments/assets/17a5074d-9a40-41f4-885c-e98d218bfe36" />

## Deployment

The plan is a local setup, not a hosted website. The tool runs on one computer, and the iPad connects to it by scanning a QR code.

1. The app runs on a computer at NRM as a small local web server.
2. The computer shows a QR code. The iPad scans it and opens the review screen in the browser.
3. The user draws corrections with the tablet's Pencil. The corrected mask goes back to the computer.
4. Nothing is sent to an outside server. Images stay on NRM's machine.
5. This likely needs the computer and iPad on the same wifi, so working from home might need a different setup.

## Tech stack

Most of the stack is not agreed yet. This shows what the team has agreed and what is still open.

| Area | Choice | Status |
| --- | --- | --- |
| App / server | Local web app on one computer, iPad connects by QR code | Agreed. Tested on a test photo, not on X-rays yet |
| Labeling | CVAT, COCO export | Agreed |
| Code and docs | GitHub repo + GitHub project board | Agreed |
| Programming language | To decide | Not agreed yet |
| Deep learning library(building and training) | To decide | Not agreed yet |
| Image processing library | To decide | Not agreed yet |
| Excel export | To decide | Not agreed yet |
| Where we train the model | To decide | Not agreed yet |

## Validation plan

We check each part on the fixed test set, and compare the final numbers with NRM's own manual measurements. We haven't decided yet how accurate the results need to be. We should agree on this with NRM.

| What we check | How | Compared against |
| --- | --- | --- |
| Bone outlines | Dice and IoU per bone, worked out in our own code from the CVAT export | CVAT labels on the test set |
| Bone naming | % of bones given the right name | CVAT labels |
| Scale | mm per pixel vs a hand measurement of the marker | A few images measured by hand |
| Area | Error in mm² and in % per bone | NRM's manual Excel measurements (ImageJ) |
| Fusion | % correct fused / not fused | NRM's records or our labels |
| Overlap | Area error on images where bones cross, reported on its own | Labeled overlap cases |
| Whole tool | Internal testing (weeks 12 to 14), then user testing with NRM (week 14) | NRM's feedback |

NRM has sent their Excel of manual measurements, so we can check the final area numbers, not only the outlines.

## Open questions

- [ ] Which model do we use to find the bones automatically (segmentation)?
- [ ] Same wifi: how do we handle people working from home?
- [ ] Laptop and iPad: NRM mostly reviews on the laptop and switches to the iPad for small areas. Should the review screen work with both mouse and pen?
- [ ] Some images show two flippers, labeled flipper 1.1 and 1.2 in the CVAT file. Do we keep them in one image or split them?
