---
layout: default
title: Pixel2Catch: Multi-Agent Sim-to-Real Transfer for Agile Manipulation with a Single RGB Camera
---

# Pixel2Catch: Multi-Agent Sim-to-Real Transfer for Agile Manipulation with a Single RGB Camera
**arXiv**：[2602.22733v1](https://arxiv.org/abs/2602.22733) · [PDF](https://arxiv.org/pdf/2602.22733.pdf)  
**作者**：Seongyong Kim, Junhyeon Cho, Kang-Won Lee, Soo-Chul Lim  

**一句话要点**：提出基于像素视觉信息与多智能体强化学习的单RGB相机敏捷抓取方法，实现仿真到现实的迁移。

**关键词**：敏捷抓取, 像素级视觉信息, 多智能体强化学习, 仿真到现实迁移, 单RGB相机

## 3 点简述
- 核心问题：机器人需及时感知抛掷物体运动并控制高自由度系统进行抓取。
- 方法要点：利用单RGB图像像素级视觉信息识别物体运动，设计异构多智能体强化学习框架，将机械臂与多指手作为独立智能体训练。
- 实验或效果：在仿真中协同训练智能体，成功将学习策略迁移到现实世界，实现稳定抓取。

## 摘要（原文）

> To catch a thrown object, a robot must be able to perceive the object's motion and generate control actions in a timely manner. Rather than explicitly estimating the object's 3D position, this work focuses on a novel approach that recognizes object motion using pixel-level visual information extracted from a single RGB image. Such visual cues capture changes in the object's position and scale, allowing the policy to reason about the object's motion. Furthermore, to achieve stable learning in a high-DoF system composed of a robot arm equipped with a multi-fingered hand, we design a heterogeneous multi-agent reinforcement learning framework that defines the arm and hand as independent agents with distinct roles. Each agent is trained cooperatively using role-specific observations and rewards, and the learned policies are successfully transferred from simulation to the real world.

