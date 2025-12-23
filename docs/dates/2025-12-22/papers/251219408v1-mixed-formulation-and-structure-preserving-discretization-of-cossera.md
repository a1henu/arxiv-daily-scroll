---
layout: default
title: Mixed formulation and structure-preserving discretization of Cosserat rod dynamics in a port-Hamiltonian framework
---

# Mixed formulation and structure-preserving discretization of Cosserat rod dynamics in a port-Hamiltonian framework
**arXiv**：[2512.19408v1](https://arxiv.org/abs/2512.19408) · [PDF](https://arxiv.org/pdf/2512.19408.pdf)  
**作者**：Philipp L. Kinon, Simon R. Eugster, Peter Betsch  

**一句话要点**：提出基于端口哈密顿框架的混合公式与结构保持离散化方法，用于模拟大位移旋转的Cosserat杆非线性动力学。

**关键词**：Cosserat杆动力学, 端口哈密顿系统, 结构保持离散化, 混合公式, 能量-动量一致, 非线性动力学

## 3 点简述
- 核心问题：模拟空间Cosserat杆在大位移和旋转下的非线性动力学，需避免奇异性、锁定和能量不一致。
- 方法要点：采用混合公式，独立变量和导演表示，实现无限维端口哈密顿系统，并通过结构保持离散化得到有限维系统。
- 实验或效果：通过数值示例验证框架支持能量-动量一致积分，并整合耗散材料和非标准驱动。

## 摘要（原文）

> An energy-based modeling framework for the nonlinear dynamics of spatial Cosserat rods undergoing large displacements and rotations is proposed. The mixed formulation features independent displacement, velocity and stress variables and is further objective and locking-free. Finite rotations are represented using a director formulation that avoids singularities and yields a constant mass matrix. This results in an infinite-dimensional nonlinear port-Hamiltonian (PH) system governed by partial differential-algebraic equations with a quadratic energy functional. Using a time-differentiated compliance form of the stress-strain relations allows for the imposition of kinematic constraints, such as inextensibility or shear-rigidity. A structure-preserving finite element discretization leads to a finite-dimensional system with PH structure, thus facilitating the design of an energy-momentum consistent integration scheme. Dissipative material behavior (via the generalized-Maxwell model) and non-standard actuation approaches (via pneumatic chambers or tendons) integrate naturally into the framework. As illustrated by selected numerical examples, the present framework establishes a new approach to energy-momentum consistent formulations in computational mechanics involving finite rotations.

