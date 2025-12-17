---
layout: default
title: FastDDHPose: Towards Unified, Efficient, and Disentangled 3D Human Pose Estimation
---

# FastDDHPose: Towards Unified, Efficient, and Disentangled 3D Human Pose Estimation
**arXiv**：[2512.14162v1](https://arxiv.org/abs/2512.14162) · [PDF](https://arxiv.org/pdf/2512.14162.pdf)  
**作者**：Qingyuan Cai, Linxin Zhang, Xuecai Hu, Saihui Hou, Yongzhen Huang  

**一句话要点**：提出FastDDHPose，基于解耦扩散模型统一高效解决单目3D人体姿态估计问题

**关键词**：3D人体姿态估计, 扩散模型, 解耦学习, 统一框架, 训练效率, 单目视觉

## 3 点简述
- 现有方法缺乏统一框架，导致公平比较困难且训练效率低
- FastDDHPose利用扩散模型显式建模骨骼长度和方向分布，避免层级误差累积
- 在Human3.6M和MPI-INF-3DHP上实现SOTA性能，提升训练效率与泛化能力

## 摘要（原文）

> Recent approaches for monocular 3D human pose estimation (3D HPE) have achieved leading performance by directly regressing 3D poses from 2D keypoint sequences. Despite the rapid progress in 3D HPE, existing methods are typically trained and evaluated under disparate frameworks, lacking a unified framework for fair comparison. To address these limitations, we propose Fast3DHPE, a modular framework that facilitates rapid reproduction and flexible development of new methods. By standardizing training and evaluation protocols, Fast3DHPE enables fair comparison across 3D human pose estimation methods while significantly improving training efficiency. Within this framework, we introduce FastDDHPose, a Disentangled Diffusion-based 3D Human Pose Estimation method which leverages the strong latent distribution modeling capability of diffusion models to explicitly model the distributions of bone length and bone direction while avoiding further amplification of hierarchical error accumulation. Moreover, we design an efficient Kinematic-Hierarchical Spatial and Temporal Denoiser that encourages the model to focus on kinematic joint hierarchies while avoiding unnecessary modeling of overly complex joint topologies. Extensive experiments on Human3.6M and MPI-INF-3DHP show that the Fast3DHPE framework enables fair comparison of all methods while significantly improving training efficiency. Within this unified framework, FastDDHPose achieves state-of-the-art performance with strong generalization and robustness in in-the-wild scenarios. The framework and models will be released at: https://github.com/Andyen512/Fast3DHPE

