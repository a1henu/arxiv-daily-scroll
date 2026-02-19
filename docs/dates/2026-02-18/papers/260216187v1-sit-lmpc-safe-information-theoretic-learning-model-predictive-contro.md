---
layout: default
title: SIT-LMPC: Safe Information-Theoretic Learning Model Predictive Control for Iterative Tasks
---

# SIT-LMPC: Safe Information-Theoretic Learning Model Predictive Control for Iterative Tasks
**arXiv**：[2602.16187v1](https://arxiv.org/abs/2602.16187) · [PDF](https://arxiv.org/pdf/2602.16187.pdf)  
**作者**：Zirui Zang, Ahmad Amine, Nick-Marios T. Kokolakis, Truong X. Nghiem, Ugo Rosolia, Rahul Mangharam  

**一句话要点**：提出SIT-LMPC算法以解决机器人迭代任务中的安全、鲁棒与高性能控制问题。

**关键词**：模型预测控制, 迭代任务, 安全控制, 信息论学习, 归一化流, GPU并行计算

## 3 点简述
- 核心问题：机器人执行迭代任务时需在复杂不确定环境中平衡鲁棒性、安全性和性能。
- 方法要点：基于信息论模型预测控制，结合自适应惩罚确保安全，利用归一化流学习值函数以建模不确定性。
- 实验或效果：通过基准仿真和硬件实验验证，SIT-LMPC能迭代提升性能并满足系统约束。

## 摘要（原文）

> Robots executing iterative tasks in complex, uncertain environments require control strategies that balance robustness, safety, and high performance. This paper introduces a safe information-theoretic learning model predictive control (SIT-LMPC) algorithm for iterative tasks. Specifically, we design an iterative control framework based on an information-theoretic model predictive control algorithm to address a constrained infinite-horizon optimal control problem for discrete-time nonlinear stochastic systems. An adaptive penalty method is developed to ensure safety while balancing optimality. Trajectories from previous iterations are utilized to learn a value function using normalizing flows, which enables richer uncertainty modeling compared to Gaussian priors. SIT-LMPC is designed for highly parallel execution on graphics processing units, allowing efficient real-time optimization. Benchmark simulations and hardware experiments demonstrate that SIT-LMPC iteratively improves system performance while robustly satisfying system constraints.

