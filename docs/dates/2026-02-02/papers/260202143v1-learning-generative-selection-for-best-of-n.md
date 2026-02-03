---
layout: default
title: Learning Generative Selection for Best-of-N
---

# Learning Generative Selection for Best-of-N
**arXiv**：[2602.02143v1](https://arxiv.org/abs/2602.02143) · [PDF](https://arxiv.org/pdf/2602.02143.pdf)  
**作者**：Shubham Toshniwal, Aleksander Ficek, Siddhartha Jain, Wei Du, Vahid Noroozi, Sadegh Mahdavi, Somshubra Majumdar, Igor Gitman  

**一句话要点**：提出基于强化学习的小模型生成选择方法，以提升最佳候选选择质量

**关键词**：生成选择, 强化学习, 小模型训练, 推理扩展, 最佳候选选择

## 3 点简述
- 核心问题：测试时并行采样中最佳候选选择质量受限，影响大语言模型推理扩展
- 方法要点：通过强化学习训练小模型，从大规模数学和代码数据合成选择任务，奖励正确选择
- 实验或效果：在数学和代码基准上超越基线，接近或超过更大模型，泛化至强模型输出选择

## 摘要（原文）

> Scaling test-time compute via parallel sampling can substantially improve LLM reasoning, but is often limited by Best-of-N selection quality. Generative selection methods, such as GenSelect, address this bottleneck, yet strong selection performance remains largely limited to large models. We show that small reasoning models can acquire strong GenSelect capabilities through targeted reinforcement learning. To this end, we synthesize selection tasks from large-scale math and code instruction datasets by filtering to instances with both correct and incorrect candidate solutions, and train 1.7B-parameter models with DAPO to reward correct selections. Across math (AIME24, AIME25, HMMT25) and code (LiveCodeBench) reasoning benchmarks, our models consistently outperform prompting and majority-voting baselines, often approaching or exceeding much larger models. Moreover, these gains generalize to selecting outputs from stronger models despite training only on outputs from weaker models. Overall, our results establish reinforcement learning as a scalable way to unlock strong generative selection in small models, enabling efficient test-time scaling.

