---
layout: default
title: Owen-Shapley Policy Optimization (OSPO): A Principled RL Algorithm for Generative Search LLMs
---

# Owen-Shapley Policy Optimization (OSPO): A Principled RL Algorithm for Generative Search LLMs
**arXiv**：[2601.08403v1](https://arxiv.org/abs/2601.08403) · [PDF](https://arxiv.org/pdf/2601.08403.pdf)  
**作者**：Abhijnan Nath, Alireza Bagheri Garakani, Tianchen Zhou, Fan Yang, Nikhil Krishnaswamy  

**一句话要点**：提出Owen-Shapley策略优化以解决生成式搜索大语言模型中的信用分配问题

**关键词**：强化学习, 信用分配, 大语言模型, 生成式搜索, Shapley值, 推荐系统

## 3 点简述
- 核心问题：序列级稀疏奖励导致信用分配困难，难以识别驱动成功的令牌
- 方法要点：基于Shapley-Owen归因，通过潜在奖励塑形分配段级信用，无需参数化价值模型
- 实验或效果：在Amazon ESCI和H&M Fashion数据集上优于基线，对未见检索器具有鲁棒性

## 摘要（原文）

> Large language models are increasingly trained via reinforcement learning for personalized recommendation tasks, but standard methods like GRPO rely on sparse, sequence-level rewards that create a credit assignment gap, obscuring which tokens drive success. This gap is especially problematic when models must infer latent user intent from under-specified language without ground truth labels, a reasoning pattern rarely seen during pretraining. We introduce Owen-Shapley Policy Optimization (OSPO), a framework that redistributes sequence-level advantages based on tokens' marginal contributions to outcomes. Unlike value-model-based methods requiring additional computation, OSPO employs potential-based reward shaping via Shapley-Owen attributions to assign segment-level credit while preserving the optimal policy, learning directly from task feedback without parametric value models. By forming coalitions of semantically coherent units (phrases describing product attributes or sentences capturing preferences), OSPO identifies which response parts drive performance. Experiments on Amazon ESCI and H&M Fashion datasets show consistent gains over baselines, with notable test-time robustness to out-of-distribution retrievers unseen during training.

