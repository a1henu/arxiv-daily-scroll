---
layout: default
title: A Task-Driven, Planner-in-the-Loop Computational Design Framework for Modular Manipulators
---

# A Task-Driven, Planner-in-the-Loop Computational Design Framework for Modular Manipulators
**arXiv**：[2512.16069v1](https://arxiv.org/abs/2512.16069) · [PDF](https://arxiv.org/pdf/2512.16069.pdf)  
**作者**：Maolin Lei, Edoardo Romiti, Arturo Laurenzi, Rui Dai, Matteo Dalle Vedove, Jiatao Ding, Daniele Fontanelli, Nikos Tsagarakis  

**一句话要点**：提出任务驱动的计算设计框架，通过形态与姿态协同优化解决模块化机械臂运动规划问题。

**关键词**：模块化机械臂, 计算设计框架, 形态优化, 运动规划, 双分支形态, 任务驱动设计

## 3 点简述
- 核心问题：模块化机械臂部署需在运动学、动力学和物理约束下联合优化形态与安装姿态，传统单分支设计易违反扭矩限制。
- 方法要点：集成轨迹规划与形态姿态协同优化，采用HMPC进行运动规划，CMA-ES探索混合搜索空间，引入虚拟模块支持双分支形态。
- 实验或效果：在抛光、钻孔和拾放任务中验证框架有效性，能生成满足约束的可行设计，实现灵活目标如最大化可操作性。

## 摘要（原文）

> Modular manipulators composed of pre-manufactured and interchangeable modules offer high adaptability across diverse tasks. However, their deployment requires generating feasible motions while jointly optimizing morphology and mounted pose under kinematic, dynamic, and physical constraints. Moreover, traditional single-branch designs often extend reach by increasing link length, which can easily violate torque limits at the base joint. To address these challenges, we propose a unified task-driven computational framework that integrates trajectory planning across varying morphologies with the co-optimization of morphology and mounted pose. Within this framework, a hierarchical model predictive control (HMPC) strategy is developed to enable motion planning for both redundant and non-redundant manipulators. For design optimization, the CMA-ES is employed to efficiently explore a hybrid search space consisting of discrete morphology configurations and continuous mounted poses. Meanwhile, a virtual module abstraction is introduced to enable bi-branch morphologies, allowing an auxiliary branch to offload torque from the primary branch and extend the achievable workspace without increasing the capacity of individual joint modules. Extensive simulations and hardware experiments on polishing, drilling, and pick-and-place tasks demonstrate the effectiveness of the proposed framework. The results show that: 1) the framework can generate multiple feasible designs that satisfy kinematic and dynamic constraints while avoiding environmental collisions for given tasks; 2) flexible design objectives, such as maximizing manipulability, minimizing joint effort, or reducing the number of modules, can be achieved by customizing the cost functions; and 3) a bi-branch morphology capable of operating in a large workspace can be realized without requiring more powerful basic modules.

