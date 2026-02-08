---
layout: default
title: Perception-Based Beliefs for POMDPs with Visual Observations
---

# Perception-Based Beliefs for POMDPs with Visual Observations
**arXiv**：[2602.05679v1](https://arxiv.org/abs/2602.05679) · [PDF](https://arxiv.org/pdf/2602.05679.pdf)  
**作者**：Miriam Schäfers, Merlijn Krale, Thiago D. Simão, Nils Jansen, Maximilian Weininger  

**一句话要点**：提出PBP框架，结合感知模型解决高维视觉观测POMDP规划问题

**关键词**：部分可观测马尔可夫决策过程, 视觉观测, 信念更新, 感知模型, 不确定性量化, 规划算法

## 3 点简述
- 核心问题：传统POMDP求解器难以处理高维视觉观测，如相机图像，导致规划不可行
- 方法要点：引入感知模型（图像分类器），将视觉观测映射为状态概率分布，直接集成到信念更新中
- 实验或效果：PBP优于端到端深度RL方法，不确定性量化提升对视觉损坏的鲁棒性

## 摘要（原文）

> Partially observable Markov decision processes (POMDPs) are a principled planning model for sequential decision-making under uncertainty. Yet, real-world problems with high-dimensional observations, such as camera images, remain intractable for traditional belief- and filtering-based solvers. To tackle this problem, we introduce the Perception-based Beliefs for POMDPs framework (PBP), which complements such solvers with a perception model. This model takes the form of an image classifier which maps visual observations to probability distributions over states. PBP incorporates these distributions directly into belief updates, so the underlying solver does not need to reason explicitly over high-dimensional observation spaces. We show that the belief update of PBP coincides with the standard belief update if the image classifier is exact. Moreover, to handle classifier imprecision, we incorporate uncertainty quantification and introduce two methods to adjust the belief update accordingly. We implement PBP using two traditional POMDP solvers and empirically show that (1) it outperforms existing end-to-end deep RL methods and (2) uncertainty quantification improves robustness of PBP against visual corruption.

