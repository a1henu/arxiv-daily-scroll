---
layout: default
title: Multi-View Foundation Models
---

# Multi-View Foundation Models
**arXiv**：[2512.15708v1](https://arxiv.org/abs/2512.15708) · [PDF](https://arxiv.org/pdf/2512.15708.pdf)  
**作者**：Leo Segre, Or Hirschorn, Shai Avidan  

**一句话要点**：提出多视图基础模型以解决多视图图像特征不一致问题

**关键词**：多视图基础模型, 特征一致性, 3D感知注意力, Transformer增强, 表面法线估计, 多视图分割

## 3 点简述
- 核心问题：基础模型处理多视图图像时，相同3D点特征不一致。
- 方法要点：通过添加3D感知注意力层，增强Transformer基础模型跨视图特征匹配。
- 实验或效果：在表面法线估计和多视图分割任务中，特征匹配性能显著提升。

## 摘要（原文）

> Foundation models are vital tools in various Computer Vision applications. They take as input a single RGB image and output a deep feature representation that is useful for various applications. However, in case we have multiple views of the same 3D scene, they operate on each image independently and do not always produce consistent features for the same 3D point. We propose a way to convert a Foundation Model into a Multi-View Foundation Model. Such a model takes as input a set of images and outputs a feature map for each image such that the features of corresponding points are as consistent as possible. This approach bypasses the need to build a consistent 3D model of the features and allows direct manipulation in the image space. Specifically, we show how to augment Transformers-based foundation models (i.e., DINO, SAM, CLIP) with intermediate 3D-aware attention layers that help match features across different views. As leading examples, we show surface normal estimation and multi-view segmentation tasks. Quantitative experiments show that our method improves feature matching considerably compared to current foundation models.

