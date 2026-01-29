---
layout: default
title: Memory Retrieval in Transformers: Insights from The Encoding Specificity Principle
---

# Memory Retrieval in Transformers: Insights from The Encoding Specificity Principle
**arXiv**：[2601.20282v1](https://arxiv.org/abs/2601.20282) · [PDF](https://arxiv.org/pdf/2601.20282.pdf)  
**作者**：Viet Hung Dinh, Ming Ding, Youyang Qu, Kanchana Thilakarathna  

**一句话要点**：基于编码特异性原则，揭示Transformer注意力层中关键词作为线索的记忆检索机制

**关键词**：Transformer注意力机制, 记忆检索, 编码特异性原则, 可解释人工智能, 机器遗忘, 神经元激活分析

## 3 点简述
- 核心问题：Transformer注意力层在LLMs中的具体记忆机制尚不明确，需结合心理学原理深入探索
- 方法要点：借鉴编码特异性原则，提出关键词作为检索线索的假设，并通过神经元激活分析验证
- 实验或效果：从注意力层神经元中提取关键词，应用于下游任务如机器遗忘，提供可解释性证据

## 摘要（原文）

> While explainable artificial intelligence (XAI) for large language models (LLMs) remains an evolving field with many unresolved questions, increasing regulatory pressures have spurred interest in its role in ensuring transparency, accountability, and privacy-preserving machine unlearning. Despite recent advances in XAI have provided some insights, the specific role of attention layers in transformer based LLMs remains underexplored. This study investigates the memory mechanisms instantiated by attention layers, drawing on prior research in psychology and computational psycholinguistics that links Transformer attention to cue based retrieval in human memory. In this view, queries encode the retrieval context, keys index candidate memory traces, attention weights quantify cue trace similarity, and values carry the encoded content, jointly enabling the construction of a context representation that precedes and facilitates memory retrieval. Guided by the Encoding Specificity Principle, we hypothesize that the cues used in the initial stage of retrieval are instantiated as keywords. We provide converging evidence for this keywords-as-cues hypothesis. In addition, we isolate neurons within attention layers whose activations selectively encode and facilitate the retrieval of context-defining keywords. Consequently, these keywords can be extracted from identified neurons and further contribute to downstream applications such as unlearning.

