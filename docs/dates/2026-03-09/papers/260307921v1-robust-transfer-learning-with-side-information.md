---
layout: default
title: Robust Transfer Learning with Side Information
---

# Robust Transfer Learning with Side Information
**arXiv**：[2603.07921v1](https://arxiv.org/abs/2603.07921) · [PDF](https://arxiv.org/pdf/2603.07921.pdf)  
**作者**：Akram S. Awad, Shihab Ahmed, Yue Wang, George K. Atia  

**一句话要点**：提出基于侧信息的鲁棒迁移学习框架，以解决环境偏移下马尔可夫决策过程的保守策略问题。

**关键词**：鲁棒马尔可夫决策过程, 分布鲁棒优化, 迁移学习, 环境偏移, 不确定性集, 侧信息

## 3 点简述
- 核心问题：标准分布鲁棒优化在环境大偏移时需扩大不确定性集，导致策略过于保守和悲观。
- 方法要点：通过整合有限目标样本和源-目标动态侧信息，构建估计中心不确定性集，以改进核估计并收紧不确定性。
- 实验或效果：在OpenAI Gym环境和经典控制问题中评估，显示优于现有鲁棒和非鲁棒基线的目标域性能。

## 摘要（原文）

> Robust Markov Decision Processes (MDPs) address environmental shift through distributionally robust optimization (DRO) by finding an optimal worst-case policy within an uncertainty set of transition kernels. However, standard DRO approaches require enlarging the uncertainty set under large shifts, which leads to overly conservative and pessimistic policies.
>   In this paper, we propose a framework for transfer under environment shift that derives a robust target-domain policy via estimate-centered uncertainty sets, constructed through constrained estimation that integrates limited target samples with side information about the source-target dynamics. The side information includes bounds on feature moments, distributional distances, and density ratios, yielding improved kernel estimates and tighter uncertainty sets.
>   The side information includes bounds on feature moments, distributional distances, and density ratios, yielding improved kernel estimates and tighter uncertainty sets.
>   Error bounds and convergence results are established for both robust and non-robust value functions. Moreover, we provide a finite-sample guarantee on the learned robust policy and analyze the robust sub-optimality gap. Under mild low-dimensional structure on the transition model, the side information reduces this gap and improves sample efficiency. We assess the performance of our approach across OpenAI Gym environments and classic control problems, consistently demonstrating superior target-domain performance over state-of-the-art robust and non-robust baselines.

