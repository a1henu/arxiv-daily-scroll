---
layout: default
title: Low-Rank Key Value Attention
---

# Low-Rank Key Value Attention
**arXiv**：[2601.11471v1](https://arxiv.org/abs/2601.11471) · [PDF](https://arxiv.org/pdf/2601.11471.pdf)  
**作者**：James O'Neill, Robert Clancy, Mariia Matskevichus, Fergal Reid  

**一句话要点**：提出低秩键值注意力以降低Transformer预训练中的KV缓存内存需求

**关键词**：Transformer注意力机制, KV缓存优化, 低秩近似, 预训练效率, 内存约束训练

## 3 点简述
- Transformer预训练中KV缓存成为内存和计算瓶颈，限制模型扩展。
- LRKV通过共享全秩KV投影和低秩头特定残差，减少KV缓存冗余，保持全令牌分辨率。
- 实验显示LRKV在2.5B规模下，用约一半KV缓存超越标准注意力，训练计算减少20-25%。

## 摘要（原文）

> Transformer pretraining is increasingly constrained by memory and compute requirements, with the key-value (KV) cache emerging as a dominant bottleneck during training and autoregressive decoding. We propose \textit{low-rank KV adaptation} (LRKV), a simple modification of multi-head attention that reduces KV cache memory by exploiting redundancy across attention heads while preserving full token-level resolution. Each layer uses a shared full-rank KV projection augmented with low-rank, head-specific residuals, yielding a continuous trade-off between complete sharing and fully independent attention.
>   LRKV is a drop-in replacement for standard multi-head attention and directly subsumes query-sharing approaches such as multi-query and grouped-query attention, while remaining distinct from latent-compression methods such as multi-latent attention (MLA). Across large-scale pretraining experiments, LRKV consistently achieves faster loss reduction, lower validation perplexity, and stronger downstream task performance than standard attention, MQA/GQA, and MLA. At the 2.5B scale, LRKV outperforms standard attention while using roughly half the KV cache, and reaches equivalent model quality with up to \textbf{20-25\% less training compute} when measured in cumulative FLOPs. To explain these gains, we analyze attention head structure in operator space and show that LRKV preserves nearly all functional head diversity relative to standard attention, whereas more aggressive KV-sharing mechanisms rely on compensatory query specialization. Together, these results establish LRKV as a practical and effective attention mechanism for scaling Transformer pretraining under memory- and compute-constrained regimes.

