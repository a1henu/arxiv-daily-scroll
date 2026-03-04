---
layout: default
title: AlphaFree: Recommendation Free from Users, IDs, and GNNs
---

# AlphaFree: Recommendation Free from Users, IDs, and GNNs
**arXiv**：[2603.02653v1](https://arxiv.org/abs/2603.02653) · [PDF](https://arxiv.org/pdf/2603.02653.pdf)  
**作者**：Minseo Jeon, Junwoo Jung, Daewon Gwak, Jinhong Jung  

**一句话要点**：提出AlphaFree推荐方法，无需用户嵌入、原始ID和图神经网络，以解决内存成本高、冷启动和泛化差问题。

**关键词**：推荐系统, 语言表示, 对比学习, 冷启动问题, 内存优化, 协同过滤

## 3 点简述
- 核心问题：现有推荐系统依赖用户嵌入、原始ID和图神经网络，导致高内存、冷启动和泛化限制。
- 方法要点：通过动态推断偏好、语言表示替代ID、对比学习捕获协同信号，实现用户、ID和GNN无关设计。
- 实验或效果：在真实数据集上优于基线，提升达40%，GPU内存减少达69%，验证有效性。

## 摘要（原文）

> Can we design effective recommender systems free from users, IDs, and GNNs? Recommender systems are central to personalized content delivery across domains, with top-K item recommendation being a fundamental task to retrieve the most relevant items from historical interactions. Existing methods rely on entrenched design conventions, often adopted without reconsideration, such as storing per-user embeddings (user-dependent), initializing features from raw IDs (ID-dependent), and employing graph neural networks (GNN-dependent). These dependencies incur several limitations, including high memory costs, cold-start and over-smoothing issues, and poor generalization to unseen interactions.
>   In this work, we propose AlphaFree, a novel recommendation method free from users, IDs, and GNNs. Our main ideas are to infer preferences on-the-fly without user embeddings (user-free), replace raw IDs with language representations (LRs) from pre-trained language models (ID-free), and capture collaborative signals through augmentation with similar items and contrastive learning, without GNNs (GNN-free). Extensive experiments on various real-world datasets show that AlphaFree consistently outperforms its competitors, achieving up to around 40% improvements over non-LR-based methods and up to 5.7% improvements over LR-based methods, while significantly reducing GPU memory usage by up to 69% under high-dimensional LRs.

