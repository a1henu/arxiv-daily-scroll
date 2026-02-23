---
layout: default
title: Homotopic information gain for sparse active target tracking
---

# Homotopic information gain for sparse active target tracking
**arXiv**：[2602.17926v1](https://arxiv.org/abs/2602.17926) · [PDF](https://arxiv.org/pdf/2602.17926.pdf)  
**作者**：Jennifer Wakulicz, Ki Myung Brian Lee, Teresa Vidal-Calleja, Robert Fitch  

**一句话要点**：提出同伦信息增益以解决多模态运动模型下主动目标跟踪的稀疏规划问题

**关键词**：主动目标跟踪, 同伦信息增益, 多模态运动模型, 稀疏规划, 移动机器人, 轨迹预测

## 3 点简述
- 核心问题：多模态运动模型下信息增益定义模糊，影响移动机器人主动目标跟踪的规划效果
- 方法要点：引入同伦信息增益，作为度量信息增益的下界，用于最大化目标高层运动信息
- 实验或效果：在真实和模拟行人数据上验证，相比度量信息方法，能以更少测量获得高精度轨迹估计

## 摘要（原文）

> The problem of planning sensing trajectories for a mobile robot to collect observations of a target and predict its future trajectory is known as active target tracking. Enabled by probabilistic motion models, one may solve this problem by exploring the belief space of all trajectory predictions given future sensing actions to maximise information gain. However, for multi-modal motion models the notion of information gain is often ill-defined. This paper proposes a planning approach designed around maximising information regarding the target's homotopy class, or high-level motion. We introduce homotopic information gain, a measure of the expected high-level trajectory information given by a measurement. We show that homotopic information gain is a lower bound for metric or low-level information gain, and is as sparsely distributed in the environment as obstacles are. Planning sensing trajectories to maximise homotopic information results in highly accurate trajectory estimates with fewer measurements than a metric information approach, as supported by our empirical evaluation on real and simulated pedestrian data.

