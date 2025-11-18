---
layout: default
title: CacheFlow: Compressive Streaming Memory for Efficient Long-Form Video Understanding
---

# CacheFlow: Compressive Streaming Memory for Efficient Long-Form Video Understanding
**arXiv**：[2511.13644v1](https://arxiv.org/abs/2511.13644) · [PDF](https://arxiv.org/pdf/2511.13644.pdf)  
**作者**：Shrenik Patel, Daivik Patel  

**一句话要点**：提出CacheFlow以解决长视频问答中注意力与KV缓存增长导致的效率问题

**关键词**：长视频理解, 动态令牌丢弃, KV缓存压缩, 流式视频问答, 无需训练方法

## 3 点简述
- 核心问题：长视频问答中注意力机制和KV缓存随运行时间增长，导致推理成本高或视野受限
- 方法要点：结合动态令牌丢弃和压缩长期记忆，在线处理令牌并构建检索索引，无需训练
- 实验或效果：在离线与流式VQA基准测试中优于基线，处理令牌减少高达87%

## 摘要（原文）

> Long-form video question answering (VQA) overwhelms current vision-language models (VLMs) because attention and key-value (KV) caches grow with runtime, forcing either expensive inference or near-sighted sliding windows. We introduce CacheFlow, a training-free pipeline that pairs Dynamic Token Dropping (DTD) with a compressive long-term memory. DTD prunes per-patch tokens online via cosine similarity to the previous frame, and surviving tokens are packed into fixed-size blocks. This online, per-frame processing makes our approach fundamentally suited for live streaming VQA. As blocks are processed, each one's keys are summarized by a tiny recurrent encoder to form a retrieval index, while the block's full KV pairs are offloaded and later rehydrated for generation, preserving answer fidelity. At inference, a consensus-based retrieval mechanism retrieves only the Top-K most relevant blocks and attends over both the retrieved and local context for precise, long-range reasoning. CacheFlow is drop-in, architecture-agnostic, and requires no fine-tuning. Experiments on both offline and streaming VQA benchmarks demonstrate that CacheFlow outperforms current strong baselines, while processing up to 87% less tokens. Our dual approach enables VLMs to be both efficient and context-aware, paving the way for practical long-form video understanding.

