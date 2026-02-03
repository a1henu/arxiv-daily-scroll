---
layout: default
title: Frictional Contact Solving for Material Point Method
---

# Frictional Contact Solving for Material Point Method
**arXiv**：[2602.02038v1](https://arxiv.org/abs/2602.02038) · [PDF](https://arxiv.org/pdf/2602.02038.pdf)  
**作者**：Etienne Ménager, Justin Carpentier  

**一句话要点**：提出基于NCP和ADMM的摩擦接触求解方法，以提升隐式MPM在机器人仿真中的精度与鲁棒性。

**关键词**：材料点法, 摩擦接触, 非线性互补问题, 交替方向乘子法, 机器人仿真, 隐式求解

## 3 点简述
- 核心问题：MPM中摩擦接触处理存在瓶颈，包括接触点检测和摩擦定律执行。
- 方法要点：使用粒子中心几何基元定位接触点，将摩擦接触建模为NCP并用ADMM求解。
- 实验或效果：在七种代表性场景中评估，涵盖弹性和弹塑性响应，验证了方法的准确性和通用性。

## 摘要（原文）

> Accurately handling contact with friction remains a core bottleneck for Material Point Method (MPM), from reliable contact point detection to enforcing frictional contact laws (non-penetration, Coulomb friction, and maximum dissipation principle). In this paper, we introduce a frictional-contact pipeline for implicit MPM that is both precise and robust. During the collision detection phase, contact points are localized with particle-centric geometric primitives; during the contact resolution phase, we cast frictional contact as a Nonlinear Complementarity Problem (NCP) over contact impulses and solve it with an Alternating Direction Method of Multipliers (ADMM) scheme. Crucially, the formulation reuses the same implicit MPM linearization, yielding efficiency and numerical stability. The method integrates seamlessly into the implicit MPM loop and is agnostic to modeling choices, including material laws, interpolation functions, and transfer schemes. We evaluate it across seven representative scenes that span elastic and elasto-plastic responses, simple and complex deformable geometries, and a wide range of contact conditions. Overall, the proposed method enables accurate contact localization, reliable frictional handling, and broad generality, making it a practical solution for MPM-based simulations in robotics and related domains.

