---
layout: default
title: CHESS: Context-aware Hierarchical Efficient Semantic Selection for Long-Context LLM Inference
---

# CHESS: Context-aware Hierarchical Efficient Semantic Selection for Long-Context LLM Inference
**arXiv**：[2602.20732v1](https://arxiv.org/abs/2602.20732) · [PDF](https://arxiv.org/pdf/2602.20732.pdf)  
**作者**：Chao Fei, Guozhong Li, Chenxi Liu, Panos Kalnis  

**一句话要点**：提出CHESS算法-系统协同设计，通过上下文感知分层选择解决长上下文LLM推理中KV缓存效率问题。

**关键词**：长上下文LLM推理, KV缓存管理, 上下文感知选择, 算法-系统协同设计, 高效语义选择, 低延迟推理

## 3 点简述
- 核心问题：长上下文LLM推理中KV缓存成为瓶颈，现有剪枝方法忽略上下文相关性和局部语义，导致质量下降和加速有限。
- 方法要点：CHESS采用上下文感知分层选择策略，动态重构解码上下文，并通过粗粒度选择减少数据移动，实现算法与系统协同优化。
- 实验或效果：CHESS仅用1% KV缓存超越全KV质量，吞吐量提升高达4.56倍，在实验中持续优于其他基线方法。

## 摘要（原文）

> Long-context LLMs demand accurate inference at low latency, yet decoding becomes primarily constrained by KV cache as context grows. Prior pruning methods are largely context-agnostic: their token selection ignores step-wise relevance and local semantics, which undermines quality. Moreover, their irregular accesses and selection overheads yield only limited wall-clock speedups. To address this, we propose \textbf{CHESS}, an \textit{algorithm-system co-design} KV-cache management system. Algorithmically, CHESS introduces a context-aware, hierarchical selection policy that dynamically reconstructs a coherent context for the current decoding. System-wise, coarse granularity selection eliminates expensive data movement, fully realizing practical acceleration from theoretical sparsity. Extensive evaluations demonstrate that CHESS surpasses Full-KV quality using only \textbf{1\%} of the KV cache, delivers low-latency stable inference with up to \textbf{4.56$\times$} higher throughput, and consistently outperforms other strong baselines. Code is available at \href{https://anonymous.4open.science/r/CHESS-9958/}{https://anonymous.4open.science/r/CHESS/}.

