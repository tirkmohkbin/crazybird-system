import os
import json

anchor_dir = "_Referencer/Anchors"
output_file = "dna_index.json"

dna_index = []

for filename in os.listdir(anchor_dir):
    if filename.endswith(".md"):
        path = os.path.join(anchor_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            title = lines[0].replace("#", "").strip()
            tag_line = [line for line in lines if "Core tag:" in line]
            notes_line = [line for line in lines if "notes:" in line.lower()]
            tag = tag_line[0].split(":")[-1].strip() if tag_line else ""
            notes = notes_line[0].split(":", 1)[-1].strip() if notes_line else ""
            dna_index.append({
                "title": title,
                "attributes": [
                    {"attribute": tag, "value": "", "notes": notes}
                ]
            })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dna_index, f, ensure_ascii=False, indent=2)

