---
layout: default
title: Joint Encoding of KV-Cache Blocks for Scalable LLM Serving
---

# Joint Encoding of KV-Cache Blocks for Scalable LLM Serving
**arXiv**：[2601.03067v1](https://arxiv.org/abs/2601.03067) · [PDF](https://arxiv.org/pdf/2601.03067.pdf)  
**作者**：Joseph Kampeas, Emir Haleva  

**一句话要点**：提出KV缓存块联合编码方法以解决LLM服务中KV缓存内存瓶颈问题

**关键词**：KV缓存压缩, LLM服务优化, 联合编码, 内存效率, 推理吞吐量

## 3 点简述
- 核心问题：LLM服务中KV缓存内存占用大，限制高并发实时吞吐量
- 方法要点：跨请求和输入块融合相似KV缓存块为共享表示，保持标准缓存结构
- 实验或效果：实现最高4.38倍压缩，单机vLLM基准测试中令牌吞吐量提升约40%

## 摘要（原文）

> Modern large language models (LLMs) drive interactive AI systems but are bottlenecked by the memory-heavy growth of key-value (KV) caches, which limits real-time throughput under concurrent loads. Existing KV-cache compression methods rely on rigid heuristics, disrupt tensor layouts, or require specialized compute, hindering scalability and deployment.
>   We propose joint encoding of KV-cache blocks, which fuses similar blocks across requests and input chunks into shared representations while preserving standard cache structure. This alleviates the KV-cache memory bottleneck, supporting high-concurrency serving without specialized hardware. Theoretically, we analyze the rate-distortion tradeoff of fused cache blocks under a Poisson process model. Empirically, our method achieves up to 4.38 $\times$ KV-cache compression with negligible accuracy loss across diverse LLMs and benchmarks, outperforming recent structured and adaptive compression baselines. In real LLM serving, joint encoding improves the token throughput by $\sim$40\% on a single-machine vLLM benchmark, demonstrating substantial gains in inference throughput. Code is available at https://github.com/sef1/kv_fast_fusion  kv_joint_encoding.

