---
layout: default
title: S2O: Early Stopping for Sparse Attention via Online Permutation
---

# S2O: Early Stopping for Sparse Attention via Online Permutation
**arXiv**：[2602.22575v1](https://arxiv.org/abs/2602.22575) · [PDF](https://arxiv.org/pdf/2602.22575.pdf)  
**作者**：Yu Zhang, Songwei Liu, Chenqian Yan, Sheng Lin, Beichen Ning, Fangmin Chen, Xing Wang  

**一句话要点**：提出S2O通过在线置换实现稀疏注意力早期停止，以提升长上下文推理效率

**关键词**：稀疏注意力, 长上下文推理, 在线置换, 早期停止, 计算优化, Transformer加速

## 3 点简述
- 注意力机制随序列长度二次方增长，限制长上下文推理；现有块粒度稀疏化存在稀疏性上限
- S2O基于注意力热图细粒度结构，通过在线置换加载非连续令牌，并引入重要性引导的早期停止规则
- 在Llama-3.1-8B上，S2O在128K上下文中显著降低误差和计算密度，实现注意力加速7.51倍

## 摘要（原文）

> Attention scales quadratically with sequence length, fundamentally limiting long-context inference. Existing block-granularity sparsification can reduce latency, but coarse blocks impose an intrinsic sparsity ceiling, making further improvements difficult even with carefully engineered designs. We present S2O, which performs early stopping for sparse attention via online permutation. Inspired by virtual-to-physical address mapping in memory systems, S2O revisits and factorizes FlashAttention execution, enabling inference to load non-contiguous tokens rather than a contiguous span in the original order. Motivated by fine-grained structures in attention heatmaps, we transform explicit permutation into an online, index-guided, discrete loading policy; with extremely lightweight preprocessing and index-remapping overhead, it concentrates importance on a small set of high-priority blocks. Building on this importance-guided online permutation for loading, S2O further introduces an early-stopping rule: computation proceeds from high to low importance; once the current block score falls below a threshold, S2O terminates early and skips the remaining low-contribution blocks, thereby increasing effective sparsity and reducing computation under a controlled error budget.
>   As a result, S2O substantially raises the practical sparsity ceiling. On Llama-3.1-8B under a 128K context, S2O reduces single-operator MSE by 3.82$\times$ at matched sparsity, and reduces prefill compute density by 3.31$\times$ at matched MSE; meanwhile, it preserves end-to-end accuracy and achieves 7.51$\times$ attention and 3.81$\times$ end-to-end speedups.

