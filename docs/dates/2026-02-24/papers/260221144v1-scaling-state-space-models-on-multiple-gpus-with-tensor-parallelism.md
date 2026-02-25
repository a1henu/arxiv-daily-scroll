---
layout: default
title: Scaling State-Space Models on Multiple GPUs with Tensor Parallelism
---

# Scaling State-Space Models on Multiple GPUs with Tensor Parallelism
**arXiv**：[2602.21144v1](https://arxiv.org/abs/2602.21144) · [PDF](https://arxiv.org/pdf/2602.21144.pdf)  
**作者**：Anurag Dutt, Nimit Shah, Hazem Masarani, Anshul Gandhi  

**一句话要点**：提出通信高效张量并行设计以解决选择性状态空间模型在多GPU推理中的性能瓶颈

**关键词**：选择性状态空间模型, 张量并行, 多GPU推理, 通信优化, 长上下文处理, 量化AllReduce

## 3 点简述
- 核心问题：选择性SSM推理受单GPU内存和带宽限制，张量并行应用困难
- 方法要点：设计SSM状态缓存、参数张量分区和量化AllReduce以优化通信效率
- 实验或效果：在Mamba等模型上实现1.6-4.0倍吞吐量提升，量化AllReduce带来额外10-18%增益

## 摘要（原文）

> Selective state space models (SSMs) have rapidly become a compelling backbone for large language models, especially for long-context workloads. Yet in deployment, their inference performance is often bounded by the memory capacity, bandwidth, and latency limits of a single GPU, making multi-GPU execution increasingly necessary. Although tensor parallelism (TP) is widely used to scale Transformer inference, applying it to selective SSM blocks is non-trivial because the SSM mixer couples large projections with a sequence-wise recurrent state update and local mixing whose efficiency depends on preserving locality and avoiding synchronization in the critical path.
>   This paper presents a communication-efficient TP design for selective SSM inference that addresses three practical engineering challenges: enabling TTFT improvements via an SSM state cache across prefill and decode, partitioning the mixer's packed parameter tensor so that recurrent updates remain local while minimizing communication, and reducing TP aggregation overhead with quantized AllReduce. We evaluate on three representative SSM-based LLMs spanning pure-SSM and hybrid architectures - Mamba, Falcon-Mamba, and Zamba - on NVIDIA A6000 and A100 clusters. Our experiments show substantial throughput gains from tensor-parallel SSM inference, improving batch-request throughput by ~1.6-2.1x on 2 GPUs and ~2.6-4.0x on 4 GPUs for Mamba, with the largest benefits at long context lengths, and achieving a further ~10-18% throughput improvement from quantized all-reduce by lowering synchronization bandwidth overhead.

