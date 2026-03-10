---
layout: default
title: mmGAT: Pose Estimation by Graph Attention with Mutual Features from mmWave Radar Point Cloud
---

# mmGAT: Pose Estimation by Graph Attention with Mutual Features from mmWave Radar Point Cloud
**arXiv**：[2603.08551v1](https://arxiv.org/abs/2603.08551) · [PDF](https://arxiv.org/pdf/2603.08551.pdf)  
**作者**：Abdullah Al Masud, Shi Xintong, Mondher Bouazizi, Ohtsuki Tomoaki  

**一句话要点**：提出mmGAT模型，利用图注意力网络与互特征处理毫米波雷达点云以提升姿态估计性能。

**关键词**：毫米波雷达, 姿态估计, 图神经网络, 注意力机制, 点云处理

## 3 点简述
- 核心问题：图像姿态估计在隐私和低光环境下性能受限，毫米波雷达可提供替代方案。
- 方法要点：采用图神经网络结合注意力机制，设计独特特征提取技术处理雷达点云细节。
- 实验或效果：在两个公开毫米波数据集上实现新SOTA，MPJPE降低35.6%，PA-MPJPE降低14.1%。

## 摘要（原文）

> Pose estimation and human action recognition (HAR) are pivotal technologies spanning various domains. While the image-based pose estimation and HAR are widely admired for their superior performance, they lack in privacy protection and suboptimal performance in low-light and dark environments. This paper exploits the capabilities of millimeter-wave (mmWave) radar technology for human pose estimation by processing radar data with Graph Neural Network (GNN) architecture, coupled with the attention mechanism. Our goal is to capture the finer details of the radar point cloud to improve the pose estimation performance. To this end, we present a unique feature extraction technique that exploits the full potential of the GNN processing method for pose estimation. Our model mmGAT demonstrates remarkable performance on two publicly available benchmark mmWave datasets and establishes new state of the art results in most scenarios in terms of human pose estimation. Our approach achieves a noteworthy reduction of pose estimation mean per joint position error (MPJPE) by 35.6% and PA-MPJPE by 14.1% from the current state of the art benchmark within this domain.

