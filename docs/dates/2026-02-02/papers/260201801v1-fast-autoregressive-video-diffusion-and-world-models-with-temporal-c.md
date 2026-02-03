---
layout: default
title: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention
---

# Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention
**arXiv**：[2602.01801v1](https://arxiv.org/abs/2602.01801) · [PDF](https://arxiv.org/pdf/2602.01801.pdf)  
**作者**：Dvir Samuel, Issar Tzachor, Matan Levy, Micahel Green, Gal Chechik, Rami Ben-Ari  

**一句话要点**：提出TempCache、AnnCA和AnnSA以解决自回归视频扩散模型推理时的注意力瓶颈问题

**关键词**：自回归视频扩散, 注意力优化, KV缓存压缩, 近似最近邻, 长视频生成, 世界模型

## 3 点简述
- 核心问题：自回归视频扩散模型推理时KV缓存增长导致延迟增加和GPU内存上升，限制长程一致性
- 方法要点：通过时间对应压缩KV缓存、近似最近邻匹配加速跨注意力和稀疏化自注意力，无需训练
- 实验或效果：实现端到端5-10倍加速，保持视觉质量稳定，长序列中维持稳定吞吐和恒定峰值GPU内存

## 摘要（原文）

> Autoregressive video diffusion models enable streaming generation, opening the door to long-form synthesis, video world models, and interactive neural game engines. However, their core attention layers become a major bottleneck at inference time: as generation progresses, the KV cache grows, causing both increasing latency and escalating GPU memory, which in turn restricts usable temporal context and harms long-range consistency. In this work, we study redundancy in autoregressive video diffusion and identify three persistent sources: near-duplicate cached keys across frames, slowly evolving (largely semantic) queries/keys that make many attention computations redundant, and cross-attention over long prompts where only a small subset of tokens matters per frame. Building on these observations, we propose a unified, training-free attention framework for autoregressive diffusion: TempCache compresses the KV cache via temporal correspondence to bound cache growth; AnnCA accelerates cross-attention by selecting frame-relevant prompt tokens using fast approximate nearest neighbor (ANN) matching; and AnnSA sparsifies self-attention by restricting each query to semantically matched keys, also using a lightweight ANN. Together, these modules reduce attention, compute, and memory and are compatible with existing autoregressive diffusion backbones and world models. Experiments demonstrate up to x5--x10 end-to-end speedups while preserving near-identical visual quality and, crucially, maintaining stable throughput and nearly constant peak GPU memory usage over long rollouts, where prior methods progressively slow down and suffer from increasing memory usage.

