---
layout: default
title: Rethinking Divisive Hierarchical Clustering from a Distributional Perspective
---

# Rethinking Divisive Hierarchical Clustering from a Distributional Perspective
**arXiv**：[2601.19718v1](https://arxiv.org/abs/2601.19718) · [PDF](https://arxiv.org/pdf/2601.19718.pdf)  
**作者**：Kaifeng Zhang, Kai Ming Ting, Tianrun Liang, Qiuran Zhao  

**一句话要点**：提出基于分布核的DHC方法，以解决传统方法在树状图属性上的不足，应用于空间转录组学数据集。

**关键词**：分裂层次聚类, 分布核, 树状图属性, 总相似度最大化, 空间转录组学, 生物信息学

## 3 点简述
- 揭示传统DHC方法因使用集合导向准则导致树状图缺乏理想属性。
- 采用分布核替代集合准则，最大化总聚类相似度，理论保证下界。
- 在人工和空间转录组学数据集上验证有效性，优于其他方法。

## 摘要（原文）

> We uncover that current objective-based Divisive Hierarchical Clustering (DHC) methods produce a dendrogram that does not have three desired properties i.e., no unwarranted splitting, group similar clusters into a same subset, ground-truth correspondence. This shortcoming has their root cause in using a set-oriented bisecting assessment criterion. We show that this shortcoming can be addressed by using a distributional kernel, instead of the set-oriented criterion; and the resultant clusters achieve a new distribution-oriented objective to maximize the total similarity of all clusters (TSC). Our theoretical analysis shows that the resultant dendrogram guarantees a lower bound of TSC. The empirical evaluation shows the effectiveness of our proposed method on artificial and Spatial Transcriptomics (bioinformatics) datasets. Our proposed method successfully creates a dendrogram that is consistent with the biological regions in a Spatial Transcriptomics dataset, whereas other contenders fail.

