---
layout: default
title: GRPO-RM: Fine-Tuning Representation Models via GRPO-Driven Reinforcement Learning
---

# GRPO-RM: Fine-Tuning Representation Models via GRPO-Driven Reinforcement Learning
**arXiv**：[2511.15256v1](https://arxiv.org/abs/2511.15256) · [PDF](https://arxiv.org/pdf/2511.15256.pdf)  
**作者**：Yanchen Xu, Ziheng Jiao, Hongyuan Zhang, Xuelong Li  

**一句话要点**：提出GRPO-RM方法，通过GRPO驱动的强化学习微调表示模型。

**关键词**：表示模型微调, 强化学习, GRPO方法, 输出集设计, 奖励函数设计

## 3 点简述
- 核心问题：GRPO能否从大语言模型泛化到表示学习模型。
- 方法要点：建立预定义输出集，设计专用奖励函数，优化表示模型。
- 实验或效果：在多个真实数据集上验证方法有效性。

## 摘要（原文）

> The Group Relative Policy Optimization (GRPO), a reinforcement learning method used to fine-tune large language models (LLMs), has proved its effectiveness in practical applications such as DeepSeek-R1. It raises a question whether GRPO can be generalized to representation learning models. In this paper, we propose Group Relative Policy Optimization for Representation Model (GRPO-RM), and investigate the performance of GRPO-like policy in post-training representation models. Specifically, our method establishes a predefined output set to functionally replace token sequence sampling in LLMs, thereby generating an output group, which is essential for the probability-driven optimization of GRPO. In addition, a specialized reward function is designed to accommodate the properties of representation models. Extensive experiments are conducted on various real-world datasets to validate the effectiveness of our proposed method.

