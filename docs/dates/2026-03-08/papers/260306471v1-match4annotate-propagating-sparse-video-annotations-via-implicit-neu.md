---
layout: default
title: Match4Annotate: Propagating Sparse Video Annotations via Implicit Neural Feature Matching
---

# Match4Annotate: Propagating Sparse Video Annotations via Implicit Neural Feature Matching
**arXiv**：[2603.06471v1](https://arxiv.org/abs/2603.06471) · [PDF](https://arxiv.org/pdf/2603.06471.pdf)  
**作者**：Zhuorui Zhang, Roger Pallarès-López, Praneeth Namburi, Brian W. Anthony  

**一句话要点**：提出Match4Annotate框架，通过隐式神经特征匹配传播稀疏视频标注，以解决医学影像等领域标注成本高的问题。

**关键词**：视频标注传播, 隐式神经表示, 特征匹配, 医学影像分析, 稀疏标注, 测试时优化

## 3 点简述
- 核心问题：视频标注成本高，现有方法在跨视频传播、时空平滑性和标注类型统一性方面存在局限。
- 方法要点：基于SIREN的隐式神经表示拟合DINOv3特征，学习平滑隐式变形场指导对应匹配。
- 实验或效果：在临床超声数据集上实现跨视频传播SOTA，同时保持视频内传播竞争力。

## 摘要（原文）

> Acquiring per-frame video annotations remains a primary bottleneck for deploying computer vision in specialized domains such as medical imaging, where expert labeling is slow and costly. Label propagation offers a natural solution, yet existing approaches face fundamental limitations. Video trackers and segmentation models can propagate labels within a single sequence but require per-video initialization and cannot generalize across videos. Classic correspondence pipelines operate on detector-chosen keypoints and struggle in low-texture scenes, while dense feature matching and one-shot segmentation methods enable cross-video propagation but lack spatiotemporal smoothness and unified support for both point and mask annotations. We present Match4Annotate, a lightweight framework for both intra-video and inter-video propagation of point and mask annotations. Our method fits a SIREN-based implicit neural representation to DINOv3 features at test time, producing a continuous, high-resolution spatiotemporal feature field, and learns a smooth implicit deformation field between frame pairs to guide correspondence matching. We evaluate on three challenging clinical ultrasound datasets. Match4Annotate achieves state-of-the-art inter-video propagation, outperforming feature matching and one-shot segmentation baselines, while remaining competitive with specialized trackers for intra-video propagation. Our results show that lightweight, test-time-optimized feature matching pipelines have the potential to offer an efficient and accessible solution for scalable annotation workflows.

