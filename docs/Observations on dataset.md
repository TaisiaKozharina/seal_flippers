# Dataset Notes

## General

First, some general stuff. The scale marker (that white dot plus ruler thing) isn't in the image metadata anywhere, it's just a physical object photographed next to the flipper each time, sometimes labeled DX/SX or L/R. So whatever we build has to actually  detect the scale separately in each image instead of using a fixed pixel to mm conversion.

Filenames differ across folders. Some have dates and sequence numbers, some don't, some use letters in the ID, some don't. We'll probably need to clean this up before we can run anything automated on it.

Also noticed some radiographs show both flippers of the same seal in one shot, and others show just one. So we'll need a crop or split step before the measuring part can run on the two-flipper ones.

## Species breakdown

### Ringed seal

10 images, but only 8 actual cases (00119, 00124, 00163, 00187, and on the 2026 side 00105, 00122, 00139, 00168). Two of those cases (00163 and 00105) show up twice each, a few minutes apart. Could be two different views, or just a retake because the first shot didn't come out well, not sure.

### Grey seal

Our biggest group, around 34 images, roughly 27 cases. Naming is messy here, we've got the usual B-prefix ones (00107, 00121 which weirdly shows up twice but from different views, 00122, 00123, 00125, 00184, 00186, 00106, 00182, 00183, 00188, 00200, 00201), some left/right pairs (B26-00194, B2026-00195), a VLT-style ID (26-VLT000801), a no-dash one (B202500164), and one that's literally just a name with no number at all (Taggad P20). There's one confirmed fetus (00141). And three cases are tagged "maybe" right in the filename by NRM themselves (00085, 00179, 00180), so even they weren't fully sure on the ID for those.

### Harbour seal

Around 41 images, about 29 cases. Same kind of B-prefix pattern (00047, 00067, 00127, 00128, 00137, 00161, 00162, 00257, 00074, 00126, 00137, 00187, 00190), left/right pairs (00189, 00193), a no-dash pair (B202500165), one more "maybe" (00075), and one odd one, B202600073_KS, different prefix entirely and I couldn't spot a scale marker in that thumbnail at all. Also worth flagging, 7 of these images (00077 to 00081, 00083, 00084) are labeled "SVA seal" with VLT numbers instead of NRM's usual format, looks like they came from a different institution (SVA, the Swedish vet authority) and just got mixed into this folder.

### Harbour porpoise

Two folders, about 65 images total, and genuinely two different naming eras. Older stuff uses plain numbers like "20240071_tumlare" up through 20240763 (2024 dates, about 24 cases, a few with two shots each). Then there's a newer batch, 20250234 through 20250450 using the same numeric style, before it switches to "A2025-00448" through "A2026-00548" (2025 to 2026). One confirmed mother and fetus pair at A2026-00548, both explicitly tagged. A2025-00449 is tagged "mother" twice, and there's a third image with the same ID but no tag, might be the calf, not confirmed.

### Borås

15 images, 6 named individuals, Asta, Ebbelina, Fien, Novi, Soraya, Wilma. Naming here is different, just a name plus a number, no case ID, no date. All 15 have the round scale dot, so that part's fine, but the side marking is just a plain L or R written on the image itself, no tag block like the others use. Framing is way less consistent though, about half of these are shot at an angle instead of straight, Asta_3, Ebbelina_1, Ebbelina_3, Fien_1, Fien_2, Novi_2, Wilma_0 and Wilma_1 are all tilted, and Asta_3 even shows the edge of the actual film in the shot. Soraya_0 is more zoomed out than the rest too. The one that really stands out is Ebbelina_1 and Ebbelina_3, they're on a noticeably lighter gray background than every other image in the whole dataset, looks like a different capture method or machine, maybe a photo of a printed film instead of a direct digital shot. So overall, no IDs, no dates, inconsistent framing, and at least one clear mismatch in how two of them were captured, all consistent with it being a quick reference sample rather than NRM's usual standard.
