---
layout: default
title: A Multi-scale Fused Graph Neural Network with Inter-view Contrastive Learning for Spatial Transcriptomics Data Clustering
---

# A Multi-scale Fused Graph Neural Network with Inter-view Contrastive Learning for Spatial Transcriptomics Data Clustering
**arXiv**：[2512.16188v1](https://arxiv.org/abs/2512.16188) · [PDF](https://arxiv.org/pdf/2512.16188.pdf)  
**作者**：Jianping Mei, Siqi Ai, Ye Yuan  

**一句话要点**：提出stMFG多尺度融合图神经网络，通过层间跨视图注意力解决空间转录组数据聚类问题

**关键词**：空间转录组学, 图神经网络, 多尺度融合, 跨视图对比学习, 数据聚类

## 3 点简述
- 核心问题：现有方法对空间和特征视图分别编码，限制了多尺度语义捕获和跨视图交互
- 方法要点：引入层间跨视图注意力动态整合空间与基因特征，结合对比学习和空间约束增强判别性
- 实验或效果：在DLPFC和乳腺癌数据集上优于现有方法，某些切片ARI提升达14%

## 摘要（原文）

> Spatial transcriptomics enables genome-wide expression analysis within native tissue context, yet identifying spatial domains remains challenging due to complex gene-spatial interactions. Existing methods typically process spatial and feature views separately, fusing only at output level - an "encode-separately, fuse-late" paradigm that limits multi-scale semantic capture and cross-view interaction. Accordingly, stMFG is proposed, a multi-scale interactive fusion graph network that introduces layer-wise cross-view attention to dynamically integrate spatial and gene features after each convolution. The model combines cross-view contrastive learning with spatial constraints to enhance discriminability while maintaining spatial continuity. On DLPFC and breast cancer datasets, stMFG outperforms state-of-the-art methods, achieving up to 14% ARI improvement on certain slices.

