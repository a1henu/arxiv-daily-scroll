---
layout: default
title: A2RAG: Adaptive Agentic Graph Retrieval for Cost-Aware and Reliable Reasoning
---

# A2RAG: Adaptive Agentic Graph Retrieval for Cost-Aware and Reliable Reasoning
**arXiv**：[2601.21162v1](https://arxiv.org/abs/2601.21162) · [PDF](https://arxiv.org/pdf/2601.21162.pdf)  
**作者**：Jiate Liu, Zebin Chen, Shaobo Qiao, Mingchen Ju, Danting Zhang, Bocheng Han, Shuyue Yu, Xin Shu, Jingling Wu, Dong Wen, Xin Cao, Guanfeng Liu, Zhengyi Yang  

**一句话要点**：提出A2RAG自适应代理图检索框架，以解决图检索增强生成中的成本浪费和提取损失问题。

**关键词**：图检索增强生成, 自适应检索, 代理检索, 多跳问答, 成本优化, 提取损失缓解

## 3 点简述
- 核心问题：图检索增强生成面临混合难度查询导致成本浪费，以及图抽象忽略细粒度信息。
- 方法要点：结合自适应控制器验证证据充分性，代理检索器逐步提升检索努力并映射回源文本。
- 实验或效果：在HotpotQA和2WikiMultiHopQA上，Recall@2提升9.9/11.8，令牌消耗和延迟降低约50%。

## 摘要（原文）

> Graph Retrieval-Augmented Generation (Graph-RAG) enhances multihop question answering by organizing corpora into knowledge graphs and routing evidence through relational structure. However, practical deployments face two persistent bottlenecks: (i) mixed-difficulty workloads where one-size-fits-all retrieval either wastes cost on easy queries or fails on hard multihop cases, and (ii) extraction loss, where graph abstraction omits fine-grained qualifiers that remain only in source text. We present A2RAG, an adaptive-and-agentic GraphRAG framework for cost-aware and reliable reasoning. A2RAG couples an adaptive controller that verifies evidence sufficiency and triggers targeted refinement only when necessary, with an agentic retriever that progressively escalates retrieval effort and maps graph signals back to provenance text to remain robust under extraction loss and incomplete graphs. Experiments on HotpotQA and 2WikiMultiHopQA demonstrate that A2RAG achieves +9.9/+11.8 absolute gains in Recall@2, while cutting token consumption and end-to-end latency by about 50% relative to iterative multihop baselines.

