---
layout: default
title: Simplifying ROS2 controllers with a modular architecture for robot-agnostic reference generation
---

# Simplifying ROS2 controllers with a modular architecture for robot-agnostic reference generation
**arXiv**：[2601.08514v1](https://arxiv.org/abs/2601.08514) · [PDF](https://arxiv.org/pdf/2601.08514.pdf)  
**作者**：Davide Risi, Vincenzo Petrone, Antonio Langella, Lorenzo Pagliara, Enrico Ferrentino, Pasquale Chiacchio  

**一句话要点**：提出模块化架构以简化ROS2控制器，实现机器人无关的参考生成

**关键词**：ROS2控制器, 模块化架构, 参考生成, 机器人控制, 代码重用

## 3 点简述
- 核心问题：ROS2控制器中重复的参考处理代码降低可重用性
- 方法要点：引入参考生成器组件，分离参考获取与跟踪逻辑
- 实验效果：在模拟和真实机器人上验证可靠跟踪，减少代码重复

## 摘要（原文）

> This paper introduces a novel modular architecture for ROS2 that decouples the logic required to acquire, validate, and interpolate references from the control laws that track them. The design includes a dedicated component, named Reference Generator, that receives references, in the form of either single points or trajectories, from external nodes (e.g., planners), and writes single-point references at the controller's sampling period via the existing ros2_control chaining mechanism to downstream controllers. This separation removes duplicated reference-handling code from controllers and improves reusability across robot platforms. We implement two reference generators: one for handling joint-space references and one for Cartesian references, along with a set of new controllers (PD with gravity compensation, Cartesian pose, and admittance controllers) and validate the approach on simulated and real Universal Robots and Franka Emika manipulators. Results show that (i) references are tracked reliably in all tested scenarios, (ii) reference generators reduce duplicated reference-handling code across chained controllers to favor the construction and reuse of complex controller pipelines, and (iii) controller implementations remain focused only on control laws.

