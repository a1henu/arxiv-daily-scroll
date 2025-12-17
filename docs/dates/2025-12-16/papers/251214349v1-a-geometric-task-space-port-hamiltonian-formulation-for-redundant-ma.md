---
layout: default
title: A Geometric Task-Space Port-Hamiltonian Formulation for Redundant Manipulators
---

# A Geometric Task-Space Port-Hamiltonian Formulation for Redundant Manipulators
**arXiv**：[2512.14349v1](https://arxiv.org/abs/2512.14349) · [PDF](https://arxiv.org/pdf/2512.14349.pdf)  
**作者**：Federico Califano, Camilla Rota, Riccardo Zanella, Antonio Franchi  

**一句话要点**：提出冗余机械臂的几何任务空间端口哈密顿公式，用于阻抗控制设计。

**关键词**：冗余机械臂, 端口哈密顿系统, 几何控制, 任务空间动力学, IDA-PBC, 阻抗控制

## 3 点简述
- 核心问题：冗余机械臂在任务空间中的动力学建模与控制，传统方法可能未充分利用几何结构。
- 方法要点：通过坐标变换将哈密顿动量分解为任务空间和零空间分量，建立几何端口哈密顿公式。
- 实验或效果：应用于IDA-PBC控制，在仿真中稳定并塑造7-DOF Panda机器人的阻抗。

## 摘要（原文）

> We present a novel geometric port-Hamiltonian formulation of redundant manipulators performing a differential kinematic task $η=J(q)\dot{q}$, where $q$ is a point on the configuration manifold, $η$ is a velocity-like task space variable, and $J(q)$ is a linear map representing the task, for example the classical analytic or geometric manipulator Jacobian matrix. The proposed model emerges from a change of coordinates from canonical Hamiltonian dynamics, and splits the standard Hamiltonian momentum variable into a task-space momentum variable and a null-space momentum variable. Properties of this model and relation to Lagrangian formulations present in the literature are highlighted. Finally, we apply the proposed model in an \textit{Interconnection and Damping Assignment Passivity-Based Control} (IDA-PBC) design to stabilize and shape the impedance of a 7-DOF Emika Panda robot in simulation.

