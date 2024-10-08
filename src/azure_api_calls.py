import os
import requests
import base64
import json
import time


# Configuration
API_KEY = "fc8009b24d584ef3ab1fd7988c7daedc"
ENDPOINT = "https://possibilities-reasearch.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

with open('generated_prompts/20_prompt_other_possibilities_expanded_3_types.json', 'r') as f:
  prompts = json.load(f)


prompt_types = ['entailment_with_neutral', 'true_false_neutral', 'entailment']
for prompt_structure in prompts:
  for prompt_type in prompt_types:
    prompt = prompt_structure[prompt_type]['prompt']
    if 'model_reply' not in prompt_structure[prompt_type]:
        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 2048
        }

        # Send request
        try:
            response = requests.post(ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        except requests.RequestException as e:
            raise SystemExit(f"Failed to make the request. Error: {e}")

        # Handle the response as needed (e.g., print or process)
        print(response.json())
        # prompt_structure[prompt_type]['model_reply'] = answer
        with open('/content/possibilities/src/results/gpt4_20_prompt_other_possibilities_expanded_3_types.json', 'w') as f:
            json.dump(prompts, f, indent=4)
        time.sleep(31)