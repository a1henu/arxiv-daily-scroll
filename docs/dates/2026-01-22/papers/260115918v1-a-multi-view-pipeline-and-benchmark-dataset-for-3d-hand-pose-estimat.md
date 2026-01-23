---
layout: default
title: A Multi-View Pipeline and Benchmark Dataset for 3D Hand Pose Estimation in Surgery
---

# A Multi-View Pipeline and Benchmark Dataset for 3D Hand Pose Estimation in Surgery
**arXiv**：[2601.15918v1](https://arxiv.org/abs/2601.15918) · [PDF](https://arxiv.org/pdf/2601.15918.pdf)  
**作者**：Valery Fischer, Alan Magdaleno, Anna-Katharina Calek, Nicola Cavalcanti, Nathan Hoffman, Christoph Germann, Joschua Wüthrich, Max Krähenmann, Mazda Farshad, Philipp Fürnstahl, Lilian Calvet  

**一句话要点**：提出无需微调的多视图管道与手术数据集，用于手术中3D手部姿态估计。

**关键词**：3D手部姿态估计, 手术计算机视觉, 多视图管道, 基准数据集, 无监督优化

## 3 点简述
- 核心问题：手术环境光照强、遮挡多、手套导致外观单一，且缺乏标注数据集。
- 方法要点：集成人员检测、全身姿态估计和2D手部关键点预测，通过约束优化实现3D估计。
- 实验或效果：在2D和3D误差上分别减少31%和76%，优于基线方法。

## 摘要（原文）

> Purpose: Accurate 3D hand pose estimation supports surgical applications such as skill assessment, robot-assisted interventions, and geometry-aware workflow analysis. However, surgical environments pose severe challenges, including intense and localized lighting, frequent occlusions by instruments or staff, and uniform hand appearance due to gloves, combined with a scarcity of annotated datasets for reliable model training.
>   Method: We propose a robust multi-view pipeline for 3D hand pose estimation in surgical contexts that requires no domain-specific fine-tuning and relies solely on off-the-shelf pretrained models. The pipeline integrates reliable person detection, whole-body pose estimation, and state-of-the-art 2D hand keypoint prediction on tracked hand crops, followed by a constrained 3D optimization. In addition, we introduce a novel surgical benchmark dataset comprising over 68,000 frames and 3,000 manually annotated 2D hand poses with triangulated 3D ground truth, recorded in a replica operating room under varying levels of scene complexity.
>   Results: Quantitative experiments demonstrate that our method consistently outperforms baselines, achieving a 31% reduction in 2D mean joint error and a 76% reduction in 3D mean per-joint position error.
>   Conclusion: Our work establishes a strong baseline for 3D hand pose estimation in surgery, providing both a training-free pipeline and a comprehensive annotated dataset to facilitate future research in surgical computer vision.

