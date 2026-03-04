---
layout: default
title: SUN: Shared Use of Next-token Prediction for Efficient Multi-LLM Disaggregated Serving
---

# SUN: Shared Use of Next-token Prediction for Efficient Multi-LLM Disaggregated Serving
**arXiv**：[2603.02599v1](https://arxiv.org/abs/2603.02599) · [PDF](https://arxiv.org/pdf/2603.02599.pdf)  
**作者**：Sunghyeon Woo, Ahreum Seo, Jaegwang Lee, Jaeeun Kil, Hanbae Seo, Joonghoon Kim, Baeseong Park, Se Jung Kwon, Dongsoo Lee  

**一句话要点**：提出SUN方法以解决多LLM服务中解码执行效率低下的问题

**关键词**：多模型LLM服务, 解码执行共享, Transformer分解, GPU利用率优化, 量化解码

## 3 点简述
- 核心问题：多模型LLM服务中，解码执行因模型特定资源分区导致GPU利用率低下，尤其在偏斜工作负载下。
- 方法要点：将仅解码器Transformer分解为预填充和解码模块，仅微调任务特定预填充模块，使冻结解码模块可跨模型共享。
- 实验或效果：SUN在保持准确性的同时，通过共享解码提高吞吐量，每GPU吞吐量提升高达2.0倍，TPOT保持在5%以内。

## 摘要（原文）

> In multi-model LLM serving, decode execution remains inefficient due to model-specific resource partitioning: since cross-model batching is not possible, memory-bound decoding often suffers from severe GPU underutilization, especially under skewed workloads. We propose Shared Use of Next-token Prediction (SUN), the first approach that enables cross-model sharing of decode execution in disaggregated multi-LLM serving. SUN decomposes a decoder-only Transformer into a prefill module and a decode module, and fine-tunes only the task-specific prefill module, enabling a frozen decode module to be shared across models. This design enables a model-agnostic decode routing policy that balances decode requests across shared workers to maximize utilization. Across diverse tasks and model families, SUN achieves accuracy comparable to full fine-tuning while maintaining system throughput with fewer decode workers. In particular, SUN improves throughput per GPU by up to 2.0x over conventional disaggregation while keeping time-per-output-token (TPOT) within 5%. SUN inherently enables and facilitates low-bit decoding; with Quantized SUN (QSUN), it achieves a 45% speedup with comparable accuracy to SUN while preserving the benefits of shared decoding.

