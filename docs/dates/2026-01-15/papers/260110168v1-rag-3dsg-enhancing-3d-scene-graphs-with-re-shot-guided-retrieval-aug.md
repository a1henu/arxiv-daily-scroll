---
layout: default
title: RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation
---

# RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation
**arXiv**：[2601.10168v1](https://arxiv.org/abs/2601.10168) · [PDF](https://arxiv.org/pdf/2601.10168.pdf)  
**作者**：Yue Chang, Rufeng Chen, Zhaofan Zhang, Yi Chen, Sihong Xie  

**一句话要点**：提出RAG-3DSG，通过重拍引导检索增强生成提升开放词汇3D场景图生成精度与速度

**关键词**：3D场景图生成, 检索增强生成, 不确定性估计, 物体识别, 跨图像聚合, 动态下采样

## 3 点简述
- 核心问题：开放词汇3D场景图生成存在物体识别精度低和速度慢，受限于视角、遮挡和冗余表面密度。
- 方法要点：采用重拍引导不确定性估计减少聚合噪声，基于低不确定性物体实现检索增强生成，并引入动态下采样映射策略加速跨图像物体聚合。
- 实验或效果：在Replica数据集上显著提升节点标注精度，同时将映射时间减少三分之二。

## 摘要（原文）

> Open-vocabulary 3D Scene Graph (3DSG) generation can enhance various downstream tasks in robotics, such as manipulation and navigation, by leveraging structured semantic representations. A 3DSG is constructed from multiple images of a scene, where objects are represented as nodes and relationships as edges. However, existing works for open-vocabulary 3DSG generation suffer from both low object-level recognition accuracy and speed, mainly due to constrained viewpoints, occlusions, and redundant surface density. To address these challenges, we propose RAG-3DSG to mitigate aggregation noise through re-shot guided uncertainty estimation and support object-level Retrieval-Augmented Generation (RAG) via reliable low-uncertainty objects. Furthermore, we propose a dynamic downsample-mapping strategy to accelerate cross-image object aggregation with adaptive granularity. Experiments on Replica dataset demonstrate that RAG-3DSG significantly improves node captioning accuracy in 3DSG generation while reducing the mapping time by two-thirds compared to the vanilla version.

