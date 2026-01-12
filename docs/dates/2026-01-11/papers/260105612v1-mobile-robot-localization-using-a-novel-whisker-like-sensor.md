---
layout: default
title: Mobile Robot Localization Using a Novel Whisker-Like Sensor
---

# Mobile Robot Localization Using a Novel Whisker-Like Sensor
**arXiv**：[2601.05612v1](https://arxiv.org/abs/2601.05612) · [PDF](https://arxiv.org/pdf/2601.05612.pdf)  
**作者**：Prasanna K. Routray, Basak Sakcak, Steven M. LaValle, Manivannan M  

**一句话要点**：提出基于虚拟传感器模型的单触须感知框架，用于已知平面环境中的机器人接触点估计与定位。

**关键词**：触须传感器, 机器人定位, 虚拟传感器模型, 接触点估计, 预像概念, 短程感知

## 3 点简述
- 核心问题：在视觉或长距离感知不可靠的受限、杂乱环境中，实现机器人短程感知与定位。
- 方法要点：开发虚拟传感器模型，通过预像概念结合运动模型估计接触点，迭代重建障碍边界并定位。
- 实验或效果：仿真与物理实验验证，使用低成本3D打印霍尔效应触须传感器，定位误差低于7毫米。

## 摘要（原文）

> Whisker-like touch sensors offer unique advantages for short-range perception in environments where visual and long-range sensing are unreliable, such as confined, cluttered, or low-visibility settings. This paper presents a framework for estimating contact points and robot localization in a known planar environment using a single whisker sensor. We develop a family of virtual sensor models. Each model maps robot configurations to sensor observations and enables structured reasoning through the concept of preimages - the set of robot states consistent with a given observation. The notion of virtual sensor models serves as an abstraction to reason about state uncertainty without dependence on physical implementation. By combining sensor observations with a motion model, we estimate the contact point. Iterative estimation then enables reconstruction of obstacle boundaries. Furthermore, intersecting states inferred from current observations with forward-projected states from previous steps allow accurate robot localization without relying on vision or external systems. The framework supports both deterministic and possibilistic formulations and is validated through simulation and physical experiments using a low-cost, 3D printed, Hall-effect-based whisker sensor. Results demonstrate accurate contact estimation and localization with errors under 7 mm, demonstrating the potential of whisker-based sensing as a lightweight, adaptable complement to vision-based navigation.

