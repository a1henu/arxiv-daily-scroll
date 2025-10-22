---
layout: default
title: Online Object-Level Semantic Mapping for Quadrupeds in Real-World Environments
---

# Online Object-Level Semantic Mapping for Quadrupeds in Real-World Environments
**arXiv**：[2510.18776v1](https://arxiv.org/abs/2510.18776) · [PDF](https://arxiv.org/pdf/2510.18776.pdf)  
**作者**：Emad Razavi, Angelo Bratta, João Carlos Virgolino Soares, Carmine Recchiuto, Claudio Semini  

**一句话要点**：提出在线语义对象映射系统，用于四足机器人在真实室内环境中的实时建图。

**关键词**：语义映射, 四足机器人, 在线建图, 对象关联, 室内环境

## 3 点简述
- 核心问题：在真实室内环境中，四足机器人需将传感器检测转换为全局地图中的命名对象。
- 方法要点：集成范围几何与相机检测，合并同帧检测并跨帧关联为持久对象实例。
- 实验或效果：在机器人测试中，对象层在视角变化下保持稳定，可查询类、姿态和置信度。

## 摘要（原文）

> We present an online semantic object mapping system for a quadruped robot
> operating in real indoor environments, turning sensor detections into named
> objects in a global map. During a run, the mapper integrates range geometry
> with camera detections, merges co-located detections within a frame, and
> associates repeated detections into persistent object instances across frames.
> Objects remain in the map when they are out of view, and repeated sightings
> update the same instance rather than creating duplicates. The output is a
> compact object layer that can be queried (class, pose, and confidence), is
> integrated with the occupancy map and readable by a planner. In on-robot tests,
> the layer remained stable across viewpoint changes.

