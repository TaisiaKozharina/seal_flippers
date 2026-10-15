# Label Schema Changes

## Changes from the original pre-annotations

| Attribute | Original pre-annotations | Now | Notes |
|---|---|---|---|
| Classes | 8 classes | **Unchanged** | `MC, P1, P2, P3, epiphysis, carpal, radius_ulna, other_bone`, category ids 1–8 in the same order |
| `flipper` | Text, pipeline groups `1.1` / `1.2` / `2.1` / `2.2` | **Select**: `unknown` / `left` / `right` | Now means the anatomical side, not the pipeline group; use `unknown` if it cannot be determined |
| `digit` | Always `null` | **Select**: `unknown` / `1`–`5` (strings) | Digit number; MC, P1, P2, P3 and epiphysis only |
| `certain` | Whether the pipeline is confident about the bone name | Checkbox, **unchanged** | Ticked for every bone after manual review, meaning "manually confirmed" |
| `overlapping` | Not present | **New**, checkbox | Bone overlaps another bone or is partly unclear; MC, P1, P2, P3 and epiphysis only |
| `fusion` | Not present | **New**, select: `unknown` / `unfused` / `partial` / `fused` | Epiphyseal fusion; MC, P1, P2 and P3 only |
| `label` | Pipeline's raw label (`MC-epi`, `L1`, etc.) | **Removed** | |
| `piece_id` | Pipeline's internal id | **Removed** | |

## Final labels (ground truth)

The schema above is used for pre-annotation and for correcting in CVAT. Only `MC`, `P1` and `P2` are manually reviewed, so the final dataset (for reporting and training) keeps these three classes only. All other classes (`P3`, `epiphysis`, `carpal`, `radius_ulna`, `other_bone`) are unreviewed pre-annotations and are removed when exporting.

| Category id | Class | Meaning | Colour |
|---|---|---|---|
| 1 | `MC` | Metacarpal | `#D59D78` (brown) |
| 2 | `P1` | Proximal phalanx | `#20D603` (green) |
| 3 | `P2` | Middle phalanx (digit 1 has only two phalanges, so its P2 is the distal one) | `#2A7DD1` (blue) |

| Attribute | Values | Meaning |
|---|---|---|
| `flipper` | `unknown` / `left` / `right` | Anatomical side |
| `digit` | `unknown` / `1`–`5` | Digit number |
| `overlapping` | `true` / `false` | Bone overlaps another bone or is partly unclear |
| `fusion` | `unknown` / `unfused` / `partial` / `fused` | Epiphyseal fusion |
| `certain` | `true` / `false` | Manually confirmed |

Notes:
- Every MC, P1 and P2 in an image must be annotated; a missing bone is treated as background during training.
- Separate epiphyses are not included, so the area of an unfused bone covers the shaft only.

