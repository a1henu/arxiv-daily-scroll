---
layout: default
title: Omni-Manip: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception
---

# Omni-Manip: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception
**arXiv**：[2603.05355v1](https://arxiv.org/abs/2603.05355) · [PDF](https://arxiv.org/pdf/2603.05355.pdf)  
**作者**：Pei Qu, Zheng Li, Yufei Jia, Ziyun Liu, Liang Zhu, Haoang Li, Jinni Zhou, Jun Ma  

**一句话要点**：提出Omni-Manip，基于LiDAR的全景3D感知方法，解决人形机器人在大工作空间中的灵巧操作问题。

**关键词**：人形机器人操作, 全景3D感知, LiDAR驱动策略, 时间感知注意力, 大工作空间, 端到端学习

## 3 点简述
- 核心问题：传统RGB-D感知视野窄、自遮挡，导致机器人需频繁移动，增加不确定性和风险。
- 方法要点：采用LiDAR驱动的时间感知注意力池化机制，处理全景点云，实现360°感知。
- 实验或效果：在仿真和真实环境中验证，在大工作空间和杂乱场景中表现稳健，优于基于深度相机的基线方法。

## 摘要（原文）

> The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information. While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, We propose Omni-Manip, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360° perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that Omni-Manip achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

