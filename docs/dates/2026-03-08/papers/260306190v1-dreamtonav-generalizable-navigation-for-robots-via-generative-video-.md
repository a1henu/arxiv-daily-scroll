---
layout: default
title: DreamToNav: Generalizable Navigation for Robots via Generative Video Planning
---

# DreamToNav: Generalizable Navigation for Robots via Generative Video Planning
**arXiv**：[2603.06190v1](https://arxiv.org/abs/2603.06190) · [PDF](https://arxiv.org/pdf/2603.06190.pdf)  
**作者**：Valerii Serpiva, Jeffrin Sam, Chidera Simon, Hajira Amjad, Iana Zhura, Artem Lykov, Dzmitry Tsetserukou  

**一句话要点**：提出DreamToNav框架，利用生成视频模型实现机器人基于自然语言指令的通用导航。

**关键词**：机器人导航, 生成视频模型, 自然语言处理, 视觉规划, 运动路径提取, 通用框架

## 3 点简述
- 核心问题：传统机器人导航依赖刚性路径点，难以处理模糊自然语言指令和复杂行为规划。
- 方法要点：使用Qwen 2.5-VL-7B-Instruct细化指令，NVIDIA Cosmos 2.5生成物理一致视频，从中提取运动路径。
- 实验或效果：在轮式和四足机器人室内导航中，成功率76.7%，目标误差0.05-0.10米，轨迹误差低于0.15米。

## 摘要（原文）

> We present DreamToNav, a novel autonomous robot framework that uses generative video models to enable intuitive, human-in-the-loop control. Instead of relying on rigid waypoint navigation, users provide natural language prompts (e.g. ``Follow the person carefully''), which the system translates into executable motion. Our pipeline first employs Qwen 2.5-VL-7B-Instruct to refine vague user instructions into precise visual descriptions. These descriptions condition NVIDIA Cosmos 2.5, a state-of-the-art video foundation model, to synthesize a physically consistent video sequence of the robot performing the task. From this synthetic video, we extract a valid kinematic path using visual pose estimation, robot detection and trajectory recovery. By treating video generation as a planning engine, DreamToNav allows robots to visually "dream" complex behaviors before executing them, providing a unified framework for obstacle avoidance and goal-directed navigation without task-specific engineering. We evaluate the approach on both a wheeled mobile robot and a quadruped robot in indoor navigation tasks. DreamToNav achieves a success rate of 76.7%, with final goal errors typically within 0.05-0.10 m and trajectory tracking errors below 0.15 m. These results demonstrate that trajectories extracted from generative video predictions can be reliably executed on physical robots across different locomotion platforms.

