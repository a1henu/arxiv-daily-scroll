---
layout: default
title: i-PhysGaussian: Implicit Physical Simulation for 3D Gaussian Splatting
---

# i-PhysGaussian: Implicit Physical Simulation for 3D Gaussian Splatting
**arXiv**：[2602.17117v1](https://arxiv.org/abs/2602.17117) · [PDF](https://arxiv.org/pdf/2602.17117.pdf)  
**作者**：Yicheng Cao, Zhuo Huang, Yu Yao, Yiming Ying, Daoyi Dong, Tongliang Liu  

**一句话要点**：提出i-PhysGaussian框架，结合3D高斯泼溅与隐式物质点法，以解决复杂物理模拟中的时间步长敏感性问题。

**关键词**：3D高斯泼溅, 隐式物理模拟, 物质点法, 时间步长稳定性, 复杂动态过渡

## 3 点简述
- 核心问题：基于3D重建的显式模拟器在复杂场景下时间步长敏感，精度易退化。
- 方法要点：通过隐式牛顿优化最小化动量平衡残差，确保物理一致性。
- 实验或效果：在高达20倍时间步长下保持稳定，维持结构连贯性和平滑运动。

## 摘要（原文）

> Physical simulation predicts future states of objects based on material properties and external loads, enabling blueprints for both Industry and Engineering to conduct risk management. Current 3D reconstruction-based simulators typically rely on explicit, step-wise updates, which are sensitive to step time and suffer from rapid accuracy degradation under complicated scenarios, such as high-stiffness materials or quasi-static movement. To address this, we introduce i-PhysGaussian, a framework that couples 3D Gaussian Splatting (3DGS) with an implicit Material Point Method (MPM) integrator. Unlike explicit methods, our solution obtains an end-of-step state by minimizing a momentum-balance residual through implicit Newton-type optimization with a GMRES solver. This formulation significantly reduces time-step sensitivity and ensures physical consistency. Our results demonstrate that i-PhysGaussian maintains stability at up to 20x larger time steps than explicit baselines, preserving structural coherence and smooth motion even in complex dynamic transitions.

