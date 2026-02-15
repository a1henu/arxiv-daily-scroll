---
layout: default
title: PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving
---

# PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving
**arXiv**：[2602.12029v1](https://arxiv.org/abs/2602.12029) · [PDF](https://arxiv.org/pdf/2602.12029.pdf)  
**作者**：Sunghyeon Woo, Hoseung Kim, Sunghwan Shim, Minjung Jo, Hyunjoon Jeong, Jeongtae Lee, Joonghoon Kim, Sungjae Lee, Baeseong Park, Se Jung Kwon, Dongsoo Lee  

**一句话要点**：提出PrefillShare算法，在多LLM解耦服务中通过共享预填充模块实现KV重用

**关键词**：多模型服务, KV缓存重用, 解耦计算, 预填充优化, 延迟降低

## 3 点简述
- 核心问题：多模型系统中重复预填充相同提示前缀，导致计算冗余和延迟增加
- 方法要点：将模型分解为预填充和解码模块，冻结预填充模块并微调解码模块以实现共享
- 实验或效果：在广泛任务中匹配全微调精度，多模型工作负载下延迟降低4.5倍，吞吐量提升3.9倍

## 摘要（原文）

> Multi-agent systems increasingly orchestrate multiple specialized language models to solve complex real-world problems, often invoking them over a shared context. This execution pattern repeatedly processes the same prompt prefix across models. Consequently, each model redundantly executes the prefill stage and maintains its own key-value (KV) cache, increasing aggregate prefill load and worsening tail latency by intensifying prefill-decode interference in existing LLM serving stacks. Disaggregated serving reduces such interference by placing prefill and decode on separate GPUs, but disaggregation does not fundamentally eliminate inter-model redundancy in computation and KV storage for the same prompt. To address this issue, we propose PrefillShare, a novel algorithm that enables sharing the prefill stage across multiple models in a disaggregated setting. PrefillShare factorizes the model into prefill and decode modules, freezes the prefill module, and fine-tunes only the decode module. This design allows multiple task-specific models to share a prefill module and the KV cache generated for the same prompt. We further introduce a routing mechanism that enables effective prefill sharing across heterogeneous models in a vLLM-based disaggregated system. PrefillShare not only matches full fine-tuning accuracy on a broad range of tasks and models, but also delivers 4.5x lower p95 latency and 3.9x higher throughput in multi-model agent workloads.

