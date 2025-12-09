---
layout: default
title: Comparative Analysis and Parametric Tuning of PPO, GRPO, and DAPO for LLM Reasoning Enhancement
---

# Comparative Analysis and Parametric Tuning of PPO, GRPO, and DAPO for LLM Reasoning Enhancement
**arXiv**：[2512.07611v1](https://arxiv.org/abs/2512.07611) · [PDF](https://arxiv.org/pdf/2512.07611.pdf)  
**作者**：Yongsheng Lian  

**一句话要点**：系统比较PPO、GRPO和DAPO三种强化学习算法，以增强大语言模型的复杂推理能力。

**关键词**：强化学习, 大语言模型, 推理增强, 参数调优, 转移学习

## 3 点简述
- 核心问题：如何有效利用强化学习提升大语言模型在复杂推理任务中的性能。
- 方法要点：采用控制转移学习评估，先在Countdown Game上微调，再在通用推理基准上测试。
- 实验或效果：RL训练模型在所有任务上优于基础模型，但改进程度因基准而异；参数分析提供实用指导。

## 摘要（原文）

> This study presents a systematic comparison of three Reinforcement Learning (RL) algorithms (PPO, GRPO, and DAPO) for improving complex reasoning in large language models (LLMs). Our main contribution is a controlled transfer-learning evaluation: models are first fine-tuned on the specialized Countdown Game and then assessed on a suite of general-purpose reasoning benchmarks. Across all tasks, RL-trained models outperform their corresponding base models, although the degree of improvement differs by benchmark.
>   Our parametric analysis offers practical guidance for RL-based LLM training. Increasing the group size in GRPO and DAPO leads to more stable training dynamics and higher accuracy, while the impact of the KL-penalty coefficient is non-monotonic. Additionally, we find that the Dynamic Sampling (DS) component in DAPO does not improve performance; in fact, the best overall results are achieved with DAPO when DS is disabled.

