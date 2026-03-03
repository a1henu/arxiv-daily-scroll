---
layout: default
title: Stochastic Multi-Armed Bandits with Limited Control Variates
---

# Stochastic Multi-Armed Bandits with Limited Control Variates
**arXiv**：[2603.02100v1](https://arxiv.org/abs/2603.02100) · [PDF](https://arxiv.org/pdf/2603.02100.pdf)  
**作者**：Arun Verma, Manjesh Kumar Hanawal, Arun Rajkumar  

**一句话要点**：提出UCB-LCV算法以解决有限控制变量下的随机多臂老虎机问题

**关键词**：随机多臂老虎机, 控制变量, 置信界算法, 无线网络应用, 正态分布奖励

## 3 点简述
- 研究随机多臂老虎机问题，其中学习者仅能有限获取辅助信息作为控制变量
- 提出UCB-LCV算法，结合奖励和控制变量估计器，提升置信界紧密度
- 实验表明UCB-LCV优于现有算法，并衍生出UCB-NORMAL用于正态分布奖励

## 摘要（原文）

> Motivated by wireless networks where interference or channel state estimates provide partial insight into throughput, we study a variant of the classical stochastic multi-armed bandit problem in which the learner has limited access to auxiliary information. Recent work has shown that such auxiliary information, when available as control variates, can be used to get tighter confidence bounds, leading to lower regret. However, existing works assume that control variates are available in every round, which may not be realistic in several real-life scenarios. To address this, we propose UCB-LCV, an upper confidence bound (UCB) based algorithm that effectively combines the estimators obtained from rewards and control variates. When there is no control variate, UCB-LCV leads to a novel algorithm that we call UCB-NORMAL, outperforming its existing algorithms for the standard MAB setting with normally distributed rewards. Finally, we discuss variants of the proposed UCB-LCV that apply to general distributions and experimentally demonstrate that UCB-LCV outperforms existing bandit algorithms.

