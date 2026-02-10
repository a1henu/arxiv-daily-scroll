---
layout: default
title: Dynamic Regret via Discounted-to-Dynamic Reduction with Applications to Curved Losses and Adam Optimizer
---

# Dynamic Regret via Discounted-to-Dynamic Reduction with Applications to Curved Losses and Adam Optimizer
**arXiv**：[2602.08372v1](https://arxiv.org/abs/2602.08372) · [PDF](https://arxiv.org/pdf/2602.08372.pdf)  
**作者**：Yan-Feng Xie, Yu-Jie Zhang, Peng Zhao, Zhi-Hua Zhou  

**一句话要点**：提出基于折扣到动态约简的模块化方法，以分析FTRL在非平稳在线学习中的动态遗憾，并应用于曲线损失和Adam优化器。

**关键词**：动态遗憾, 非平稳在线学习, FTRL方法, 曲线损失, Adam优化器, 折扣约简

## 3 点简述
- 研究非平稳在线学习中的动态遗憾最小化，重点关注FTRL方法及其在曲线损失和Adam优化器中的应用。
- 基于折扣到动态约简，提供模块化方式推导FTRL相关问题的动态遗憾界，简化线性回归证明并扩展至逻辑回归。
- 将约简应用于Adam优化器分析，在随机、非凸、非光滑设置下获得最优收敛率，并处理带两个折扣参数的变体。

## 摘要（原文）

> We study dynamic regret minimization in non-stationary online learning, with a primary focus on follow-the-regularized-leader (FTRL) methods. FTRL is important for curved losses and for understanding adaptive optimizers such as Adam, yet existing dynamic regret analyses are less explored for FTRL. To address this, we build on the discounted-to-dynamic reduction and present a modular way to obtain dynamic regret bounds of FTRL-related problems. Specifically, we focus on two representative curved losses: linear regression and logistic regression. Our method not only simplifies existing proofs for the optimal dynamic regret of online linear regression, but also yields new dynamic regret guarantees for online logistic regression. Beyond online convex optimization, we apply the reduction to analyze the Adam optimizers, obtaining optimal convergence rates in stochastic, non-convex, and non-smooth settings. The reduction also enables a more detailed treatment of Adam with two discount parameters $(β_1,β_2)$, leading to new results for both clipped and clip-free variants of Adam optimizers.

