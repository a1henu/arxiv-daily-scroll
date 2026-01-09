---
layout: default
title: UniBiDex: A Unified Teleoperation Framework for Robotic Bimanual Dexterous Manipulation
---

# UniBiDex: A Unified Teleoperation Framework for Robotic Bimanual Dexterous Manipulation
**arXiv**：[2601.04629v1](https://arxiv.org/abs/2601.04629) · [PDF](https://arxiv.org/pdf/2601.04629.pdf)  
**作者**：Zhongxuan Li, Zeliang Guo, Jun Hu, David Navarro-Alarcon, Jia Pan, Hongmin Wu, Peng Zhou  

**一句话要点**：提出UniBiDex统一遥操作框架，支持VR和主从输入，实现机器人灵巧双手实时接触式操控。

**关键词**：机器人遥操作, 双手灵巧操控, 零空间控制, 异构输入集成, 开源框架

## 3 点简述
- 核心问题：机器人灵巧双手操控需统一遥操作框架，以处理异构输入并保证安全运动。
- 方法要点：集成异构设备到共享控制栈，采用零空间控制优化双手配置，确保平滑无碰撞运动。
- 实验或效果：在厨房整理任务中验证，相比基线提高成功率、轨迹平滑性和鲁棒性，并开源硬件软件。

## 摘要（原文）

> We present UniBiDex a unified teleoperation framework for robotic bimanual dexterous manipulation that supports both VRbased and leaderfollower input modalities UniBiDex enables realtime contactrich dualarm teleoperation by integrating heterogeneous input devices into a shared control stack with consistent kinematic treatment and safety guarantees The framework employs nullspace control to optimize bimanual configurations ensuring smooth collisionfree and singularityaware motion across tasks We validate UniBiDex on a longhorizon kitchentidying task involving five sequential manipulation subtasks demonstrating higher task success rates smoother trajectories and improved robustness compared to strong baselines By releasing all hardware and software components as opensource we aim to lower the barrier to collecting largescale highquality human demonstration datasets and accelerate progress in robot learning.

