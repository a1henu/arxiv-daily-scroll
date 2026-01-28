---
layout: default
title: CollectiveKV: Decoupling and Sharing Collaborative Information in Sequential Recommendation
---

# CollectiveKV: Decoupling and Sharing Collaborative Information in Sequential Recommendation
**arXiv**：[2601.19178v1](https://arxiv.org/abs/2601.19178) · [PDF](https://arxiv.org/pdf/2601.19178.pdf)  
**作者**：Jingyu Li, Zhaocheng Du, Qianhui Zhu, kaiyuan Li, Zhicheng Zhang, Song-Li Wu, Chaolang Li, Pengwen Dai  

**一句话要点**：提出CollectiveKV以解决序列推荐中KV缓存存储开销大的问题

**关键词**：序列推荐, KV缓存, 跨用户共享, 存储压缩, 推理优化

## 3 点简述
- 序列推荐模型面临长序列延迟挑战，KV缓存虽降低推理延迟但引入高存储开销
- 通过SVD分析发现KV信息可分解为跨用户共享和用户特定部分，提出CollectiveKV机制
- 实验表明方法可将KV缓存压缩至原大小0.8%，同时保持或提升模型性能

## 摘要（原文）

> Sequential recommendation models are widely used in applications, yet they face stringent latency requirements. Mainstream models leverage the Transformer attention mechanism to improve performance, but its computational complexity grows with the sequence length, leading to a latency challenge for long sequences. Consequently, KV cache technology has recently been explored in sequential recommendation systems to reduce inference latency. However, KV cache introduces substantial storage overhead in sequential recommendation systems, which often have a large user base with potentially very long user history sequences. In this work, we observe that KV sequences across different users exhibit significant similarities, indicating the existence of collaborative signals in KV. Furthermore, we analyze the KV using singular value decomposition (SVD) and find that the information in KV can be divided into two parts: the majority of the information is shareable across users, while a small portion is user-specific. Motivated by this, we propose CollectiveKV, a cross-user KV sharing mechanism. It captures the information shared across users through a learnable global KV pool. During inference, each user retrieves high-dimensional shared KV from the pool and concatenates them with low-dimensional user-specific KV to obtain the final KV. Experiments on five sequential recommendation models and three datasets show that our method can compress the KV cache to only 0.8% of its original size, while maintaining or even enhancing model performance.

