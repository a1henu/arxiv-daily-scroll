---
layout: default
title: Convex Markov Games and Beyond: New Proof of Existence, Characterization and Learning Algorithms for Nash Equilibria
---

# Convex Markov Games and Beyond: New Proof of Existence, Characterization and Learning Algorithms for Nash Equilibria
**arXiv**：[2602.12181v1](https://arxiv.org/abs/2602.12181) · [PDF](https://arxiv.org/pdf/2602.12181.pdf)  
**作者**：Anas Barakat, Ioannis Panageas, Antonios Varvitsiotis  

**一句话要点**：提出广义效用马尔可夫博弈，证明纳什均衡存在性并提供学习算法理论保证

**关键词**：广义效用马尔可夫博弈, 纳什均衡, 策略梯度算法, 代理梯度支配性, 势博弈, 样本复杂度

## 3 点简述
- 研究广义效用马尔可夫博弈，扩展凸马尔可夫博弈以建模代理占用测度耦合的应用
- 证明纳什均衡与投影伪梯度动态固定点重合，基于代理梯度支配性提供存在性新证明
- 建立策略梯度定理，设计无模型算法，并在势博弈中提供迭代和样本复杂度保证

## 摘要（原文）

> Convex Markov Games (cMGs) were recently introduced as a broad class of multi-agent learning problems that generalize Markov games to settings where strategic agents optimize general utilities beyond additive rewards. While cMGs expand the modeling frontier, their theoretical foundations, particularly the structure of Nash equilibria (NE) and guarantees for learning algorithms, are not yet well understood. In this work, we address these gaps for an extension of cMGs, which we term General Utility Markov Games (GUMGs), capturing new applications requiring coupling between agents' occupancy measures. We prove that in GUMGs, Nash equilibria coincide with the fixed points of projected pseudo-gradient dynamics (i.e., first-order stationary points), enabled by a novel agent-wise gradient domination property. This insight also yields a simple proof of NE existence using Brouwer's fixed-point theorem. We further show the existence of Markov perfect equilibria. Building on this characterization, we establish a policy gradient theorem for GUMGs and design a model-free policy gradient algorithm. For potential GUMGs, we establish iteration complexity guarantees for computing approximate-NE under exact gradients and provide sample complexity bounds in both the generative model and on-policy settings. Our results extend beyond prior work restricted to zero-sum cMGs, providing the first theoretical analysis of common-interest cMGs.

