---
layout: default
title: Vision-based Goal-Reaching Control for Mobile Robots Using a Hierarchical Learning Framework
---

# Vision-based Goal-Reaching Control for Mobile Robots Using a Hierarchical Learning Framework
**arXiv**：[2601.00610v1](https://arxiv.org/abs/2601.00610) · [PDF](https://arxiv.org/pdf/2601.00610.pdf)  
**作者**：Mehdi Heydari Shahna, Pauli Mustalahti, Jouni Mattila  

**一句话要点**：提出基于分层学习框架的视觉目标到达控制，以解决大型机器人在不稳定地形上的安全运动问题。

**关键词**：视觉目标到达控制, 分层学习框架, 强化学习运动规划, 鲁棒自适应控制, 机器人安全监控

## 3 点简述
- 核心问题：强化学习在机器人应用中需大量探索，可能导致不安全行为，限制其在复杂地形大型机器人的应用。
- 方法要点：采用分层框架，结合视觉姿态估计、强化学习运动规划、深度学习建模和鲁棒自适应控制，确保稳定性和安全性。
- 实验或效果：在6000公斤机器人上实验验证，框架能保证执行系统均匀指数稳定性和整体操作安全。

## 摘要（原文）

> Reinforcement learning (RL) is effective in many robotic applications, but it requires extensive exploration of the state-action space, during which behaviors can be unsafe. This significantly limits its applicability to large robots with complex actuators operating on unstable terrain. Hence, to design a safe goal-reaching control framework for large-scale robots, this paper decomposes the whole system into a set of tightly coupled functional modules. 1) A real-time visual pose estimation approach is employed to provide accurate robot states to 2) an RL motion planner for goal-reaching tasks that explicitly respects robot specifications. The RL module generates real-time smooth motion commands for the actuator system, independent of its underlying dynamic complexity. 3) In the actuation mechanism, a supervised deep learning model is trained to capture the complex dynamics of the robot and provide this model to 4) a model-based robust adaptive controller that guarantees the wheels track the RL motion commands even on slip-prone terrain. 5) Finally, to reduce human intervention, a mathematical safety supervisor monitors the robot, stops it on unsafe faults, and autonomously guides it back to a safe inspection area. The proposed framework guarantees uniform exponential stability of the actuation system and safety of the whole operation. Experiments on a 6,000 kg robot in different scenarios confirm the effectiveness of the proposed framework.

