---
layout: default
title: SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning
---

# SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning
**arXiv**：[2602.22603v1](https://arxiv.org/abs/2602.22603) · [PDF](https://arxiv.org/pdf/2602.22603.pdf)  
**作者**：Sanjay Kariyappa, G. Edward Suh  

**一句话要点**：提出SideQuest模型驱动KV缓存管理方法，以解决长程智能体推理中的内存增长问题。

**关键词**：KV缓存压缩, 长程智能体推理, 模型驱动管理, 并行任务, 内存优化

## 3 点简述
- 核心问题：长程智能体任务中，外部检索令牌导致KV缓存内存快速增长，影响解码性能。
- 方法要点：利用大型推理模型自身进行KV缓存压缩，通过并行辅助任务避免污染主推理内存。
- 实验或效果：仅用215样本训练，在智能体任务中减少峰值令牌使用达65%，精度损失小。

## 摘要（原文）

> Long-running agentic tasks, such as deep research, require multi-hop reasoning over information distributed across multiple webpages and documents. In such tasks, the LLM context is dominated by tokens from external retrieval, causing memory usage to grow rapidly and limiting decode performance. While several KV cache compression techniques exist for long-context inputs, we find that existing heuristics fail to support multi-step reasoning models effectively. We address this challenge with SideQuest -- a novel approach that leverages the Large Reasoning Model (LRM) itself to perform KV cache compression by reasoning about the usefulness of tokens in its context. To prevent the tokens associated with this management process from polluting the model's memory, we frame KV cache compression as an auxiliary task executed in parallel to the main reasoning task. Our evaluations, using a model trained with just 215 samples, show that SideQuest reduces peak token usage by up to 65% on agentic tasks with minimal degradation in accuracy, outperforming heuristic-based KV cache compression techniques.

