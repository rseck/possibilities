import json
import pandas as pd

file_name = "/Users/roeeesquira/Study/מדעי המחשב/תואר שני/לקראת תזה/experiments.xlsx"
tr_data_point_template = {"premise_type": "", "premise": "","hypothesis_type":"","false_hypothesis": ""}


def generate_data():
    tr_data = []
    df = pd.read_excel(file_name, sheet_name='relational timing')
    for index, row in df.iterrows():
        premises_types = [premise for premise in list(row.keys()) if 'premise' in premise]
        hypothesis_types = [hypothesis for hypothesis in list(row.keys()) if 'hypothesis' in hypothesis]
        for premise_type in premises_types:
            for hypothesis_type in hypothesis_types:
                data_point = tr_data_point_template.copy()
                data_point['premise_type'] = premise_type
                data_point['premise'] = row.get(premise_type)
                data_point['hypothesis_type'] = hypothesis_type
                data_point['false_hypothesis'] = row.get(hypothesis_type)
                tr_data.append(data_point)

    with open('resources/temporal_relations_data.json', 'w') as f:
        json.dump(tr_data, f, indent=4)


def generate_prompts_from_tr_data():
    with open('prompts_templates/reasoning_prompt_templates.json', 'r') as f:
        prompt_templates = json.load(f)

    with open('resources/temporal_relations_data.json', 'r') as f:
        tr_data = json.load(f)

    prompts_descriptions = prompt_templates.keys()
    tr_prompts = []
    for item in tr_data:
        for prompt_description in prompts_descriptions:
            prompt_template = prompt_templates.get(prompt_description)
            prompt = prompt_template.format(premise=item['premise'], hypothesis=item['false_hypothesis'])
            match prompt_description:
                case 'entailment_with_neutral':
                    answer = "contradiction"
                case 'entailment':
                    answer = 'no'
                case 'true_false_neutral':
                    answer = "False"
                case _:
                    raise ValueError()
            item[prompt_description] = {"prompt": prompt, "answer": answer}
        tr_prompts.append(item)
    with open('generated_prompts/30_prompts_temporal_relations_3_types.json', 'w') as f:
        json.dump(tr_prompts, f, indent=4)  #


if __name__ == '__main__':
    # generate_data()
    generate_prompts_from_tr_data()
