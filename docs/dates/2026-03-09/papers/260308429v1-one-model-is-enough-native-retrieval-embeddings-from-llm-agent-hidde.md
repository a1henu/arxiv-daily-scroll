---
layout: default
title: One Model Is Enough: Native Retrieval Embeddings from LLM Agent Hidden States
---

# One Model Is Enough: Native Retrieval Embeddings from LLM Agent Hidden States
**arXiv**：[2603.08429v1](https://arxiv.org/abs/2603.08429) · [PDF](https://arxiv.org/pdf/2603.08429.pdf)  
**作者**：Bo Jiang  

**一句话要点**：提出通过投影头从LLM隐藏状态直接生成检索嵌入，以简化检索型智能体架构。

**关键词**：LLM智能体, 检索嵌入, 隐藏状态投影, 对比学习, 排序蒸馏, QReCC基准

## 3 点简述
- 问题：LLM智能体检索外部知识时需额外嵌入模型，增加复杂性和延迟。
- 方法：添加轻量投影头，将LLM隐藏状态映射到嵌入空间，结合对齐、对比和排序蒸馏损失训练。
- 效果：在QReCC基准上保持97%检索质量，Recall@10和MRR@10与基线竞争。

## 摘要（原文）

> LLM agents that retrieve external knowledge typically generate a search query as text, then run a separate embedding model to encode it into a vector. This two-model pipeline adds infrastructure complexity and latency, yet is redundant: the LLM already encodes the full conversational context in its hidden states. We propose equipping LLM agents with native retrieval capability by adding a lightweight projection head that maps hidden states directly into the embedding space, eliminating the need for a separate embedding model. Trained with a combination of alignment, contrastive, and rank distillation losses, our method retains 97\% of baseline retrieval quality while enabling the LLM agent to search with its own representations. Experiments on the QReCC conversational search benchmark show competitive Recall@10 and MRR@10 compared to the standard generate-then-encode pipeline, with systematic ablations confirming the contribution of each loss component.

