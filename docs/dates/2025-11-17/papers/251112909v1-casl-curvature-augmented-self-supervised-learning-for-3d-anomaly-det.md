---
layout: default
title: CASL: Curvature-Augmented Self-supervised Learning for 3D Anomaly Detection
---

# CASL: Curvature-Augmented Self-supervised Learning for 3D Anomaly Detection
**arXiv**：[2511.12909v1](https://arxiv.org/abs/2511.12909) · [PDF](https://arxiv.org/pdf/2511.12909.pdf)  
**作者**：Yaohua Zha, Xue Yuerong, Chunlin Fan, Yuansong Wang, Tao Dai, Ke Chen, Shu-Tao Xia  

**一句话要点**：提出曲率增强自监督学习框架以改进3D异常检测与通用表示学习

**关键词**：3D异常检测, 自监督学习, 点云重建, 曲率提示, 通用表示学习

## 3 点简述
- 核心问题：现有自监督点云模型在异常检测中表现不佳，缺乏通用性。
- 方法要点：基于U-Net架构，引入多尺度曲率提示指导点坐标重建。
- 实验或效果：仅用曲率作异常分数即超越经典模型，实现领先检测性能。

## 摘要（原文）

> Deep learning-based 3D anomaly detection methods have demonstrated significant potential in industrial manufacturing. However, many approaches are specifically designed for anomaly detection tasks, which limits their generalizability to other 3D understanding tasks. In contrast, self-supervised point cloud models aim for general-purpose representation learning, yet our investigation reveals that these classical models are suboptimal at anomaly detection under the unified fine-tuning paradigm. This motivates us to develop a more generalizable 3D model that can effectively detect anomalies without relying on task-specific designs. Interestingly, we find that using only the curvature of each point as its anomaly score already outperforms several classical self-supervised and dedicated anomaly detection models, highlighting the critical role of curvature in 3D anomaly detection. In this paper, we propose a Curvature-Augmented Self-supervised Learning (CASL) framework based on a reconstruction paradigm. Built upon the classical U-Net architecture, our approach introduces multi-scale curvature prompts to guide the decoder in predicting the spatial coordinates of each point. Without relying on any dedicated anomaly detection mechanisms, it achieves leading detection performance through straightforward anomaly classification fine-tuning. Moreover, the learned representations generalize well to standard 3D understanding tasks such as point cloud classification. The code is available at https://github.com/zyh16143998882/CASL.

