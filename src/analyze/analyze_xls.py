import os
import matplotlib.pyplot as plt
import pandas as pd


def main():
    verified_results_dir = 'results/manually_verified_results'

    # Iterate through all files in the directory
    for filename in os.listdir(verified_results_dir):
        file_path = os.path.join(verified_results_dir, filename)
        # Check if it's a file (and not a subdirectory)
        if os.path.isfile(file_path):
            match filename:
                case "unified_results_44_prompts_salva_varitate_3_types manually.xlsx":
                    title = f'success rates in salva varitate prompts'
                    open_xl_and_print_plot(file_path, title, "success")
                case "unified_results_20_prompt_other_possibilities_expanded_3_types with manually parsed results.xlsx":
                    title = f'success rates in direct reasoning when asked to provide other possibilities'
                    open_xl_and_print_plot(file_path, title, "success with base answer")
                    title_2 = f'success rates in providing other possibilities direct reasoning'
                    open_xl_and_print_plot(file_path, title_2, "success with other possibilities")
                case "unified_results_14_prompts_absolute_temporal_3_types manual.xlsx":
                    title = f'success rates in absolute temporal prompts'
                    open_xl_and_print_plot(file_path, title, "success")
                case "unified_results_102_prompts_relation_determine_1_type manually.xlsx":
                    title = f'success rates in relation determining'
                    open_xl_and_print_plot(file_path, title, "success")
                case "unified_results_30_prompts_relative_temporal_3_types with manually parsed results.xlsx":
                    title = f'success rates in relative temporal prompts'
                    open_xl_and_print_plot(file_path, title, "success")


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))  # Calculate count
        return f'{pct:.1f}%\n(count: {val:d})'  # Format as "percentage\n(count)"

    return my_autopct


def open_xl_and_print_plot(file_path, title, column):
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    success_counts = df[column].value_counts()
    success_counts = success_counts.sort_index()
    success_counts.plot.pie(
        autopct=make_autopct(success_counts),  # Custom autopct to show percentage and count
        labels=['False', 'True'], colors=['red', 'lightgreen'])
    plt.ylabel('')
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    main()
