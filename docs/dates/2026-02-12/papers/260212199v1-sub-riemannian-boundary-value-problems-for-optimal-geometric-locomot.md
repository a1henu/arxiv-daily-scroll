---
layout: default
title: Sub--Riemannian boundary value problems for Optimal Geometric Locomotion
---

# Sub--Riemannian boundary value problems for Optimal Geometric Locomotion
**arXiv**：[2602.12199v1](https://arxiv.org/abs/2602.12199) · [PDF](https://arxiv.org/pdf/2602.12199.pdf)  
**作者**：Oliver Gross, Florine Hartwig, Martin Rumpf, Peter Schröder  

**一句话要点**：提出基于次黎曼几何的边界值问题模型，用于优化细长体（如蛇）的形状变化诱导运动效率。

**关键词**：次黎曼几何, 最优运动控制, 边界值问题, 细长体动力学, 能量耗散优化, 数值计算

## 3 点简述
- 核心问题：建模细长体（如蛇或机器人）通过形状变化（如弯曲和拉伸）在环境中运动时的整体能量耗散优化问题。
- 方法要点：将拉格朗日最小耗散原理表述为边界值问题，其解由次黎曼测地线给出，同时考虑环境位移和内部代谢或执行器能耗。
- 实验或效果：数值计算次黎曼测地线，结果与蛇、精子等生物运动轨迹及低维系统（如Purcell游泳者）的已知最优性匹配，并提供公开代码。

## 摘要（原文）

> We propose a geometric model for optimal shape-change-induced motions of slender locomotors, e.g., snakes slithering on sand. In these scenarios, the motion of a body in world coordinates is completely determined by the sequence of shapes it assumes. Specifically, we formulate Lagrangian least-dissipation principles as boundary value problems whose solutions are given by sub-Riemannian geodesics. Notably, our geometric model accounts not only for the energy dissipated by the body's displacement through the environment, but also for the energy dissipated by the animal's metabolism or a robot's actuators to induce shape changes such as bending and stretching, thus capturing overall locomotion efficiency. Our continuous model, together with a consistent time and space discretization, enables numerical computation of sub-Riemannian geodesics for three different types of boundary conditions, i.e., fixing initial and target body, restricting to cyclic motion, or solely prescribing body displacement and orientation. The resulting optimal deformation gaits qualitatively match observed motion trajectories of organisms such as snakes and spermatozoa, as well as known optimality results for low-dimensional systems such as Purcell's swimmers. Moreover, being geometrically less rigid than previous frameworks, our model enables new insights into locomotion mechanisms of, e.g., generalized Purcell's swimmers. The code is publicly available.

