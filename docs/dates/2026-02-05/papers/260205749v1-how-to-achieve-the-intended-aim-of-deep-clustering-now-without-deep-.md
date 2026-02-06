---
layout: default
title: How to Achieve the Intended Aim of Deep Clustering Now, without Deep Learning
---

# How to Achieve the Intended Aim of Deep Clustering Now, without Deep Learning
**arXiv**：[2602.05749v1](https://arxiv.org/abs/2602.05749) · [PDF](https://arxiv.org/pdf/2602.05749.pdf)  
**作者**：Kai Ming Ting, Wei-Jie Xu, Hang Zhang  

**一句话要点**：揭示非深度学习方法通过利用分布信息实现深度聚类的目标

**关键词**：深度聚类, k-means限制, 分布信息, 非深度学习, 簇发现, 数据表示

## 3 点简述
- 核心问题：深度聚类是否克服了k-means无法发现任意形状、大小和密度簇的根本限制
- 方法要点：分析深度嵌入聚类，发现其未利用底层数据分布，提出非深度学习方法利用簇的分布信息
- 实验或效果：非深度学习方法有效解决了k-means的根本限制，实现了深度聚类的预期目标

## 摘要（原文）

> Deep clustering (DC) is often quoted to have a key advantage over $k$-means clustering. Yet, this advantage is often demonstrated using image datasets only, and it is unclear whether it addresses the fundamental limitations of $k$-means clustering. Deep Embedded Clustering (DEC) learns a latent representation via an autoencoder and performs clustering based on a $k$-means-like procedure, while the optimization is conducted in an end-to-end manner. This paper investigates whether the deep-learned representation has enabled DEC to overcome the known fundamental limitations of $k$-means clustering, i.e., its inability to discover clusters of arbitrary shapes, varied sizes and densities. Our investigations on DEC have a wider implication on deep clustering methods in general. Notably, none of these methods exploit the underlying data distribution. We uncover that a non-deep learning approach achieves the intended aim of deep clustering by making use of distributional information of clusters in a dataset to effectively address these fundamental limitations.

