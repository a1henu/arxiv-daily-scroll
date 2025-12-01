---
layout: default
title: Serving Heterogeneous LoRA Adapters in Distributed LLM Inference Systems
---

# Serving Heterogeneous LoRA Adapters in Distributed LLM Inference Systems
**arXiv**：[2511.22880v1](https://arxiv.org/abs/2511.22880) · [PDF](https://arxiv.org/pdf/2511.22880.pdf)  
**作者**：Shashwat Jaiswal, Shrikara Arun, Anjaly Parayil, Ankur Mallick, Spyros Mastorakis, Alind Khare, Chloi Alverti, Renee St Amant, Chetan Bansal, Victor Rühle, Josep Torrellas  

**一句话要点**：提出LoRAServe框架以解决分布式LLM推理中异构LoRA适配器服务性能不均问题

**关键词**：LoRA适配器服务, 分布式LLM推理, 性能优化, 动态资源管理, GPU Direct RDMA

## 3 点简述
- 核心问题：现有系统在服务异构LoRA适配器时忽略秩（大小）差异，导致性能倾斜和GPU资源未充分利用。
- 方法要点：LoRAServe通过动态适配器放置和路由，结合GPU Direct RDMA远程访问，优化资源分配以应对工作负载变化。
- 实验或效果：在真实生产轨迹评估中，相比先进系统，LoRAServe在满足SLO下提升吞吐量达2倍，降低TTFT达9倍，减少GPU使用达50%。

## 摘要（原文）

> Low-Rank Adaptation (LoRA) has become the de facto method for parameter-efficient fine-tuning of large language models (LLMs), enabling rapid adaptation to diverse domains. In production, LoRA-based models are served at scale, creating multi-tenant environments with hundreds of adapters sharing a base model. However, state-of-the-art serving systems co-batch heterogeneous adapters without accounting for rank (size) variability, leading to severe performance skew, which ultimately requires adding more GPUs to satisfy service-level objectives (SLOs). Existing optimizations, focused on loading, caching, and kernel execution, ignore this heterogeneity, leaving GPU resources underutilized. We present LoRAServe, a workload-aware dynamic adapter placement and routing framework designed to tame rank diversity in LoRA serving. By dynamically rebalancing adapters across GPUs and leveraging GPU Direct RDMA for remote access, LoRAServe maximizes throughput and minimizes tail latency under real-world workload drift. Evaluations on production traces from Company X show that LoRAServe elicits up to 2$\times$ higher throughput, up to 9$\times$ lower TTFT, while using up to 50% fewer GPUs under SLO constraints compared to state-of-the-art systems.

