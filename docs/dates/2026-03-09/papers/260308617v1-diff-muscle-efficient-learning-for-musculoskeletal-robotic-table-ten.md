---
layout: default
title: Diff-Muscle: Efficient Learning for Musculoskeletal Robotic Table Tennis
---

# Diff-Muscle: Efficient Learning for Musculoskeletal Robotic Table Tennis
**arXiv**：[2603.08617v1](https://arxiv.org/abs/2603.08617) · [PDF](https://arxiv.org/pdf/2603.08617.pdf)  
**作者**：Wentao Zhao, Jun Guo, Kangyao Huang, Xin Liu, Huaping Liu  

**一句话要点**：提出Diff-Muscle算法，利用微分平坦性将肌肉激活空间策略学习重构到低维关节空间，以解决肌肉骨骼机器人高效学习挑战。

**关键词**：肌肉骨骼机器人, 微分平坦性, 分层强化学习, 机器人乒乓球, 高效学习, 过驱动控制

## 3 点简述
- 核心问题：肌肉骨骼机器人因高维动作空间和过驱动结构导致高效学习困难，限制其在多段协调任务中的应用。
- 方法要点：基于微分平坦性，将冗余肌肉激活空间策略学习重构到低维关节空间，结合分层强化学习框架集成K-MAC与高层轨迹规划。
- 实验或效果：在动态乒乓球任务中，Diff-Muscle显著优于基线方法，成功率高且肌肉激活最小，支持双机器人连续对打。

## 摘要（原文）

> Musculoskeletal robots provide superior advantages in flexibility and dexterity, positioning them as a promising frontier towards embodied intelligence. However, current research is largely confined to relative simple tasks, restricting the exploration of their full potential in multi-segment coordination. Furthermore, efficient learning remains a challenge, primarily due to the high-dimensional action space and inherent overactuated structures. To address these challenges, we propose Diff-Muscle, a musculoskeletal robot control algorithm that leverages differential flatness to reformulate policy learning from the redundant muscle-activation space into a significantly lower-dimensional joint space. Furthermore, we utilize the highly dynamic robotic table tennis task to evaluate our algorithm. Specifically, we propose a hierarchical reinforcement learning framework that integrates a Kinematics-based Muscle Actuation Controller (K-MAC) with high-level trajectory planning, enabling a musculoskeletal robot to perform dexterous and precise rallies. Experimental results demonstrate that Diff-Muscle significantly outperforms state-of-the-art baselines in success rates while maintaining minimal muscle activation. Notably, the proposed framework successfully enables the musculoskeletal robots to achieve continuous rallies in a challenging dual-robot setting.

