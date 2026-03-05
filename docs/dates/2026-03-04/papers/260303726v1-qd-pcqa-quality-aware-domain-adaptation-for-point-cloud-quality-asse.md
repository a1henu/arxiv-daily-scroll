---
layout: default
title: QD-PCQA: Quality-Aware Domain Adaptation for Point Cloud Quality Assessment
---

# QD-PCQA: Quality-Aware Domain Adaptation for Point Cloud Quality Assessment
**arXiv**：[2603.03726v1](https://arxiv.org/abs/2603.03726) · [PDF](https://arxiv.org/pdf/2603.03726.pdf)  
**作者**：Guohua Zhang, Jian Jin, Meiqin Liu, Chao Yao, Weisi Lin  

**一句话要点**：提出QD-PCQA框架，通过质量感知域适应解决无参考点云质量评估泛化问题。

**关键词**：点云质量评估, 无参考评估, 域适应, 质量感知对齐, 特征增强, 泛化性能

## 3 点简述
- 核心问题：无参考点云质量评估因标注数据稀缺而泛化能力不足，现有域适应方法忽视感知质量特性。
- 方法要点：设计排序加权条件对齐和质量引导特征增强策略，强化质量排名感知和特征对齐。
- 实验或效果：跨域实验显示QD-PCQA显著提升无参考点云质量评估的泛化性能。

## 摘要（原文）

> No-Reference Point Cloud Quality Assessment (NR-PCQA) still struggles with generalization, primarily due to the scarcity of annotated point cloud datasets. Since the Human Visual System (HVS) drives perceptual quality assessment independently of media types, prior knowledge on quality learned from images can be repurposed for point clouds. This insight motivates adopting Unsupervised Domain Adaptation (UDA) to transfer quality-relevant priors from labeled images to unlabeled point clouds. However, existing UDA-based PCQA methods often overlook key characteristics of perceptual quality, such as sensitivity to quality ranking and quality-aware feature alignment, thereby limiting their effectiveness. To address these issues, we propose a novel Quality-aware Domain adaptation framework for PCQA, termed QD-PCQA. The framework comprises two main components: i) a Rank-weighted Conditional Alignment (RCA) strategy that aligns features under consistent quality levels and adaptively emphasizes misranked samples to reinforce perceptual quality ranking awareness; and ii) a Quality-guided Feature Augmentation (QFA) strategy, which includes quality-guided style mixup, multi-layer extension, and dual-domain augmentation modules to augment perceptual feature alignment. Extensive cross-domain experiments demonstrate that QD-PCQA significantly improves generalization in NR-PCQA tasks. The code is available at https://github.com/huhu-code/QD-PCQA.

