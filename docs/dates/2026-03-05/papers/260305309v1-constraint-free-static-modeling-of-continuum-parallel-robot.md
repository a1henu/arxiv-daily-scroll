---
layout: default
title: Constraint-Free Static Modeling of Continuum Parallel Robot
---

# Constraint-Free Static Modeling of Continuum Parallel Robot
**arXiv**：[2603.05309v1](https://arxiv.org/abs/2603.05309) · [PDF](https://arxiv.org/pdf/2603.05309.pdf)  
**作者**：Lingxiao Xun, Matyas Diezinger, Azad Artinian, Guillaume Laurent, Brahim Tamadazte  

**一句话要点**：提出无约束静态建模方法以解决连续体并联机器人的正向静力学挑战

**关键词**：连续体并联机器人, 静态建模, 无约束优化, 几何非线性, 牛顿迭代, 产品流形

## 3 点简述
- 核心问题：传统基于约束的建模引入额外变量，使数值求解和控制复杂化
- 方法要点：通过运动学嵌入消除连接约束，采用几何精确的配置基无约束模型
- 实验或效果：在三伺服电机六杆原型上验证，模拟与测量在无载和外部加载下吻合良好

## 摘要（原文）

> Continuum parallel robots (CPR) combine rigid actuation mechanisms with multiple elastic rods in a closed-loop topology, making forward statics challenging when rigid--continuum junctions are enforced by explicit kinematic constraints. Such constraint-based formulations typically introduce additional algebraic variables and complicate both numerical solution and downstream control. This paper presents a geometric exact, configuration-based and constraint-free static model of CPR that remains valid under geometrically nonlinear, large-deformation and large-rotation conditions. Connectivity constraints are eliminated by kinematic embedding, yielding a reduced unconstrained problem. Each rod of CPR is discretized by nodal poses on SE(3), while the element-wise strain field is reconstructed through a linear strain parameterization. A fourth-order Magnus approximation yields an explicit and geometrically consistent mapping between element end poses and the strain. Rigid attachments at the motor-driven base and the end-effector platforms are handled through kinematic embeddings. Based on total potential energy and virtual work, we derive assembly-ready residuals and explicit Newton tangents, and solve the resulting nonlinear equilibrium equations using a Riemannian Newton iteration on the product manifold. Experiments on a three-servomotor, six-rod prototype validate the model by showing good agreement between simulation and measurements for both unloaded motions and externally loaded cases.

