---
layout: default
title: A Modular and Scalable System Architecture for Heterogeneous UAV Swarms Using ROS 2 and PX4-Autopilot
---

# A Modular and Scalable System Architecture for Heterogeneous UAV Swarms Using ROS 2 and PX4-Autopilot
**arXiv**：[2510.27327v1](https://arxiv.org/abs/2510.27327) · [PDF](https://arxiv.org/pdf/2510.27327.pdf)  
**作者**：Robert Pommeranz, Kevin Tebbe, Ralf Heynicke, Gerd Scholl  

**一句话要点**：提出基于ROS 2和PX4的模块化异构无人机群系统架构，以支持反无人机应用。

**关键词**：无人机群系统, ROS 2框架, PX4自动驾驶, 模块化架构, 计算机视觉集成, 编队控制

## 3 点简述
- 核心问题：异构无人机群系统集成与通信抽象，需适应多种硬件和任务。
- 方法要点：采用ROS 2节点独立封装硬件，软件抽象通信，支持编队飞行和视觉算法。
- 实验或效果：在Gazebo仿真和真实环境中验证系统可行性与协调能力。

## 摘要（原文）

> In this paper a modular and scalable architecture for heterogeneous
> swarm-based Counter Unmanned Aerial Systems (C-UASs) built on PX4-Autopilot and
> Robot Operating System 2 (ROS 2) framework is presented. The proposed
> architecture emphasizes seamless integration of hardware components by
> introducing independent ROS 2 nodes for each component of a Unmanned Aerial
> Vehicle (UAV). Communication between swarm participants is abstracted in
> software, allowing the use of various technologies without architectural
> changes. Key functionalities are supported, e.g. leader following and formation
> flight to maneuver the swarm. The system also allows computer vision algorithms
> to be integrated for the detection and tracking of UAVs. Additionally, a ground
> station control is integrated for the coordination of swarm operations.
> Swarm-based Unmanned Aerial System (UAS) architecture is verified within a
> Gazebo simulation environment but also in real-world demonstrations.

