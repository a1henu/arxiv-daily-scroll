---
layout: default
title: MediX-R1: Open Ended Medical Reinforcement Learning
---

# MediX-R1: Open Ended Medical Reinforcement Learning
**arXiv**：[2602.23363v1](https://arxiv.org/abs/2602.23363) · [PDF](https://arxiv.org/pdf/2602.23363.pdf)  
**作者**：Sahal Shaji Mullappilly, Mohammed Irfan Kurpath, Omair Mohamed, Mohamed Zidan, Fahad Khan, Salman Khan, Rao Anwer, Hisham Cholakkal  

**一句话要点**：提出MediX-R1框架，通过强化学习提升医疗多模态大语言模型的开放式回答能力

**关键词**：医疗强化学习, 多模态大语言模型, 开放式回答, 复合奖励设计, LLM作为评判者

## 3 点简述
- 针对医疗多模态大语言模型在开放式任务中传统奖励机制不足的问题
- 采用基于组的强化学习和复合奖励，包括准确性、语义、格式和模态奖励
- 在少量指令数据上实现优异性能，尤其在开放式临床任务中表现突出

## 摘要（原文）

> We introduce MediX-R1, an open-ended Reinforcement Learning (RL) framework for medical multimodal large language models (MLLMs) that enables clinically grounded, free-form answers beyond multiple-choice formats. MediX-R1 fine-tunes a baseline vision-language backbone with Group Based RL and a composite reward tailored for medical reasoning: an LLM-based accuracy reward that judges semantic correctness with a strict YES/NO decision, a medical embedding-based semantic reward to capture paraphrases and terminology variants, and lightweight format and modality rewards that enforce interpretable reasoning and modality recognition. This multi-signal design provides stable, informative feedback for open-ended outputs where traditional verifiable or MCQ-only rewards fall short. To measure progress, we propose a unified evaluation framework for both text-only and image+text tasks that uses a Reference-based LLM-as-judge in place of brittle string-overlap metrics, capturing semantic correctness, reasoning, and contextual alignment. Despite using only $\sim51$K instruction examples, MediX-R1 achieves excellent results across standard medical LLM (text-only) and VLM (image + text) benchmarks, outperforming strong open-source baselines and delivering particularly large gains on open-ended clinical tasks. Our results demonstrate that open-ended RL with comprehensive reward signals and LLM-based evaluation is a practical path toward reliable medical reasoning in multimodal models. Our trained models, curated datasets and source code are available at https://medix.cvmbzuai.com

