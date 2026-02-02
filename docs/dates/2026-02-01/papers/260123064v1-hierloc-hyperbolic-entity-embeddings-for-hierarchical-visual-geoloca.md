---
layout: default
title: HierLoc: Hyperbolic Entity Embeddings for Hierarchical Visual Geolocation
---

# HierLoc: Hyperbolic Entity Embeddings for Hierarchical Visual Geolocation
**arXiv**：[2601.23064v1](https://arxiv.org/abs/2601.23064) · [PDF](https://arxiv.org/pdf/2601.23064.pdf)  
**作者**：Hari Krishna Gadi, Daniel Matos, Hongyi Luo, Lu Liu, Yongliang Wang, Yanfeng Zhang, Liqiu Meng  

**一句话要点**：提出基于双曲空间层次实体嵌入的视觉地理定位方法，以解决大规模检索和地理连续性忽略问题。

**关键词**：视觉地理定位, 双曲嵌入, 层次实体, 对比学习, 地理距离整合, 高效推理

## 3 点简述
- 核心问题：视觉地理定位面临全球尺度、视觉模糊性和地理层次结构挑战，现有方法存在存储开销大或忽略地理连续性。
- 方法要点：采用实体中心化框架，将图像直接对齐到双曲空间中的地理实体层次，通过Geo-Weighted Hyperbolic对比学习整合地理距离。
- 实验或效果：在OSV5M基准上实现新SOTA，平均测地误差降低19.5%，细粒度子区域准确率提升43%，推理效率高。

## 摘要（原文）

> Visual geolocalization, the task of predicting where an image was taken, remains challenging due to global scale, visual ambiguity, and the inherently hierarchical structure of geography. Existing paradigms rely on either large-scale retrieval, which requires storing a large number of image embeddings, grid-based classifiers that ignore geographic continuity, or generative models that diffuse over space but struggle with fine detail. We introduce an entity-centric formulation of geolocation that replaces image-to-image retrieval with a compact hierarchy of geographic entities embedded in Hyperbolic space. Images are aligned directly to country, region, subregion, and city entities through Geo-Weighted Hyperbolic contrastive learning by directly incorporating haversine distance into the contrastive objective. This hierarchical design enables interpretable predictions and efficient inference with 240k entity embeddings instead of over 5 million image embeddings on the OSV5M benchmark, on which our method establishes a new state-of-the-art performance. Compared to the current methods in the literature, it reduces mean geodesic error by 19.5\%, while improving the fine-grained subregion accuracy by 43%. These results demonstrate that geometry-aware hierarchical embeddings provide a scalable and conceptually new alternative for global image geolocation.

