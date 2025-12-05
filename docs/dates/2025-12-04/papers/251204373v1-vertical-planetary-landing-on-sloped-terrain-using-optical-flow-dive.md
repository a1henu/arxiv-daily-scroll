---
layout: default
title: Vertical Planetary Landing on Sloped Terrain Using Optical Flow Divergence Estimates
---

# Vertical Planetary Landing on Sloped Terrain Using Optical Flow Divergence Estimates
**arXiv**：[2512.04373v1](https://arxiv.org/abs/2512.04373) · [PDF](https://arxiv.org/pdf/2512.04373.pdf)  
**作者**：Hann Woei Ho, Ye Zhou  

**一句话要点**：提出基于局部光流发散的非线性控制策略，实现小型航天器在斜坡地形的垂直着陆

**关键词**：光流发散, 非线性控制, 斜坡着陆, 航天器自主着陆, 生物启发控制

## 3 点简述
- 核心问题：小型航天器在斜坡着陆时，全局光流发散估计忽略地形倾斜，传统控制器易不稳定
- 方法要点：利用两个局部光流发散估计，通过增量非线性动态反演控制推力和姿态
- 实验或效果：数值模拟显示，该方法能稳定着陆，速度与高度指数衰减，并有效对齐倾斜表面

## 摘要（原文）

> Autonomous landing on sloped terrain poses significant challenges for small, lightweight spacecraft, such as rotorcraft and landers. These vehicles have limited processing capability and payload capacity, which makes advanced deep learning methods and heavy sensors impractical. Flying insects, such as bees, achieve remarkable landings with minimal neural and sensory resources, relying heavily on optical flow. By regulating flow divergence, a measure of vertical velocity divided by height, they perform smooth landings in which velocity and height decay exponentially together. However, adapting this bio-inspired strategy for spacecraft landings on sloped terrain presents two key challenges: global flow-divergence estimates obscure terrain inclination, and the nonlinear nature of divergence-based control can lead to instability when using conventional controllers. This paper proposes a nonlinear control strategy that leverages two distinct local flow divergence estimates to regulate both thrust and attitude during vertical landings. The control law is formulated based on Incremental Nonlinear Dynamic Inversion to handle the nonlinear flow divergence. The thrust control ensures a smooth vertical descent by keeping a constant average of the local flow divergence estimates, while the attitude control aligns the vehicle with the inclined surface at touchdown by exploiting their difference. The approach is evaluated in numerical simulations using a simplified 2D spacecraft model across varying slopes and divergence setpoints. Results show that regulating the average divergence yields stable landings with exponential decay of velocity and height, and using the divergence difference enables effective alignment with inclined terrain. Overall, the method offers a robust, low-resource landing strategy that enhances the feasibility of autonomous planetary missions with small spacecraft.

