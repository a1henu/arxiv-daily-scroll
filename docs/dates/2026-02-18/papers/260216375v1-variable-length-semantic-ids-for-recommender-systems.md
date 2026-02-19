---
layout: default
title: Variable-Length Semantic IDs for Recommender Systems
---

# Variable-Length Semantic IDs for Recommender Systems
**arXiv**：[2602.16375v1](https://arxiv.org/abs/2602.16375) · [PDF](https://arxiv.org/pdf/2602.16375.pdf)  
**作者**：Kirill Khrylchenko  

**一句话要点**：提出变长语义标识符以解决推荐系统中生成模型训练困难与词汇鸿沟问题

**关键词**：推荐系统, 语义标识符, 变分自编码器, Gumbel-Softmax, 离散表示学习

## 3 点简述
- 核心问题：固定长度语义标识符效率低，与自然语言不匹配，忽略物品频率差异。
- 方法要点：基于离散变分自编码器与Gumbel-Softmax重参数化，学习自适应长度的物品表示。
- 实验或效果：未知，论文未提供具体实验细节或效果数据。

## 摘要（原文）

> Generative models are increasingly used in recommender systems, both for modeling user behavior as event sequences and for integrating large language models into recommendation pipelines. A key challenge in this setting is the extremely large cardinality of item spaces, which makes training generative models difficult and introduces a vocabulary gap between natural language and item identifiers. Semantic identifiers (semantic IDs), which represent items as sequences of low-cardinality tokens, have recently emerged as an effective solution to this problem.
>   However, existing approaches generate semantic identifiers of fixed length, assigning the same description length to all items. This is inefficient, misaligned with natural language, and ignores the highly skewed frequency structure of real-world catalogs, where popular items and rare long-tail items exhibit fundamentally different information requirements. In parallel, the emergent communication literature studies how agents develop discrete communication protocols, often producing variable-length messages in which frequent concepts receive shorter descriptions. Despite the conceptual similarity, these ideas have not been systematically adopted in recommender systems.
>   In this work, we bridge recommender systems and emergent communication by introducing variable-length semantic identifiers for recommendation. We propose a discrete variational autoencoder with Gumbel-Softmax reparameterization that learns item representations of adaptive length under a principled probabilistic framework, avoiding the instability of REINFORCE-based training and the fixed-length constraints of prior semantic ID methods.

