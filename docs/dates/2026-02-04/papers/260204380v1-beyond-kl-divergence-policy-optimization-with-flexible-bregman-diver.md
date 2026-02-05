---
layout: default
title: Beyond KL Divergence: Policy Optimization with Flexible Bregman Divergences for LLM Reasoning
---

# Beyond KL Divergence: Policy Optimization with Flexible Bregman Divergences for LLM Reasoning
**arXiv**：[2602.04380v1](https://arxiv.org/abs/2602.04380) · [PDF](https://arxiv.org/pdf/2602.04380.pdf)  
**作者**：Rui Yuan, Mykola Khandoga, Vinay Kumar Sankarapu  

**一句话要点**：提出GBMPO框架，扩展基于组的策略优化至灵活Bregman散度，提升LLM推理性能。

**关键词**：策略优化, Bregman散度, LLM推理, 数学推理, 代码生成, 神经镜像映射

## 3 点简述
- 现有基于组的策略优化方法仅使用KL散度进行正则化，散度函数选择未被探索。
- GBMPO引入灵活Bregman散度，包括手动设计（如概率空间L2）和学习的神经镜像映射。
- 在GSM8K数学推理和MBPP代码生成任务上，GBMPO显著提升准确率，神经镜像映射随机初始化已足够实用。

## 摘要（原文）

> Policy optimization methods like Group Relative Policy Optimization (GRPO) and its variants have achieved strong results on mathematical reasoning and code generation tasks. Despite extensive exploration of reward processing strategies and training dynamics, all existing group-based methods exclusively use KL divergence for policy regularization, leaving the choice of divergence function unexplored. We introduce Group-Based Mirror Policy Optimization (GBMPO), a framework that extends group-based policy optimization to flexible Bregman divergences, including hand-designed alternatives (L2 in probability space) and learned neural mirror maps. On GSM8K mathematical reasoning, hand-designed ProbL2-GRPO achieves 86.7% accuracy, improving +5.5 points over the Dr. GRPO baseline. On MBPP code generation, neural mirror maps reach 60.1-60.8% pass@1, with random initialization already capturing most of the benefit. While evolutionary strategies meta-learning provides marginal accuracy improvements, its primary value lies in variance reduction ($\pm$0.2 versus $\pm$0.6) and efficiency gains (15% shorter responses on MBPP), suggesting that random initialization of neural mirror maps is sufficient for most practical applications. These results establish divergence choice as a critical, previously unexplored design dimension in group-based policy optimization for LLM reasoning.

