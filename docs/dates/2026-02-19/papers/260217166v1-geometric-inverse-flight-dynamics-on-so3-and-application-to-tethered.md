---
layout: default
title: Geometric Inverse Flight Dynamics on SO(3) and Application to Tethered Fixed-Wing Aircraft
---

# Geometric Inverse Flight Dynamics on SO(3) and Application to Tethered Fixed-Wing Aircraft
**arXiv**：[2602.17166v1](https://arxiv.org/abs/2602.17166) · [PDF](https://arxiv.org/pdf/2602.17166.pdf)  
**作者**：Antonio Franchi, Chiara Gabellieri  

**一句话要点**：提出基于SO(3)的几何逆飞行动力学框架，应用于系留固定翼飞机的轨迹设计。

**关键词**：逆飞行动力学, 几何建模, SO(3)群, 系留固定翼飞机, 轨迹设计, 协调飞行

## 3 点简述
- 核心问题：在SO(3)上建立坐标无关的逆飞行动力学，避免局部姿态坐标，用于固定翼飞机。
- 方法要点：通过协调飞行假设，推导闭式轨迹到输入映射，包括姿态、角速度和推力-攻角对。
- 实验或效果：应用于系留飞行，解析获得所需滚转角，识别零滚转轨迹，展示气动协调与表观重力解耦。

## 摘要（原文）

> We present a robotics-oriented, coordinate-free formulation of inverse flight dynamics for fixed-wing aircraft on SO(3). Translational force balance is written in the world frame and rotational dynamics in the body frame; aerodynamic directions (drag, lift, side) are defined geometrically, avoiding local attitude coordinates. Enforcing coordinated flight (no sideslip), we derive a closed-form trajectory-to-input map yielding the attitude, angular velocity, and thrust-angle-of-attack pair, and we recover the aerodynamic moment coefficients component-wise. Applying such a map to tethered flight on spherical parallels, we obtain analytic expressions for the required bank angle and identify a specific zero-bank locus where the tether tension exactly balances centrifugal effects, highlighting the decoupling between aerodynamic coordination and the apparent gravity vector. Under a simple lift/drag law, the minimal-thrust angle of attack admits a closed form. These pointwise quasi-steady inversion solutions become steady-flight trim when the trajectory and rotational dynamics are time-invariant. The framework bridges inverse simulation in aeronautics with geometric modeling in robotics, providing a rigorous building block for trajectory design and feasibility checks.

