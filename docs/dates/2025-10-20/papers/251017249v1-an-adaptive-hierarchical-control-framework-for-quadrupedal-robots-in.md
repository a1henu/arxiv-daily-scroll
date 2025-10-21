---
layout: default
title: An adaptive hierarchical control framework for quadrupedal robots in planetary exploration
---

# An adaptive hierarchical control framework for quadrupedal robots in planetary exploration
**arXiv**：[2510.17249v1](https://arxiv.org/abs/2510.17249) · [PDF](https://arxiv.org/pdf/2510.17249.pdf)  
**作者**：Franek Stark, Rohit Kumar, Shubham Vyas, Hannah Isermann, Jonas Haack, Mihaela Popescu, Jakob Middelberg, Dennis Mronga, Frank Kirchner  

**一句话要点**：提出自适应分层控制框架以解决四足机器人在未知行星探索中的不确定性问题

**关键词**：四足机器人控制, 行星探索, 自适应控制, 模型适应, 脚步规划, ROS 2集成

## 3 点简述
- 核心问题：未知环境和机器人参数不确定性限制四足机器人在行星探索中的部署。
- 方法要点：结合模型动态控制、在线模型适应和自适应脚步规划，支持状态估计和运行时重配置。
- 实验或效果：在多个平台和火山实地测试中验证，机器人行走超过700米。

## 摘要（原文）

> Planetary exploration missions require robots capable of navigating extreme
> and unknown environments. While wheeled rovers have dominated past missions,
> their mobility is limited to traversable surfaces. Legged robots, especially
> quadrupeds, can overcome these limitations by handling uneven, obstacle-rich,
> and deformable terrains. However, deploying such robots in unknown conditions
> is challenging due to the need for environment-specific control, which is
> infeasible when terrain and robot parameters are uncertain. This work presents
> a modular control framework that combines model-based dynamic control with
> online model adaptation and adaptive footstep planning to address uncertainties
> in both robot and terrain properties. The framework includes state estimation
> for quadrupeds with and without contact sensing, supports runtime
> reconfiguration, and is integrated into ROS 2 with open-source availability.
> Its performance was validated on two quadruped platforms, multiple hardware
> architectures, and in a volcano field test, where the robot walked over 700 m.

