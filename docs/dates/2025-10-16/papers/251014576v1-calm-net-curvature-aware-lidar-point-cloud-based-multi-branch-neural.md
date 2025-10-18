---
layout: default
title: CALM-Net: Curvature-Aware LiDAR Point Cloud-based Multi-Branch Neural Network for Vehicle Re-Identification
---

# CALM-Net: Curvature-Aware LiDAR Point Cloud-based Multi-Branch Neural Network for Vehicle Re-Identification
**arXiv**：[2510.14576v1](https://arxiv.org/abs/2510.14576) · [PDF](https://arxiv.org/pdf/2510.14576.pdf)  
**作者**：Dongwook Lee, Sol Han, Jinwhan Kim  

**一句话要点**：提出CALM-Net，通过多分支网络结合曲率信息解决LiDAR点云车辆重识别问题

**关键词**：LiDAR点云, 车辆重识别, 多分支神经网络, 曲率嵌入, 边缘卷积, 点注意力

## 3 点简述
- 核心问题：从三维点云中学习区分性特征以识别不同车辆
- 方法要点：采用多分支架构，集成边缘卷积、点注意力和曲率嵌入
- 实验或效果：在nuScenes数据集上，平均重识别准确率提升约1.97%

## 摘要（原文）

> This paper presents CALM-Net, a curvature-aware LiDAR point cloud-based
> multi-branch neural network for vehicle re-identification. The proposed model
> addresses the challenge of learning discriminative and complementary features
> from three-dimensional point clouds to distinguish between vehicles. CALM-Net
> employs a multi-branch architecture that integrates edge convolution, point
> attention, and a curvature embedding that characterizes local surface variation
> in point clouds. By combining these mechanisms, the model learns richer
> geometric and contextual features that are well suited for the
> re-identification task. Experimental evaluation on the large-scale nuScenes
> dataset demonstrates that CALM-Net achieves a mean re-identification accuracy
> improvement of approximately 1.97\% points compared with the strongest baseline
> in our study. The results confirms the effectiveness of incorporating curvature
> information into deep learning architectures and highlight the benefit of
> multi-branch feature learning for LiDAR point cloud-based vehicle
> re-identification.

