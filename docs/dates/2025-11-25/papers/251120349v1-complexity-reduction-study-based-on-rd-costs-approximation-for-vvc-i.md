---
layout: default
title: Complexity Reduction Study Based on RD Costs Approximation for VVC Intra Partitioning
---

# Complexity Reduction Study Based on RD Costs Approximation for VVC Intra Partitioning
**arXiv**：[2511.20349v1](https://arxiv.org/abs/2511.20349) · [PDF](https://arxiv.org/pdf/2511.20349.pdf)  
**作者**：M. E. A. Kherchouche, F. Galpin, T. Dumas, F. Schnitzler, D. Menard, L. Zhang  

**一句话要点**：提出基于RD成本近似的机器学习方法以加速VVC帧内分区的复杂度优化

**关键词**：VVC帧内分区, RD成本近似, 回归预测, 强化学习, 复杂度降低, CU分割决策

## 3 点简述
- 核心问题：VVC帧内分区中RDO过程计算复杂度高，需加速穷举搜索。
- 方法要点：使用回归预测归一化RD成本，并基于MDP采用RL代理决策分区。
- 实验或效果：应用预定义阈值选择CU分割，比较两种方法的性能。

## 摘要（原文）

> In this paper, a complexity study is conducted for Versatile Video Codec (VVC) intra partitioning to accelerate the exhaustive search involved in Rate-Distortion Optimization (RDO) process. To address this problem, two main machine learning techniques are proposed and compared. Unlike existing methods, the proposed approaches are size independent and incorporate the Rate-Distortion (RD) costs of neighboring blocks as input features. The first method is a regression based technique that predicts normalized RD costs of a given Coding Unit (CU). As partitioning possesses the Markov property, the associated decision-making problem can be modeled as a Markov Decision Process (MDP) and solved by Reinforcement Learning (RL). The second approach is a RL agent learned from trajectories of CU decision across two depths with Deep Q-Network (DQN) algorithm. Then a pre-determined thresholds are applied for both methods to select a suitable split for the current CU.

