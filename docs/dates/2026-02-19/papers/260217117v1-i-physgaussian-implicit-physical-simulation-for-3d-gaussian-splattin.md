---
layout: default
title: i-PhysGaussian: Implicit Physical Simulation for 3D Gaussian Splatting
---

# i-PhysGaussian: Implicit Physical Simulation for 3D Gaussian Splatting
**arXiv**：[2602.17117v1](https://arxiv.org/abs/2602.17117) · [PDF](https://arxiv.org/pdf/2602.17117.pdf)  
**作者**：Yicheng Cao, Zhuo Huang, Yu Yao, Yiming Ying, Daoyi Dong, Tongliang Liu  

**一句话要点**：提出i-PhysGaussian框架，通过隐式物理模拟解决3D高斯泼溅在复杂场景下的时间步长敏感性问题。

**关键词**：3D高斯泼溅, 隐式物理模拟, 材料点法, 时间步长稳定性, 动量平衡优化

## 3 点简述
- 核心问题：基于3D重建的显式物理模拟对时间步长敏感，在高刚度材料或准静态运动等复杂场景下精度快速下降。
- 方法要点：将3D高斯泼溅与隐式材料点法积分器耦合，通过GMRES求解器最小化动量平衡残差，实现隐式牛顿型优化。
- 实验或效果：i-PhysGaussian在时间步长比显式基线大20倍时仍保持稳定，确保结构连贯性和运动平滑性。

## 摘要（原文）

> Physical simulation predicts future states of objects based on material properties and external loads, enabling blueprints for both Industry and Engineering to conduct risk management. Current 3D reconstruction-based simulators typically rely on explicit, step-wise updates, which are sensitive to step time and suffer from rapid accuracy degradation under complicated scenarios, such as high-stiffness materials or quasi-static movement. To address this, we introduce i-PhysGaussian, a framework that couples 3D Gaussian Splatting (3DGS) with an implicit Material Point Method (MPM) integrator. Unlike explicit methods, our solution obtains an end-of-step state by minimizing a momentum-balance residual through implicit Newton-type optimization with a GMRES solver. This formulation significantly reduces time-step sensitivity and ensures physical consistency. Our results demonstrate that i-PhysGaussian maintains stability at up to 20x larger time steps than explicit baselines, preserving structural coherence and smooth motion even in complex dynamic transitions.

