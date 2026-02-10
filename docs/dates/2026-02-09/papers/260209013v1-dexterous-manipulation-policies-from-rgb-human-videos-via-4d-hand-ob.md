---
layout: default
title: Dexterous Manipulation Policies from RGB Human Videos via 4D Hand-Object Trajectory Reconstruction
---

# Dexterous Manipulation Policies from RGB Human Videos via 4D Hand-Object Trajectory Reconstruction
**arXiv**：[2602.09013v1](https://arxiv.org/abs/2602.09013) · [PDF](https://arxiv.org/pdf/2602.09013.pdf)  
**作者**：Hongyi Chen, Tony Dong, Tiancheng Wu, Liquan Wang, Yash Jangir, Yaru Niu, Yufei Ye, Homanga Bharadhwaj, Zackory Erickson, Jeffrey Ichnowski  

**一句话要点**：提出VIDEOMANIP框架，从RGB人类视频学习灵巧操作策略，无需穿戴设备。

**关键词**：灵巧操作, 视频学习, 轨迹重建, 接触优化, 演示合成, 机器人策略

## 3 点简述
- 核心问题：多指机器人操作数据获取难，现有方法依赖穿戴设备，可扩展性受限。
- 方法要点：从单目视频重建4D手-物体轨迹，通过接触优化和演示合成生成训练数据。
- 实验或效果：在仿真和真实世界测试中，成功率分别达70.25%和62.86%，优于基于重定向的方法。

## 摘要（原文）

> Multi-finger robotic hand manipulation and grasping are challenging due to the high-dimensional action space and the difficulty of acquiring large-scale training data. Existing approaches largely rely on human teleoperation with wearable devices or specialized sensing equipment to capture hand-object interactions, which limits scalability. In this work, we propose VIDEOMANIP, a device-free framework that learns dexterous manipulation directly from RGB human videos. Leveraging recent advances in computer vision, VIDEOMANIP reconstructs explicit 4D robot-object trajectories from monocular videos by estimating human hand poses, object meshes, and retargets the reconstructed human motions to robotic hands for manipulation learning. To make the reconstructed robot data suitable for dexterous manipulation training, we introduce hand-object contact optimization with interaction-centric grasp modeling, as well as a demonstration synthesis strategy that generates diverse training trajectories from a single video, enabling generalizable policy learning without additional robot demonstrations. In simulation, the learned grasping model achieves a 70.25% success rate across 20 diverse objects using the Inspire Hand. In the real world, manipulation policies trained from RGB videos achieve an average 62.86% success rate across seven tasks using the LEAP Hand, outperforming retargeting-based methods by 15.87%. Project videos are available at videomanip.github.io.

