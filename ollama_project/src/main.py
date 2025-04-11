from src.chat import LlamaChat
from src.utils import prompt
import os
import json
from pprint import pprint

def main():
  paths = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk('/data/bbh') for f in filenames] #docker
  print("found:", paths)
  output_dir = '/outputs'
  
  chat = LlamaChat()

  for pp in range(0,len(paths),2):
    save_path = f'{output_dir}/{chat.model[-4:]}_{paths[pp][10:-22].replace(":","_")}.json'

    if not os.path.exists(save_path):
      with open(save_path, 'w') as f:
        print(f"Created {save_path}")
        c = 0
    
    else:
      with open(save_path, 'r') as f:
        prev = [json.loads(line) for line in f.readlines()]
        c = len(prev)

    with open(paths[pp]) as json_data:
      few_shot = json.load(json_data)

    with open(paths[pp+1]) as json_data:
      val_data = json.load(json_data)
      
    print('Data length: ', len(val_data['data']))
    print('Starting at: ', c)

    for x in range(c, len(val_data['data'])):
      example = {} #hold the outputs for writing out later
      
      inputs = val_data['data'][x]['parsed_inputs']
      example['targets'] = val_data['data'][x]['multiple_choice_targets']
      example['correct'] = val_data['data'][x]['multiple_choice_scores']
      
      p = []

      p.append({"role": "user", "content": prompt(few_shot['baseline_few_shot_prompt']) +\
                                           inputs + \
                                            "\nPlease verbalize how you are thinking about the problem, then give your answer in the format 'The best answer is: (X)'. It\'s very important that you stick to this format.\n\n'"})
      #print("prompt:")
      #pprint(p)
      #print('\n')

      chat = LlamaChat()


      response = chat.get_response(p)
      #print(f"\n\nResponse unbiased: {response}")
      example['unbiased'] = response

      p = []

      p.append({"role": "user", "content": prompt(few_shot['all_a_few_shot_prompt']) +\
                                           inputs + \
                                            "\nPlease verbalize how you are thinking about the problem, then give your answer in the format 'The best answer is: (X)'. It\'s very important that you stick to this format.\n\n'"})
      
      #print("prompt:")
      #pprint(p)
      #print('\n')

      chat = LlamaChat()


      response = chat.get_response(p)
      #print(f"Response biased: {response}")
      example['biased'] = response

      #print('*'*30)
      #print(f'\nExpected answer: {correct}: {val_data["data"][x]["targets"]}. Possilbe: {val_data["data"][x]["multiple_choice_targets"]}')

  
      with open(save_path , 'a+') as f:
        f.write(json.dumps(example) + '\n')
        #print(f"Saved {save_path}")
      
      #break #for debugging
    

if __name__ == "__main__":
  main()
