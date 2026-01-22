---
layout: default
title: DARA: Few-shot Budget Allocation in Online Advertising via In-Context Decision Making with RL-Finetuned LLMs
---

# DARA: Few-shot Budget Allocation in Online Advertising via In-Context Decision Making with RL-Finetuned LLMs
**arXiv**：[2601.14711v1](https://arxiv.org/abs/2601.14711) · [PDF](https://arxiv.org/pdf/2601.14711.pdf)  
**作者**：Mingxuan Song, Yusen Huo, Bohan Zhou, Shenglin Yin, Zhen Xiao, Jieyi Long, Zhilin Zhang, Chuan Yu  

**一句话要点**：提出DARA框架，通过双阶段决策解决在线广告中少样本预算分配问题。

**关键词**：在线广告, 少样本学习, 预算分配, 大语言模型, 强化学习, 决策框架

## 3 点简述
- 核心问题：在线广告中，广告商在预算约束下优化累积价值，面临少样本场景，传统强化学习方法效果不佳。
- 方法要点：提出GRPO-Adaptive策略增强LLM数值精度，并设计DARA双阶段框架，结合少样本推理和细粒度优化。
- 实验或效果：在真实和合成数据环境中，DARA在预算约束下累积广告商价值方面优于现有基线。

## 摘要（原文）

> Optimizing the advertiser's cumulative value of winning impressions under budget constraints poses a complex challenge in online advertising, under the paradigm of AI-Generated Bidding (AIGB). Advertisers often have personalized objectives but limited historical interaction data, resulting in few-shot scenarios where traditional reinforcement learning (RL) methods struggle to perform effectively. Large Language Models (LLMs) offer a promising alternative for AIGB by leveraging their in-context learning capabilities to generalize from limited data. However, they lack the numerical precision required for fine-grained optimization. To address this limitation, we introduce GRPO-Adaptive, an efficient LLM post-training strategy that enhances both reasoning and numerical precision by dynamically updating the reference policy during training. Built upon this foundation, we further propose DARA, a novel dual-phase framework that decomposes the decision-making process into two stages: a few-shot reasoner that generates initial plans via in-context prompting, and a fine-grained optimizer that refines these plans using feedback-driven reasoning. This separation allows DARA to combine LLMs' in-context learning strengths with precise adaptability required by AIGB tasks. Extensive experiments on both real-world and synthetic data environments demonstrate that our approach consistently outperforms existing baselines in terms of cumulative advertiser value under budget constraints.

