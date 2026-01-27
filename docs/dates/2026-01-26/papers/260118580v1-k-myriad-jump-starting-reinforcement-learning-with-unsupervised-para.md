---
layout: default
title: K-Myriad: Jump-starting reinforcement learning with unsupervised parallel agents
---

# K-Myriad: Jump-starting reinforcement learning with unsupervised parallel agents
**arXiv**：[2601.18580v1](https://arxiv.org/abs/2601.18580) · [PDF](https://arxiv.org/pdf/2601.18580.pdf)  
**作者**：Vincenzo De Paola, Mirco Mutti, Riccardo Zamboni, Marcello Restelli  

**一句话要点**：提出K-Myriad方法，通过无监督并行代理最大化状态熵以提升强化学习初始化效率

**关键词**：强化学习, 并行化策略, 无监督探索, 状态熵最大化, 连续控制任务

## 3 点简述
- 核心问题：传统并行强化学习采用相同采样分布，限制了多样化探索策略的优势。
- 方法要点：K-Myriad通过最大化并行策略群体诱导的集体状态熵，培养专业化探索策略组合。
- 实验或效果：在高维连续控制任务中，K-Myriad能学习到多样策略，提高训练效率和发现异构解决方案。

## 摘要（原文）

> Parallelization in Reinforcement Learning is typically employed to speed up the training of a single policy, where multiple workers collect experience from an identical sampling distribution. This common design limits the potential of parallelization by neglecting the advantages of diverse exploration strategies. We propose K-Myriad, a scalable and unsupervised method that maximizes the collective state entropy induced by a population of parallel policies. By cultivating a portfolio of specialized exploration strategies, K-Myriad provides a robust initialization for Reinforcement Learning, leading to both higher training efficiency and the discovery of heterogeneous solutions. Experiments on high-dimensional continuous control tasks, with large-scale parallelization, demonstrate that K-Myriad can learn a broad set of distinct policies, highlighting its effectiveness for collective exploration and paving the way towards novel parallelization strategies.

