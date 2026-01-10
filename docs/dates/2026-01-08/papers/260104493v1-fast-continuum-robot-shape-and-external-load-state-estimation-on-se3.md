---
layout: default
title: Fast Continuum Robot Shape and External Load State Estimation on SE(3)
---

# Fast Continuum Robot Shape and External Load State Estimation on SE(3)
**arXiv**：[2601.04493v1](https://arxiv.org/abs/2601.04493) · [PDF](https://arxiv.org/pdf/2601.04493.pdf)  
**作者**：James M. Ferguson, Alan Kuntz, Tucker Hermans  

**一句话要点**：提出基于SE(3)的连续体机器人形状与外部负载状态估计框架，结合时空先验实现快速优化。

**关键词**：连续体机器人, 状态估计, SE(3)流形, 因子图优化, 外部负载估计, 手术机器人

## 3 点简述
- 核心问题：现有方法忽略驱动输入和外部负载，简化模型限制状态估计精度。
- 方法要点：引入不确定性模型，结合时空先验，通过因子图进行快速稀疏非线性优化。
- 实验或效果：仿真验证实时运动学与负载估计，实验展示手术机器人精确力感知潜力。

## 摘要（原文）

> Previous on-manifold approaches to continuum robot state estimation have typically adopted simplified Cosserat rod models, which cannot directly account for actuation inputs or external loads. We introduce a general framework that incorporates uncertainty models for actuation (e.g., tendon tensions), applied forces and moments, process noise, boundary conditions, and arbitrary backbone measurements. By adding temporal priors across time steps, our method additionally performs joint estimation in both the spatial (arclength) and temporal domains, enabling full \textit{spacetime} state estimation. Discretizing the arclength domain yields a factor graph representation of the continuum robot model, which can be exploited for fast batch sparse nonlinear optimization in the style of SLAM. The framework is general and applies to a broad class of continuum robots; as illustrative cases, we show (i) tendon-driven robots in simulation, where we demonstrate real-time kinematics with uncertainty, tip force sensing from position feedback, and distributed load estimation from backbone strain, and (ii) a surgical concentric tube robot in experiment, where we validate accurate kinematics and tip force estimation, highlighting potential for surgical palpation.

