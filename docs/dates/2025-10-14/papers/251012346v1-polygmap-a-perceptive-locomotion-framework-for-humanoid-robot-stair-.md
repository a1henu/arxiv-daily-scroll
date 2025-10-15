---
layout: default
title: PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing
---

# PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing
**arXiv**：[2510.12346v1](https://arxiv.org/abs/2510.12346) · [PDF](https://arxiv.org/pdf/2510.12346.pdf)  
**作者**：Bingquan Li, Ning Wang, Tianwei Zhang, Zhicheng He, Yucong Wu  

**一句话要点**：提出PolygMap感知运动框架以解决人形机器人楼梯攀爬问题

**关键词**：人形机器人, 楼梯攀爬, 感知运动规划, 多边形语义地图, 多传感器融合, 实时规划

## 3 点简述
- 核心问题：人形机器人需在未知空间中精确踩踏位置以模拟人类行走
- 方法要点：构建实时多边形楼梯平面语义地图，并基于此进行脚步规划
- 实验或效果：在NVIDIA Orin上实现20-30Hz全身运动规划，室内外实验显示高效鲁棒

## 摘要（原文）

> Recently, biped robot walking technology has been significantly developed,
> mainly in the context of a bland walking scheme. To emulate human walking,
> robots need to step on the positions they see in unknown spaces accurately. In
> this paper, we present PolyMap, a perception-based locomotion planning
> framework for humanoid robots to climb stairs. Our core idea is to build a
> real-time polygonal staircase plane semantic map, followed by a footstep planar
> using these polygonal plane segments. These plane segmentation and visual
> odometry are done by multi-sensor fusion(LiDAR, RGB-D camera and IMUs). The
> proposed framework is deployed on a NVIDIA Orin, which performs 20-30 Hz
> whole-body motion planning output. Both indoor and outdoor real-scene
> experiments indicate that our method is efficient and robust for humanoid robot
> stair climbing.

