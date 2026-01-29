---
layout: default
title: StreamFusion: Scalable Sequence Parallelism for Distributed Inference of Diffusion Transformers on GPUs
---

# StreamFusion: Scalable Sequence Parallelism for Distributed Inference of Diffusion Transformers on GPUs
**arXiv**：[2601.20273v1](https://arxiv.org/abs/2601.20273) · [PDF](https://arxiv.org/pdf/2601.20273.pdf)  
**作者**：Jiacheng Yang, Jun Wu, Yaoyao Ding, Zhiying Xu, Yida Wang, Gennady Pekhimenko  

**一句话要点**：提出StreamFusion以解决扩散变换器分布式推理中的序列并行效率问题

**关键词**：扩散变换器, 序列并行, 分布式推理, GPU优化, 通信效率

## 3 点简述
- 核心问题：现有序列并行技术存在通信模式不佳、跨机全对全操作延迟高及GPU同步开销大
- 方法要点：采用拓扑感知序列并行、Torus Attention重叠通信与计算、单边通信减少同步
- 实验或效果：实验显示StreamFusion平均性能提升1.35倍，最高达1.77倍

## 摘要（原文）

> Diffusion Transformers (DiTs) have gained increasing adoption in high-quality image and video generation. As demand for higher-resolution images and longer videos increases, single-GPU inference becomes inefficient due to increased latency and large activation sizes. Current frameworks employ sequence parallelism (SP) techniques such as Ulysses Attention and Ring Attention to scale inference. However, these implementations have three primary limitations: (1) suboptimal communication patterns for network topologies on modern GPU machines, (2) latency bottlenecks from all-to-all operations in inter-machine communication, and (3) GPU sender-receiver synchronization and computation overheads from using two-sided communication libraries. To address these issues, we present StreamFusion, a topology-aware efficient DiT serving engine. StreamFusion incorporates three key innovations: (1) a topology-aware sequence parallelism technique that accounts for inter- and intra-machine bandwidth differences, (2) Torus Attention, a novel SP technique enabling overlapping of inter-machine all-to-all operations with computation, and (3) a one-sided communication implementation that minimizes GPU sender-receiver synchronization and computation overheads. Our experiments demonstrate that StreamFusion outperforms the state-of-the-art approach by an average of $1.35\times$ (up to $1.77\times$).

