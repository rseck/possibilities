from datasets import load_dataset
import json


def main():
    ds_entailment_with_neutral = load_dataset("sentence-transformers/all-nli", "pair-class")
    ds_entailment_with_neutral_subset = ds_entailment_with_neutral['test'].shuffle().select(range(20))
    entailment_with_neutral_labels_dict = {0: "entailment", 1: "neutral", 2: "contradiction"}
    true_false_neutral_labels_dict = {0: "true", 1: "neutral", 2: "false"}
    with open('prompts_templates/prompts_formats_other_possibilities.json', 'r') as f:
        prompt_templates = json.load(f)

    prompts_descriptions = list(prompt_templates.keys())

    results = []
    for item in ds_entailment_with_neutral_subset:
        for prompt_description in prompts_descriptions:
            prompt_template = prompt_templates.get(prompt_description)
            other_possibilities_prompt = prompt_template.format(premise=item['premise'], hypothesis=item['hypothesis'])
            print(other_possibilities_prompt)
            label_idx = item['label']
            match prompt_description:
                case 'entailment_with_neutral':
                    base_answer = entailment_with_neutral_labels_dict[label_idx]
                case 'entailment':
                    base_answer = 'yes' if label_idx == 0 else 'no'
                case 'true_false_neutral':
                    base_answer = true_false_neutral_labels_dict[label_idx]
                case _:
                    raise ValueError()
            item[prompt_description] = {"prompt": other_possibilities_prompt, "base_answer": base_answer}
        results.append(item)

    with open('../generated_prompts/20_prompt_other_possibilities_expanded_3_types.json', 'w') as f:
        json.dump(results, f, indent=4)  #


if __name__ == "__main__":
    main()
