---
layout: default
title: Multi-Head Low-Rank Attention
---

# Multi-Head Low-Rank Attention
**arXiv**：[2603.02188v1](https://arxiv.org/abs/2603.02188) · [PDF](https://arxiv.org/pdf/2603.02188.pdf)  
**作者**：Songtao Liu, Hongwu Peng, Zhiwei Zhang, Zhengyu Chen, Yue Guo  

**一句话要点**：提出多头部低秩注意力以解决长上下文推理中KV缓存加载的分布式解码瓶颈

**关键词**：长上下文推理, KV缓存优化, 张量并行, 低秩注意力, 解码加速

## 3 点简述
- 核心问题：长上下文推理中KV缓存加载在解码阶段成为瓶颈，多头部潜在注意力在张量并行解码时存在分片瓶颈
- 方法要点：引入多头部低秩注意力，实现可分区的潜在状态，支持高效4路张量并行解码
- 实验或效果：在困惑度和下游任务上达到先进性能，解码速度比多头部潜在注意力提升2.8倍

## 摘要（原文）

> Long-context inference in large language models is bottlenecked by Key--Value (KV) cache loading during the decoding stage, where the sequential nature of generation requires repeatedly transferring the KV cache from off-chip High-Bandwidth Memory (HBM) to on-chip Static Random-Access Memory (SRAM) at each step. While Multi-Head Latent Attention (MLA) significantly reduces the total KV cache size, it suffers from a sharding bottleneck during distributed decoding via Tensor Parallelism (TP). Since its single latent head cannot be partitioned, each device is forced to redundantly load the complete KV cache for every token, consuming excessive memory traffic and diminishing TP benefits like weight sharding. In this work, we propose Multi-Head Low-Rank Attention (MLRA), which enables partitionable latent states for efficient 4-way TP decoding. Extensive experiments show that MLRA achieves state-of-the-art perplexity and downstream task performance, while also delivering a 2.8$\times$ decoding speedup over MLA. Code is available at https://github.com/SongtaoLiu0823/MLRA. Pretrained weights, along with the training and evaluation data, are available at https://huggingface.co/Soughing/MLRA.

