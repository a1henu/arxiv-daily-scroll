---
layout: default
title: Learning vertical coordinates via automatic differentiation of a dynamical core
---

# Learning vertical coordinates via automatic differentiation of a dynamical core
**arXiv**：[2512.17877v1](https://arxiv.org/abs/2512.17877) · [PDF](https://arxiv.org/pdf/2512.17877.pdf)  
**作者**：Tim Whittaker, Seth Taylor, Elsa Cardoso-Bihlo, Alejandro Di Luca, Alex Bihlo  

**一句话要点**：提出可学习垂直坐标框架，通过自动微分优化大气模型地形跟随坐标以减少数值误差。

**关键词**：大气模型, 可微编程, 垂直坐标优化, 自动微分, 神经网络参数化, 数值模拟

## 3 点简述
- 地形跟随坐标在陡峭地形上易产生虚假运动，传统方法依赖手动调参的解析衰减函数。
- 开发端到端可微二维非静力欧拉方程求解器，引入基于神经网络的单调性保证坐标NEUVE。
- 通过自动微分计算精确几何度量项，优化坐标结构，实验显示误差降低1.4至2倍并消除虚假垂直速度条纹。

## 摘要（原文）

> Terrain-following coordinates in atmospheric models often imprint their grid structure onto the solution, particularly over steep topography, where distorted coordinate layers can generate spurious horizontal and vertical motion. Standard formulations, such as hybrid or SLEVE coordinates, mitigate these errors by using analytic decay functions controlled by heuristic scale parameters that are typically tuned by hand and fixed a priori. In this work, we propose a framework to define a parametric vertical coordinate system as a learnable component within a differentiable dynamical core. We develop an end-to-end differentiable numerical solver for the two-dimensional non-hydrostatic Euler equations on an Arakawa C-grid, and introduce a NEUral Vertical Enhancement (NEUVE) terrain-following coordinate based on an integral transformed neural network that guarantees monotonicity. A key feature of our approach is the use of automatic differentiation to compute exact geometric metric terms, thereby eliminating truncation errors associated with finite-difference coordinate derivatives. By coupling simulation errors through the time integration to the parameterization, our formulation finds a grid structure optimized for both the underlying physics and numerics. Using several standard tests, we demonstrate that these learned coordinates reduce the mean squared error by a factor of 1.4 to 2 in non-linear statistical benchmarks, and eliminate spurious vertical velocity striations over steep topography.

