---
layout: default
title: RoboGPU: Accelerating GPU Collision Detection for Robotics
---

# RoboGPU: Accelerating GPU Collision Detection for Robotics
**arXiv**：[2603.01517v1](https://arxiv.org/abs/2603.01517) · [PDF](https://arxiv.org/pdf/2603.01517.pdf)  
**作者**：Lufei Liu, Liwei Xue, Youssef Mohammed, Jocelyn Zhao, Yuan Hsi Chou, Tor M. Aamodt  

**一句话要点**：提出RoboGPU架构以加速机器人GPU碰撞检测，提升灵活性与性能

**关键词**：GPU加速, 碰撞检测, 机器人运动规划, 光线追踪加速器, 硬件架构优化

## 3 点简述
- 核心问题：现有GPU光线追踪加速器缺乏机器人碰撞检测所需的控制流机制，导致计算效率低。
- 方法要点：引入RoboCore单元，通过架构修改增强GPU光线追踪加速器，支持机器人查询的灵活控制流。
- 实验或效果：RoboCore在碰撞检测上比RTA快3.1倍，比CUDA基线快14.8倍，并加速其他机器人任务。

## 摘要（原文）

> Autonomous robots are increasingly prevalent in our society, emerging in medical care, transportation vehicles, and home assistance. These robots rely on motion planning and collision detection to identify a sequence of movements allowing them to navigate to an end goal without colliding with the surrounding environment. While many specialized accelerators have been proposed to meet the real-time requirements of robotics planning tasks, they often lack the flexibility to adapt to the rapidly changing landscape of robotics and support future advancements. However, GPUs are well-positioned for robotics and we find that they can also tackle collision detection algorithms with enhancements to existing ray tracing accelerator (RTA) units. Unlike intersection tests in ray tracing, collision queries in robotics require control flow mechanisms to avoid unnecessary computations in each query. In this work, we explore and compare different architectural modifications to address the gaps of existing GPU RTAs. Our proposed RoboGPU architecture introduces a RoboCore that computes collision queries 3.1$\times$ faster than RTA implementations and 14.8$\times$ faster than a CUDA baseline. RoboCore is also useful for other robotics tasks, achieving 3.6$\times$ speedup on a state-of-the-art neural motion planner and 1.1$\times$ speedup on Monte Carlo Localization compared to a baseline GPU. RoboGPU matches the performance of dedicated hardware accelerators while being able to adapt to evolving motion planning algorithms and support classical algorithms.

