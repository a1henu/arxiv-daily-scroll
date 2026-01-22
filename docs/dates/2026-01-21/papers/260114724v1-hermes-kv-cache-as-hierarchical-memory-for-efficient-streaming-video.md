---
layout: default
title: HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding
---

# HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding
**arXiv**：[2601.14724v1](https://arxiv.org/abs/2601.14724) · [PDF](https://arxiv.org/pdf/2601.14724.pdf)  
**作者**：Haowei Zhang, Shudong Yang, Jinlan Fu, See-Kiong Ng, Xipeng Qiu  

**一句话要点**：提出HERMES架构，将KV缓存作为分层内存，以高效处理流式视频理解任务。

**关键词**：流式视频理解, KV缓存, 分层内存, 多模态大语言模型, 实时推理

## 3 点简述
- 核心问题：现有MLLMs在流式视频输入下难以兼顾性能、实时响应和低内存开销。
- 方法要点：基于注意力机制分析，将KV缓存设计为多粒度分层内存，重用紧凑缓存以提升效率。
- 实验或效果：在减少视频令牌达68%时，准确率保持领先或相当，TTFT提升10倍，内存开销降低。

## 摘要（原文）

> Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated significant improvement in offline video understanding. However, extending these capabilities to streaming video inputs, remains challenging, as existing models struggle to simultaneously maintain stable understanding performance, real-time responses, and low GPU memory overhead. To address this challenge, we propose HERMES, a novel training-free architecture for real-time and accurate understanding of video streams. Based on a mechanistic attention investigation, we conceptualize KV cache as a hierarchical memory framework that encapsulates video information across multiple granularities. During inference, HERMES reuses a compact KV cache, enabling efficient streaming understanding under resource constraints. Notably, HERMES requires no auxiliary computations upon the arrival of user queries, thereby guaranteeing real-time responses for continuous video stream interactions, which achieves 10$\times$ faster TTFT compared to prior SOTA. Even when reducing video tokens by up to 68% compared with uniform sampling, HERMES achieves superior or comparable accuracy across all benchmarks, with up to 11.4% gains on streaming datasets.

