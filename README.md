# MSc Thesis project

## Examining the Faithfulness of Deepseek R1’s Chain-of-Thought Reasoning

Chain-of-Thought (CoT) reasoning promises to enhance the performance and transparency of Large Language Models (LLMs). Models, such as Deepseek R1, are trained via reinforcement learning to automatically generate CoT explanations in their outputs. Their *faithfulness*, how well the explanations actually reflect their internal reasoning process, has been called into doubt by recent papers, such as those by [Chen et al 2025](https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf) and [Chua and Evans 2025](http://arxiv.org/abs/2501.08156).
This paper extends previous work by probing Deepseek R1 with 445 logical puzzles under zero- and few-shot settings. 
We find that whilst the model explicitly acknowledges a strong harmful hint in 94.6\% of cases, it reports less than 2\% of helpful hints. Further analysis reveals implicit *unfaithfulness* as the model significantly reduces answer-rechecking behaviour for helpful hints (p<0.01) despite rarely mentioning them in its CoT, demonstrating a discrepancy between its *reported* reasoning and the *actual* decision process, a smoking gun that the CoT is not entirely faithful. Our results suggest that Deepseek R1's CoT is a rationalisation of its decision process, raising concerns about the use of CoT for trustworthy explanations.

The data used was sampled from [Turpin et al](https://github.com/milesaturpin/cot-unfaithfulness/tree/main?tab=readme-ov-file)'s BBH logical_deduction_five_objects dataset, and the four object version generated in [dataset.ipynb](https://github.com/Xannadoo/thesis_cot_faithful/blob/main/data_set.ipynb).

[Ollama Project](https://github.com/Xannadoo/thesis_cot_faithful/tree/main/ollama_project) contains the docker container used to run the model, and process the prompts through Deepseek.

[EDA](https://github.com/Xannadoo/thesis_cot_faithful/blob/main/EDA.ipynb) is an exploration of the dataset properties.

[Analysis2](https://github.com/Xannadoo/thesis_cot_faithful/blob/main/Analysis2.ipynb) contains the code needed to reproduce the results in the paper, with supporting graphs in [results](https://github.com/Xannadoo/thesis_cot_faithful/blob/main/results_display.ipynb)
