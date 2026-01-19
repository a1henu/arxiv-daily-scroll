---
layout: default
title: Clustering High-dimensional Data: Balancing Abstraction and Representation Tutorial at AAAI 2026
---

# Clustering High-dimensional Data: Balancing Abstraction and Representation Tutorial at AAAI 2026
**arXiv**：[2601.11160v1](https://arxiv.org/abs/2601.11160) · [PDF](https://arxiv.org/pdf/2601.11160.pdf)  
**作者**：Claudia Plant, Lena G. M. Bauer, Christian Böhm  

**一句话要点**：探讨高维数据聚类中抽象与表示的平衡，以提升聚类性能与可解释性

**关键词**：高维数据聚类, 抽象与表示平衡, 子空间聚类, 深度聚类, 聚类损失, 可解释性

## 3 点简述
- 核心问题：高维数据聚类需平衡抽象（忽略冗余细节）与表示（突出关键特征）以找到自然分组
- 方法要点：比较K-means、子空间聚类和深度聚类，通过聚类损失强制抽象，避免仅学习表示
- 实验或效果：未来方法将自适应平衡抽象与表示，提高性能、能效和可解释性，借鉴人脑机制

## 摘要（原文）

> How to find a natural grouping of a large real data set? Clustering requires a balance between abstraction and representation. To identify clusters, we need to abstract from superfluous details of individual objects. But we also need a rich representation that emphasizes the key features shared by groups of objects that distinguish them from other groups of objects.
>   Each clustering algorithm implements a different trade-off between abstraction and representation. Classical K-means implements a high level of abstraction - details are simply averaged out - combined with a very simple representation - all clusters are Gaussians in the original data space. We will see how approaches to subspace and deep clustering support high-dimensional and complex data by allowing richer representations. However, with increasing representational expressiveness comes the need to explicitly enforce abstraction in the objective function to ensure that the resulting method performs clustering and not just representation learning. We will see how current deep clustering methods define and enforce abstraction through centroid-based and density-based clustering losses. Balancing the conflicting goals of abstraction and representation is challenging. Ideas from subspace clustering help by learning one latent space for the information that is relevant to clustering and another latent space to capture all other information in the data.
>   The tutorial ends with an outlook on future research in clustering. Future methods will more adaptively balance abstraction and representation to improve performance, energy efficiency and interpretability. By automatically finding the sweet spot between abstraction and representation, the human brain is very good at clustering and other related tasks such as single-shot learning. So, there is still much room for improvement.

