---
layout: default
title: Enhancing Retrieval-Augmented Generation with Entity Linking for Educational Platforms
---

# Enhancing Retrieval-Augmented Generation with Entity Linking for Educational Platforms
**arXiv**：[2512.05967v1](https://arxiv.org/abs/2512.05967) · [PDF](https://arxiv.org/pdf/2512.05967.pdf)  
**作者**：Francesco Granata, Francesco Poggi, Misael Mongiovì  

**一句话要点**：提出集成实体链接的增强RAG架构，以提升意大利教育平台问答的事实准确性。

**关键词**：检索增强生成, 实体链接, 教育问答系统, 重排序策略, 领域适应, 事实准确性

## 3 点简述
- 核心问题：基于语义相似性的RAG在专业领域因术语歧义影响检索相关性和事实准确性。
- 方法要点：整合基于Wikidata的实体链接模块，采用混合评分、互逆排名融合和交叉编码器三种重排序策略。
- 实验或效果：在特定领域数据集上，互逆排名融合策略显著优于基线，交叉编码器在通用数据集表现最佳。

## 摘要（原文）

> In the era of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) architectures are gaining significant attention for their ability to ground language generation in reliable knowledge sources. Despite their impressive effectiveness in many areas, RAG systems based solely on semantic similarity often fail to ensure factual accuracy in specialized domains, where terminological ambiguity can affect retrieval relevance. This study proposes an enhanced RAG architecture that integrates a factual signal derived from Entity Linking to improve the accuracy of educational question-answering systems in Italian. The system includes a Wikidata-based Entity Linking module and implements three re-ranking strategies to combine semantic and entity-based information: a hybrid score weighting model, reciprocal rank fusion, and a cross-encoder re-ranker. Experiments were conducted on two benchmarks: a custom academic dataset and the standard SQuAD-it dataset. Results show that, in domain-specific contexts, the hybrid schema based on reciprocal rank fusion significantly outperforms both the baseline and the cross-encoder approach, while the cross-encoder achieves the best results on the general-domain dataset. These findings confirm the presence of an effect of domain mismatch and highlight the importance of domain adaptation and hybrid ranking strategies to enhance factual precision and reliability in retrieval-augmented generation. They also demonstrate the potential of entity-aware RAG systems in educational environments, fostering adaptive and reliable AI-based tutoring tools.

