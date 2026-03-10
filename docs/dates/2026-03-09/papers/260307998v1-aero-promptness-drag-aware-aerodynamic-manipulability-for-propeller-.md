---
layout: default
title: Aero-Promptness: Drag-Aware Aerodynamic Manipulability for Propeller-driven Vehicles
---

# Aero-Promptness: Drag-Aware Aerodynamic Manipulability for Propeller-driven Vehicles
**arXiv**：[2603.07998v1](https://arxiv.org/abs/2603.07998) · [PDF](https://arxiv.org/pdf/2603.07998.pdf)  
**作者**：Antonio Franchi  

**一句话要点**：提出基于黎曼度量的阻力感知气动可操纵性框架，用于冗余多旋翼飞行器的控制分配。

**关键词**：多旋翼控制, 控制分配, 气动阻力, 黎曼几何, 冗余解析, 可操纵性分析

## 3 点简述
- 核心问题：冗余多旋翼控制分配中需考虑电机扭矩限制和气动阻力，以避免饱和和推力损失。
- 方法要点：在螺旋桨转速空间引入基于剩余对称加速度容量的黎曼度量，映射到广义力空间形成状态依赖的可操纵性体积。
- 实验或效果：优化该体积提供冗余解析策略，对广义力空间坐标缩放不变，并分析最优分配的局部光滑性和全局跳跃不连续性。

## 摘要（原文）

> This work introduces the Drag-Aware Aerodynamic Manipulability (DAAM), a geometric framework for control allocation in redundant multirotors. By equipping the propeller spin-rate space with a Riemannian metric based on the remaining symmetric acceleration capacity of each motor, the formulation explicitly accounts for motor torque limits and aerodynamic drag. Mapping this metric through the nonlinear thrust law to the generalized force space yields a state-dependent manipulability volume. The log-determinant of this volume acts as a natural barrier function, strictly penalizing drag-induced saturation and low-spin thrust loss. Optimizing this volume along the allocation fibers provides a redundancy resolution strategy inherently invariant to arbitrary coordinate scaling in the generalized-force space. Analytically, we prove that the resulting optimal allocations locally form smooth embedded manifolds, and we geometrically characterize the global jump discontinuities that inevitably arise from physical actuator limits and spin-rate sign transitions.

