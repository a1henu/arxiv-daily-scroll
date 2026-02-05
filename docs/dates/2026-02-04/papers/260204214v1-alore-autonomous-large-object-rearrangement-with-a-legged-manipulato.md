---
layout: default
title: ALORE: Autonomous Large-Object Rearrangement with a Legged Manipulator
---

# ALORE: Autonomous Large-Object Rearrangement with a Legged Manipulator
**arXiv**：[2602.04214v1](https://arxiv.org/abs/2602.04214) · [PDF](https://arxiv.org/pdf/2602.04214.pdf)  
**作者**：Zhihai Bi, Yushan Zhang, Kai Chen, Guoyang Zhao, Yulin Li, Jun Ma  

**一句话要点**：提出ALORE系统，用于腿式操纵器自主重排大型物体，提升多物体重排效率与稳定性。

**关键词**：腿式操纵器, 物体重排, 分层强化学习, 任务-运动规划, 自主机器人

## 3 点简述
- 核心问题：大型物体重排需处理多样物体、复杂环境和无碰撞运动，挑战巨大。
- 方法要点：采用分层强化学习训练管道、统一交互配置表示和任务-运动规划框架，优化多物体学习与重排。
- 实验或效果：系统在仿真和真实实验中表现优越，完成32把椅子重排和40米长距离自主重排，无失败。

## 摘要（原文）

> Endowing robots with the ability to rearrange various large and heavy objects, such as furniture, can substantially alleviate human workload. However, this task is extremely challenging due to the need to interact with diverse objects and efficiently rearrange multiple objects in complex environments while ensuring collision-free loco-manipulation. In this work, we present ALORE, an autonomous large-object rearrangement system for a legged manipulator that can rearrange various large objects across diverse scenarios. The proposed system is characterized by three main features: (i) a hierarchical reinforcement learning training pipeline for multi-object environment learning, where a high-level object velocity controller is trained on top of a low-level whole-body controller to achieve efficient and stable joint learning across multiple objects; (ii) two key modules, a unified interaction configuration representation and an object velocity estimator, that allow a single policy to regulate planar velocity of diverse objects accurately; and (iii) a task-and-motion planning framework that jointly optimizes object visitation order and object-to-target assignment, improving task efficiency while enabling online replanning. Comparisons against strong baselines show consistent superiority in policy generalization, object-velocity tracking accuracy, and multi-object rearrangement efficiency. Key modules are systematically evaluated, and extensive simulations and real-world experiments are conducted to validate the robustness and effectiveness of the entire system, which successfully completes 8 continuous loops to rearrange 32 chairs over nearly 40 minutes without a single failure, and executes long-distance autonomous rearrangement over an approximately 40 m route. The open-source packages are available at https://zhihaibi.github.io/Alore/.

