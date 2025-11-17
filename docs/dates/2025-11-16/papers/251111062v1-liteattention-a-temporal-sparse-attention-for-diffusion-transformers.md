---
layout: default
title: LiteAttention: A Temporal Sparse Attention for Diffusion Transformers
---

# LiteAttention: A Temporal Sparse Attention for Diffusion Transformers
**arXiv**：[2511.11062v1](https://arxiv.org/abs/2511.11062) · [PDF](https://arxiv.org/pdf/2511.11062.pdf)  
**作者**：Dor Shmilovich, Tony Wu, Aviad Dahan, Yuval Domb  

**一句话要点**：提出LiteAttention以解决扩散变换器在视频生成中的高延迟问题

**关键词**：扩散变换器, 注意力机制, 视频生成, 计算优化, 时间相干性

## 3 点简述
- 扩散变换器在视频生成中因注意力复杂度高导致延迟显著
- 利用时间相干性动态跳过非必要计算，结合动态适应性与静态效率
- 在FlashAttention上实现优化，视频生成加速且无质量损失

## 摘要（原文）

> Diffusion Transformers, particularly for video generation, achieve remarkable quality but suffer from quadratic attention complexity, leading to prohibitive latency. Existing acceleration methods face a fundamental trade-off: dynamically estimating sparse attention patterns at each denoising step incurs high computational overhead and estimation errors, while static sparsity patterns remain fixed and often suboptimal throughout denoising. We identify a key structural property of diffusion attention, namely, its sparsity patterns exhibit strong temporal coherence across denoising steps. Tiles deemed non-essential at step $t$ typically remain so at step $t+δ$. Leveraging this observation, we introduce LiteAttention, a method that exploits temporal coherence to enable evolutionary computation skips across the denoising sequence. By marking non-essential tiles early and propagating skip decisions forward, LiteAttention eliminates redundant attention computations without repeated profiling overheads, combining the adaptivity of dynamic methods with the efficiency of static ones. We implement a highly optimized LiteAttention kernel on top of FlashAttention and demonstrate substantial speedups on production video diffusion models, with no degradation in quality. The code and implementation details will be publicly released.

