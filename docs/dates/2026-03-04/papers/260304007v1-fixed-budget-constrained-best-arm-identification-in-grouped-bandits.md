---
layout: default
title: Fixed-Budget Constrained Best Arm Identification in Grouped Bandits
---

# Fixed-Budget Constrained Best Arm Identification in Grouped Bandits
**arXiv**：[2603.04007v1](https://arxiv.org/abs/2603.04007) · [PDF](https://arxiv.org/pdf/2603.04007.pdf)  
**作者**：Raunak Mukherjee, Sharayu Moharir  

**一句话要点**：提出FCSR算法以解决分组多臂老虎机中固定预算约束下的最优可行臂识别问题

**关键词**：分组多臂老虎机, 固定预算约束, 最优臂识别, 可行性约束, FCSR算法, 随机奖励

## 3 点简述
- 研究分组多臂老虎机中固定预算约束下的最优可行臂识别，要求所有属性均值超过阈值
- 提出FCSR算法，在确保可行性的同时识别最优臂，理论证明达到参数依赖的最优性
- 实验显示FCSR优于基线方法，并保持可行性保证

## 摘要（原文）

> We study fixed budget constrained best-arm identification in grouped bandits, where each arm consists of multiple independent attributes with stochastic rewards. An arm is considered feasible only if all its attributes' means are above a given threshold. The aim is to find the feasible arm with the largest overall mean. We first derive a lower bound on the error probability for any algorithm on this setting. We then propose Feasibility Constrained Successive Rejects (FCSR), a novel algorithm that identifies the best arm while ensuring feasibility. We show it attains optimal dependence on problem parameters up to constant factors in the exponent. Empirically, FCSR outperforms natural baselines while preserving feasibility guarantees.

