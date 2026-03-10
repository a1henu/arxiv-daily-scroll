---
layout: default
title: PCFEx: Point Cloud Feature Extraction for Graph Neural Networks
---

# PCFEx: Point Cloud Feature Extraction for Graph Neural Networks
**arXiv**：[2603.08540v1](https://arxiv.org/abs/2603.08540) · [PDF](https://arxiv.org/pdf/2603.08540.pdf)  
**作者**：Abdullah Al Masud, Shi Xintong, Mondher Bouazizi, Ohtsuki Tomoaki  

**一句话要点**：提出点云特征提取技术PCFEx与GNN架构，用于毫米波雷达点云的人体姿态估计与活动识别。

**关键词**：点云特征提取, 图神经网络, 毫米波雷达, 人体姿态估计, 人体活动识别

## 3 点简述
- 核心问题：将点云视为图，提取点、边和图级别特征以增强GNN处理3D点云的能力。
- 方法要点：设计新颖的PCFEx技术，并构建高效GNN架构处理这些特征。
- 实验或效果：在四个毫米波雷达数据集上评估，HPE误差显著降低，HAR准确率达98.8%，超越现有最佳模型。

## 摘要（原文）

> Graph neural networks (GNNs) have gained significant attention for their effectiveness across various domains. This study focuses on applying GNN to process 3D point cloud data for human pose estimation (HPE) and human activity recognition (HAR). We propose novel point cloud feature extraction (PCFEx) techniques to capture meaningful information at the point, edge, and graph levels of the point cloud by considering point cloud as a graph. Moreover, we introduce a GNN architecture designed to efficiently process these features. Our approach is evaluated on four most popular publicly available millimeter wave radar datasets, three for HPE and one for HAR. The results show substantial improvements, with significantly reduced errors in all three HPE benchmarks, and an overall accuracy of 98.8% in mmWave-based HAR, outperforming the existing state of the art models. This work demonstrates the great potential of feature extraction incorporated with GNN modeling approach to enhance the precision of point cloud processing.

