---
layout: default
title: InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning
---

# InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning
**arXiv**：[2601.14209v1](https://arxiv.org/abs/2601.14209) · [PDF](https://arxiv.org/pdf/2601.14209.pdf)  
**作者**：Matthew Y. R. Yang, Hao Bai, Ian Wu, Gene Yang, Amrith Setlur, Aviral Kumar  

**一句话要点**：提出干预训练以解决大语言模型推理中的信用分配问题

**关键词**：信用分配, 干预训练, 推理优化, 强化学习, 大语言模型, 数学推理

## 3 点简述
- 标准强化学习在推理中仅基于最终答案分配信用，导致中间步骤信用分配不当
- 引入干预训练，模型通过提出单步修正来自行分配信用，结合监督微调定位错误
- 在IMO-AnswerBench上，4B参数模型准确率提升近14%，优于更大开源模型

## 摘要（原文）

> Outcome-reward reinforcement learning (RL) has proven effective at improving the reasoning capabilities of large language models (LLMs). However, standard RL assigns credit only at the level of the final answer, penalizing entire reasoning traces when the outcome is incorrect and uniformly reinforcing all steps when it is correct. As a result, correct intermediate steps may be discouraged in failed traces, while spurious steps may be reinforced in successful ones. We refer to this failure mode as the problem of credit assignment. While a natural remedy is to train a process reward model, accurately optimizing such models to identify corrective reasoning steps remains challenging. We introduce Intervention Training (InT), a training paradigm in which the model performs fine-grained credit assignment on its own reasoning traces by proposing short, targeted corrections that steer trajectories toward higher reward. Using reference solutions commonly available in mathematical reasoning datasets and exploiting the fact that verifying a model-generated solution is easier than generating a correct one from scratch, the model identifies the first error in its reasoning and proposes a single-step intervention to redirect the trajectory toward the correct solution. We then apply supervised fine-tuning (SFT) to the on-policy rollout up to the point of error concatenated with the intervention, localizing error to the specific step that caused failure. We show that the resulting model serves as a far better initialization for RL training. After running InT and subsequent fine-tuning with RL, we improve accuracy by nearly 14% over a 4B-parameter base model on IMO-AnswerBench, outperforming larger open-source models such as gpt-oss-20b.

