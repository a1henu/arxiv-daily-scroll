---
layout: default
title: LeafTrackNet: A Deep Learning Framework for Robust Leaf Tracking in Top-Down Plant Phenotyping
---

# LeafTrackNet: A Deep Learning Framework for Robust Leaf Tracking in Top-Down Plant Phenotyping
**arXiv**：[2512.13130v1](https://arxiv.org/abs/2512.13130) · [PDF](https://arxiv.org/pdf/2512.13130.pdf)  
**作者**：Shanghua Liu, Majharulislam Babor, Christoph Verduyn, Breght Vandenberghe, Bruno Betoni Parodi, Cornelia Weltzien, Marina M. -C. Höhne  

**一句话要点**：提出LeafTrackNet框架以解决复杂作物叶片在真实条件下的鲁棒跟踪问题

**关键词**：叶片跟踪, 深度学习框架, 植物表型分析, 多目标跟踪, 数据集构建

## 3 点简述
- 核心问题：缺乏鲁棒方法跟踪复杂作物叶片，现有方法受限或不适于动态生物场景
- 方法要点：结合YOLOv10检测器和MobileNetV3嵌入网络，采用基于嵌入的记忆关联策略
- 实验或效果：在CanolaTrack数据集上优于植物专用跟踪器和MOT基线，HOTA提升9%

## 摘要（原文）

> High resolution phenotyping at the level of individual leaves offers fine-grained insights into plant development and stress responses. However, the full potential of accurate leaf tracking over time remains largely unexplored due to the absence of robust tracking methods-particularly for structurally complex crops such as canola. Existing plant-specific tracking methods are typically limited to small-scale species or rely on constrained imaging conditions. In contrast, generic multi-object tracking (MOT) methods are not designed for dynamic biological scenes. Progress in the development of accurate leaf tracking models has also been hindered by a lack of large-scale datasets captured under realistic conditions. In this work, we introduce CanolaTrack, a new benchmark dataset comprising 5,704 RGB images with 31,840 annotated leaf instances spanning the early growth stages of 184 canola plants. To enable accurate leaf tracking over time, we introduce LeafTrackNet, an efficient framework that combines a YOLOv10-based leaf detector with a MobileNetV3-based embedding network. During inference, leaf identities are maintained over time through an embedding-based memory association strategy. LeafTrackNet outperforms both plant-specific trackers and state-of-the-art MOT baselines, achieving a 9% HOTA improvement on CanolaTrack. With our work we provide a new standard for leaf-level tracking under realistic conditions and we provide CanolaTrack - the largest dataset for leaf tracking in agriculture crops, which will contribute to future research in plant phenotyping. Our code and dataset are publicly available at https://github.com/shl-shawn/LeafTrackNet.

