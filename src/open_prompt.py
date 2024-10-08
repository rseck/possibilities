import json
def main():
    with open('generated_prompts/44_prompts_salva_varitate_3_types.json', 'r') as f:
        prompts = json.load(f)

    prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
    for prompt_structure in prompts:
        for prompt_type in prompt_types:
            prompt = prompt_structure[prompt_type]['prompt']
            if 'model_reply' not in prompt_structure[prompt_type]:
                answer = "response.text"
                prompt_structure[prompt_type]['model_reply'] = answer
                with open(
                        '/content/possibilities/src/results/gemini-1.5-pro-002_20_prompt_other_possibilities_expanded_3_types.json',
                        'w') as f:
                    json.dump(prompts, f, indent=4)
                # time.sleep(31)

    # with open('results/20_prompt_other_possibilities_expanded_3_types.json', 'w') as f:
    #     json.dump(prompts, f, indent=4)  #


if __name__ == '__main__':
    main()


