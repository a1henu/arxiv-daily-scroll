---
layout: default
title: Deep Kernel Fusion for Transformers
---

# Deep Kernel Fusion for Transformers
**arXiv**：[2602.11808v1](https://arxiv.org/abs/2602.11808) · [PDF](https://arxiv.org/pdf/2602.11808.pdf)  
**作者**：Zixi Zhang, Zhiwen Mo, Yiren Zhao, Robert Mullins  

**一句话要点**：提出DeepFusionKernel以解决长上下文LLM推理中SwiGLU MLP块的内存带宽瓶颈问题。

**关键词**：长上下文推理, 内存带宽优化, 内核融合, LLM加速, SGLang集成

## 3 点简述
- 核心问题：长上下文LLM推理受限于内存带宽，SwiGLU MLP块权重过大导致缓存不足成为瓶颈。
- 方法要点：设计深度融合内核，减少HBM流量并提升缓存重用，集成SGLang和内核调度器。
- 实验或效果：在H100和A100上分别实现最高13.2%和9.7%的加速，适应多种模型和硬件。

## 摘要（原文）

> Agentic LLM inference with long contexts is increasingly limited by memory bandwidth rather than compute. In this setting, SwiGLU MLP blocks, whose large weights exceed cache capacity, become a major yet under-optimized bottleneck. We propose DeepFusionKernel, a deeply fused kernel that cuts HBM traffic and boosts cache reuse, delivering up to 13.2% speedup on H100 and 9.7% on A100 over SGLang. Integrated with SGLang and paired with a kernel scheduler, DeepFusionKernel ensures consistent accelerations over generation lengths, while remaining adaptable to diverse models, inference configurations, and hardware platforms.

