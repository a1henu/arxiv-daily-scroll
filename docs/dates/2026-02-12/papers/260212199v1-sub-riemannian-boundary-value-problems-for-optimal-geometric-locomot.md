---
layout: default
title: Sub--Riemannian boundary value problems for Optimal Geometric Locomotion
---

# Sub--Riemannian boundary value problems for Optimal Geometric Locomotion
**arXiv**：[2602.12199v1](https://arxiv.org/abs/2602.12199) · [PDF](https://arxiv.org/pdf/2602.12199.pdf)  
**作者**：Oliver Gross, Florine Hartwig, Martin Rumpf, Peter Schröder  

**一句话要点**：提出基于亚黎曼几何的边界值问题模型，以优化细长体（如蛇）通过形状变化诱导的运动效率。

**关键词**：亚黎曼几何, 最优运动控制, 细长体动力学, 能量耗散模型, 边界值问题, 数值计算

## 3 点简述
- 核心问题：建模细长体（如蛇或机器人）通过形状变化（如弯曲和拉伸）诱导的运动，以最小化总能量耗散（包括环境位移和内部代谢/执行器能耗）。
- 方法要点：将拉格朗日最小耗散原理表述为亚黎曼测地线边界值问题，并开发连续模型与时空离散化进行数值计算。
- 实验或效果：模型匹配蛇和精子等生物运动轨迹，验证了普塞尔游泳者等低维系统的最优性，并揭示广义普塞尔游泳者的新机制。

## 摘要（原文）

> We propose a geometric model for optimal shape-change-induced motions of slender locomotors, e.g., snakes slithering on sand. In these scenarios, the motion of a body in world coordinates is completely determined by the sequence of shapes it assumes. Specifically, we formulate Lagrangian least-dissipation principles as boundary value problems whose solutions are given by sub-Riemannian geodesics. Notably, our geometric model accounts not only for the energy dissipated by the body's displacement through the environment, but also for the energy dissipated by the animal's metabolism or a robot's actuators to induce shape changes such as bending and stretching, thus capturing overall locomotion efficiency. Our continuous model, together with a consistent time and space discretization, enables numerical computation of sub-Riemannian geodesics for three different types of boundary conditions, i.e., fixing initial and target body, restricting to cyclic motion, or solely prescribing body displacement and orientation. The resulting optimal deformation gaits qualitatively match observed motion trajectories of organisms such as snakes and spermatozoa, as well as known optimality results for low-dimensional systems such as Purcell's swimmers. Moreover, being geometrically less rigid than previous frameworks, our model enables new insights into locomotion mechanisms of, e.g., generalized Purcell's swimmers. The code is publicly available.

