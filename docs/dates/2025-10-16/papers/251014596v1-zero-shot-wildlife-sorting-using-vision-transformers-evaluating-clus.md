---
layout: default
title: Zero-Shot Wildlife Sorting Using Vision Transformers: Evaluating Clustering and Continuous Similarity Ordering
---

# Zero-Shot Wildlife Sorting Using Vision Transformers: Evaluating Clustering and Continuous Similarity Ordering
**arXiv**：[2510.14596v1](https://arxiv.org/abs/2510.14596) · [PDF](https://arxiv.org/pdf/2510.14596.pdf)  
**作者**：Hugo Markoff, Jevgenijs Galaktionovs  

**一句话要点**：评估零样本方法使用视觉变换器对野生动物图像进行聚类和连续相似性排序，以加速生物多样性监测。

**关键词**：零样本学习, 视觉变换器, 无监督聚类, 相似性排序, 生物多样性监测, 相机陷阱图像

## 3 点简述
- 核心问题：相机陷阱图像中物种未标注，现有分类器无法覆盖，需零样本方法组织图像。
- 方法要点：比较自监督视觉变换器架构与降维技术，实现无监督聚类和连续相似性排序。
- 实验或效果：DINOv2结合UMAP和GMM在5物种测试集上达88.6%准确率，排序在哺乳动物和鸟类达88.2%一致性。

## 摘要（原文）

> Camera traps generate millions of wildlife images, yet many datasets contain
> species that are absent from existing classifiers. This work evaluates
> zero-shot approaches for organizing unlabeled wildlife imagery using
> self-supervised vision transformers, developed and tested within the Animal
> Detect platform for camera trap analysis. We compare unsupervised clustering
> methods (DBSCAN, GMM) across three architectures (CLIP, DINOv2, MegaDescriptor)
> combined with dimensionality reduction techniques (PCA, UMAP), and we
> demonstrate continuous 1D similarity ordering via t-SNE projection. On a
> 5-species test set with ground truth labels used only for evaluation, DINOv2
> with UMAP and GMM achieves 88.6 percent accuracy (macro-F1 = 0.874), while 1D
> sorting reaches 88.2 percent coherence for mammals and birds and 95.2 percent
> for fish across 1,500 images. Based on these findings, we deployed continuous
> similarity ordering in production, enabling rapid exploratory analysis and
> accelerating manual annotation workflows for biodiversity monitoring.

