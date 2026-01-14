---
layout: default
title: Greedy Is Enough: Sparse Action Discovery in Agentic LLMs
---

# Greedy Is Enough: Sparse Action Discovery in Agentic LLMs
**arXiv**：[2601.08280v1](https://arxiv.org/abs/2601.08280) · [PDF](https://arxiv.org/pdf/2601.08280.pdf)  
**作者**：Angshul Majumdar  

**一句话要点**：提出基于贪婪算法的稀疏动作发现方法，以解决智能体系统在大动作空间中的决策效率问题。

**关键词**：稀疏动作发现, 贪婪算法, 智能体系统, 大动作空间, 理论分析

## 3 点简述
- 核心问题：大动作空间中仅少数动作有效，需高效识别相关动作集。
- 方法要点：采用贪婪算法，在结构化稀疏假设下，理论保证高概率精确恢复相关动作。
- 实验或效果：样本需求随稀疏度和潜在维度多项式增长，动作总数对数增长，决策规则接近最优。

## 摘要（原文）

> Modern agentic systems operate in environments with extremely large action spaces, such as tool-augmented language models with thousands of available APIs or retrieval operations. Despite this scale, empirical evidence suggests that only a small subset of actions meaningfully influences performance in a given deployment. Motivated by this observation, we study a contextual linear reward model in which action relevance is governed by a structured sparsity assumption: only a small number of actions have nonzero effects across latent states.
>   We formulate action discovery as a block-sparse recovery problem and analyze a greedy algorithm inspired by Orthogonal Matching Pursuit. Under standard assumptions on incoherence, signal strength, and action coverage, we prove that the greedy procedure exactly recovers the relevant action set with high probability, using a number of samples that scales polynomially in the sparsity level and latent dimension, and only logarithmically in the total number of actions. We further provide estimation error guarantees for refitted parameters and show that the resulting decision rule is near-optimal for new latent states.
>   Complementing these results, we establish information-theoretic lower bounds demonstrating that sparsity and sufficient coverage are necessary for tractability. Together, our results identify sparse action discovery as a fundamental principle underlying large-action decision-making and provide a theoretical foundation for action pruning in agentic systems.

