from datasets import load_dataset
import json


ds_entailment_with_neutral = load_dataset("sentence-transformers/all-nli", "pair-class")
ds_entailment_with_neutral_subset = ds_entailment_with_neutral['test'].shuffle().select(range(20))
i = ds_entailment_with_neutral_subset[0]
labels_dict = {"0": "entailment", "1": "neutral", "2": "contradiction"}

with open('other_possibilities.json', 'r') as f:
    prompt_templates = json.load(f)

prompt_entailment_with_neutral = prompt_templates.get("prompt")
new = prompt_entailment_with_neutral.format(premise=i['premise'], hypothesis=i['hypothesis'])

for item in ds_entailment_with_neutral_subset:
    # copy item
# format extanded prompt



i=1
