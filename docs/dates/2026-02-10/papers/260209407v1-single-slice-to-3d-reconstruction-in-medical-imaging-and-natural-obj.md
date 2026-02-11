---
layout: default
title: Single-Slice-to-3D Reconstruction in Medical Imaging and Natural Objects: A Comparative Benchmark with SAM 3D
---

# Single-Slice-to-3D Reconstruction in Medical Imaging and Natural Objects: A Comparative Benchmark with SAM 3D
**arXiv**：[2602.09407v1](https://arxiv.org/abs/2602.09407) · [PDF](https://arxiv.org/pdf/2602.09407.pdf)  
**作者**：Yan Luo, Advaith Ravishankar, Serena Liu, Yutong Yang, Mengyu Wang  

**一句话要点**：比较SAM 3D等模型在医学与自然图像单切片到3D重建中的零样本性能

**关键词**：单切片到3D重建, 医学图像, 零样本基准, 几何先验, 深度模糊, 拓扑相似性

## 3 点简述
- 核心问题：探究自然图像训练的几何先验是否适用于医学数据单切片到3D重建
- 方法要点：在五个先进模型上构建零样本基准，评估六个医学和两个自然数据集
- 实验或效果：SAM 3D在医学数据上拓扑相似性最佳，但所有模型因深度模糊而重建有限

## 摘要（原文）

> A 3D understanding of anatomy is central to diagnosis and treatment planning, yet volumetric imaging remains costly with long wait times. Image-to-3D foundations models can solve this issue by reconstructing 3D data from 2D modalites. Current foundation models are trained on natural image distributions to reconstruct naturalistic objects from a single image by leveraging geometric priors across pixels. However, it is unclear whether these learned geometric priors transfer to medical data. In this study, we present a controlled zero-shot benchmark of single slice medical image-to-3D reconstruction across five state-of-the-art image-to-3D models: SAM3D, Hunyuan3D-2.1, Direct3D, Hi3DGen, and TripoSG. These are evaluated across six medical datasets spanning anatomical and pathological structures and two natrual datasets, using voxel based metrics and point cloud distance metrics. Across medical datasets, voxel based overlap remains moderate for all models, consistent with a depth reconstruction failure mode when inferring volume from a single slice. In contrast, global distance metrics show more separation between methods: SAM3D achieves the strongest overall topological similarity to ground truth medical 3D data, while alternative models are more prone to over-simplication of reconstruction. Our results quantify the limits of single-slice medical reconstruction and highlight depth ambiguity caused by the planar nature of 2D medical data, motivating multi-view image-to-3D reconstruction to enable reliable medical 3D inference.

