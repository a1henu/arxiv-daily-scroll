---
layout: default
title: CADGrasp: Learning Contact and Collision Aware General Dexterous Grasping in Cluttered Scenes
---

# CADGrasp: Learning Contact and Collision Aware General Dexterous Grasping in Cluttered Scenes
**arXiv**：[2601.15039v1](https://arxiv.org/abs/2601.15039) · [PDF](https://arxiv.org/pdf/2601.15039.pdf)  
**作者**：Jiyao Zhang, Zhiyuan Ma, Tianhao Wu, Zeyuan Chen, Hao Dong  

**一句话要点**：提出CADGrasp两阶段算法，基于单视角点云实现杂乱场景中灵巧抓取的接触与碰撞感知

**关键词**：灵巧抓取, 碰撞感知, 点云处理, 优化算法, 杂乱场景

## 3 点简述
- 核心问题：灵巧手在杂乱场景中抓取面临高自由度、遮挡和碰撞挑战，需稳定无碰撞的抓取姿态
- 方法要点：第一阶段预测稀疏IBS作为优化目标，第二阶段基于能量函数和排序策略优化生成高质量抓取姿态
- 实验或效果：在模拟和真实场景中验证有效性，能减少碰撞并保持高抓取成功率

## 摘要（原文）

> Dexterous grasping in cluttered environments presents substantial challenges due to the high degrees of freedom of dexterous hands, occlusion, and potential collisions arising from diverse object geometries and complex layouts. To address these challenges, we propose CADGrasp, a two-stage algorithm for general dexterous grasping using single-view point cloud inputs. In the first stage, we predict sparse IBS, a scene-decoupled, contact- and collision-aware representation, as the optimization target. Sparse IBS compactly encodes the geometric and contact relationships between the dexterous hand and the scene, enabling stable and collision-free dexterous grasp pose optimization. To enhance the prediction of this high-dimensional representation, we introduce an occupancy-diffusion model with voxel-level conditional guidance and force closure score filtering. In the second stage, we develop several energy functions and ranking strategies for optimization based on sparse IBS to generate high-quality dexterous grasp poses. Extensive experiments in both simulated and real-world settings validate the effectiveness of our approach, demonstrating its capability to mitigate collisions while maintaining a high grasp success rate across diverse objects and complex scenes.

