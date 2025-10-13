---
layout: default
title: Exploring Single Domain Generalization of LiDAR-based Semantic Segmentation under Imperfect Labels
---

# Exploring Single Domain Generalization of LiDAR-based Semantic Segmentation under Imperfect Labels
**arXiv**：[2510.09035v1](https://arxiv.org/abs/2510.09035) · [PDF](https://arxiv.org/pdf/2510.09035.pdf)  
**作者**：Weitong Kong, Zichao Zeng, Di Wen, Jiale Wei, Kunyu Peng, June Moh Goo, Jan Boehm, Rainer Stiefelhagen  
**一句话要点**：提出DuNe双视图框架以解决LiDAR语义分割在噪声标签下的单域泛化问题

**关键词**：LiDAR语义分割, 域泛化, 噪声标签学习, 双视图框架, 3D点云处理

## 3 点简述
- 核心问题：LiDAR标注噪声在域泛化中加剧，影响3D语义分割的鲁棒性
- 方法要点：采用强弱分支双视图框架，通过特征一致性和置信度过滤优化损失
- 实验或效果：在多个数据集上实现SOTA性能，mIoU达49.57%算术平均

## 摘要（原文）

> Accurate perception is critical for vehicle safety, with LiDAR as a key
> enabler in autonomous driving. To ensure robust performance across
> environments, sensor types, and weather conditions without costly
> re-annotation, domain generalization in LiDAR-based 3D semantic segmentation is
> essential. However, LiDAR annotations are often noisy due to sensor
> imperfections, occlusions, and human errors. Such noise degrades segmentation
> accuracy and is further amplified under domain shifts, threatening system
> reliability. While noisy-label learning is well-studied in images, its
> extension to 3D LiDAR segmentation under domain generalization remains largely
> unexplored, as the sparse and irregular structure of point clouds limits direct
> use of 2D methods. To address this gap, we introduce the novel task Domain
> Generalization for LiDAR Semantic Segmentation under Noisy Labels (DGLSS-NL)
> and establish the first benchmark by adapting three representative noisy-label
> learning strategies from image classification to 3D segmentation. However, we
> find that existing noisy-label learning approaches adapt poorly to LiDAR data.
> We therefore propose DuNe, a dual-view framework with strong and weak branches
> that enforce feature-level consistency and apply cross-entropy loss based on
> confidence-aware filtering of predictions. Our approach shows state-of-the-art
> performance by achieving 56.86% mIoU on SemanticKITTI, 42.28% on nuScenes, and
> 52.58% on SemanticPOSS under 10% symmetric label noise, with an overall
> Arithmetic Mean (AM) of 49.57% and Harmonic Mean (HM) of 48.50%, thereby
> demonstrating robust domain generalization in DGLSS-NL tasks. The code is
> available on our project page.

