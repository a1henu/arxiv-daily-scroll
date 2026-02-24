---
layout: default
title: Bayesian Meta-Learning with Expert Feedback for Task-Shift Adaptation through Causal Embeddings
---

# Bayesian Meta-Learning with Expert Feedback for Task-Shift Adaptation through Causal Embeddings
**arXiv**：[2602.19788v1](https://arxiv.org/abs/2602.19788) · [PDF](https://arxiv.org/pdf/2602.19788.pdf)  
**作者**：Lotta Mäkinen, Jorge Loría, Samuel Kaski  

**一句话要点**：提出基于因果嵌入的贝叶斯元学习方法，利用专家反馈进行任务偏移适应

**关键词**：贝叶斯元学习, 因果嵌入, 任务偏移适应, 负迁移缓解, 专家反馈, 临床预测

## 3 点简述
- 核心问题：元学习方法在分布外任务上易因负迁移而失败
- 方法要点：通过因果任务嵌入调节任务特定先验，基于机制相似性而非虚假相关性进行迁移
- 实验或效果：在模拟和临床预测中减少负迁移，提升分布外适应能力

## 摘要（原文）

> Meta-learning methods perform well on new within-distribution tasks but often fail when adapting to out-of-distribution target tasks, where transfer from source tasks can induce negative transfer. We propose a causally-aware Bayesian meta-learning method, by conditioning task-specific priors on precomputed latent causal task embeddings, enabling transfer based on mechanistic similarity rather than spurious correlations. Our approach explicitly considers realistic deployment settings where access to target-task data is limited, and adaptation relies on noisy (expert-provided) pairwise judgments of causal similarity between source and target tasks. We provide a theoretical analysis showing that conditioning on causal embeddings controls prior mismatch and mitigates negative transfer under task shift. Empirically, we demonstrate reductions in negative transfer and improved out-of-distribution adaptation in both controlled simulations and a large-scale real-world clinical prediction setting for cross-disease transfer, where causal embeddings align with underlying clinical mechanisms.

