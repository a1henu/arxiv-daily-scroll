---
layout: default
title: DynamiQ: Accelerating Gradient Synchronization using Compressed Multi-hop All-reduce
---

# DynamiQ: Accelerating Gradient Synchronization using Compressed Multi-hop All-reduce
**arXiv**：[2602.08923v1](https://arxiv.org/abs/2602.08923) · [PDF](https://arxiv.org/pdf/2602.08923.pdf)  
**作者**：Wenchen Han, Shay Vargaftik, Michael Mitzenmacher, Ran Ben Basat  

**一句话要点**：提出DynamiQ量化框架以优化多跳全归约中的梯度同步效率

**关键词**：梯度量化, 多跳全归约, 分布式训练, 模型加速, 压缩通信

## 3 点简述
- 核心问题：多跳全归约中梯度部分和多次累加，现有量化方法未优化此场景。
- 方法要点：设计新部分和表示技术，结合解压-累加-重压缩融合内核加速执行。
- 实验或效果：在多种LLM和任务中，比Omni-Reduce等方法快达34.2%，精度接近基线。

## 摘要（原文）

> Multi-hop all-reduce is the de facto backbone of large model training. As the training scale increases, the network often becomes a bottleneck, motivating reducing the volume of transmitted data. Accordingly, recent systems demonstrated significant acceleration of the training process using gradient quantization. However, these systems are not optimized for multi-hop aggregation, where entries are partially summed multiple times along their aggregation topology.
>   This paper presents DynamiQ, a quantization framework that bridges the gap between quantization best practices and multi-hop aggregation. DynamiQ introduces novel techniques to better represent partial sums, co-designed with a decompress-accumulate-recompress fused kernel to facilitate fast execution.
>   We extended PyTorch DDP to support DynamiQ over NCCL P2P, and across different LLMs, tasks, and scales, we demonstrate consistent improvement of up to 34.2% over the best among state-of-the-art methods such as Omni-Reduce, THC, and emerging standards such as MXFP4, MXFP6, and MXFP8. Further, DynamiQ is the only evaluated method that consistently reaches near-baseline accuracy (e.g., 99.9% of the BF16 baseline) and does so while significantly accelerating the training.

