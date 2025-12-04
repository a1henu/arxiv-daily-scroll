---
layout: default
title: DINO-RotateMatch: A Rotation-Aware Deep Framework for Robust Image Matching in Large-Scale 3D Reconstruction
---

# DINO-RotateMatch: A Rotation-Aware Deep Framework for Robust Image Matching in Large-Scale 3D Reconstruction
**arXiv**：[2512.03715v1](https://arxiv.org/abs/2512.03715) · [PDF](https://arxiv.org/pdf/2512.03715.pdf)  
**作者**：Kaichen Zhang, Tianxiang Sheng, Xuanming Shi  

**一句话要点**：提出DINO-RotateMatch框架，结合旋转感知匹配解决大规模3D重建中的图像匹配挑战。

**关键词**：大规模3D重建, 图像匹配, 旋转感知特征, 自监督学习, 深度学习框架

## 3 点简述
- 核心问题：大规模非结构化网络图像在3D重建中面临图像匹配的鲁棒性和可扩展性挑战。
- 方法要点：集成数据集自适应图像配对与旋转增强的局部特征提取匹配，使用DINO进行语义检索。
- 实验或效果：在Kaggle Image Matching Challenge 2025中提升mAA，获得银奖，验证了方法的有效性。

## 摘要（原文）

> This paper presents DINO-RotateMatch, a deep-learning framework designed to address the chal lenges of image matching in large-scale 3D reconstruction from unstructured Internet images. The
>   method integrates a dataset-adaptive image pairing strategy with rotation-aware keypoint extraction and
>   matching. DINO is employed to retrieve semantically relevant image pairs in large collections, while
>   rotation-based augmentation captures orientation-dependent local features using ALIKED and Light Glue. Experiments on the Kaggle Image Matching Challenge 2025 demonstrate consistent improve ments in mean Average Accuracy (mAA), achieving a Silver Award (47th of 943 teams). The results
>   confirm that combining self-supervised global descriptors with rotation-enhanced local matching offers
>   a robust and scalable solution for large-scale 3D reconstruction.

