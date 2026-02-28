---
layout: default
title: Pixel2Catch: Multi-Agent Sim-to-Real Transfer for Agile Manipulation with a Single RGB Camera
---

# Pixel2Catch: Multi-Agent Sim-to-Real Transfer for Agile Manipulation with a Single RGB Camera
**arXiv**：[2602.22733v1](https://arxiv.org/abs/2602.22733) · [PDF](https://arxiv.org/pdf/2602.22733.pdf)  
**作者**：Seongyong Kim, Junhyeon Cho, Kang-Won Lee, Soo-Chul Lim  

**一句话要点**：提出基于像素视觉信息的单RGB相机多智能体强化学习框架，实现敏捷抓取抛掷物体的仿真到现实迁移。

**关键词**：单RGB相机感知, 像素级视觉信息, 多智能体强化学习, 仿真到现实迁移, 敏捷抓取, 异构智能体

## 3 点简述
- 核心问题：机器人需及时感知抛掷物体运动并生成控制动作，传统方法依赖3D位置估计，计算复杂且实时性差。
- 方法要点：利用单RGB图像提取像素级视觉信息捕捉物体位置和尺度变化，设计异构多智能体强化学习框架，将机械臂和多指手定义为独立智能体进行协同训练。
- 实验或效果：在仿真中稳定学习高自由度系统策略，并成功迁移到现实世界，实现敏捷抓取任务。

## 摘要（原文）

> To catch a thrown object, a robot must be able to perceive the object's motion and generate control actions in a timely manner. Rather than explicitly estimating the object's 3D position, this work focuses on a novel approach that recognizes object motion using pixel-level visual information extracted from a single RGB image. Such visual cues capture changes in the object's position and scale, allowing the policy to reason about the object's motion. Furthermore, to achieve stable learning in a high-DoF system composed of a robot arm equipped with a multi-fingered hand, we design a heterogeneous multi-agent reinforcement learning framework that defines the arm and hand as independent agents with distinct roles. Each agent is trained cooperatively using role-specific observations and rewards, and the learned policies are successfully transferred from simulation to the real world.

