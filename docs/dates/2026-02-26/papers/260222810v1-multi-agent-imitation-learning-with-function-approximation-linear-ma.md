---
layout: default
title: Multi-agent imitation learning with function approximation: Linear Markov games and beyond
---

# Multi-agent imitation learning with function approximation: Linear Markov games and beyond
**arXiv**：[2602.22810v1](https://arxiv.org/abs/2602.22810) · [PDF](https://arxiv.org/pdf/2602.22810.pdf)  
**作者**：Luca Viano, Till Freihaut, Emanuele Nevali, Volkan Cevher, Matthieu Geist, Giorgia Ramponi  

**一句话要点**：提出多智能体模仿学习理论分析，在线性马尔可夫博弈中降低样本复杂度并设计高效交互算法。

**关键词**：多智能体模仿学习, 线性马尔可夫博弈, 特征级集中系数, 交互式算法, 样本复杂度

## 3 点简述
- 首次在线性马尔可夫博弈中分析多智能体模仿学习，假设转移动态和奖励函数为线性特征。
- 利用特征结构，将状态-动作级集中系数替换为特征级系数，降低样本复杂度。
- 设计交互式算法，样本复杂度仅依赖特征维度，并在Tic-Tac-Toe和Connect4游戏中超越行为克隆。

## 摘要（原文）

> In this work, we present the first theoretical analysis of multi-agent imitation learning (MAIL) in linear Markov games where both the transition dynamics and each agent's reward function are linear in some given features. We demonstrate that by leveraging this structure, it is possible to replace the state-action level "all policy deviation concentrability coefficient" (Freihaut et al., arXiv:2510.09325) with a concentrability coefficient defined at the feature level which can be much smaller than the state-action analog when the features are informative about states' similarity. Furthermore, to circumvent the need for any concentrability coefficient, we turn to the interactive setting. We provide the first, computationally efficient, interactive MAIL algorithm for linear Markov games and show that its sample complexity depends only on the dimension of the feature map $d$. Building on these theoretical findings, we propose a deep MAIL interactive algorithm which clearly outperforms BC on games such as Tic-Tac-Toe and Connect4.

