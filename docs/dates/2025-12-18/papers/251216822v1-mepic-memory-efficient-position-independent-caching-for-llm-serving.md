---
layout: default
title: MEPIC: Memory Efficient Position Independent Caching for LLM Serving
---

# MEPIC: Memory Efficient Position Independent Caching for LLM Serving
**arXiv**：[2512.16822v1](https://arxiv.org/abs/2512.16822) · [PDF](https://arxiv.org/pdf/2512.16822.pdf)  
**作者**：Qian Wang, Zahra Yousefijamarani, Morgan Lindsay Heisler, Rongzhi Gu, Bai Xiaolong, Shan Yizhou, Wei Zhang, Wang Lan, Ying Xiong, Yong Zhang, Zhenan Fan  

**一句话要点**：提出MEPIC系统以解决LLM服务中KV缓存内存效率低的问题，实现跨位置和请求的块级重用。

**关键词**：KV缓存优化, 位置无关缓存, 内存效率, LLM服务, RoPE融合, 块级重用

## 3 点简述
- 核心问题：LLM应用中长提示历史导致KV缓存内存压力大，现有位置无关缓存因查询差异和内存布局不齐而重用有限。
- 方法要点：通过页对齐存储、块级重计算和RoPE融合，使块KV在内存中可跨请求共享，消除重复。
- 实验或效果：在可比延迟和精度下，HBM使用减少达2倍，长提示场景下可达5倍，无需模型修改。

## 摘要（原文）

> Modern LLM applications such as deep-research assistants, coding agents, and Retrieval-Augmented Generation (RAG) systems, repeatedly process long prompt histories containing shared document or code chunks, creating significant pressure on the Key Value (KV) cache, which must operate within limited memory while sustaining high throughput and low latency. Prefix caching partially alleviates some of these costs by reusing KV cache for previously processed tokens, but limited by strict prefix matching. Position-independent caching (PIC) enables chunk-level reuse at arbitrary positions, but requires selective recomputation and positional-encoding (PE) adjustments. However, because these operations vary across queries, KV for the same chunk diverges across requests. Moreover, without page alignment, chunk KV layouts diverge in memory, preventing page sharing. These issues result in only modest HBM savings even when many requests reuse the same content.
>   We present MEPIC, a memory-efficient PIC system that enables chunk KV reuse across positions, requests, and batches. MEPIC aligns chunk KV to paged storage, shifts recomputation from token- to block-level so only the first block is request-specific, removes positional encodings via Rotary Position Embedding (RoPE) fusion in the attention kernel, and makes remaining blocks fully shareable. These techniques eliminate most duplicate chunk KV in HBM, reducing usage by up to 2x over state-of-the-art PIC at comparable latency and accuracy, and up to 5x for long prompts, without any model changes.

