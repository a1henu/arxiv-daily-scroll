---
layout: default
title: Interacting safely with cyclists using Hamilton-Jacobi reachability and reinforcement learning
---

# Interacting safely with cyclists using Hamilton-Jacobi reachability and reinforcement learning
**arXiv**：[2602.18097v1](https://arxiv.org/abs/2602.18097) · [PDF](https://arxiv.org/pdf/2602.18097.pdf)  
**作者**：Aarati Andrea Noronha, Jean Oh  

**一句话要点**：提出结合Hamilton-Jacobi可达性分析与深度Q学习的框架，以平衡自动驾驶车辆与骑行者交互的安全性和效率。

**关键词**：自动驾驶交互, Hamilton-Jacobi可达性, 强化学习, 安全度量, 骑行者建模, 深度Q学习

## 3 点简述
- 核心问题：自动驾驶车辆与骑行者交互时需兼顾安全保证和时间效率，避免冲突。
- 方法要点：通过Hamilton-Jacobi可达性分析计算安全度量，并作为结构化奖励信号集成到强化学习中。
- 实验或效果：通过模拟评估，与人类驾驶行为和现有先进方法比较，验证框架的有效性。

## 摘要（原文）

> In this paper, we present a framework for enabling autonomous vehicles to interact with cyclists in a manner that balances safety and optimality. The approach integrates Hamilton-Jacobi reachability analysis with deep Q-learning to jointly address safety guarantees and time-efficient navigation. A value function is computed as the solution to a time-dependent Hamilton-Jacobi-Bellman inequality, providing a quantitative measure of safety for each system state. This safety metric is incorporated as a structured reward signal within a reinforcement learning framework. The method further models the cyclist's latent response to the vehicle, allowing disturbance inputs to reflect human comfort and behavioral adaptation. The proposed framework is evaluated through simulation and comparison with human driving behavior and an existing state-of-the-art method.

