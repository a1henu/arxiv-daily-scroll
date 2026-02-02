---
layout: default
title: Automatic Constraint Policy Optimization based on Continuous Constraint Interpolation Framework for Offline Reinforcement Learning
---

# Automatic Constraint Policy Optimization based on Continuous Constraint Interpolation Framework for Offline Reinforcement Learning
**arXiv**：[2601.23010v1](https://arxiv.org/abs/2601.23010) · [PDF](https://arxiv.org/pdf/2601.23010.pdf)  
**作者**：Xinchen Han, Qiuyang Fang, Hossam Afifi, Michel Marot  

**一句话要点**：提出连续约束插值框架和自动约束策略优化算法，以统一离线强化学习中的约束方法并提升性能。

**关键词**：离线强化学习, 约束优化, 策略约束, 连续插值, 自动调整, 性能下界

## 3 点简述
- 核心问题：离线强化学习中约束形式和强度选择缺乏统一原则，影响性能。
- 方法要点：通过连续约束插值框架统一三种约束家族，并基于此开发自动调整插值参数的算法。
- 实验或效果：在D4RL和NeoRL2基准测试中实现稳健性能提升，达到先进水平。

## 摘要（原文）

> Offline Reinforcement Learning (RL) relies on policy constraints to mitigate extrapolation error, where both the constraint form and constraint strength critically shape performance. However, most existing methods commit to a single constraint family: weighted behavior cloning, density regularization, or support constraints, without a unified principle that explains their connections or trade-offs. In this work, we propose Continuous Constraint Interpolation (CCI), a unified optimization framework in which these three constraint families arise as special cases along a common constraint spectrum. The CCI framework introduces a single interpolation parameter that enables smooth transitions and principled combinations across constraint types. Building on CCI, we develop Automatic Constraint Policy Optimization (ACPO), a practical primal--dual algorithm that adapts the interpolation parameter via a Lagrangian dual update. Moreover, we establish a maximum-entropy performance difference lemma and derive performance lower bounds for both the closed-form optimal policy and its parametric projection. Experiments on D4RL and NeoRL2 demonstrate robust gains across diverse domains, achieving state-of-the-art performance overall.

