---
layout: default
title: Shape-Interpretable Visual Self-Modeling Enables Geometry-Aware Continuum Robot Control
---

# Shape-Interpretable Visual Self-Modeling Enables Geometry-Aware Continuum Robot Control
**arXiv**：[2603.01751v1](https://arxiv.org/abs/2603.01751) · [PDF](https://arxiv.org/pdf/2603.01751.pdf)  
**作者**：Peng Yu, Xin Wang, Ning Tan  

**一句话要点**：提出形状可解释视觉自建模框架，实现连续体机器人的几何感知控制。

**关键词**：连续体机器人, 视觉自建模, 贝塞尔曲线, 神经常微分方程, 几何感知控制, 障碍物避让

## 3 点简述
- 核心问题：连续体机器人连续变形和非线性动力学导致感知、建模和控制困难。
- 方法要点：使用贝塞尔曲线编码多视图图像，结合神经常微分方程自建模形状和末端执行器动力学。
- 实验或效果：在电缆驱动连续体机器人上实现形状误差小于1.56%图像分辨率，末端执行器误差小于2%机器人长度。

## 摘要（原文）

> Continuum robots possess high flexibility and redundancy, making them well suited for safe interaction in complex environments, yet their continuous deformation and nonlinear dynamics pose fundamental challenges to perception, modeling, and control. Existing vision-based control approaches often rely on end-to-end learning, achieving shape regulation without explicit awareness of robot geometry or its interaction with the environment. Here, we introduce a shape-interpretable visual self-modeling framework for continuum robots that enables geometry-aware control. Robot shapes are encoded from multi-view planar images using a Bezier-curve representation, transforming visual observations into a compact and physically meaningful shape space that uniquely characterizes the robot's three-dimensional configuration. Based on this representation, neural ordinary differential equations are employed to self-model both shape and end-effector dynamics directly from data, enabling hybrid shape-position control without analytical models or dense body markers. The explicit geometric structure of the learned shape space allows the robot to reason about its body and surroundings, supporting environment-aware behaviors such as obstacle avoidance and self-motion while maintaining end-effector objectives. Experiments on a cable-driven continuum robot demonstrate accurate shape-position regulation and tracking, with shape errors within 1.56% of image resolution and end-effector errors within 2% of robot length, as well as robust performance in constrained environments. By elevating visual shape representations from two-dimensional observations to an interpretable three-dimensional self-model, this work establishes a principled alternative to vision-based end-to-end control and advances autonomous, geometry-aware manipulation for continuum robots.

