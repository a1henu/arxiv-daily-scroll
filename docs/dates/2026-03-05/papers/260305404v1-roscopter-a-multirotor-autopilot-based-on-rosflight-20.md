---
layout: default
title: ROScopter: A Multirotor Autopilot based on ROSflight 2.0
---

# ROScopter: A Multirotor Autopilot based on ROSflight 2.0
**arXiv**：[2603.05404v1](https://arxiv.org/abs/2603.05404) · [PDF](https://arxiv.org/pdf/2603.05404.pdf)  
**作者**：Jacob Moore, Ian Reid, Phil Tokumaru, Tim McLain  

**一句话要点**：提出ROS多旋翼自动驾驶仪以加速研究代码的仿真与硬件测试

**关键词**：多旋翼自动驾驶仪, ROS 2, 模块化架构, 仿真测试, 硬件测试, 研究加速

## 3 点简述
- 核心问题：研究代码在仿真和硬件测试中缺乏易于理解和修改的自动驾驶仪架构
- 方法要点：基于ROSflight 2.0设计轻量级自动驾驶仪，利用ROS 2提高模块化，完全在机载计算机上运行
- 实验或效果：硬件测试显示，在基本航点跟随任务中性能与先进自动驾驶仪相当，但代码库更精简和模块化

## 摘要（原文）

> ROScopter is a lean multirotor autopilot built for researchers. ROScopter seeks to accelerate simulation and hardware testing of research code with an architecture that is both easy to understand and simple to modify. ROScopter is designed to interface with ROSflight 2.0 and runs entirely on an onboard flight computer, leveraging the features of ROS 2 to improve modularity. This work describes the architecture of ROScopter and how it can be used to test application code in both simulated and hardware environments. Hardware results of the default ROScopter behavior are presented, showing that ROScopter achieves similar performance to another state-of-the-art autopilot for basic waypoint-following maneuvers, but with a significantly reduced and more modular code-base.

