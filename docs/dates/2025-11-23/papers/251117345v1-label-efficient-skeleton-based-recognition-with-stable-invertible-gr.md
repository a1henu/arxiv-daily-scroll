---
layout: default
title: Label-Efficient Skeleton-based Recognition with Stable-Invertible Graph Convolutional Networks
---

# Label-Efficient Skeleton-based Recognition with Stable-Invertible Graph Convolutional Networks
**arXiv**：[2511.17345v1](https://arxiv.org/abs/2511.17345) · [PDF](https://arxiv.org/pdf/2511.17345.pdf)  
**作者**：Hichem Sahbi  

**一句话要点**：提出稳定可逆图卷积网络以解决骨架动作识别中的标签效率问题

**关键词**：骨架动作识别, 图卷积网络, 标签效率, 可逆网络, 数据采集函数

## 3 点简述
- 核心问题：骨架动作识别依赖大量手动标注数据，获取成本高且耗时。
- 方法要点：学习新颖采集函数，优化数据代表性、多样性和不确定性，并使用可逆GCN映射数据。
- 实验或效果：在两个挑战性数据集上验证，方法优于相关工作，实现标签高效识别。

## 摘要（原文）

> Skeleton-based action recognition is a hotspot in image processing. A key challenge of this task lies in its dependence on large, manually labeled datasets whose acquisition is costly and time-consuming. This paper devises a novel, label-efficient method for skeleton-based action recognition using graph convolutional networks (GCNs). The contribution of the proposed method resides in learning a novel acquisition function -- scoring the most informative subsets for labeling -- as the optimum of an objective function mixing data representativity, diversity and uncertainty. We also extend this approach by learning the most informative subsets using an invertible GCN which allows mapping data from ambient to latent spaces where the inherent distribution of the data is more easily captured. Extensive experiments, conducted on two challenging skeleton-based recognition datasets, show the effectiveness and the outperformance of our label-frugal GCNs against the related work.

