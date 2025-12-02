---
layout: default
title: Tangram: Accelerating Serverless LLM Loading through GPU Memory Reuse and Affinity
---

# Tangram: Accelerating Serverless LLM Loading through GPU Memory Reuse and Affinity
**arXiv**：[2512.01357v1](https://arxiv.org/abs/2512.01357) · [PDF](https://arxiv.org/pdf/2512.01357.pdf)  
**作者**：Wenbin Zhu, Zhaoyan Shen, Zili Shao, Hongjun Dai, Feng Chen  

**一句话要点**：提出Tangram系统，通过GPU内存重用和亲和性调度加速Serverless LLM加载

**关键词**：Serverless LLM, GPU内存重用, 冷启动优化, KV缓存管理, GPU亲和性调度, 模型加载加速

## 3 点简述
- 核心问题：Serverless LLM冷启动延迟，特别是模型加载阶段，随模型大小线性增长，成为性能瓶颈。
- 方法要点：利用未使用的GPU内存保留模型参数，包括统一GPU内存池、按需KV缓存分配和GPU亲和性调度。
- 实验或效果：原型实现显示，加载速度提升最高达6.2倍，冷启动时首令牌时间减少23-55%。

## 摘要（原文）

> Serverless Large Language Models (LLMs) have emerged as a cost-effective solution for deploying AI services by enabling a 'pay-as-you-go' pricing model through GPU resource sharing. However, cold-start latency, especially the model loading phase, has become a critical performance bottleneck, as it scales linearly with model size and severely limits the practical deployment of large-scale LLM services. This paper presents Tangram, a novel system that accelerates Serverless LLM loading through efficient GPU memory reuse. By leveraging the unused GPU memory to retain model parameters, Tangram significantly reduces model transfer time and cold-start latency. Its design includes three key components: unified GPU memory pool for tensor-level parameter sharing across models, on-demand KV cache allocation for dynamic memory management, and GPU-affinity-aware scheduling for maximizing resource utilization. These techniques collectively address the critical challenges of inefficient memory usage and the cold-start problem in Serverless LLM platforms. We have implemented a fully functional prototype, and experiments show that Tangram achieves up to 6.2 times faster loading and reduces Time-To-First-Token (TTFT) during cold-start by 23--55% over state-of-the-art methods.

