---
layout: default
title: Fast Continuum Robot Shape and External Load State Estimation on SE(3)
---

# Fast Continuum Robot Shape and External Load State Estimation on SE(3)
**arXiv**：[2601.04493v1](https://arxiv.org/abs/2601.04493) · [PDF](https://arxiv.org/pdf/2601.04493.pdf)  
**作者**：James M. Ferguson, Alan Kuntz, Tucker Hermans  

**一句话要点**：提出基于SE(3)的连续体机器人形状与外部负载状态估计框架，实现时空联合估计。

**关键词**：连续体机器人, 状态估计, SE(3)流形, 因子图优化, 手术机器人, 负载估计

## 3 点简述
- 核心问题：现有流形方法采用简化Cosserat杆模型，无法直接处理驱动输入或外部负载。
- 方法要点：引入通用框架，整合驱动、外力、噪声等不确定性模型，通过因子图实现快速批量优化。
- 实验或效果：在仿真中展示实时运动学与负载估计，实验中验证手术机器人运动学与力估计准确性。

## 摘要（原文）

> Previous on-manifold approaches to continuum robot state estimation have typically adopted simplified Cosserat rod models, which cannot directly account for actuation inputs or external loads. We introduce a general framework that incorporates uncertainty models for actuation (e.g., tendon tensions), applied forces and moments, process noise, boundary conditions, and arbitrary backbone measurements. By adding temporal priors across time steps, our method additionally performs joint estimation in both the spatial (arclength) and temporal domains, enabling full \textit{spacetime} state estimation. Discretizing the arclength domain yields a factor graph representation of the continuum robot model, which can be exploited for fast batch sparse nonlinear optimization in the style of SLAM. The framework is general and applies to a broad class of continuum robots; as illustrative cases, we show (i) tendon-driven robots in simulation, where we demonstrate real-time kinematics with uncertainty, tip force sensing from position feedback, and distributed load estimation from backbone strain, and (ii) a surgical concentric tube robot in experiment, where we validate accurate kinematics and tip force estimation, highlighting potential for surgical palpation.

