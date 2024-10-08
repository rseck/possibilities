import json

import pandas as pd
file_name = "/Users/roeeesquira/Study/מדעי המחשב/תואר שני/לקראת תזה/experiments.xlsx"
sv_data_point_template = {"type": "", "central_verb": "", "premise": "", "false_hypothesis": ""}
def generate_data():
    sv_data = []
    df = pd.read_excel(file_name, sheet_name='salva_varitate_prompts')
    for index, row in df.iterrows():
        central_verb = row.get('main verb')

        data_point_1 = sv_data_point_template.copy()
        data_point_1['type'] = "basic"
        data_point_1['central_verb'] = central_verb
        data_point_1['premise'] = row.get('text1.1')
        data_point_1['false_hypothesis'] = row.get('tex2.1 - with falsely made salva varitate')
        sv_data.append(data_point_1)

        data_point_2 = sv_data_point_template.copy()
        data_point_2['type'] = "basic_with_epistemic_state"
        data_point_2['central_verb'] = central_verb
        data_point_2['premise'] = row.get('text1.1 with explicitly stating epistemic state')
        data_point_2['false_hypothesis'] = row.get('tex2.1 - with falsely made salva varitate')
        sv_data.append(data_point_2)

        data_point_3 = sv_data_point_template.copy()
        data_point_3['type'] = "mentioning_words"
        data_point_3['central_verb'] = central_verb
        data_point_3['premise'] = row.get('text1.2')
        data_point_3['false_hypothesis'] = row.get('tex2.2 - with falsely made salva varitate')
        sv_data.append(data_point_3)

        data_point_4 = sv_data_point_template.copy()
        data_point_4['type'] = "mentioning_words_and_epistemic_state"
        data_point_4['central_verb'] = central_verb
        data_point_4['premise'] = row.get('text1.2 with explicitly stating epistemic state')
        data_point_4['false_hypothesis'] = row.get('tex2.2 - with falsely made salva varitate')
        sv_data.append(data_point_4)

    with open('resources/salva_varitate_data.json', 'w') as f:
        json.dump(sv_data, f, indent=4)  #

    #open excel
    #convert excel to json
    # save each suting premise and hypothesis together and main verb, save to resources folder
    # manually create json for formats of entailement and entail/contradiction/neutral
    # generate all the prompts
    pass

if __name__ == '__main__':
    generate_data()