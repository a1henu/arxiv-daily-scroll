---
layout: default
title: ThinkDrive: Chain-of-Thought Guided Progressive Reinforcement Learning Fine-Tuning for Autonomous Driving
---

# ThinkDrive: Chain-of-Thought Guided Progressive Reinforcement Learning Fine-Tuning for Autonomous Driving
**arXiv**：[2601.04714v1](https://arxiv.org/abs/2601.04714) · [PDF](https://arxiv.org/pdf/2601.04714.pdf)  
**作者**：Chang Zhao, Zheming Yang, Yunqing Hu, Qi Guo, Zijian Wang, Pengcheng Li, Wen Ji  

**一句话要点**：提出ThinkDrive框架，通过思维链引导的渐进强化学习微调解决自动驾驶决策问题。

**关键词**：自动驾驶, 思维链推理, 强化学习微调, 渐进训练, 难度感知优化

## 3 点简述
- 现有方法存在推理无结构、泛化差和与人类意图不对齐的问题。
- 采用两阶段训练：先用思维链进行监督微调，再用难度感知自适应策略优化进行渐进强化学习。
- 在公开数据集上，ThinkDrive在多项指标上优于基线，小模型超越GPT-4o。

## 摘要（原文）

> With the rapid advancement of large language models (LLMs) technologies, their application in the domain of autonomous driving has become increasingly widespread. However, existing methods suffer from unstructured reasoning, poor generalization, and misalignment with human driving intent. While Chain-of-Thought (CoT) reasoning enhances decision transparency, conventional supervised fine-tuning (SFT) fails to fully exploit its potential, and reinforcement learning (RL) approaches face instability and suboptimal reasoning depth. We propose ThinkDrive, a CoT guided progressive RL fine-tuning framework for autonomous driving that synergizes explicit reasoning with difficulty-aware adaptive policy optimization. Our method employs a two-stage training strategy. First, we perform SFT using CoT explanations. Then, we apply progressive RL with a difficulty-aware adaptive policy optimizer that dynamically adjusts learning intensity based on sample complexity. We evaluate our approach on a public dataset. The results show that ThinkDrive outperforms strong RL baselines by 1.45%, 1.95%, and 1.01% on exam, easy-exam, and accuracy, respectively. Moreover, a 2B-parameter model trained with our method surpasses the much larger GPT-4o by 3.28% on the exam metric.

