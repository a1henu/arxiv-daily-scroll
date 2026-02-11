---
layout: default
title: Optimal Control of Microswimmers for Trajectory Tracking Using Bayesian Optimization
---

# Optimal Control of Microswimmers for Trajectory Tracking Using Bayesian Optimization
**arXiv**：[2602.09563v1](https://arxiv.org/abs/2602.09563) · [PDF](https://arxiv.org/pdf/2602.09563.pdf)  
**作者**：Lucas Palazzolo, Mickaël Binois, Laëtitia Giraldi  

**一句话要点**：提出基于贝叶斯优化的最优控制方法，解决微泳体轨迹跟踪问题

**关键词**：微泳体控制, 贝叶斯优化, 轨迹跟踪, 最优控制, 流体结构相互作用

## 3 点简述
- 核心问题：微泳体在低雷诺数流体中的轨迹跟踪控制设计复杂，涉及高计算成本
- 方法要点：结合B样条参数化和贝叶斯优化，避免复杂梯度计算，处理高计算成本
- 实验或效果：应用于鞭毛磁泳体和三球泳体模型，成功跟踪目标轨迹并部分补偿壁面流体效应

## 摘要（原文）

> Trajectory tracking for microswimmers remains a key challenge in microrobotics, where low-Reynolds-number dynamics make control design particularly complex. In this work, we formulate the trajectory tracking problem as an optimal control problem and solve it using a combination of B-spline parametrization with Bayesian optimization, allowing the treatment of high computational costs without requiring complex gradient computations. Applied to a flagellated magnetic swimmer, the proposed method reproduces a variety of target trajectories, including biologically inspired paths observed in experimental studies. We further evaluate the approach on a three-sphere swimmer model, demonstrating that it can adapt to and partially compensate for wall-induced hydrodynamic effects. The proposed optimization strategy can be applied consistently across models of different fidelity, from low-dimensional ODE-based models to high-fidelity PDE-based simulations, showing its robustness and generality. These results highlight the potential of Bayesian optimization as a versatile tool for optimal control strategies in microscale locomotion under complex fluid-structure interactions.

