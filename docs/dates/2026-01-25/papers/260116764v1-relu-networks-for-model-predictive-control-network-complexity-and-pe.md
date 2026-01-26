---
layout: default
title: ReLU Networks for Model Predictive Control: Network Complexity and Performance Guarantees
---

# ReLU Networks for Model Predictive Control: Network Complexity and Performance Guarantees
**arXiv**：[2601.16764v1](https://arxiv.org/abs/2601.16764) · [PDF](https://arxiv.org/pdf/2601.16764.pdf)  
**作者**：Xingchen Li, Keyou You  

**一句话要点**：提出基于投影和状态感知缩放的ReLU网络方法，以解决模型预测控制中网络复杂度与闭环性能的权衡问题。

**关键词**：模型预测控制, ReLU神经网络, 网络复杂度, 闭环性能, Lipschitz连续性, 非均匀误差框架

## 3 点简述
- 核心问题：确定ReLU网络复杂度以确保模型预测控制策略的闭环性能，涉及精度与复杂度的权衡。
- 方法要点：通过投影方法强制硬约束，建立状态依赖Lipschitz连续性，并引入非均匀误差框架自适应调整网络输入输出。
- 实验或效果：首次推导出ReLU网络宽度和深度的显式边界，以近似MPC策略并保证闭环性能。

## 摘要（原文）

> Recent years have witnessed a resurgence in using ReLU neural networks (NNs) to represent model predictive control (MPC) policies. However, determining the required network complexity to ensure closed-loop performance remains a fundamental open problem. This involves a critical precision-complexity trade-off: undersized networks may fail to capture the MPC policy, while oversized ones may outweigh the benefits of ReLU network approximation. In this work, we propose a projection-based method to enforce hard constraints and establish a state-dependent Lipschitz continuity property for the optimal MPC cost function, which enables sharp convergence analysis of the closed-loop system. For the first time, we derive explicit bounds on ReLU network width and depth for approximating MPC policies with guaranteed closed-loop performance. To further reduce network complexity and enhance closed-loop performance, we propose a non-uniform error framework with a state-aware scaling function to adaptively adjust both the input and output of the ReLU network. Our contributions provide a foundational step toward certifiable ReLU NN-based MPC.

