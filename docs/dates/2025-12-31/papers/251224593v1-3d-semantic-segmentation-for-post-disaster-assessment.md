---
layout: default
title: 3D Semantic Segmentation for Post-Disaster Assessment
---

# 3D Semantic Segmentation for Post-Disaster Assessment
**arXiv**：[2512.24593v1](https://arxiv.org/abs/2512.24593) · [PDF](https://arxiv.org/pdf/2512.24593.pdf)  
**作者**：Nhut Le, Maryam Rahnemoonfar  

**一句话要点**：构建灾后3D数据集并评估SOTA模型，揭示现有方法在灾后场景的局限性

**关键词**：3D语义分割, 灾后评估, 无人机数据, 点云重建, 模型评估

## 3 点简述
- 核心问题：缺乏针对灾后环境的3D语义分割专用数据集，影响评估准确性
- 方法要点：使用无人机采集飓风灾后影像，通过SfM和MVS技术重建3D点云数据集
- 实验或效果：评估FPT、PTv3和OA-CNNs等模型，发现其在灾后区域表现显著不足

## 摘要（原文）

> The increasing frequency of natural disasters poses severe threats to human lives and leads to substantial economic losses. While 3D semantic segmentation is crucial for post-disaster assessment, existing deep learning models lack datasets specifically designed for post-disaster environments. To address this gap, we constructed a specialized 3D dataset using unmanned aerial vehicles (UAVs)-captured aerial footage of Hurricane Ian (2022) over affected areas, employing Structure-from-Motion (SfM) and Multi-View Stereo (MVS) techniques to reconstruct 3D point clouds. We evaluated the state-of-the-art (SOTA) 3D semantic segmentation models, Fast Point Transformer (FPT), Point Transformer v3 (PTv3), and OA-CNNs on this dataset, exposing significant limitations in existing methods for disaster-stricken regions. These findings underscore the urgent need for advancements in 3D segmentation techniques and the development of specialized 3D benchmark datasets to improve post-disaster scene understanding and response.

