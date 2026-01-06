---
layout: default
title: Distorted Distributional Policy Evaluation for Offline Reinforcement Learning
---

# Distorted Distributional Policy Evaluation for Offline Reinforcement Learning
**arXiv**：[2601.01917v1](https://arxiv.org/abs/2601.01917) · [PDF](https://arxiv.org/pdf/2601.01917.pdf)  
**作者**：Ryo Iwaki, Takayuki Osogami  

**一句话要点**：提出分位数扭曲方法以解决离线分布强化学习中均匀悲观估计的局限性

**关键词**：离线强化学习, 分布强化学习, 分位数估计, 悲观策略评估, 泛化性能

## 3 点简述
- 核心问题：离线分布强化学习中均匀低估分位数导致保守估计，限制泛化性能
- 方法要点：引入分位数扭曲概念，基于数据支持度调整悲观程度，实现非均匀悲观
- 实验或效果：理论分析支持，实证验证优于均匀悲观方法，提升性能

## 摘要（原文）

> While Distributional Reinforcement Learning (DRL) methods have demonstrated strong performance in online settings, its success in offline scenarios remains limited. We hypothesize that a key limitation of existing offline DRL methods lies in their approach to uniformly underestimate return quantiles. This uniform pessimism can lead to overly conservative value estimates, ultimately hindering generalization and performance. To address this, we introduce a novel concept called quantile distortion, which enables non-uniform pessimism by adjusting the degree of conservatism based on the availability of supporting data. Our approach is grounded in theoretical analysis and empirically validated, demonstrating improved performance over uniform pessimism.

