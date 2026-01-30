---
layout: default
title: Managing Solution Stability in Decision-Focused Learning with Cost Regularization
---

# Managing Solution Stability in Decision-Focused Learning with Cost Regularization
**arXiv**：[2601.21883v1](https://arxiv.org/abs/2601.21883) · [PDF](https://arxiv.org/pdf/2601.21883.pdf)  
**作者**：Victor Spitzer, Francois Sanson  

**一句话要点**：提出成本向量正则化以解决决策聚焦学习中扰动强度波动导致的训练失效问题

**关键词**：决策聚焦学习, 组合优化, 成本正则化, 解稳定性, 扰动近似

## 3 点简述
- 核心问题：决策聚焦学习中扰动强度波动影响训练效果，与组合优化解稳定性相关
- 方法要点：引入成本向量正则化，提升学习过程的鲁棒性和可靠性
- 实验或效果：通过大量数值实验验证了方法的有效性

## 摘要（原文）

> Decision-focused learning integrates predictive modeling and combinatorial optimization by training models to directly improve decision quality rather than prediction accuracy alone. Differentiating through combinatorial optimization problems represents a central challenge, and recent approaches tackle this difficulty by introducing perturbation-based approximations. In this work, we focus on estimating the objective function coefficients of a combinatorial optimization problem. Our study demonstrates that fluctuations in perturbation intensity occurring during the learning phase can lead to ineffective training, by establishing a theoretical link to the notion of solution stability in combinatorial optimization. We propose addressing this issue by introducing a regularization of the estimated cost vectors which improves the robustness and reliability of the learning process, as demonstrated by extensive numerical experiments.

