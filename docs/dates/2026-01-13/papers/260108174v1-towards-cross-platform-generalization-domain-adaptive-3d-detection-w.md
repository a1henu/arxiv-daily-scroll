---
layout: default
title: Towards Cross-Platform Generalization: Domain Adaptive 3D Detection with Augmentation and Pseudo-Labeling
---

# Towards Cross-Platform Generalization: Domain Adaptive 3D Detection with Augmentation and Pseudo-Labeling
**arXiv**：[2601.08174v1](https://arxiv.org/abs/2601.08174) · [PDF](https://arxiv.org/pdf/2601.08174.pdf)  
**作者**：Xiyan Feng, Wenbo Zhang, Lu Zhang, Yunzhi Zhuge, Huchuan Lu, You He  

**一句话要点**：提出基于数据增强和伪标签自训练的域自适应方法，以提升跨平台3D检测的泛化能力。

**关键词**：跨平台3D检测, 域自适应, 数据增强, 伪标签自训练, PVRCNN++

## 3 点简述
- 核心问题：跨平台3D检测中的域差异导致模型泛化性能下降。
- 方法要点：在PVRCNN++基础上，通过定制数据增强和伪标签自训练策略缩小域差距。
- 实验或效果：在RoboSense2025挑战赛中获第三名，Car类别3D AP达62.67%（阶段一）和58.76%（阶段二）。

## 摘要（原文）

> This technical report represents the award-winning solution to the Cross-platform 3D Object Detection task in the RoboSense2025 Challenge. Our approach is built upon PVRCNN++, an efficient 3D object detection framework that effectively integrates point-based and voxel-based features. On top of this foundation, we improve cross-platform generalization by narrowing domain gaps through tailored data augmentation and a self-training strategy with pseudo-labels. These enhancements enabled our approach to secure the 3rd place in the challenge, achieving a 3D AP of 62.67% for the Car category on the phase-1 target domain, and 58.76% and 49.81% for Car and Pedestrian categories respectively on the phase-2 target domain.

