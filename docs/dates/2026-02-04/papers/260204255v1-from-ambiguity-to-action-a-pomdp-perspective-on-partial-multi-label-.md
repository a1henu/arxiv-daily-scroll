---
layout: default
title: From Ambiguity to Action: A POMDP Perspective on Partial Multi-Label Ambiguity and Its Horizon-One Resolution
---

# From Ambiguity to Action: A POMDP Perspective on Partial Multi-Label Ambiguity and Its Horizon-One Resolution
**arXiv**：[2602.04255v1](https://arxiv.org/abs/2602.04255) · [PDF](https://arxiv.org/pdf/2602.04255.pdf)  
**作者**：Hanlin Pan, Yuhao Tang, Wanfu Gao  

**一句话要点**：提出基于POMDP的框架以解决部分多标签学习中的标签消歧与特征选择问题

**关键词**：部分多标签学习, 标签消歧, 强化学习, 特征选择, POMDP, Transformer策略

## 3 点简述
- 核心问题：部分多标签学习中真实标签未观测，标签模糊性易传播错误至下游任务
- 方法要点：将消歧与特征选择建模为POMDP，分两阶段训练Transformer策略进行强化学习
- 实验或效果：多数据集验证框架优势，理论分析提供误差分解与风险界

## 摘要（原文）

> In partial multi-label learning (PML), the true labels are unobserved, which makes label disambiguation important but difficult. A key challenge is that ambiguous candidate labels can propagate errors into downstream tasks such as feature engineering. To solve this issue, we jointly model the disambiguation and feature selection tasks as Partially Observable Markov Decision Processes (POMDP) to turn PML risk minimization into expected-return maximization. Stage 1 trains a transformer policy via reinforcement learning to produce high-quality hard pseudo-labels; Stage 2 describes feature selection as a sequential reinforcement learning problem, selecting features step by step and outputting an interpretable global ranking. We further provide the theoretical analysis of PML-POMDP correspondence and the excess-risk bound that decompose the error into pseudo label quality term and sample size. Experiments in multiple metrics and data sets verify the advantages of the framework.

