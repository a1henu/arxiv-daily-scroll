---
layout: default
title: Modeling and Measuring Redundancy in Multisource Multimodal Data for Autonomous Driving
---

# Modeling and Measuring Redundancy in Multisource Multimodal Data for Autonomous Driving
**arXiv**：[2603.06544v1](https://arxiv.org/abs/2603.06544) · [PDF](https://arxiv.org/pdf/2603.06544.pdf)  
**作者**：Yuhan Zhou, Mehri Sattari, Haihua Chen, Kewei Sha  

**一句话要点**：提出多源多模态数据冗余建模与度量方法，以提升自动驾驶感知性能

**关键词**：自动驾驶感知, 数据冗余度量, 多模态数据融合, 目标检测, 数据质量分析

## 3 点简述
- 核心问题：自动驾驶数据质量中冗余问题未充分探索，影响算法性能
- 方法要点：基于nuScenes和Argoverse 2数据集，建模并度量多源相机和多模态图像-LiDAR数据冗余
- 实验或效果：选择性移除冗余标签可提升YOLOv8检测mAP，如nuScenes中mAP50从0.66增至0.70

## 摘要（原文）

> Next-generation autonomous vehicles (AVs) rely on large volumes of multisource and multimodal ($M^2$) data to support real-time decision-making. In practice, data quality (DQ) varies across sources and modalities due to environmental conditions and sensor limitations, yet AV research has largely prioritized algorithm design over DQ analysis. This work focuses on redundancy as a fundamental but underexplored DQ issue in AV datasets. Using the nuScenes and Argoverse 2 (AV2) datasets, we model and measure redundancy in multisource camera data and multimodal image-LiDAR data, and evaluate how removing redundant labels affects the YOLOv8 object detection task. Experimental results show that selectively removing redundant multisource image object labels from cameras with shared fields of view improves detection. In nuScenes, mAP${50}$ gains from $0.66$ to $0.70$, $0.64$ to $0.67$, and from $0.53$ to $0.55$, on three representative overlap regions, while detection on other overlapping camera pairs remains at the baseline even under stronger pruning. In AV2, $4.1$-$8.6\%$ of labels are removed, and mAP${50}$ stays near the $0.64$ baseline. Multimodal analysis also reveals substantial redundancy between image and LiDAR data. These findings demonstrate that redundancy is a measurable and actionable DQ factor with direct implications for AV performance. This work highlights the role of redundancy as a data quality factor in AV perception and motivates a data-centric perspective for evaluating and improving AV datasets. Code, data, and implementation details are publicly available at: https://github.com/yhZHOU515/RedundancyAD

