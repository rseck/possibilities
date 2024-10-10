import itertools
import json
import random
import pandas as pd

file_name = "/Users/roeeesquira/Study/מדעי המחשב/תואר שני/לקראת תזה/experiments.xlsx"
relations_data_point_template = {"premise": "", "hypothesis": "", "possible_answers": [],
                                 "possible_answers_explanations": []}
possible_relations = {"Composition": "Composition (A is made up of B, and B cannot exist independently of A)",
                      "Containment": "Containment (A contains B, but B can exist independently of A)",
                      "Inheritance": "Inheritance (A is a type of B, sharing characteristics)",
                      "Aggregation": "Aggregation (A is made up of B, but B can exist independently of A)",
                      "Association": "Association (A and B are related but are independent entities)",
                      "None": "No relation from the above list is possible"}


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

    with open('../data/relation_determine_data.json', 'w') as f:
        json.dump(relation_data, f, indent=4)  #


def generate_prompts_from_relation_data():
    pass
    with open('../prompts_templates/relations_determining.json', 'r') as f:
        prompt_templates = json.load(f)

    with open('../data/relation_determine_data.json', 'r') as f:
        relation_data = json.load(f)

    prompts_descriptions = prompt_templates.keys()
    relation_prompts = []
    for item in relation_data:
        for prompt_description in prompts_descriptions:
            for correct_answer in item['possible_answers']:
                incorrect_answers = [word for word in list(possible_relations.values()) if not any(element.lower() in word.lower() for element in item['possible_answers'])]
                for subgroup in itertools.combinations(incorrect_answers, 3):
                    work_item = item.copy()
                    prompt_template = prompt_templates.get(prompt_description)
                    expanded_correct_answer = possible_relations.get(correct_answer)
                    possible_answers = list(subgroup) + [expanded_correct_answer]
                    random.shuffle(possible_answers)
                    prompt = prompt_template.format(premise=work_item['premise'], hypothesis=work_item['hypothesis'], answers=possible_answers)
                    work_item[prompt_description] = {"prompt": prompt, "answer": expanded_correct_answer,
                                                     "possible_answers_given": possible_answers}
                    relation_prompts.append(work_item.copy())
    with open('../generated_prompts/102_prompts_relation_determine_1_type.json', 'w') as f:
        json.dump(relation_prompts, f, indent=4)  #


if __name__ == '__main__':
    # generate_data()
    generate_prompts_from_relation_data()
