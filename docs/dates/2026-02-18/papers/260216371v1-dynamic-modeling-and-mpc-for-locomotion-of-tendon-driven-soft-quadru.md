---
layout: default
title: Dynamic Modeling and MPC for Locomotion of Tendon-Driven Soft Quadruped
---

# Dynamic Modeling and MPC for Locomotion of Tendon-Driven Soft Quadruped
**arXiv**：[2602.16371v1](https://arxiv.org/abs/2602.16371) · [PDF](https://arxiv.org/pdf/2602.16371.pdf)  
**作者**：Saumya Karan, Neerav Maram, Suraj Borate, Madhu Vadali  

**一句话要点**：提出基于离散Cosserat杆理论的肌腱驱动软四足机器人建模与凸模型预测控制框架，实现高精度运动控制。

**关键词**：软四足机器人, 离散Cosserat杆理论, 模型预测控制, 肌腱驱动, 柔顺腿式运动, 物理建模

## 3 点简述
- 核心问题：研究仅用四个执行器的柔顺腿式运动物理建模与控制，以集成连续软腿到基于模型的运动控制中。
- 方法要点：采用离散Cosserat杆理论建模腿为可变形连续体，结合刚体躯干模块化框架，嵌入凸模型预测控制优化地面反作用力。
- 实验或效果：在物理原型上验证，质心轨迹RMSE小于5毫米，实现渐近稳定性和高精度爬行与行走步态。

## 摘要（原文）

> SLOT (Soft Legged Omnidirectional Tetrapod), a tendon-driven soft quadruped robot with 3D-printed TPU legs, is presented to study physics-informed modeling and control of compliant legged locomotion using only four actuators. Each leg is modeled as a deformable continuum using discrete Cosserat rod theory, enabling the capture of large bending deformations, distributed elasticity, tendon actuation, and ground contact interactions. A modular whole-body modeling framework is introduced, in which compliant leg dynamics are represented through physically consistent reaction forces applied to a rigid torso, providing a scalable interface between continuum soft limbs and rigid-body locomotion dynamics. This formulation allows efficient whole-body simulation and real-time control without sacrificing physical fidelity. The proposed model is embedded into a convex model predictive control framework that optimizes ground reaction forces over a 0.495 s prediction horizon and maps them to tendon actuation through a physics-informed force-angle relationship. The resulting controller achieves asymptotic stability under diverse perturbations. The framework is experimentally validated on a physical prototype during crawling and walking gaits, achieving high accuracy with less than 5 mm RMSE in center of mass trajectories. These results demonstrate a generalizable approach for integrating continuum soft legs into model-based locomotion control, advancing scalable and reusable modeling and control methods for soft quadruped robots.

