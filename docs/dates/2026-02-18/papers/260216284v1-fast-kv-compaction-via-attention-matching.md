---
layout: default
title: Fast KV Compaction via Attention Matching
---

# Fast KV Compaction via Attention Matching
**arXiv**：[2602.16284v1](https://arxiv.org/abs/2602.16284) · [PDF](https://arxiv.org/pdf/2602.16284.pdf)  
**作者**：Adam Zweiger, Xinghong Fu, Han Guo, Yoon Kim  

**一句话要点**：提出注意力匹配方法以快速压缩KV缓存，解决长上下文语言模型部署中的性能瓶颈。

**关键词**：KV缓存压缩, 注意力匹配, 长上下文语言模型, 潜在空间优化, 快速部署

## 3 点简述
- 核心问题：长上下文语言模型部署中，KV缓存大小成为瓶颈，传统token空间压缩方法损失性能。
- 方法要点：通过注意力匹配在潜在空间构建紧凑KV，以每头级别保留注意力输出和质量。
- 实验或效果：实现高达50倍快速压缩，在部分数据集上秒级完成且性能损失小。

## 摘要（原文）

> Scaling language models to long contexts is often bottlenecked by the size of the key-value (KV) cache. In deployed settings, long contexts are typically managed through compaction in token space via summarization. However, summarization can be highly lossy, substantially harming downstream performance. Recent work on Cartridges has shown that it is possible to train highly compact KV caches in latent space that closely match full-context performance, but at the cost of slow and expensive end-to-end optimization. This work describes an approach for fast context compaction in latent space through Attention Matching, which constructs compact keys and values to reproduce attention outputs and preserve attention mass at a per-KV-head level. We show that this formulation naturally decomposes into simple subproblems, some of which admit efficient closed-form solutions. Within this framework, we develop a family of methods that significantly push the Pareto frontier of compaction time versus quality, achieving up to 50x compaction in seconds on some datasets with little quality loss.

