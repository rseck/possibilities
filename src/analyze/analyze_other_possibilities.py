import json
import pandas as pd


def get_json_dict(file_name):
    with open(file_name, 'r') as f:
        at_prompts = json.load(f)
    return at_prompts


def main():
    data = {'premise': [],
            'hypothesis': [],
            'prompt_type': [],
            'model_type': [],
            'base_answer': [],
            'model_reply': [],
            'prompt': [],
            }

    files = [('claude', 'results/claude-3-5-sonnet_20240620_20_prompt_other_possibilities_expanded_3_types.json'),
             ('gemini', 'results/gemini-1.5-pro-002_20_prompt_other_possibilities_expanded_3_types.json'),
             (
             'llama', 'results/Meta-Llama-3.1-405B-Instruct-Turbo_20_prompt_other_possibilities_expanded_3_types.json')]
    prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
    results_dicts = [(file[0], get_json_dict(file[1])) for file in files]
    for model_name, results_dict in results_dicts:
        for prompt_structure in results_dict:
            for prompt_type in prompt_types:
                data['premise'].append(prompt_structure['premise'])
                data['hypothesis'].append(prompt_structure['hypothesis'])
                data['prompt_type'].append(prompt_type)
                data['model_type'].append(model_name)
                data['base_answer'].append(prompt_structure[prompt_type]['base_answer'])
                data['model_reply'].append(prompt_structure[prompt_type]['model_reply'])
                data['prompt'].append(prompt_structure[prompt_type]['prompt'])
            i = 1
    df = pd.DataFrame(data)
    df.to_excel('results/unified_results_20_prompt_other_possibilities_expanded_3_types.xlsx',
                index=False)  # Set index=False to avoid writing row numbers


if __name__ == '__main__':
    main()
