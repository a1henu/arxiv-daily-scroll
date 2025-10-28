---
layout: default
title: Workspace Registration and Collision Detection for Industrial Robotics Applications
---

# Workspace Registration and Collision Detection for Industrial Robotics Applications
**arXiv**：[2510.23227v1](https://arxiv.org/abs/2510.23227) · [PDF](https://arxiv.org/pdf/2510.23227.pdf)  
**作者**：Klaus Zauner, Josef El Dib, Hubert Gattringer, Andreas Mueller  

**一句话要点**：比较传感器与流程，实现工业机器人工作空间注册与碰撞检测

**关键词**：工业机器人, 工作空间注册, 碰撞检测, 点云处理, 区域生长分割, VCCS算法

## 3 点简述
- 核心问题：机器人运动规划需精确环境知识，以定义限制区域和考虑碰撞对象。
- 方法要点：使用点云采集、区域生长分割和VCCS算法识别碰撞对象并近似点簇。
- 实验或效果：比较不同传感器，展示从检测到完整碰撞环境的流程，检测机器人与环境碰撞。

## 摘要（原文）

> Motion planning for robotic manipulators relies on precise knowledge of the
> environment in order to be able to define restricted areas and to take
> collision objects into account. To capture the workspace, point clouds of the
> environment are acquired using various sensors. The collision objects are
> identified by region growing segmentation and VCCS algorithm. Subsequently the
> point clusters are approximated. The aim of the present paper is to compare
> different sensors, to illustrate the process from detection to the finished
> collision environment and to detect collisions between the robot and this
> environment.

