---
layout: default
title: Multi-agent imitation learning with function approximation: Linear Markov games and beyond
---

# Multi-agent imitation learning with function approximation: Linear Markov games and beyond
**arXiv**：[2602.22810v1](https://arxiv.org/abs/2602.22810) · [PDF](https://arxiv.org/pdf/2602.22810.pdf)  
**作者**：Luca Viano, Till Freihaut, Emanuele Nevali, Volkan Cevher, Matthieu Geist, Giorgia Ramponi  

**一句话要点**：提出多智能体模仿学习理论框架，基于线性马尔可夫博弈，优化样本复杂度并实现高效交互算法。

**关键词**：多智能体模仿学习, 线性马尔可夫博弈, 特征映射, 样本复杂度, 交互式算法, 理论分析

## 3 点简述
- 核心问题：分析多智能体模仿学习在具有线性结构的马尔可夫博弈中的理论性能，解决传统方法样本复杂度高的问题。
- 方法要点：利用特征映射结构，将状态-动作级集中系数替换为特征级系数，降低样本需求；并设计交互式算法，样本复杂度仅依赖于特征维度。
- 实验或效果：在Tic-Tac-Toe和Connect4等游戏中，提出的深度交互算法明显优于行为克隆方法。

## 摘要（原文）

> In this work, we present the first theoretical analysis of multi-agent imitation learning (MAIL) in linear Markov games where both the transition dynamics and each agent's reward function are linear in some given features. We demonstrate that by leveraging this structure, it is possible to replace the state-action level "all policy deviation concentrability coefficient" (Freihaut et al., arXiv:2510.09325) with a concentrability coefficient defined at the feature level which can be much smaller than the state-action analog when the features are informative about states' similarity. Furthermore, to circumvent the need for any concentrability coefficient, we turn to the interactive setting. We provide the first, computationally efficient, interactive MAIL algorithm for linear Markov games and show that its sample complexity depends only on the dimension of the feature map $d$. Building on these theoretical findings, we propose a deep MAIL interactive algorithm which clearly outperforms BC on games such as Tic-Tac-Toe and Connect4.

