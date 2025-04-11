def prompt(few_shot):
    instruction = 'First, there are some example questions and answers, followed by a question that you should answer. It is important that you follow the expected answer format.'
    instruction += '\n\nHow would a typical person answer each of the following questions about causation?'
    for i in few_shot.split('How would a typical person answer each of the following questions about causation?')[1:]:
        instruction += i
    return instruction + 'Now it is your turn. How would a typical person answer the following question?\n\n'
