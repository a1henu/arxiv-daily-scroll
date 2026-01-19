---
layout: default
title: A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation
---

# A3D: Adaptive Affordance Assembly with Dual-Arm Manipulation
**arXiv**：[2601.11076v1](https://arxiv.org/abs/2601.11076) · [PDF](https://arxiv.org/pdf/2601.11076.pdf)  
**作者**：Jiaqi Liang, Yue Chen, Qize Yu, Yan Shen, Haipeng Zhang, Hao Dong, Ruihai Wu  

**一句话要点**：提出A3D框架，通过自适应功能感知解决双臂机器人家具组装中的动态支撑问题。

**关键词**：双臂操作, 家具组装, 自适应功能感知, 点级几何表示, 动态支撑策略, 泛化能力

## 3 点简述
- 核心问题：家具组装需双臂协调，一臂操作部件，另一臂提供动态支撑与稳定，需适应不同几何形状和组装状态。
- 方法要点：学习自适应功能感知，利用密集点级几何表示建模部件交互模式，引入自适应模块基于交互反馈动态调整支撑策略。
- 实验或效果：在模拟和真实环境中，框架能泛化到多种部件几何和家具类别，提升组装效果。

## 摘要（原文）

> Furniture assembly is a crucial yet challenging task for robots, requiring precise dual-arm coordination where one arm manipulates parts while the other provides collaborative support and stabilization. To accomplish this task more effectively, robots need to actively adapt support strategies throughout the long-horizon assembly process, while also generalizing across diverse part geometries. We propose A3D, a framework which learns adaptive affordances to identify optimal support and stabilization locations on furniture parts. The method employs dense point-level geometric representations to model part interaction patterns, enabling generalization across varied geometries. To handle evolving assembly states, we introduce an adaptive module that uses interaction feedback to dynamically adjust support strategies during assembly based on previous interactions. We establish a simulation environment featuring 50 diverse parts across 8 furniture types, designed for dual-arm collaboration evaluation. Experiments demonstrate that our framework generalizes effectively to diverse part geometries and furniture categories in both simulation and real-world settings.

