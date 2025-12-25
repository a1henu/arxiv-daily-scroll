---
layout: default
title: Tracing Energy Flow: Learning Tactile-based Grasping Force Control to Prevent Slippage in Dynamic Object Interaction
---

# Tracing Energy Flow: Learning Tactile-based Grasping Force Control to Prevent Slippage in Dynamic Object Interaction
**arXiv**：[2512.21043v1](https://arxiv.org/abs/2512.21043) · [PDF](https://arxiv.org/pdf/2512.21043.pdf)  
**作者**：Cheng-Yu Kuo, Hirofumi Shin, Takamitsu Matsubara  

**一句话要点**：提出基于触觉的能量流追踪方法，以在动态交互中学习抓取力控制防止滑动

**关键词**：触觉传感, 抓取力控制, 能量抽象, 动态交互, 模型学习, 防滑动

## 3 点简述
- 核心问题：动态物体交互中，未知属性和有限传感下抓取力调节以防止滑动是机器人操作的关键挑战。
- 方法要点：引入物理信息能量抽象，将物体建模为虚拟能量容器，基于触觉传感学习能量动态并进行实时抓取力优化。
- 实验或效果：在仿真和硬件实验中，方法能在几分钟内从零学习抓取力控制，有效减少滑动并延长抓取时间，无需外部传感或先验知识。

## 摘要（原文）

> Regulating grasping force to reduce slippage during dynamic object interaction remains a fundamental challenge in robotic manipulation, especially when objects are manipulated by multiple rolling contacts, have unknown properties (such as mass or surface conditions), and when external sensing is unreliable. In contrast, humans can quickly regulate grasping force by touch, even without visual cues. Inspired by this ability, we aim to enable robotic hands to rapidly explore objects and learn tactile-driven grasping force control under motion and limited sensing. We propose a physics-informed energy abstraction that models the object as a virtual energy container. The inconsistency between the fingers' applied power and the object's retained energy provides a physically grounded signal for inferring slip-aware stability. Building on this abstraction, we employ model-based learning and planning to efficiently model energy dynamics from tactile sensing and perform real-time grasping force optimization. Experiments in both simulation and hardware demonstrate that our method can learn grasping force control from scratch within minutes, effectively reduce slippage, and extend grasp duration across diverse motion-object pairs, all without relying on external sensing or prior object knowledge.

