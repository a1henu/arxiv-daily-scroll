---
layout: default
title: MediX-R1: Open Ended Medical Reinforcement Learning
---

# MediX-R1: Open Ended Medical Reinforcement Learning
**arXiv**：[2602.23363v1](https://arxiv.org/abs/2602.23363) · [PDF](https://arxiv.org/pdf/2602.23363.pdf)  
**作者**：Sahal Shaji Mullappilly, Mohammed Irfan Kurpath, Omair Mohamed, Mohamed Zidan, Fahad Khan, Salman Khan, Rao Anwer, Hisham Cholakkal  

**一句话要点**：提出MediX-R1框架，通过强化学习提升医疗多模态大语言模型的开放式回答能力。

**关键词**：医疗强化学习, 多模态大语言模型, 开放式回答, 复合奖励设计, LLM评估框架

## 3 点简述
- 针对医疗多模态大语言模型在开放式回答中缺乏有效反馈的问题，提出基于复合奖励的强化学习框架。
- 采用基于LLM的准确性奖励、医学嵌入语义奖励和轻量级格式奖励，稳定优化模型输出。
- 在少量指令数据上，MediX-R1在医疗文本和图像+文本基准测试中表现优异，尤其在开放式临床任务上提升显著。

## 摘要（原文）

> We introduce MediX-R1, an open-ended Reinforcement Learning (RL) framework for medical multimodal large language models (MLLMs) that enables clinically grounded, free-form answers beyond multiple-choice formats. MediX-R1 fine-tunes a baseline vision-language backbone with Group Based RL and a composite reward tailored for medical reasoning: an LLM-based accuracy reward that judges semantic correctness with a strict YES/NO decision, a medical embedding-based semantic reward to capture paraphrases and terminology variants, and lightweight format and modality rewards that enforce interpretable reasoning and modality recognition. This multi-signal design provides stable, informative feedback for open-ended outputs where traditional verifiable or MCQ-only rewards fall short. To measure progress, we propose a unified evaluation framework for both text-only and image+text tasks that uses a Reference-based LLM-as-judge in place of brittle string-overlap metrics, capturing semantic correctness, reasoning, and contextual alignment. Despite using only $\sim51$K instruction examples, MediX-R1 achieves excellent results across standard medical LLM (text-only) and VLM (image + text) benchmarks, outperforming strong open-source baselines and delivering particularly large gains on open-ended clinical tasks. Our results demonstrate that open-ended RL with comprehensive reward signals and LLM-based evaluation is a practical path toward reliable medical reasoning in multimodal models. Our trained models, curated datasets and source code are available at https://medix.cvmbzuai.com

