---
layout: default
title: Adaptive Cost-Map-based Path Planning in Partially Unknown Environments with Movable Obstacles
---

# Adaptive Cost-Map-based Path Planning in Partially Unknown Environments with Movable Obstacles
**arXiv**：[2510.15336v1](https://arxiv.org/abs/2510.15336) · [PDF](https://arxiv.org/pdf/2510.15336.pdf)  
**作者**：Liviu-Mihai Stan, Ranulfo Bezerra, Shotaro Kojima, Tsige Tadesse Alemayoh, Satoshi Tadokoro, Masashi Konyo, Kazunori Ohno  

**一句话要点**：提出自适应成本地图路径规划方法，用于部分未知环境中可移动障碍物的机器人导航

**关键词**：路径规划, 可移动障碍物, 自适应成本地图, ROS2导航, LiDAR感知, 灾难响应机器人

## 3 点简述
- 核心问题：机器人在灾难响应等非结构化环境中需识别并处理可移动障碍物以避免死锁
- 方法要点：基于LiDAR和里程计，在ROS2 Nav2中嵌入可移动障碍物层和慢速姿态检查器
- 实验或效果：Gazebo仿真显示比基线更高的目标到达率和更少死锁，计算轻量适合资源受限机器人

## 摘要（原文）

> Reliable navigation in disaster-response and other unstructured indoor
> settings requires robots not only to avoid obstacles but also to recognise when
> those obstacles can be pushed aside. We present an adaptive, LiDAR and
> odometry-based path-planning framework that embeds this capability into the
> ROS2 Nav2 stack. A new Movable Obstacles Layer labels all LiDAR returns missing
> from a prior static map as tentatively movable and assigns a reduced traversal
> cost. A companion Slow-Pose Progress Checker monitors the ratio of commanded to
> actual velocity; when the robot slows appreciably, the local cost is raised
> from light to heavy, and on a stall to lethal, prompting the global planner to
> back out and re-route. Gazebo evaluations on a Scout Mini, spanning isolated
> objects and cluttered corridors, show higher goal-reach rates and fewer
> deadlocks than a no-layer baseline, with traversal times broadly comparable.
> Because the method relies only on planar scans and CPU-level computation, it
> suits resource-constrained search and rescue robots and integrates into
> heterogeneous platforms with minimal engineering. Overall, the results indicate
> that interaction-aware cost maps are a lightweight, ROS2-native extension for
> navigating among potentially movable obstacles in unstructured settings. The
> full implementation will be released as open source
> athttps://costmap-namo.github.io.

