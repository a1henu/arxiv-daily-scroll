---
layout: default
title: Control Barrier Corridors: From Safety Functions to Safe Sets
---

# Control Barrier Corridors: From Safety Functions to Safe Sets
**arXiv**：[2603.06494v1](https://arxiv.org/abs/2603.06494) · [PDF](https://arxiv.org/pdf/2603.06494.pdf)  
**作者**：Ömür Arslan, Nikolay Atanasov  

**一句话要点**：提出控制屏障走廊以统一功能与几何安全方法，用于机器人安全自主控制

**关键词**：控制屏障函数, 安全运动规划, 自主机器人, 反馈控制, 安全走廊

## 3 点简述
- 核心问题：现有安全方法如控制屏障函数和运动走廊在功能与几何上分离，难以统一应用
- 方法要点：引入控制屏障走廊概念，将控制屏障函数转换为局部安全目标区域，用于反馈控制中的目标选择
- 实验或效果：在全驱动系统、运动学独轮车和线性输出调节系统上验证，展示安全与响应性之间的权衡

## 摘要（原文）

> Safe autonomy is a critical requirement and a key enabler for robots to operate safely in unstructured complex environments. Control barrier functions and safe motion corridors are two widely used but technically distinct safety methods, functional and geometric, respectively, for safe motion planning and control. Control barrier functions are applied to the safety filtering of control inputs to limit the decay rate of system safety, whereas safe motion corridors are geometrically constructed to define a local safe zone around the system state for use in motion optimization and reference-governor design. This paper introduces a new notion of control barrier corridors, which unifies these two approaches by converting control barrier functions into local safe goal regions for reference goal selection in feedback control systems. We show, with examples on fully actuated systems, kinematic unicycles, and linear output regulation systems, that individual state safety can be extended locally over control barrier corridors for convex barrier functions, provided the control convergence rate matches the barrier decay rate, highlighting a trade-off between safety and reactiveness. Such safe control barrier corridors enable safely reachable persistent goal selection over continuously changing barrier corridors during system motion, which we demonstrate for verifiably safe and persistent path following in autonomous exploration of unknown environments.

