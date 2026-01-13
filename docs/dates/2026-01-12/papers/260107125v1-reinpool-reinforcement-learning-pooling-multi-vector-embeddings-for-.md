---
layout: default
title: ReinPool: Reinforcement Learning Pooling Multi-Vector Embeddings for Retrieval System
---

# ReinPool: Reinforcement Learning Pooling Multi-Vector Embeddings for Retrieval System
**arXiv**：[2601.07125v1](https://arxiv.org/abs/2601.07125) · [PDF](https://arxiv.org/pdf/2601.07125.pdf)  
**作者**：Sungguk Cha, DongWook Kim, Mintae Kim, Youngsub Han, Byoung-Ki Jeon, Sangyeob Lee  

**一句话要点**：提出ReinPool强化学习框架，动态池化多向量嵌入以解决检索系统存储成本高的问题。

**关键词**：多向量嵌入, 强化学习池化, 检索系统优化, 视觉语言模型, 压缩表示

## 3 点简述
- 多向量嵌入模型存储成本高，索引大小增加超1000倍，限制可扩展性。
- 使用强化学习动态过滤和池化嵌入，基于逆检索目标和NDCG奖励优化表示。
- 在Vidore V2基准上压缩746-1249倍，恢复76-81%性能，NDCG@3提升22-33%。

## 摘要（原文）

> Multi-vector embedding models have emerged as a powerful paradigm for document retrieval, preserving fine-grained visual and textual details through token-level representations. However, this expressiveness comes at a staggering cost: storing embeddings for every token inflates index sizes by over $1000\times$ compared to single-vector approaches, severely limiting scalability. We introduce \textbf{ReinPool}, a reinforcement learning framework that learns to dynamically filter and pool multi-vector embeddings into compact, retrieval-optimized representations. By training with an inverse retrieval objective and NDCG-based rewards, ReinPool identifies and retains only the most discriminative vectors without requiring manual importance annotations. On the Vidore V2 benchmark across three vision-language embedding models, ReinPool compresses multi-vector representations by $746$--$1249\times$ into single vectors while recovering 76--81\% of full multi-vector retrieval performance. Compared to static mean pooling baselines, ReinPool achieves 22--33\% absolute NDCG@3 improvement, demonstrating that learned selection significantly outperforms heuristic aggregation.

