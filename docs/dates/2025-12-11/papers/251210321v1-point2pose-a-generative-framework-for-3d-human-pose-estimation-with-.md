---
layout: default
title: Point2Pose: A Generative Framework for 3D Human Pose Estimation with Multi-View Point Cloud Dataset
---

# Point2Pose: A Generative Framework for 3D Human Pose Estimation with Multi-View Point Cloud Dataset
**arXiv**：[2512.10321v1](https://arxiv.org/abs/2512.10321) · [PDF](https://arxiv.org/pdf/2512.10321.pdf)  
**作者**：Hyunsoo Lee, Daeum Jeon, Hyeokjae Oh  

**一句话要点**：提出Point2Pose生成框架，基于多视角点云进行3D人体姿态估计

**关键词**：3D人体姿态估计, 生成模型, 点云处理, 多视角数据集, 注意力机制

## 3 点简述
- 核心问题：3D人体姿态估计面临复杂几何、自遮挡关节和大规模真实运动数据需求挑战
- 方法要点：使用时空点云编码器和姿态特征编码器提取关节特征，结合注意力生成回归器
- 实验或效果：在多个数据集上优于基线模型，并发布多模态数据集MVPose3D

## 摘要（原文）

> We propose a novel generative approach for 3D human pose estimation. 3D human pose estimation poses several key challenges due to the complex geometry of the human body, self-occluding joints, and the requirement for large-scale real-world motion datasets. To address these challenges, we introduce Point2Pose, a framework that effectively models the distribution of human poses conditioned on sequential point cloud and pose history. Specifically, we employ a spatio-temporal point cloud encoder and a pose feature encoder to extract joint-wise features, followed by an attention-based generative regressor. Additionally, we present a large-scale indoor dataset MVPose3D, which contains multiple modalities, including IMU data of non-trivial human motions, dense multi-view point clouds, and RGB images. Experimental results show that the proposed method outperforms the baseline models, demonstrating its superior performance across various datasets.

