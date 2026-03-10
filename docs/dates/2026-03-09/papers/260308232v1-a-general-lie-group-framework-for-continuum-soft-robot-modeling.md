---
layout: default
title: A General Lie-Group Framework for Continuum Soft Robot Modeling
---

# A General Lie-Group Framework for Continuum Soft Robot Modeling
**arXiv**：[2603.08232v1](https://arxiv.org/abs/2603.08232) · [PDF](https://arxiv.org/pdf/2603.08232.pdf)  
**作者**：Lingxiao Xun, Benoît Rosa, Jérôme Szewczyk, Brahim Tamadazte  

**一句话要点**：提出基于李群SE(3)的通用框架，以改进连续体软机器人建模的几何控制与计算效率。

**关键词**：连续体软机器人, 李群建模, Cosserat杆理论, 实时仿真, 几何控制, 机器人结构

## 3 点简述
- 针对现有应变和配置方法在几何局部控制与单位四元数约束上的局限性。
- 结合Cosserat杆理论与累积参数化，推导统一运动学、静力学和动力学解析表达式。
- 通过多种机器人结构验证框架的有效性、通用性和实时仿真能力。

## 摘要（原文）

> This paper introduces a general Lie group framework for modeling continuum soft robots, employing Cosserat rod theory combined with cumulative parameterization on the Lie group SE(3). This novel approach addresses limitations present in current strain-based and configuration-based methods by providing geometric local control and eliminating unit quaternion constraints. The paper derives unified analytical expressions for kinematics, statics, and dynamics, including recursive Jacobian computations and an energy-conserving integrator suitable for real-time simulation and control. Additionally, the framework is extended to handle complex robotic structures, including segmented, branched, nested, and rigid-soft composite configurations, facilitating a modular and unified modeling strategy. The effectiveness, generality, and computational efficiency of the proposed methodology are demonstrated through various scenarios, including large-deformation rods, concentric tube robots, parallel robots, cable-driven robots, and articulated fingers. This work enhances modeling flexibility and numerical performance, providing an improved toolset for designing, simulating, and controlling soft robotic systems.

