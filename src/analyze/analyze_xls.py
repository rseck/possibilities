import os

import pandas as pd



def main():
    verified_results_dir = '/path/to/your/directory'

    # Iterate through all files in the directory
    for filename in os.listdir(verified_results_dir):
        file_path = os.path.join(verified_results_dir, filename)

        # Check if it's a file (and not a subdirectory)
        if os.path.isfile(file_path):
    for file_name in
    df = pd.read_excel(file_name, sheet_name='absolute timing')
    for index, row in df.iterrows():
        data_point = ta_data_point_template.copy()
        premise = row.get('premise 1') + " " + row.get('premise 2')
        data_point['premise'] = premise
        data_point['false_hypothesis'] = row.get("false hypothesis")
        ta_data.append(data_point)


if __name__ == '__main__':
    main()