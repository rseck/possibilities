import json
def main():
    with open('generated_prompts/20_prompt_other_possibilities_expanded_3_types.json', 'r') as f:
        prompts = json.load(f)

    prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
    for prompt_structure in prompts:
        for prompt_type in prompt_types:
            prompt = prompt_structure[prompt_type]['prompt']
            answer = ""
            prompt_structure[prompt_type]['model_reply'] = answer
            'model_reply' in prompt_structure[prompt_type]

    with open('results/20_prompt_other_possibilities_expanded_3_types.json', 'w') as f:
        json.dump(prompts, f, indent=4)  #


if __name__ == '__main__':
    main()