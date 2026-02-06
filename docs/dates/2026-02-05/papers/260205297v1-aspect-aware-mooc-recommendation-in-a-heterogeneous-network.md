---
layout: default
title: Aspect-Aware MOOC Recommendation in a Heterogeneous Network
---

# Aspect-Aware MOOC Recommendation in a Heterogeneous Network
**arXiv**：[2602.05297v1](https://arxiv.org/abs/2602.05297) · [PDF](https://arxiv.org/pdf/2602.05297.pdf)  
**作者**：Seongyeub Chu, Jongwoo Kim, Mun Yong Yi  

**一句话要点**：提出AMR框架，通过自动发现元路径和嵌入语义内容，解决MOOC推荐中数据稀疏和元路径依赖问题。

**关键词**：MOOC推荐, 异质网络, 元路径发现, 方面感知表示, 图神经网络, 语义嵌入

## 3 点简述
- 核心问题：传统MOOC推荐方法存在数据稀疏和过度依赖手动定义元路径，导致推荐效果受限。
- 方法要点：AMR自动发现元路径，使用bi-LSTM编码器生成方面感知路径表示，并融入子图特征进行细粒度推荐。
- 实验或效果：在MOOCCube和PEEK数据集上，AMR在HR@K和nDCG@K等指标上优于现有图神经网络基线。

## 摘要（原文）

> MOOC recommendation systems have received increasing attention to help learners navigate and select preferred learning content. Traditional methods such as collaborative filtering and content-based filtering suffer from data sparsity and over-specialization. To alleviate these limitations, graph-based approaches have been proposed; however, they still rely heavily on manually predefined metapaths, which often capture only superficial structural relationships and impose substantial burdens on domain experts as well as significant engineering costs. To overcome these limitations, we propose AMR (Aspect-aware MOOC Recommendation), a novel framework that models path-specific multiple aspects by embedding the semantic content of nodes within each metapath. AMR automatically discovers metapaths through bi-directional walks, derives aspect-aware path representations using a bi-LSTM-based encoder, and incorporates these representations as edge features in the learner-learner and KC-KC subgraphs to achieve fine-grained semantically informed KC recommendations. Extensive experiments on the large-scale MOOCCube and PEEK datasets show that AMR consistently outperforms state-of-the-art graph neural network baselines across key metrics such as HR@K and nDCG@K. Further analysis confirms that AMR effectively captures rich path-specific aspect information, allowing more accurate recommendations than those methods that rely solely on predefined metapaths. The code will be available upon accepted.

