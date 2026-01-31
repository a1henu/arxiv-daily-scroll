---
layout: default
title: Multi-Modular MANTA-RAY: A Modular Soft Surface Platform for Distributed Multi-Object Manipulation
---

# Multi-Modular MANTA-RAY: A Modular Soft Surface Platform for Distributed Multi-Object Manipulation
**arXiv**：[2601.21884v1](https://arxiv.org/abs/2601.21884) · [PDF](https://arxiv.org/pdf/2601.21884.pdf)  
**作者**：Pratik Ingle, Jørn Lambertsen, Kasper Støy, Andres Faina  

**一句话要点**：提出多模块MANTA-RAY平台，通过分布式模块化设计解决软表面操纵系统的可扩展性问题。

**关键词**：软表面操纵, 模块化系统, 分布式控制, PID控制器, 多对象操纵, 可扩展性

## 3 点简述
- 核心问题：高密度致动器阵列导致自由度增加，限制软表面操纵系统的可扩展性和复杂性。
- 方法要点：采用模块化软表面平台，结合对象传递和几何变换驱动的PID控制器，减少致动器密度并避免数据驱动训练。
- 实验或效果：在仿真和物理原型中验证，成功操纵多种几何、质量和纹理的物体，包括易碎物品，并实现并行操纵。

## 摘要（原文）

> Manipulation surfaces control objects by actively deforming their shape rather than directly grasping them. While dense actuator arrays can generate complex deformations, they also introduce high degrees of freedom (DOF), increasing system complexity and limiting scalability. The MANTA-RAY (Manipulation with Adaptive Non-rigid Textile Actuation with Reduced Actuation densitY) platform addresses these challenges by leveraging a soft, fabric-based surface with reduced actuator density to manipulate fragile and heterogeneous objects. Previous studies focused on single-module implementations supported by four actuators, whereas the feasibility and benefits of a scalable, multi-module configuration remain unexplored. In this work, we present a distributed, modular, and scalable variant of the MANTA-RAY platform that maintains manipulation performance with a reduced actuator density. The proposed multi-module MANTA-RAY platform and control strategy employs object passing between modules and a geometric transformation driven PID controller that directly maps tilt-angle control outputs to actuator commands, eliminating the need for extensive data-driven or black-box training. We evaluate system performance in simulation across surface configurations of varying modules (3x3 and 4x4) and validate its feasibility through experiments on a physical 2x2 hardware prototype. The system successfully manipulates objects with diverse geometries, masses, and textures including fragile items such as eggs and apples as well as enabling parallel manipulation. The results demonstrate that the multi-module MANTA-RAY improves scalability and enables coordinated manipulation of multiple objects across larger areas, highlighting its potential for practical, real-world applications.

