---
layout: default
title: Whole-Body Safe Control of Robotic Systems with Koopman Neural Dynamics
---

# Whole-Body Safe Control of Robotic Systems with Koopman Neural Dynamics
**arXiv**：[2603.03740v1](https://arxiv.org/abs/2603.03740) · [PDF](https://arxiv.org/pdf/2603.03740.pdf)  
**作者**：Sebin Jung, Abulikemu Abuduweili, Jiaxing Li, Changliu Liu  

**一句话要点**：提出基于Koopman神经动力学与安全集算法的机器人全身安全控制框架，以解决非线性高维动态实时优化难题。

**关键词**：Koopman算子, 机器人安全控制, 非线性系统线性化, 数据驱动建模, 二次规划优化, 实时控制

## 3 点简述
- 核心问题：强非线性高维机器人动态导致带安全约束的直接非线性优化在实时中难以处理。
- 方法要点：数据驱动学习Koopman嵌入与算子，结合安全集算法，通过单一二次规划实现跟踪与安全约束。
- 实验或效果：在Kinova Gen3机械臂和Go2四足机器人上验证，实现精确跟踪与避障。

## 摘要（原文）

> Controlling robots with strongly nonlinear, high-dimensional dynamics remains challenging, as direct nonlinear optimization with safety constraints is often intractable in real time. The Koopman operator offers a way to represent nonlinear systems linearly in a lifted space, enabling the use of efficient linear control. We propose a data-driven framework that learns a Koopman embedding and operator from data, and integrates the resulting linear model with the Safe Set Algorithm (SSA). This allows the tracking and safety constraints to be solved in a single quadratic program (QP), ensuring feasibility and optimality without a separate safety filter. We validate the method on a Kinova Gen3 manipulator and a Go2 quadruped, showing accurate tracking and obstacle avoidance.

