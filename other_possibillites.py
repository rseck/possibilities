from datasets import load_dataset

ds_entailment_with_neutral = load_dataset("sentence-transformers/all-nli", "pair-class")
ds_entailment_with_neutral_subset = ds_entailment_with_neutral['test'].shuffle().select(range(20))
i = ds_entailment_with_neutral_subset[0]
labels_dict = {"0": "entailment", "1": "neutral", "2": "contradiction"}

for item in ds_entailment_with_neutral_subset:
    print(item['text'], item['label'])

i=1


