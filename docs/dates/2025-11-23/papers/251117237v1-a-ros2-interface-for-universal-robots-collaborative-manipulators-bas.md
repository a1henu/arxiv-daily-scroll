---
layout: default
title: A ROS2 Interface for Universal Robots Collaborative Manipulators Based on ur_rtde
---

# A ROS2 Interface for Universal Robots Collaborative Manipulators Based on ur_rtde
**arXiv**：[2511.17237v1](https://arxiv.org/abs/2511.17237) · [PDF](https://arxiv.org/pdf/2511.17237.pdf)  
**作者**：Alessio Saccuti, Riccardo Monica, Jacopo Aleotti  

**一句话要点**：提出基于ur_rtde的ROS2驱动，为UR协作机械臂提供灵活解决方案。

**关键词**：ROS2驱动, UR协作机械臂, ur_rtde库, 路径规划, 开源软件

## 3 点简述
- 核心问题：缺乏通用ROS2驱动支持UR机械臂的多样化应用。
- 方法要点：基于ur_rtde库，暴露URScripts高级命令并支持插件自定义。
- 实验或效果：实现基于路径点的运动执行，并开源发布。

## 摘要（原文）

> In this paper a novel ROS2 driver for UR robot manipulators is presented, based on the ur_rtde C++ library. The proposed driver aims to be a flexible solution, adaptable to a wide range of applications. The driver exposes the high-level commands of Universal Robots URScripts, and custom commands can be added using a plugin system. Several commands have been implemented, including motion execution along a waypoint-based path. The driver is published as open source.

