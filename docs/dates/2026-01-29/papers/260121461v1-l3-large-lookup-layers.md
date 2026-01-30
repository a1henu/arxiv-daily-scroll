---
layout: default
title: L$^3$: Large Lookup Layers
---

# L$^3$: Large Lookup Layers
**arXiv**：[2601.21461v1](https://arxiv.org/abs/2601.21461) · [PDF](https://arxiv.org/pdf/2601.21461.pdf)  
**作者**：Albert Tseng, Christopher De Sa  

**一句话要点**：提出大型查找层（L³）以在稀疏语言模型中实现静态路由，提升效率与性能。

**关键词**：稀疏语言模型, 静态路由, 嵌入表, 硬件效率, 信息论分配, Transformer训练

## 3 点简述
- 核心问题：稀疏语言模型中动态路由（如MoE）存在硬件效率低和训练不稳定问题。
- 方法要点：L³层通过静态基于令牌的路由，在上下文中聚合学习嵌入，平衡内存与计算。
- 实验或效果：在语言建模和下游任务中，L³优于密集模型和等稀疏MoE，训练参数达2.6B。

## 摘要（原文）

> Modern sparse language models typically achieve sparsity through Mixture-of-Experts (MoE) layers, which dynamically route tokens to dense MLP "experts." However, dynamic hard routing has a number of drawbacks, such as potentially poor hardware efficiency and needing auxiliary losses for stable training. In contrast, the tokenizer embedding table, which is natively sparse, largely avoids these issues by selecting a single embedding per token at the cost of not having contextual information. In this work, we introduce the Large Lookup Layer (L$^3$), which unlocks a new axis of sparsity by generalizing embedding tables to model decoder layers. L$^3$ layers use static token-based routing to aggregate a set of learned embeddings per token in a context-dependent way, allowing the model to efficiently balance memory and compute by caching information in embeddings. L$^3$ has two main components: (1) a systems-friendly architecture that allows for fast training and CPU-offloaded inference with no overhead, and (2) an information-theoretic embedding allocation algorithm that effectively balances speed and quality. We empirically test L$^3$ by training transformers with up to 2.6B active parameters and find that L$^3$ strongly outperforms both dense models and iso-sparse MoEs in both language modeling and downstream tasks.

