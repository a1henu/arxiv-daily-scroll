---
layout: default
title: Emergence of Nonequilibrium Latent Cycles in Unsupervised Generative Modeling
---

# Emergence of Nonequilibrium Latent Cycles in Unsupervised Generative Modeling
**arXiv**：[2512.11415v1](https://arxiv.org/abs/2512.11415) · [PDF](https://arxiv.org/pdf/2512.11415.pdf)  
**作者**：Marco Baiesi, Alberto Rosso  

**一句话要点**：提出非平衡隐变量循环模型以增强无监督生成性能

**关键词**：非平衡统计物理, 无监督生成模型, 隐变量循环, 马尔可夫链, 熵产生

## 3 点简述
- 核心问题：传统平衡模型如受限玻尔兹曼机在生成任务中可能因可逆动态导致低似然。
- 方法要点：引入双参数化转移矩阵的马尔可夫链，打破详细平衡，驱动隐空间形成自发循环。
- 实验或效果：模型通过最大化似然实现非平衡稳态，提高数据类分布拟合度，避免低似然区域。

## 摘要（原文）

> We show that nonequilibrium dynamics can play a constructive role in unsupervised machine learning by inducing the spontaneous emergence of latent-state cycles. We introduce a model in which visible and hidden variables interact through two independently parametrized transition matrices, defining a Markov chain whose steady state is intrinsically out of equilibrium. Likelihood maximization drives this system toward nonequilibrium steady states with finite entropy production, reduced self-transition probabilities, and persistent probability currents in the latent space. These cycles are not imposed by the architecture but arise from training, and models that develop them avoid the low-log-likelihood regime associated with nearly reversible dynamics while more faithfully reproducing the empirical distribution of data classes. Compared with equilibrium approaches such as restricted Boltzmann machines, our model breaks the detailed balance between the forward and backward conditional transitions and relies on a log-likelihood gradient that depends explicitly on the last two steps of the Markov chain. Hence, this exploration of the interface between nonequilibrium statistical physics and modern machine learning suggests that introducing irreversibility into latent-variable models can enhance generative performance.

