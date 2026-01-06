---
layout: default
title: Rank-based Geographical Regularization: Revisiting Contrastive Self-Supervised Learning for Multispectral Remote Sensing Imagery
---

# Rank-based Geographical Regularization: Revisiting Contrastive Self-Supervised Learning for Multispectral Remote Sensing Imagery
**arXiv**：[2601.02289v1](https://arxiv.org/abs/2601.02289) · [PDF](https://arxiv.org/pdf/2601.02289.pdf)  
**作者**：Tom Burgert, Leonard Hackel, Paolo Rota, Begüm Demir  

**一句话要点**：提出GeoRank正则化方法，优化对比自监督学习在遥感图像中的地理嵌入

**关键词**：自监督学习, 多光谱遥感, 地理正则化, 对比学习, 特征嵌入, 遥感图像分析

## 3 点简述
- 针对多光谱遥感图像的地理和时间变异性，改进对比自监督学习
- 通过直接优化球面距离，将地理关系嵌入特征空间
- 在多种对比算法上表现优于或匹配现有方法，并系统评估关键适应因素

## 摘要（原文）

> Self-supervised learning (SSL) has become a powerful paradigm for learning from large, unlabeled datasets, particularly in computer vision (CV). However, applying SSL to multispectral remote sensing (RS) images presents unique challenges and opportunities due to the geographical and temporal variability of the data. In this paper, we introduce GeoRank, a novel regularization method for contrastive SSL that improves upon prior techniques by directly optimizing spherical distances to embed geographical relationships into the learned feature space. GeoRank outperforms or matches prior methods that integrate geographical metadata and consistently improves diverse contrastive SSL algorithms (e.g., BYOL, DINO). Beyond this, we present a systematic investigation of key adaptations of contrastive SSL for multispectral RS images, including the effectiveness of data augmentations, the impact of dataset cardinality and image size on performance, and the task dependency of temporal views. Code is available at https://github.com/tomburgert/georank.

