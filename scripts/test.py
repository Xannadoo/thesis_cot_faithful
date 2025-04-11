
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from pprint import pprint

def load_model(model_name):
    print('load model internal')
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.to('cuda')
    print('model loaded, loading tokeniser')
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print('tokeniser loaded')
    return model, tokenizer

## Qwen was designed for math problems but its the only distilled model small
# enough to run on my laptop. They advise not using for other tasks.

model = 'deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B'

ds, tokeniser = load_model(model)

with open('cot-unfaithfulness/data/bbh/causal_judgment/few_shot_prompts.json') as json_data:
    few_shot = json.load(json_data)
    json_data.close()

with open('cot-unfaithfulness/data/bbh/causal_judgment/val_data.json') as json_data:
    val_data = json.load(json_data)
    json_data.close()

prompt_biased = few_shot['all_a_few_shot_prompt'] + val_data['data'][0]['inputs']
pprint(prompt_biased)

print('tokenising')
input_ids = tokeniser.encode(prompt_biased, return_tensors='pt', add_special_tokens=True).to('cuda')

print('generating')
output = ds.generate(input_ids, max_new_tokens=500, num_return_sequences=1, temperature=0.7) #temp 0.7 recommended

print('decoding\n')
for i, k in enumerate(output):
    print(tokeniser.decode(output[i]))
    print('*'*30)


output = tokeniser.decode(output[0])

with open('output_biased.txt', 'w') as f:
    f.write(output)
    f.close()