---
layout: default
title: Differentiable Material Point Method for the Control of Deformable Objects
---

# Differentiable Material Point Method for the Control of Deformable Objects
**arXiv**：[2512.13214v1](https://arxiv.org/abs/2512.13214) · [PDF](https://arxiv.org/pdf/2512.13214.pdf)  
**作者**：Diego Bolliger, Gabriele Fadini, Markus Bambach, Alisa Rupenyan  

**一句话要点**：提出可微分材料点法模拟器以优化柔性物体的控制轨迹

**关键词**：可微分模拟, 材料点法, 柔性物体控制, 主动阻尼, 轨迹优化

## 3 点简述
- 核心问题：柔性物体因非线性动力学和高维配置空间而难以控制变形
- 方法要点：开发可微分MPM模拟器，利用其可微性优化控制轨迹
- 实验或效果：在超弹性绳索主动阻尼问题中，比基线MPPI方法快约2倍，能量降低20%，计算时间减少约97%

## 摘要（原文）

> Controlling the deformation of flexible objects is challenging due to their non-linear dynamics and high-dimensional configuration space. This work presents a differentiable Material Point Method (MPM) simulator targeted at control applications. We exploit the differentiability of the simulator to optimize a control trajectory in an active damping problem for a hyperelastic rope. The simulator effectively minimizes the kinetic energy of the rope around 2$\times$ faster than a baseline MPPI method and to a 20% lower energy level, while using about 3% of the computation time.

