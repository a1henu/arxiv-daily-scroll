---
layout: default
title: Interface-Aware Trajectory Reconstruction of Limited Demonstrations for Robot Learning
---

# Interface-Aware Trajectory Reconstruction of Limited Demonstrations for Robot Learning
**arXiv**：[2602.23287v1](https://arxiv.org/abs/2602.23287) · [PDF](https://arxiv.org/pdf/2602.23287.pdf)  
**作者**：Demiana R. Barsoum, Mahdieh Nejati Javaremi, Larisa Y. C. Loke, Brenna D. Argall  

**一句话要点**：提出接口感知轨迹重建算法，以解决辅助机器人因接口限制导致演示轨迹次优的问题。

**关键词**：辅助机器人, 轨迹重建, 接口限制, 机器人学习, 演示学习

## 3 点简述
- 核心问题：低维接口控制高自由度机器人导致演示轨迹受接口限制，无法反映用户意图。
- 方法要点：基于任务、环境和接口约束，将演示轨迹重建到机器人完整控制空间。
- 实验或效果：在真实世界任务中，重建轨迹比接口受限轨迹更快、更高效，同时尊重用户偏好。

## 摘要（原文）

> Assistive robots offer agency to humans with severe motor impairments. Often, these users control high-DoF robots through low-dimensional interfaces, such as using a 1-D sip-and-puff interface to operate a 6-DoF robotic arm. This mismatch results in having access to only a subset of control dimensions at a given time, imposing unintended and artificial constraints on robot motion. As a result, interface-limited demonstrations embed suboptimal motions that reflect interface restrictions rather than user intent. To address this, we present a trajectory reconstruction algorithm that reasons about task, environment, and interface constraints to lift demonstrations into the robot's full control space. We evaluate our approach using real-world demonstrations of ADL-inspired tasks performed via a 2-D joystick and 1-D sip-and-puff control interface, teleoperating two distinct 7-DoF robotic arms. Analyses of the reconstructed demonstrations and derived control policies show that lifted trajectories are faster and more efficient than their interface-constrained counterparts while respecting user preferences.

