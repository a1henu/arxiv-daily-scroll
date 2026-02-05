---
layout: default
title: Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism
---

# Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism
**arXiv**：[2602.04870v1](https://arxiv.org/abs/2602.04870) · [PDF](https://arxiv.org/pdf/2602.04870.pdf)  
**作者**：Chenwei Cui, Rockwell Jackson, Benjamin Joseph Herrera, Ana María Tárano, Hannah Kerner  

**一句话要点**：提出Multi-Head LatentMoE与Head Parallel以解决稀疏专家混合模型训练中的通信开销与负载不平衡问题。

**关键词**：稀疏专家混合模型, 分布式训练, 通信效率, 负载平衡, 确定性并行, 大语言模型

## 3 点简述
- 核心问题：专家并行方法存在通信成本随激活专家数线性增长、负载不平衡及数据依赖通信问题。
- 方法要点：引入Multi-Head LatentMoE架构和Head Parallel并行策略，实现O(1)通信成本、完全平衡流量和确定性通信。
- 实验或效果：相比专家并行，训练速度提升最高1.61倍，性能相同；粒度加倍时性能更高且速度仍快1.11倍。

## 摘要（原文）

> Large language models have transformed many applications but remain expensive to train. Sparse Mixture of Experts (MoE) addresses this through conditional computation, with Expert Parallel (EP) as the standard distributed training method. However, EP has three limitations: communication cost grows linearly with the number of activated experts $k$, load imbalance affects latency and memory usage, and data-dependent communication requires metadata exchange. We propose Multi-Head LatentMoE and Head Parallel (HP), a new architecture and parallelism achieving $O(1)$ communication cost regardless of $k$, completely balanced traffic, and deterministic communication, all while remaining compatible with EP. To accelerate Multi-Head LatentMoE, we propose IO-aware routing and expert computation. Compared to MoE with EP, Multi-Head LatentMoE with HP trains up to $1.61\times$ faster while having identical performance. With doubled granularity, it achieves higher overall performance while still being $1.11\times$ faster. Our method makes multi-billion-parameter foundation model research more accessible.

