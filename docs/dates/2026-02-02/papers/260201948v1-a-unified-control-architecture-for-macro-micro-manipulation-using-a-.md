---
layout: default
title: A Unified Control Architecture for Macro-Micro Manipulation using a Active Remote Center of Compliance for Manufacturing Applications
---

# A Unified Control Architecture for Macro-Micro Manipulation using a Active Remote Center of Compliance for Manufacturing Applications
**arXiv**：[2602.01948v1](https://arxiv.org/abs/2602.01948) · [PDF](https://arxiv.org/pdf/2602.01948.pdf)  
**作者**：Patrick Frank, Christian Friedrich  

**一句话要点**：提出统一控制架构，通过主动远程柔顺中心提升宏微操作器在制造应用中的交互控制带宽。

**关键词**：宏微操作器, 交互控制, 控制架构, 制造应用, 远程柔顺中心, 控制带宽

## 3 点简述
- 传统宏微操作器将位置控制与交互控制分离，限制了交互控制带宽。
- 新架构将宏操作器纳入主动交互控制，提高控制带宽2.1倍于领先方法。
- 实验验证包括碰撞、力轨迹跟踪和工业装配任务，支持高效控制器设计。

## 摘要（原文）

> Macro-micro manipulators combine a macro manipulator with a large workspace, such as an industrial robot, with a lightweight, high-bandwidth micro manipulator. This enables highly dynamic interaction control while preserving the wide workspace of the robot. Traditionally, position control is assigned to the macro manipulator, while the micro manipulator handles the interaction with the environment, limiting the achievable interaction control bandwidth. To solve this, we propose a novel control architecture that incorporates the macro manipulator into the active interaction control. This leads to a increase in control bandwidth by a factor of 2.1 compared to the state of the art architecture, based on the leader-follower approach and factor 12.5 compared to traditional robot-based force control. Further we propose surrogate models for a more efficient controller design and easy adaptation to hardware changes. We validate our approach by comparing it against the other control schemes in different experiments, like collision with an object, following a force trajectory and industrial assembly tasks.

