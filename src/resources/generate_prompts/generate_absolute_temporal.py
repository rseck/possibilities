import json
import pandas as pd

file_name = "/Users/roeeesquira/Study/מדעי המחשב/תואר שני/לקראת תזה/experiments.xlsx"
ta_data_point_template = {"premise": "","false_hypothesis": ""}


def generate_data():
    ta_data = []
    df = pd.read_excel(file_name, sheet_name='absolute timing')
    for index, row in df.iterrows():
        data_point = ta_data_point_template.copy()
        premise = row.get('premise 1') + " " + row.get('premise 2')
        data_point['premise'] = premise
        data_point['false_hypothesis'] = row.get("false hypothesis")
        ta_data.append(data_point)

    with open('resources/temporal_absolute_data.json', 'w') as f:
        json.dump(ta_data, f, indent=4)


def generate_prompts_from_tr_data():
    with open('../prompts_templates/reasoning_prompt_templates.json', 'r') as f:
        prompt_templates = json.load(f)

    with open('../data/absolute_temporal_data.json', 'r') as f:
        ta_data = json.load(f)

    prompts_descriptions = prompt_templates.keys()
    ta_prompts = []
    for item in ta_data:
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
        ta_prompts.append(item)
    with open('../generated_prompts/14_prompts_absolute_temporal_3_types.json', 'w') as f:
        json.dump(ta_prompts, f, indent=4)  #


if __name__ == '__main__':
    # generate_data()
    generate_prompts_from_tr_data()
