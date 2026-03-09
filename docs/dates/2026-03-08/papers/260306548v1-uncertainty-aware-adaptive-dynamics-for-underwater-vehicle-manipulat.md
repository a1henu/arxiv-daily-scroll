---
layout: default
title: Uncertainty-Aware Adaptive Dynamics For Underwater Vehicle-Manipulator Robots
---

# Uncertainty-Aware Adaptive Dynamics For Underwater Vehicle-Manipulator Robots
**arXiv**：[2603.06548v1](https://arxiv.org/abs/2603.06548) · [PDF](https://arxiv.org/pdf/2603.06548.pdf)  
**作者**：Edward Morgan, Nenyi K Dadson, Corina Barbalata  

**一句话要点**：提出不确定性感知自适应动力学模型框架，以解决水下机器人-机械臂系统时变参数建模问题。

**关键词**：水下机器人-机械臂系统, 自适应动力学模型, 不确定性量化, 移动视界估计, 物理一致性约束, 在线控制

## 3 点简述
- 核心问题：水下机器人-机械臂系统受流体动力学影响，参数时变，需准确自适应模型。
- 方法要点：采用线性参数化模型，结合移动视界估计和凸物理一致性约束，在线估计并量化不确定性。
- 实验或效果：在BlueROV2 Heavy上实验，模型快速收敛，预测校准良好，误差降低，支持在线控制。

## 摘要（原文）

> Accurate and adaptive dynamic models are critical for underwater vehicle-manipulator systems where hydrodynamic effects induce time-varying parameters. This paper introduces a novel uncertainty-aware adaptive dynamics model framework that remains linear in lumped vehicle and manipulator parameters, and embeds convex physical consistency constraints during online estimation. Moving horizon estimation is used to stack horizon regressors, enforce realizable inertia, damping, friction, and hydrostatics, and quantify uncertainty from parameter evolution. Experiments on a BlueROV2 Heavy with a 4-DOF manipulator demonstrate rapid convergence and calibrated predictions. Manipulator fits achieve R2 = 0.88 to 0.98 with slopes near unity, while vehicle surge, heave, and roll are reproduced with good fidelity under stronger coupling and noise. Median solver time is approximately 0.023 s per update, confirming online feasibility. A comparison against a fixed parameter model shows consistent reductions in MAE and RMSE across degrees of freedom. Results indicate physically plausible parameters and confidence intervals with near 100% coverage, enabling reliable feedforward control and simulation in underwater environments.

