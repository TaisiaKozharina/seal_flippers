# CVAT Annotation Guide

How to correct the pre-annotations of seal flipper radiographs in CVAT. Label definitions and their history are in `label_schema_changes.md`.

## Files

| File | Purpose |
|---|---|
| `labels_annotation.json` | Full label definition (8 classes) used in CVAT during annotation |
| `labels_final.json` | Final ground-truth classes: `MC`, `P1`, `P2` |
| `prepare_cvat.py` | Converts pipeline pre-annotations into COCO files that match `labels_annotation.json` |

Images and annotation files are NRM data and are **not** stored in this repository.

## 1. Install

1. Install Docker Desktop: https://www.docker.com/products/docker-desktop/
2. Install CVAT locally: https://docs.cvat.ai/docs/administration/basics/installation/

Data stays on your own machine; do not use the online CVAT (app.cvat.ai).

## 2. Create Project and Task

1. **Projects → +** → Labels → **Raw** → paste `labels_annotation.json`. This also sets the fixed label colours: `MC` #D59D78 (brown), `P1` #20D603 (green), `P2` #2A7DD1 (blue). Keep these colours so that screenshots and figures look the same for everyone.
2. Create the Task **inside the Project** (otherwise the Task has no labels and import fails with `Label 'xx' is not registered for this task`).
3. Upload the images without renaming them.
4. `Actions → Upload annotations → COCO 1.0` → select the converted pre-annotation file (`*_cvat.json`).

## 3. What to correct

Only `MC`, `P1` and `P2` are reviewed and used as ground truth. Other classes can be ignored.

1. **Bone names**: fix wrong `MC` / `P1` / `P2`.
2. **Missing bones**: every MC, P1 and P2 must be annotated; a missing bone counts as background during training.
3. **Boundaries**: fix obvious errors only; do not retrace every bone.
4. **Attributes**:

| Attribute | How to fill in |
|---|---|
| `flipper` | `left` / `right` from the file name or the DX (right) / SX (left) marker; otherwise `unknown` |
| `digit` | `1`–`5`; the same number for MC, P1 and P2 of one digit; `unknown` if unclear, do not guess |
| `overlapping` | Tick if the bone overlaps another bone or is partly unclear |
| `fusion` | `unfused` / `partial` / `fused`; `unknown` if unclear |
| `certain` | Tick after reviewing the bone |

## 4. Tips

- Draw with **Shape**, not Track. A track is copied onto every following image.
- Redraw part of a boundary: Shift + click a vertex, draw the new section, click back on the outline.
- Delete a vertex: Option (Alt) + click. Delete an object: Delete.
- No merge button for polygons: extend one polygon over the other area, then delete the other.
- Zoom the image with two-finger scroll or the mouse wheel over the image. If the whole page zooms, press Cmd + 0.
- Shortcut list: F1.

## 5. Export

- **Export a backup regularly**: `Actions → Export task dataset → COCO 1.0`.
- Uploading annotations **replaces** all annotations in the Task, so always export first.
- Only `MC`, `P1` and `P2` from the export are used as the final dataset (see `labels_final.json`).
