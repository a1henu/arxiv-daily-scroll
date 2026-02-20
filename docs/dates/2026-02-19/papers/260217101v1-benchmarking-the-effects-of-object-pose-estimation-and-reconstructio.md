---
layout: default
title: Benchmarking the Effects of Object Pose Estimation and Reconstruction on Robotic Grasping Success
---

# Benchmarking the Effects of Object Pose Estimation and Reconstruction on Robotic Grasping Success
**arXiv**：[2602.17101v1](https://arxiv.org/abs/2602.17101) · [PDF](https://arxiv.org/pdf/2602.17101.pdf)  
**作者**：Varun Burde, Pavel Burget, Torsten Sattler  

**一句话要点**：提出基于物理的大规模基准，评估6D姿态估计与3D重建对机器人抓取性能的影响

**关键词**：机器人抓取, 6D姿态估计, 3D重建, 基准评估, 物理模拟

## 3 点简述
- 核心问题：现有3D重建评估未反映其对机器人抓取等下游任务的影响
- 方法要点：通过模拟抓取执行，分析姿态误差、抓取鲁棒性和几何不准确性
- 实验或效果：重建伪影减少抓取候选，但准确姿态下对抓取性能影响可忽略

## 摘要（原文）

> 3D reconstruction serves as the foundational layer for numerous robotic perception tasks, including 6D object pose estimation and grasp pose generation. Modern 3D reconstruction methods for objects can produce visually and geometrically impressive meshes from multi-view images, yet standard geometric evaluations do not reflect how reconstruction quality influences downstream tasks such as robotic manipulation performance. This paper addresses this gap by introducing a large-scale, physics-based benchmark that evaluates 6D pose estimators and 3D mesh models based on their functional efficacy in grasping. We analyze the impact of model fidelity by generating grasps on various reconstructed 3D meshes and executing them on the ground-truth model, simulating how grasp poses generated with an imperfect model affect interaction with the real object. This assesses the combined impact of pose error, grasp robustness, and geometric inaccuracies from 3D reconstruction. Our results show that reconstruction artifacts significantly decrease the number of grasp pose candidates but have a negligible effect on grasping performance given an accurately estimated pose. Our results also reveal that the relationship between grasp success and pose error is dominated by spatial error, and even a simple translation error provides insight into the success of the grasping pose of symmetric objects. This work provides insight into how perception systems relate to object manipulation using robots.

