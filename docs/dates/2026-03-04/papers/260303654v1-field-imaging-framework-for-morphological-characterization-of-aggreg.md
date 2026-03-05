---
layout: default
title: Field imaging framework for morphological characterization of aggregates with computer vision: Algorithms and applications
---

# Field imaging framework for morphological characterization of aggregates with computer vision: Algorithms and applications
**arXiv**：[2603.03654v1](https://arxiv.org/abs/2603.03654) · [PDF](https://arxiv.org/pdf/2603.03654.pdf)  
**作者**：Haohang Huang  

**一句话要点**：提出现场成像框架以解决多场景下骨料形态表征的挑战

**关键词**：骨料形态表征, 现场成像框架, 3D实例分割, 3D形状补全, 多场景分析

## 3 点简述
- 核心问题：现有骨料成像方法局限于规则尺寸和受控条件，无法适应现场多场景需求。
- 方法要点：开发了针对非重叠骨料、骨料堆2D图像和3D点云的多场景成像与分析算法，包括3D重建-分割-补全集成方法。
- 实验或效果：在真实骨料堆上验证，集成方法能有效捕获和预测骨料未观测面，性能良好。

## 摘要（原文）

> Construction aggregates, including sand and gravel, crushed stone and riprap, are the core building blocks of the construction industry. State-of-the-practice characterization methods mainly relies on visual inspection and manual measurement. State-of-the-art aggregate imaging methods have limitations that are only applicable to regular-sized aggregates under well-controlled conditions. This dissertation addresses these major challenges by developing a field imaging framework for the morphological characterization of aggregates as a multi-scenario solution. For individual and non-overlapping aggregates, a field imaging system was designed and the associated segmentation and volume estimation algorithms were developed. For 2D image analyses of aggregates in stockpiles, an automated 2D instance segmentation and morphological analysis approach was established. For 3D point cloud analyses of aggregate stockpiles, an integrated 3D Reconstruction-Segmentation-Completion (RSC-3D) approach was established: 3D reconstruction procedures from multi-view images, 3D stockpile instance segmentation, and 3D shape completion to predict the unseen sides. First, a 3D reconstruction procedure was developed to obtain high-fidelity 3D models of collected aggregate samples, based on which a 3D aggregate particle library was constructed. Next, two datasets were derived from the 3D particle library for 3D learning: a synthetic dataset of aggregate stockpiles with ground-truth instance labels, and a dataset of partial-complete shape pairs, developed with varying-view raycasting schemes. A state-of-the-art 3D instance segmentation network and a 3D shape completion network were trained on the datasets, respectively. The application of the integrated approach was demonstrated on real stockpiles and validated with ground-truth, showing good performance in capturing and predicting the unseen sides of aggregates.

