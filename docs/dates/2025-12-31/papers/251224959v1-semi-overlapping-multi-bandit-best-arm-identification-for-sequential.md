---
layout: default
title: Semi-overlapping Multi-bandit Best Arm Identification for Sequential Support Network Learning
---

# Semi-overlapping Multi-bandit Best Arm Identification for Sequential Support Network Learning
**arXiv**：[2512.24959v1](https://arxiv.org/abs/2512.24959) · [PDF](https://arxiv.org/pdf/2512.24959.pdf)  
**作者**：András Antos, András Millinghoffer, Péter Antal  

**一句话要点**：提出半重叠多臂赌博机模型以高效学习序列支持网络，提升多任务学习等场景的样本效率。

**关键词**：序列支持网络学习, 多臂赌博机, 最佳臂识别, 多任务学习, 联邦学习, 样本复杂度

## 3 点简述
- 核心问题：在序列支持网络学习中，如何从稀疏候选列表中高效识别最优合作伙伴集，涉及共享但不对称的评估过程。
- 方法要点：引入半重叠多臂赌博机模型，利用臂的结构重叠实现单次评估为多个赌博机提供反馈，并开发广义GapE算法。
- 实验或效果：推导出指数误差界，显示样本复杂度随重叠度线性缩放，为多任务学习等应用提供理论改进。

## 摘要（原文）

> Many modern AI and ML problems require evaluating partners' contributions through shared yet asymmetric, computationally intensive processes and the simultaneous selection of the most beneficial candidates. Sequential approaches to these problems can be unified under a new framework, Sequential Support Network Learning (SSNL), in which the goal is to select the most beneficial candidate set of partners for all participants using trials; that is, to learn a directed graph that represents the highest-performing contributions. We demonstrate that a new pure-exploration model, the semi-overlapping multi-(multi-armed) bandit (SOMMAB), in which a single evaluation provides distinct feedback to multiple bandits due to structural overlap among their arms, can be used to learn a support network from sparse candidate lists efficiently.
>   We develop a generalized GapE algorithm for SOMMABs and derive new exponential error bounds that improve the best known constant in the exponent for multi-bandit best-arm identification. The bounds scale linearly with the degree of overlap, revealing significant sample-complexity gains arising from shared evaluations.
>   From an application point of view, this work provides a theoretical foundation and improved performance guarantees for sequential learning tools for identifying support networks from sparse candidates in multiple learning problems, such as in multi-task learning (MTL), auxiliary task learning (ATL), federated learning (FL), and in multi-agent systems (MAS).

