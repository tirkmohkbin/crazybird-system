import json

prompt = {
  "prompt_name": "Ena Arisa – DNA Locked Prompt",
  "description": "Millimeter-locked facial DNA prompt for ComfyUI rendering.",
  "prompt": "portrait of Ena Arisa, serene expression, pastel skin #FFE9E4, soft white lighting, oval-slim face",
  "style_lock": {
    "lighting": "soft white only",
    "skin": "#FFE9E4",
    "texture": "visible pores, pastel tone",
    "expression": "serene, kind",
    "no_exaggeration": True,
    "no_cartoon": True,
    "no_yellow_light": True
  },
  "version": "1.0",
  "source": "https://www.notion.so/DNA-Tables-from-GitHub-218c51083b6680acbd9af0b12e328793"
}

with open("output/ena_comfy_prompt.json", "w") as f:
    json.dump(prompt, f, indent=2)
