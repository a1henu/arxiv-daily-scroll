---
layout: default
title: Convex Chance-Constrained Stochastic Control under Uncertain Specifications with Application to Learning-Based Hybrid Powertrain Control
---

# Convex Chance-Constrained Stochastic Control under Uncertain Specifications with Application to Learning-Based Hybrid Powertrain Control
**arXiv**：[2601.18313v1](https://arxiv.org/abs/2601.18313) · [PDF](https://arxiv.org/pdf/2601.18313.pdf)  
**作者**：Teruki Kato, Ryotaro Shima, Kenji Kashima  

**一句话要点**：提出严格凸机会约束随机控制框架，以处理混合动力系统控制中的不确定性规范问题。

**关键词**：机会约束控制, 随机控制, 混合动力系统, 模型预测控制, 机器学习建模

## 3 点简述
- 核心问题：控制规范（如参考轨迹和操作约束）存在不确定性，需在非高斯分布下保证概率约束满足。
- 方法要点：联合优化控制输入和风险分配，确保严格凸性，实现最优解的唯一性和连续性。
- 实验或效果：应用于基于机器学习的非线性模型预测控制，在混合动力系统中验证有效性。

## 摘要（原文）

> This paper presents a strictly convex chance-constrained stochastic control framework that accounts for uncertainty in control specifications such as reference trajectories and operational constraints. By jointly optimizing control inputs and risk allocation under general (possibly non-Gaussian) uncertainties, the proposed method guarantees probabilistic constraint satisfaction while ensuring strict convexity, leading to uniqueness and continuity of the optimal solution. The formulation is further extended to nonlinear model-based control using exactly linearizable models identified through machine learning. The effectiveness of the proposed approach is demonstrated through model predictive control applied to a hybrid powertrain system.

