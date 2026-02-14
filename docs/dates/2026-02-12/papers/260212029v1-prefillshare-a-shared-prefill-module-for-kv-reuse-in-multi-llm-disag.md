---
layout: default
title: PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving
---

# PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving
**arXiv**：[2602.12029v1](https://arxiv.org/abs/2602.12029) · [PDF](https://arxiv.org/pdf/2602.12029.pdf)  
**作者**：Sunghyeon Woo, Hoseung Kim, Sunghwan Shim, Minjung Jo, Hyunjoon Jeong, Jeongtae Lee, Joonghoon Kim, Sungjae Lee, Baeseong Park, Se Jung Kwon, Dongsoo Lee  

**一句话要点**：提出PrefillShare算法，在多LLM解耦服务中通过共享预填充模块减少KV冗余

**关键词**：多模型服务, KV缓存共享, 解耦架构, 预填充优化, 大语言模型推理

## 3 点简述
- 多模型系统重复处理相同提示前缀，导致预填充阶段冗余和KV缓存浪费
- PrefillShare将模型分解为预填充和解码模块，冻结预填充模块并微调解码模块以实现共享
- 实验显示在保持精度的同时，显著降低延迟并提高吞吐量

## 摘要（原文）

> Multi-agent systems increasingly orchestrate multiple specialized language models to solve complex real-world problems, often invoking them over a shared context. This execution pattern repeatedly processes the same prompt prefix across models. Consequently, each model redundantly executes the prefill stage and maintains its own key-value (KV) cache, increasing aggregate prefill load and worsening tail latency by intensifying prefill-decode interference in existing LLM serving stacks. Disaggregated serving reduces such interference by placing prefill and decode on separate GPUs, but disaggregation does not fundamentally eliminate inter-model redundancy in computation and KV storage for the same prompt. To address this issue, we propose PrefillShare, a novel algorithm that enables sharing the prefill stage across multiple models in a disaggregated setting. PrefillShare factorizes the model into prefill and decode modules, freezes the prefill module, and fine-tunes only the decode module. This design allows multiple task-specific models to share a prefill module and the KV cache generated for the same prompt. We further introduce a routing mechanism that enables effective prefill sharing across heterogeneous models in a vLLM-based disaggregated system. PrefillShare not only matches full fine-tuning accuracy on a broad range of tasks and models, but also delivers 4.5x lower p95 latency and 3.9x higher throughput in multi-model agent workloads.

