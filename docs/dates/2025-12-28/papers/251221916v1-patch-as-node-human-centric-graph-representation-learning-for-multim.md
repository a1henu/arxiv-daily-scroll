---
layout: default
title: Patch as Node: Human-Centric Graph Representation Learning for Multimodal Action Recognition
---

# Patch as Node: Human-Centric Graph Representation Learning for Multimodal Action Recognition
**arXiv**：[2512.21916v1](https://arxiv.org/abs/2512.21916) · [PDF](https://arxiv.org/pdf/2512.21916.pdf)  
**作者**：Zeyu Liang, Hailun Xia, Naichuan Zheng  

**一句话要点**：提出PAN框架，以人体为中心构建图表示学习，解决RGB与骨架模态融合中的异构性问题。

**关键词**：多模态动作识别, 图表示学习, 人体中心建模, 注意力校准, RGB-骨架融合

## 3 点简述
- 核心问题：RGB与骨架模态的异构性阻碍了多模态动作识别的有效融合。
- 方法要点：将RGB补丁表示为时空图，并引入注意力后校准以减少对高质量骨架数据的依赖。
- 实验或效果：在三个数据集上，PAN-Ensemble和PAN-Unified分别在分离和统一建模中达到SOTA性能。

## 摘要（原文）

> While human action recognition has witnessed notable achievements, multimodal methods fusing RGB and skeleton modalities still suffer from their inherent heterogeneity and fail to fully exploit the complementary potential between them. In this paper, we propose PAN, the first human-centric graph representation learning framework for multimodal action recognition, in which token embeddings of RGB patches containing human joints are represented as spatiotemporal graphs. The human-centric graph modeling paradigm suppresses the redundancy in RGB frames and aligns well with skeleton-based methods, thus enabling a more effective and semantically coherent fusion of multimodal features. Since the sampling of token embeddings heavily relies on 2D skeletal data, we further propose attention-based post calibration to reduce the dependency on high-quality skeletal data at a minimal cost interms of model performance. To explore the potential of PAN in integrating with skeleton-based methods, we present two variants: PAN-Ensemble, which employs dual-path graph convolution networks followed by late fusion, and PAN-Unified, which performs unified graph representation learning within a single network. On three widely used multimodal action recognition datasets, both PAN-Ensemble and PAN-Unified achieve state-of-the-art (SOTA) performance in their respective settings of multimodal fusion: separate and unified modeling, respectively.

