import pandas as pd
from analyze.analyze_other_possibilities import get_json_dict


def main():
    data_template = {'premise': [],
                     'hypothesis': [],
                     'model_type': [],
                     'gold_answer': [],
                     'model_reply': [],
                     'is_answer_in_reply': [],
                     'prompt': []}
    files_starts = [('gemini', 'results/gemini-1.5-pro-002_'),
                    ('llama', 'results/Meta-Llama-3.1-405B-Instruct-Turbo_')]
    files_ends = ["102_prompts_relation_determine_1_type"]
    prompt_types = ['entailment']

    for file_end in files_ends:
        data = data_template.copy()
        for model_name, file_start in files_starts:
            results_dict = get_json_dict(file_start + file_end + ".json")
            for prompt_structure in results_dict:
                for prompt_type in prompt_types:
                    data['premise'].append(prompt_structure['premise'])
                    data['hypothesis'].append(prompt_structure['hypothesis'])
                    data['model_type'].append(model_name)
                    gold_answer = prompt_structure[prompt_type]['answer']
                    data['gold_answer'].append(gold_answer)
                    model_reply = prompt_structure[prompt_type]['model_reply']
                    data['model_reply'].append(model_reply)
                    data['is_answer_in_reply'].append(gold_answer.lower().split()[0] == model_reply.lower().split()[0] or gold_answer.lower().split()[0] in model_reply.lower())
                    data['prompt'].append(prompt_structure[prompt_type]['prompt'])
        df = pd.DataFrame(data)
        df.to_excel('results/unified_results_' + file_end + '.xlsx',
                    index=False)  # Set index=False to avoid writing row numbers


if __name__ == '__main__':
    main()
