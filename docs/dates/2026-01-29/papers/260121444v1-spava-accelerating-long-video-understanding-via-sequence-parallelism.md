---
layout: default
title: Spava: Accelerating Long-Video Understanding via Sequence-Parallelism-aware Approximate Attention
---

# Spava: Accelerating Long-Video Understanding via Sequence-Parallelism-aware Approximate Attention
**arXiv**：[2601.21444v1](https://arxiv.org/abs/2601.21444) · [PDF](https://arxiv.org/pdf/2601.21444.pdf)  
**作者**：Yuxiang Huang, Mingye Li, Xu Han, Chaojun Xiao, Weilin Zhao, Ao Sun, Ziqi Yuan, Hao Zhou, Fandong Meng, Zhiyuan Liu  

**一句话要点**：提出Spava框架，通过序列并行感知的近似注意力加速长视频理解

**关键词**：长视频理解, 序列并行, 近似注意力, 多GPU加速, 大型多模态模型

## 3 点简述
- 核心问题：长视频推理效率低，主要因大型多模态模型预填充阶段计算密集。
- 方法要点：采用序列并行框架，在多GPU上分布近似注意力，减少计算并提升并行性。
- 实验或效果：系统优化后，相比FlashAttn、ZigZagRing和APB，分别加速12.72倍、1.70倍和1.18倍，性能无显著损失。

## 摘要（原文）

> The efficiency of long-video inference remains a critical bottleneck, mainly due to the dense computation in the prefill stage of Large Multimodal Models (LMMs). Existing methods either compress visual embeddings or apply sparse attention on a single GPU, yielding limited acceleration or degraded performance and restricting LMMs from handling longer, more complex videos. To overcome these issues, we propose Spava, a sequence-parallel framework with optimized attention that accelerates long-video inference across multiple GPUs. By distributing approximate attention, Spava reduces computation and increases parallelism, enabling efficient processing of more visual embeddings without compression and thereby improving task performance. System-level optimizations, such as load balancing and fused forward passes, further unleash the potential of Spava, delivering speedups of 12.72x, 1.70x, and 1.18x over FlashAttn, ZigZagRing, and APB, without notable performance loss. Code available at https://github.com/thunlp/APB

