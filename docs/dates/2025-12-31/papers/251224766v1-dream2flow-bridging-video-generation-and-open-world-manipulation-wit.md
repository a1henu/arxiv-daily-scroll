---
layout: default
title: Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow
---

# Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow
**arXiv**：[2512.24766v1](https://arxiv.org/abs/2512.24766) · [PDF](https://arxiv.org/pdf/2512.24766.pdf)  
**作者**：Karthik Dharmarajan, Wenlong Huang, Jiajun Wu, Li Fei-Fei, Ruohan Zhang  

**一句话要点**：提出Dream2Flow框架，通过3D物体流连接视频生成与开放世界机器人操作

**关键词**：视频生成, 机器人操作, 3D物体流, 轨迹跟踪, 零样本学习

## 3 点简述
- 核心问题：视频生成模型难以将人类引导的运动转换为机器人可执行的低级动作
- 方法要点：从生成视频重建3D物体运动，将操作任务建模为物体轨迹跟踪
- 实验或效果：在模拟和真实世界实验中，实现零样本指导，操作多种物体类别

## 摘要（原文）

> Generative video modeling has emerged as a compelling tool to zero-shot reason about plausible physical interactions for open-world manipulation. Yet, it remains a challenge to translate such human-led motions into the low-level actions demanded by robotic systems. We observe that given an initial image and task instruction, these models excel at synthesizing sensible object motions. Thus, we introduce Dream2Flow, a framework that bridges video generation and robotic control through 3D object flow as an intermediate representation. Our method reconstructs 3D object motions from generated videos and formulates manipulation as object trajectory tracking. By separating the state changes from the actuators that realize those changes, Dream2Flow overcomes the embodiment gap and enables zero-shot guidance from pre-trained video models to manipulate objects of diverse categories-including rigid, articulated, deformable, and granular. Through trajectory optimization or reinforcement learning, Dream2Flow converts reconstructed 3D object flow into executable low-level commands without task-specific demonstrations. Simulation and real-world experiments highlight 3D object flow as a general and scalable interface for adapting video generation models to open-world robotic manipulation. Videos and visualizations are available at https://dream2flow.github.io/.

