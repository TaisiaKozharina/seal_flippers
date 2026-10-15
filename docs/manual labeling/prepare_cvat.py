"""Build CVAT label definitions and a matching COCO file from the pre-annotations.

Usage: python3 prepare_cvat.py [in.json]
Writes labels_annotation.json (paste into CVAT: Project -> Labels -> Raw) and <in>_cvat.json
for Upload annotations -> COCO 1.0.
Every annotation gets exactly the attributes its label defines, so the import never
sees an unknown attribute or a value outside a select list.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

CATEGORIES = ["MC", "P1", "P2", "P3", "epiphysis", "carpal", "radius_ulna", "other_bone"]
TARGET = {"MC", "P1", "P2", "P3", "epiphysis"}
LONG_BONES = {"MC", "P1", "P2", "P3"}
DIGITS = ["unknown", "1", "2", "3", "4", "5"]
FUSION = ["unknown", "unfused", "partial", "fused"]
FLIPPER = ["unknown", "left", "right"]
COLORS = {"MC": "#d59d78", "P1": "#20d603", "P2": "#2a7dd1"}  # fixed display colours; others are assigned by CVAT


def attr(name, input_type, default, values):
    return {"name": name, "mutable": False, "input_type": input_type,
            "default_value": default, "values": values}


def attributes_for(label):
    # kept from annotations_coco.json; its "label" and "piece_id" are pipeline internals and dropped
    out = [
        attr("certain", "checkbox", "false", ["false"]),
        attr("flipper", "select", "unknown", FLIPPER),  # pipeline groups (1.1, 2.1...) become unknown
    ]
    if label in TARGET:
        out.append(attr("digit", "select", "unknown", DIGITS))
        out.append(attr("overlapping", "checkbox", "false", ["false"]))
    if label in LONG_BONES:
        out.append(attr("fusion", "select", "unknown", FUSION))
    return out


def labels():
    out = []
    for n in CATEGORIES:
        label = {"name": n, "type": "polygon", "attributes": attributes_for(n)}
        if n in COLORS:
            label["color"] = COLORS[n]
        out.append(label)
    return out


def convert_attrs(label, src):
    out = {}
    for a in attributes_for(label):
        name, v = a["name"], src.get(a["name"])
        if a["input_type"] == "checkbox":
            out[name] = bool(v) if v is not None else False
        elif a["input_type"] == "select":
            if isinstance(v, float) and v.is_integer():  # CVAT number attributes export as 1.0
                v = int(v)
            v = None if v is None else str(v)
            out[name] = v if v in a["values"] else a["default_value"]
        else:
            out[name] = "" if v is None else str(v)
    return out


def main():
    args = sys.argv[1:]
    src = args[0] if args else os.path.join(HERE, "annotations_coco.json")

    d = json.load(open(src))
    names = {c["id"]: c["name"] for c in d["categories"]}
    assert set(names.values()) == set(CATEGORIES), f"unexpected categories: {sorted(names.values())}"
    for a in d["annotations"]:
        a["attributes"] = convert_attrs(names[a["category_id"]], a.get("attributes", {}))

    dst = os.path.splitext(src)[0] + "_cvat.json"
    json.dump(d, open(dst, "w"))
    json.dump(labels(), open(os.path.join(HERE, "labels_annotation.json"), "w"), indent=1)
    print(f"{len(d['images'])} images, {len(d['annotations'])} annotations -> {os.path.basename(dst)}; labels_annotation.json updated")


if __name__ == "__main__":
    main()
