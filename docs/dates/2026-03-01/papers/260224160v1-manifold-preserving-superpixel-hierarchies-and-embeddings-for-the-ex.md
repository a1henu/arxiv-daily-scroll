---
layout: default
title: Manifold-Preserving Superpixel Hierarchies and Embeddings for the Exploration of High-Dimensional Images
---

# Manifold-Preserving Superpixel Hierarchies and Embeddings for the Exploration of High-Dimensional Images
**arXiv**：[2602.24160v1](https://arxiv.org/abs/2602.24160) · [PDF](https://arxiv.org/pdf/2602.24160.pdf)  
**作者**：Alexander Vieth, Boudewijn Lelieveldt, Elmar Eisemann, Anna Vilanova, Thomas Höllt  

**一句话要点**：提出基于超像素层次结构和嵌入的方法，以支持高维图像在图像空间和属性空间中的一致探索。

**关键词**：高维图像探索, 超像素层次结构, 流形保持, 层次降维, 嵌入技术

## 3 点简述
- 核心问题：现有层次降维方法忽略像素空间布局，导致图像空间感兴趣区域与属性层次结构不一致。
- 方法要点：构建考虑高维属性流形的超像素层次结构，实现图像和属性空间的协同探索。
- 实验或效果：通过两个用例比较，验证了该方法在嵌入探索中的有效性优于传统层次嵌入方法。

## 摘要（原文）

> High-dimensional images, or images with a high-dimensional attribute vector per pixel, are commonly explored with coordinated views of a low-dimensional embedding of the attribute space and a conventional image representation. Nowadays, such images can easily contain several million pixels. For such large datasets, hierarchical embedding techniques are better suited to represent the high-dimensional attribute space than flat dimensionality reduction methods. However, available hierarchical dimensionality reduction methods construct the hierarchy purely based on the attribute information and ignore the spatial layout of pixels in the images. This impedes the exploration of regions of interest in the image space, since there is no congruence between a region of interest in image space and the associated attribute abstractions in the hierarchy. In this paper, we present a superpixel hierarchy for high-dimensional images that takes the high-dimensional attribute manifold into account during construction. Through this, our method enables consistent exploration of high-dimensional images in both image and attribute space. We show the effectiveness of this new image-guided hierarchy in the context of embedding exploration by comparing it with classical hierarchical embedding-based image exploration in two use cases.

