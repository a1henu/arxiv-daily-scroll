---
layout: default
title: Enhancing Few-Shot Classification of Benchmark and Disaster Imagery with ATTBHFA-Net
---

# Enhancing Few-Shot Classification of Benchmark and Disaster Imagery with ATTBHFA-Net
**arXiv**：[2510.18326v1](https://arxiv.org/abs/2510.18326) · [PDF](https://arxiv.org/pdf/2510.18326.pdf)  
**作者**：Gao Yu Lee, Tanmoy Dam, Md Meftahul Ferdaus, Daniel Puiu Poenar, Vu Duong  

**一句话要点**：提出ATTBHFA-Net以解决灾难图像少样本分类中的高类内变异和类间相似性问题

**关键词**：少样本学习, 灾难图像分类, 特征分布聚合, Bhattacharyya系数, Hellinger距离, 对比学习

## 3 点简述
- 核心问题：灾难图像数据稀缺、类内变异高、类间相似性强，限制少样本学习性能。
- 方法要点：结合Bhattacharyya系数和Hellinger距离，聚合特征分布以增强原型鲁棒性。
- 实验或效果：在四个少样本基准和两个灾难数据集上表现优于现有方法，泛化能力强。

## 摘要（原文）

> The increasing frequency of natural and human-induced disasters necessitates
> advanced visual recognition techniques capable of analyzing critical
> photographic data. With progress in artificial intelligence and resilient
> computational systems, rapid and accurate disaster classification has become
> crucial for efficient rescue operations. However, visual recognition in
> disaster contexts faces significant challenges due to limited and diverse data
> from the difficulties in collecting and curating comprehensive, high-quality
> disaster imagery. Few-Shot Learning (FSL) provides a promising approach to data
> scarcity, yet current FSL research mainly relies on generic benchmark datasets
> lacking remote-sensing disaster imagery, limiting its practical effectiveness.
> Moreover, disaster images exhibit high intra-class variation and inter-class
> similarity, hindering the performance of conventional metric-based FSL methods.
> To address these issues, this paper introduces the Attention-based
> Bhattacharyya-Hellinger Feature Aggregation Network (ATTBHFA-Net), which
> linearly combines the Bhattacharyya coefficient and Hellinger distances to
> compare and aggregate feature probability distributions for robust prototype
> formation. The Bhattacharyya coefficient serves as a contrastive margin that
> enhances inter-class separability, while the Hellinger distance regularizes
> same-class alignment. This framework parallels contrastive learning but
> operates over probability distributions rather than embedded feature points.
> Furthermore, a Bhattacharyya-Hellinger distance-based contrastive loss is
> proposed as a distributional counterpart to cosine similarity loss, used
> jointly with categorical cross-entropy to significantly improve FSL
> performance. Experiments on four FSL benchmarks and two disaster image datasets
> demonstrate the superior effectiveness and generalization of ATTBHFA-Net
> compared to existing approaches.

