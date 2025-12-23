---
layout: default
title: ICP-4D: Bridging Iterative Closest Point and LiDAR Panoptic Segmentation
---

# ICP-4D: Bridging Iterative Closest Point and LiDAR Panoptic Segmentation
**arXiv**：[2512.18991v1](https://arxiv.org/abs/2512.18991) · [PDF](https://arxiv.org/pdf/2512.18991.pdf)  
**作者**：Gyeongrok Oh, Youngdong Jang, Jonghyun Choi, Suk-Ju Kang, Guang Lin, Sangpil Kim  

**一句话要点**：提出ICP-4D框架，通过几何关系实现无训练的4D LiDAR全景分割

**关键词**：4D LiDAR全景分割, 迭代最近点算法, Sinkhorn匹配, 几何对齐, 无训练框架, 时序实例关联

## 3 点简述
- 核心问题：现有4D LiDAR全景分割方法计算冗余且忽略点云几何先验
- 方法要点：使用ICP算法和Sinkhorn软匹配关联时序实例，提升几何对齐鲁棒性
- 实验或效果：在SemanticKITTI和panoptic nuScenes上超越先进方法，无需额外训练

## 摘要（原文）

> Dominant paradigms for 4D LiDAR panoptic segmentation are usually required to train deep neural networks with large superimposed point clouds or design dedicated modules for instance association. However, these approaches perform redundant point processing and consequently become computationally expensive, yet still overlook the rich geometric priors inherently provided by raw point clouds. To this end, we introduce ICP-4D, a simple yet effective training-free framework that unifies spatial and temporal reasoning through geometric relations among instance-level point sets. Specifically, we apply the Iterative Closest Point (ICP) algorithm to directly associate temporally consistent instances by aligning the source and target point sets through the estimated transformation. To stabilize association under noisy instance predictions, we introduce a Sinkhorn-based soft matching. This exploits the underlying instance distribution to obtain accurate point-wise correspondences, resulting in robust geometric alignment. Furthermore, our carefully designed pipeline, which considers three instance types-static, dynamic, and missing-offers computational efficiency and occlusion-aware matching. Our extensive experiments across both SemanticKITTI and panoptic nuScenes demonstrate that our method consistently outperforms state-of-the-art approaches, even without additional training or extra point cloud inputs.

