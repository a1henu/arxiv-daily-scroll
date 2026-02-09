---
layout: default
title: Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping
---

# Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping
**arXiv**：[2602.06850v1](https://arxiv.org/abs/2602.06850) · [PDF](https://arxiv.org/pdf/2602.06850.pdf)  
**作者**：Chao Zhou, Tianyi Wei, Yiling Chen, Wenbo Zhou, Nenghai Yu  

**一句话要点**：提出位置对齐与关键词范围注意力以解决多条件扩散变换器中的冗余计算问题

**关键词**：多条件控制, 扩散变换器, 注意力机制, 计算效率, 条件生成, 语义掩码

## 3 点简述
- 多条件控制中传统注意力策略导致计算和内存开销随条件数量二次增长
- PKA框架通过位置对齐和关键词范围注意力消除空间和语义冗余交互
- 实验显示PKA实现10倍推理加速和5.1倍显存节省，提升条件生成效率

## 摘要（原文）

> While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi-condition control addresses this, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate-and-attend'' strategy, which suffers from quadratic computational and memory overhead as the number of conditions scales. Our analysis reveals that much of this cross-modal interaction is spatially or semantically redundant. To this end, we propose Position-aligned and Keyword-scoped Attention (PKA), a highly efficient framework designed to eliminate these redundancies. Specifically, Position-Aligned Attention (PAA) linearizes spatial control by enforcing localized patch alignment, while Keyword-Scoped Attention (KSA) prunes irrelevant subject-driven interactions via semantic-aware masking. To facilitate efficient learning, we further introduce a Conditional Sensitivity-Aware Sampling (CSAS) strategy that reweights the training objective towards critical denoising phases, drastically accelerating convergence and enhancing conditional fidelity. Empirically, PKA delivers a 10.0$\times$ inference speedup and a 5.1$\times$ VRAM saving, providing a scalable and resource-friendly solution for high-fidelity multi-conditioned generation.

