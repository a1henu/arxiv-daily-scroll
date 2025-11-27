---
layout: default
title: Dual-Agent Reinforcement Learning for Adaptive and Cost-Aware Visual-Inertial Odometry
---

# Dual-Agent Reinforcement Learning for Adaptive and Cost-Aware Visual-Inertial Odometry
**arXiv**：[2511.21083v1](https://arxiv.org/abs/2511.21083) · [PDF](https://arxiv.org/pdf/2511.21083.pdf)  
**作者**：Feiyang Pan, Shenghe Zheng, Chunyan Yin, Guangbin Dou  

**一句话要点**：提出双智能体强化学习框架，自适应优化视觉惯性里程计精度与效率

**关键词**：视觉惯性里程计, 强化学习, 自适应控制, 计算效率优化, 机器人导航

## 3 点简述
- 核心问题：视觉惯性里程计在精度与计算效率间存在权衡，优化方法计算成本高
- 方法要点：使用轻量级强化学习智能体，智能控制视觉前端执行与状态融合
- 实验效果：在EuRoC和TUM-VI数据集上，实现更高精度、更快速度和更低内存占用

## 摘要（原文）

> Visual-Inertial Odometry (VIO) is a critical component for robust ego-motion estimation, enabling foundational capabilities such as autonomous navigation in robotics and real-time 6-DoF tracking for augmented reality. Existing methods face a well-known trade-off: filter-based approaches are efficient but prone to drift, while optimization-based methods, though accurate, rely on computationally prohibitive Visual-Inertial Bundle Adjustment (VIBA) that is difficult to run on resource-constrained platforms. Rather than removing VIBA altogether, we aim to reduce how often and how heavily it must be invoked. To this end, we cast two key design choices in modern VIO, when to run the visual frontend and how strongly to trust its output, as sequential decision problems, and solve them with lightweight reinforcement learning (RL) agents. Our framework introduces a lightweight, dual-pronged RL policy that serves as our core contribution: (1) a Select Agent intelligently gates the entire VO pipeline based only on high-frequency IMU data; and (2) a composite Fusion Agent that first estimates a robust velocity state via a supervised network, before an RL policy adaptively fuses the full (p, v, q) state. Experiments on the EuRoC MAV and TUM-VI datasets show that, in our unified evaluation, the proposed method achieves a more favorable accuracy-efficiency-memory trade-off than prior GPU-based VO/VIO systems: it attains the best average ATE while running up to 1.77 times faster and using less GPU memory. Compared to classical optimization-based VIO systems, our approach maintains competitive trajectory accuracy while substantially reducing computational load.

