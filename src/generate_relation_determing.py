import json
import pandas as pd

file_name = "/Users/roeeesquira/Study/מדעי המחשב/תואר שני/לקראת תזה/experiments.xlsx"
relations_data_point_template = {"premise": "", "hypothesis": "", "possible_answers": [],
                                 "possible_answers_explanations": []}


def generate_data():
    relation_data = []
    df = pd.read_excel(file_name, sheet_name='possible relations')
    for index, row in df.iterrows():
        premise_hypothesis = row.get('premise/hypothesis')
        premise = premise_hypothesis.replace("{var}", "{var_1}")
        hypothesis = premise_hypothesis.replace("{var}", "{var_2}")
        data_point = relations_data_point_template.copy()
        data_point['premise'] = premise
        data_point['hypothesis'] = hypothesis
        data_point['possible_answers'] = row.get('possible answers').strip().split(", ")
        data_point['possible_answers_explanations'] = row.get('possible answers explanations')
        relation_data.append(data_point)


    with open('resources/relation_determine_data.json', 'w') as f:
        json.dump(relation_data, f, indent=4)  #


def generate_prompts_from_relation_data():
    pass
    # with open('prompts_templates/reasoning_prompt_templates.json', 'r') as f:
    #     prompt_templates = json.load(f)
    #
    # with open('resources/salva_varitate_data.json', 'r') as f:
    #     sv_data = json.load(f)
    #
    # prompts_descriptions = prompt_templates.keys()
    # sv_prompts = []
    # for item in sv_data:
    #     for prompt_description in prompts_descriptions:
    #         prompt_template = prompt_templates.get(prompt_description)
    #         prompt = prompt_template.format(premise=item['premise'], hypothesis=item['false_hypothesis'])
    #         print(prompt)
    #         match prompt_description:
    #             case 'entailment_with_neutral':
    #                 answer = "contradiction"
    #             case 'entailment':
    #                 answer = 'no'
    #             case 'true_false_neutral':
    #                 answer = "False"
    #             case _:
    #                 raise ValueError()
    #         item[prompt_description] = {"prompt": prompt, "answer": answer}
    #     sv_prompts.append(item)
    #
    # with open('generated_prompts/44_prompts_salva_varitate_3_types.json', 'w') as f:
    #     json.dump(sv_prompts, f, indent=4)  #


if __name__ == '__main__':
    generate_data()
    generate_prompts_from_relation_data()
