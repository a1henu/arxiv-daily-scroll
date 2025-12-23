---
layout: default
title: MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning
---

# MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning
**arXiv**：[2512.19206v1](https://arxiv.org/abs/2512.19206) · [PDF](https://arxiv.org/pdf/2512.19206.pdf)  
**作者**：Tao Zhang, Ziqian Zeng, Hao Peng, Huiping Zhuang, Cen Chen  

**一句话要点**：提出MixKVQ以解决长上下文推理中KV缓存量化性能下降问题

**关键词**：KV缓存量化, 长上下文推理, 混合精度, 查询感知, 内存优化, 大语言模型

## 3 点简述
- 核心问题：现有低比特KV缓存量化方法在复杂推理任务中性能下降严重，固定精度量化难以处理关键缓存中的异常通道。
- 方法要点：基于关键通道量化难度和查询相关性，设计轻量级查询感知算法，识别并保留高精度关键通道，同时对值缓存进行逐令牌量化。
- 实验或效果：在复杂推理数据集上，MixKVQ显著优于现有低比特方法，在减少内存占用下达到全精度基线可比性能。

## 摘要（原文）

> Long Chain-of-Thought (CoT) reasoning has significantly advanced the capabilities of Large Language Models (LLMs), but this progress is accompanied by substantial memory and latency overhead from the extensive Key-Value (KV) cache. Although KV cache quantization is a promising compression technique, existing low-bit quantization methods often exhibit severe performance degradation on complex reasoning tasks. Fixed-precision quantization struggles to handle outlier channels in the key cache, while current mixed-precision strategies fail to accurately identify components requiring high-precision representation. We find that an effective low-bit KV cache quantization strategy must consider two factors: a key channel's intrinsic quantization difficulty and its relevance to the query. Based on this insight, we propose MixKVQ, a novel plug-and-play method that introduces a lightweight, query-aware algorithm to identify and preserve critical key channels that need higher precision, while applying per-token quantization for value cache. Experiments on complex reasoning datasets demonstrate that our approach significantly outperforms existing low-bit methods, achieving performance comparable to a full-precision baseline at a substantially reduced memory footprint.

