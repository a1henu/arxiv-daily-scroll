---
layout: default
title: SPAD: Seven-Source Token Probability Attribution with Syntactic Aggregation for Detecting Hallucinations in RAG
---

# SPAD: Seven-Source Token Probability Attribution with Syntactic Aggregation for Detecting Hallucinations in RAG
**arXiv**：[2512.07515v1](https://arxiv.org/abs/2512.07515) · [PDF](https://arxiv.org/pdf/2512.07515.pdf)  
**作者**：Pengqian Lu, Jie Lu, Anjin Liu, Guangquan Zhang  

**一句话要点**：提出SPAD方法，通过七源概率归因与句法聚合检测RAG中的幻觉

**关键词**：检索增强生成, 幻觉检测, 概率归因, 句法聚合, 令牌生成分析

## 3 点简述
- 核心问题：现有方法将幻觉归因于内部知识与检索上下文间的二元冲突，忽略其他生成组件的影响。
- 方法要点：将每个令牌的概率归因到七个来源，并通过词性聚合分数以识别异常贡献。
- 实验或效果：广泛实验显示SPAD在检测幻觉方面达到最先进性能。

## 摘要（原文）

> Detecting hallucinations in Retrieval-Augmented Generation (RAG) remains a challenge. Prior approaches attribute hallucinations to a binary conflict between internal knowledge (stored in FFNs) and retrieved context. However, this perspective is incomplete, failing to account for the impact of other components in the generative process, such as the user query, previously generated tokens, the current token itself, and the final LayerNorm adjustment. To address this, we introduce SPAD. First, we mathematically attribute each token's probability into seven distinct sources: Query, RAG, Past, Current Token, FFN, Final LayerNorm, and Initial Embedding. This attribution quantifies how each source contributes to the generation of the current token. Then, we aggregate these scores by POS tags to quantify how different components drive specific linguistic categories. By identifying anomalies, such as Nouns relying on Final LayerNorm, SPAD effectively detects hallucinations. Extensive experiments demonstrate that SPAD achieves state-of-the-art performance

