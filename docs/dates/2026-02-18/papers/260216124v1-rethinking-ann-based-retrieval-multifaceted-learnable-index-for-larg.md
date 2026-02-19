---
layout: default
title: Rethinking ANN-based Retrieval: Multifaceted Learnable Index for Large-scale Recommendation System
---

# Rethinking ANN-based Retrieval: Multifaceted Learnable Index for Large-scale Recommendation System
**arXiv**：[2602.16124v1](https://arxiv.org/abs/2602.16124) · [PDF](https://arxiv.org/pdf/2602.16124.pdf)  
**作者**：Jiang Zhang, Yubo Wang, Wei Chang, Lu Han, Xingying Cheng, Feng Zhang, Min Li, Songhao Jiang, Wei Zheng, Harry Tran, Zhen Wang, Lei Chen, Yueming Wang, Benyu Zhang, Xiangjun Fan, Bi Xue, Qifan Wang  

**一句话要点**：提出多面可学习索引以解决大规模推荐系统中近似最近邻检索的离线索引与在线计算成本问题。

**关键词**：近似最近邻检索, 大规模推荐系统, 可学习索引, 残差量化, 实时检索, 多面嵌入

## 3 点简述
- 核心问题：近似最近邻检索存在离线索引与嵌入学习分离导致质量次优，以及在线计算成本高的问题。
- 方法要点：通过残差量化构建多面分层码本，并与嵌入联合训练，实现统一框架下的实时检索。
- 实验或效果：在数十亿用户数据上，召回率提升达11.8%，冷内容交付提升57.29%，语义相关性提升13.5%。

## 摘要（原文）

> Approximate nearest neighbor (ANN) search is widely used in the retrieval stage of large-scale recommendation systems. In this stage, candidate items are indexed using their learned embedding vectors, and ANN search is executed for each user (or item) query to retrieve a set of relevant items. However, ANN-based retrieval has two key limitations. First, item embeddings and their indices are typically learned in separate stages: indexing is often performed offline after embeddings are trained, which can yield suboptimal retrieval quality-especially for newly created items. Second, although ANN offers sublinear query time, it must still be run for every request, incurring substantial computation cost at industry scale. In this paper, we propose MultiFaceted Learnable Index (MFLI), a scalable, real-time retrieval paradigm that learns multifaceted item embeddings and indices within a unified framework and eliminates ANN search at serving time. Specifically, we construct a multifaceted hierarchical codebook via residual quantization of item embeddings and co-train the codebook with the embeddings. We further introduce an efficient multifaceted indexing structure and mechanisms that support real-time updates. At serving time, the learned hierarchical indices are used directly to identify relevant items, avoiding ANN search altogether. Extensive experiments on real-world data with billions of users show that MFLI improves recall on engagement tasks by up to 11.8\%, cold-content delivery by up to 57.29\%, and semantic relevance by 13.5\% compared with prior state-of-the-art methods. We also deploy MFLI in the system and report online experimental results demonstrating improved engagement, less popularity bias, and higher serving efficiency.

