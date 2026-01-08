---
layout: default
title: Towards Safe Autonomous Driving: A Real-Time Motion Planning Algorithm on Embedded Hardware
---

# Towards Safe Autonomous Driving: A Real-Time Motion Planning Algorithm on Embedded Hardware
**arXiv**：[2601.03904v1](https://arxiv.org/abs/2601.03904) · [PDF](https://arxiv.org/pdf/2601.03904.pdf)  
**作者**：Korbinian Moller, Glenn Johannes Tungka, Lucas Jürgens, Johannes Betz  

**一句话要点**：提出嵌入式硬件上的实时运动规划算法，以增强自动驾驶的主动安全扩展

**关键词**：自动驾驶安全, 实时运动规划, 嵌入式硬件, 采样轨迹规划, 故障操作

## 3 点简述
- 核心问题：现有安全层缺乏主动机制，无法在主规划器故障时确保安全操作
- 方法要点：在嵌入式实时操作系统上部署轻量级采样轨迹规划器，实现资源受限下的连续轨迹计算
- 实验或效果：实验显示确定性时序行为，验证了在安全认证硬件上轨迹规划的可行性

## 摘要（原文）

> Ensuring the functional safety of Autonomous Vehicles (AVs) requires motion planning modules that not only operate within strict real-time constraints but also maintain controllability in case of system faults. Existing safeguarding concepts, such as Online Verification (OV), provide safety layers that detect infeasible planning outputs. However, they lack an active mechanism to ensure safe operation in the event that the main planner fails. This paper presents a first step toward an active safety extension for fail-operational Autonomous Driving (AD). We deploy a lightweight sampling-based trajectory planner on an automotive-grade, embedded platform running a Real-Time Operating System (RTOS). The planner continuously computes trajectories under constrained computational resources, forming the foundation for future emergency planning architectures. Experimental results demonstrate deterministic timing behavior with bounded latency and minimal jitter, validating the feasibility of trajectory planning on safety-certifiable hardware. The study highlights both the potential and the remaining challenges of integrating active fallback mechanisms as an integral part of next-generation safeguarding frameworks. The code is available at: https://github.com/TUM-AVS/real-time-motion-planning

