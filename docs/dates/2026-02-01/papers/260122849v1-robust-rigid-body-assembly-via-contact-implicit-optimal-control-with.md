---
layout: default
title: Robust Rigid Body Assembly via Contact-Implicit Optimal Control with Exact Second-Order Derivatives
---

# Robust Rigid Body Assembly via Contact-Implicit Optimal Control with Exact Second-Order Derivatives
**arXiv**：[2601.22849v1](https://arxiv.org/abs/2601.22849) · [PDF](https://arxiv.org/pdf/2601.22849.pdf)  
**作者**：Christian Dietz, Sebastian Albrecht, Gianluca Frison, Moritz Diehl, Armin Nurkanović  

**一句话要点**：提出基于接触隐式最优控制与精确二阶导数的鲁棒刚体装配方法，以提升规划效率与成功率。

**关键词**：刚体装配, 最优控制, 可微模拟, 接触动力学, 鲁棒规划, 二阶导数

## 3 点简述
- 核心问题：机器人装配运动规划依赖大量物理模拟，效率低且难以处理模拟到现实的差异。
- 方法要点：构建可微物理模拟，提供二阶解析导数，结合平滑化接触动力学与多场景优化确保鲁棒性。
- 实验或效果：真实实验中成功率超99%，模拟测试显示精确Hessian优于近似方法。

## 摘要（原文）

> Efficient planning of assembly motions is a long standing challenge in the field of robotics that has been primarily tackled with reinforcement learning and sampling-based methods by using extensive physics simulations. This paper proposes a sample-efficient robust optimal control approach for the determination of assembly motions, which requires significantly less physics simulation steps during planning through the efficient use of derivative information. To this end, a differentiable physics simulation is constructed that provides second-order analytic derivatives to the numerical solver and allows one to traverse seamlessly from informative derivatives to accurate contact simulation. The solution of the physics simulation problem is made differentiable by using smoothing inspired by interior-point methods applied to both the collision detection as well as the contact resolution problem. We propose a modified variant of an optimization-based formulation of collision detection formulated as a linear program and present an efficient implementation for the nominal evaluation and corresponding first- and second-order derivatives. Moreover, a multi-scenario-based trajectory optimization problem that ensures robustness with respect to sim-to-real mismatches is derived. The capability of the considered formulation is illustrated by results where over 99\% successful executions are achieved in real-world experiments. Thereby, we carefully investigate the effect of smooth approximations of the contact dynamics and robust modeling on the success rates. Furthermore, the method's capability is tested on different peg-in-hole problems in simulation to show the benefit of using exact Hessians over commonly used Hessian approximations.

