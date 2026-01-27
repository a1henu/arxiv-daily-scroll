---
layout: default
title: Quest2ROS2: A ROS 2 Framework for Bi-manual VR Teleoperation
---

# Quest2ROS2: A ROS 2 Framework for Bi-manual VR Teleoperation
**arXiv**：[2601.18289v1](https://arxiv.org/abs/2601.18289) · [PDF](https://arxiv.org/pdf/2601.18289.pdf)  
**作者**：Jialong Li, Zhenguo Wang, Tianci Wang, Maj Stenmark, Volker Krueger  

**一句话要点**：提出Quest2ROS2框架，通过相对运动控制实现双手机器人VR遥操作，以扩展机器人数据收集。

**关键词**：双手机器人遥操作, ROS2框架, VR控制, 相对运动控制, 数据收集扩展

## 3 点简述
- 核心问题：传统VR遥操作受限于工作空间，影响机器人数据收集的扩展性。
- 方法要点：基于VR控制器姿态变化计算机器人运动，实现直观、姿态无关的相对运动控制。
- 实验或效果：集成实时RViz可视化、简化夹爪控制和暂停重置功能，支持多种控制模式优化操作体验。

## 摘要（原文）

> Quest2ROS2 is an open-source ROS2 framework for bi-manual teleoperation designed to scale robot data collection. Extending Quest2ROS, it overcomes workspace limitations via relative motion-based control, calculating robot movement from VR controller pose changes to enable intuitive, pose-independent operation. The framework integrates essential usability and safety features, including real-time RViz visualization, streamlined gripper control, and a pause-and-reset function for smooth transitions. We detail a modular architecture that supports "Side-by-Side" and "Mirror" control modes to optimize operator experience across diverse platforms. Code is available at: https://github.com/Taokt/Quest2ROS2.

