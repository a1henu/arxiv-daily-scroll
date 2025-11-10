---
layout: default
title: Stable and Robust SLIP Model Control via Energy Conservation-Based Feedback Cancellation for Quadrupedal Applications
---

# Stable and Robust SLIP Model Control via Energy Conservation-Based Feedback Cancellation for Quadrupedal Applications
**arXiv**：[2511.05402v1](https://arxiv.org/abs/2511.05402) · [PDF](https://arxiv.org/pdf/2511.05402.pdf)  
**作者**：Muhammad Saud Ul Hassan, Derek Vasquez, Hamza Asif, Christian Hubicki  

**一句话要点**：提出基于能量守恒的SLIP模型控制方法，实现四足机器人稳定动态运动

**关键词**：四足机器人控制, SLIP模型, 能量守恒控制, 动态运动稳定性, 弹跳步态, 传感器误差鲁棒性

## 3 点简述
- 核心问题：四足机器人动态运动稳定性控制，需处理传感器误差等扰动
- 方法要点：利用能量守恒原理设计控制算法，跟踪稳定抛物线样条
- 实验或效果：仿真验证在Minitaur机器人上生成稳定弹跳步态，抗10%传感器误差

## 摘要（原文）

> In this paper, we present an energy-conservation based control architecture
> for stable dynamic motion in quadruped robots. We model the robot as a
> Spring-loaded Inverted Pendulum (SLIP), a model well-suited to represent the
> bouncing motion characteristic of running gaits observed in various biological
> quadrupeds and bio-inspired robotic systems. The model permits leg-orientation
> control during flight and leg-length control during stance, a design choice
> inspired by natural quadruped behaviors and prevalent in robotic quadruped
> systems. Our control algorithm uses the reduced-order SLIP dynamics of the
> quadruped to track a stable parabolic spline during stance, which is calculated
> using the principle of energy conservation. Through simulations based on the
> design specifications of an actual quadruped robot, Ghost Robotics Minitaur, we
> demonstrate that our control algorithm generates stable bouncing gaits.
> Additionally, we illustrate the robustness of our controller by showcasing its
> ability to maintain stable bouncing even when faced with up to a 10% error in
> sensor measurements.

