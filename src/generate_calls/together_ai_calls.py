from together import Together
import os
import json
import time

with open('../resources/generated_prompts/20_prompt_other_possibilities_expanded_3_types.json', 'r') as f:
  prompts = json.load(f)

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

model = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"

# prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
# i=0
# for prompt_structure in prompts:
#   for prompt_type in prompt_types:
#     prompt = prompt_structure[prompt_type]['prompt']
#     if 'model_reply' not in prompt_structure[prompt_type]:
#         response = client.chat.completions.create(model=model,messages=[{"role": "user", "content": prompt}],)
#         answer = response.choices[0].message.content
#         prompt_structure[prompt_type]['model_reply'] = answer
#         i +=1
#         print(i)
#         with open('results/Meta-Llama-3.1-405B-Instruct-Turbo_20_prompt_other_possibilities_expanded_3_types.json', 'w') as f:
#             json.dump(prompts, f, indent=4)
#         # time.sleep(31)

# with open('generated_prompts/44_prompts_salva_varitate_3_types.json', 'r') as f:
#   sv_prompts = json.load(f)
#
# i=0
# prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
# for prompt_structure in sv_prompts:
#   for prompt_type in prompt_types:
#     prompt = prompt_structure[prompt_type]['prompt']
#     if 'model_reply' not in prompt_structure[prompt_type]:
#       i+=1
#       response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}], )
#       answer = response.choices[0].message.content
#       print(i)
#       prompt_structure[prompt_type]['model_reply'] = answer
#       with open('results/Meta-Llama-3.1-405B-Instruct-Turbo_44_prompts_salva_varitate_3_types.json', 'w') as f:
#         json.dump(sv_prompts, f, indent=4)

with open('../resources/generated_prompts/102_prompts_relation_determine_1_type.json', 'r') as f:
  dr_prompts = json.load(f)

i=0
prompt_types = ['entailment']
for prompt_structure in dr_prompts:
  for prompt_type in prompt_types:
    prompt = prompt_structure[prompt_type]['prompt']
    if 'model_reply' not in prompt_structure[prompt_type]:
      i+=1
      response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}], )
      answer = response.choices[0].message.content
      print(i)
      prompt_structure[prompt_type]['model_reply'] = answer
      with open('../results/Meta-Llama-3.1-405B-Instruct-Turbo_102_prompts_relation_determine_1_type.json', 'w') as f:
        json.dump(dr_prompts, f, indent=4)




with open('../resources/generated_prompts/30_prompts_relative_temporal_3_types.json', 'r') as f:
  rt_prompts = json.load(f)

i=0
prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
for prompt_structure in rt_prompts:
  for prompt_type in prompt_types:
    prompt = prompt_structure[prompt_type]['prompt']
    if 'model_reply' not in prompt_structure[prompt_type]:
      i+=1
      response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}], )
      answer = response.choices[0].message.content
      print(i)
      prompt_structure[prompt_type]['model_reply'] = answer
      with open('../results/Meta-Llama-3.1-405B-Instruct-Turbo_30_prompts_relative_temporal_3_types.json', 'w') as f:
        json.dump(rt_prompts, f, indent=4)

with open('../resources/generated_prompts/14_prompts_absolute_temporal_3_types.json', 'r') as f:
  at_prompts = json.load(f)

i=0
prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
for prompt_structure in at_prompts:
  for prompt_type in prompt_types:
    prompt = prompt_structure[prompt_type]['prompt']
    if 'model_reply' not in prompt_structure[prompt_type]:
      i+=1
      response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}], )
      answer = response.choices[0].message.content
      print(i)
      prompt_structure[prompt_type]['model_reply'] = answer
      with open('../results/Meta-Llama-3.1-405B-Instruct-Turbo_14_prompts_absolute_temporal_3_types.json', 'w') as f:
        json.dump(rt_prompts, f, indent=4)
