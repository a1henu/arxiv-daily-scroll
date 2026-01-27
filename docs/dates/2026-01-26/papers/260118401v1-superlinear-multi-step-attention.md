---
layout: default
title: Superlinear Multi-Step Attention
---

# Superlinear Multi-Step Attention
**arXiv**：[2601.18401v1](https://arxiv.org/abs/2601.18401) · [PDF](https://arxiv.org/pdf/2601.18401.pdf)  
**作者**：Yufeng Huang  

**一句话要点**：提出超线性注意力以降低长序列注意力计算复杂度并保持随机上下文访问能力

**关键词**：超线性注意力, 长序列处理, 多步注意力, 随机上下文访问, 计算复杂度优化, 端到端学习

## 3 点简述
- 核心问题：标准因果自注意力在长序列上计算复杂度高，难以高效处理百万级上下文
- 方法要点：将注意力重构为多步搜索，实现O(L^{1+1/N})复杂度，通过两步实现O(L^{3/2})基线
- 实验或效果：在单GPU上实现百万上下文解码吞吐量达114 tokens/sec，NIAH任务上展示可学习性

## 摘要（原文）

> In this paper, we propose \textbf{Superlinear attention}, a fully trainable multi-step attention architecture that achieves subquadratic complexity for long sequences while preserving \textbf{random context access} (a.k.a.\ structural non-exclusion): no eligible token position is structurally excluded from being selected for attention. Superlinear attention reformulates standard causal self-attention as a multi-step search problem with $N$ steps, yielding an overall complexity of $O(L^{1+\frac{1}{N}})$. To illustrate the architecture, we present a baseline $N=2$ implementation, which is algorithmically analogous to standard jump search. In this $O(L^{3/2})$ instantiation, the first step performs $O(L^{3/2})$ span-search to select relevant spans of the sequence, and the second step applies $O(L^{3/2})$ span-attention (standard attention restricted to the selected spans). In an upscaled $O(L^{1.54})$ configuration for robustness, we achieve an average decoding throughput of 114 tokens/sec at 1M context length and 80 tokens/sec at 10M context in our implementation on a modified 30B hybrid MoE model on a single B200 GPU. With limited training, we also obtain strong performance on the NIAH (Needle In A Haystack) task up to 256K context length, demonstrating that the routed span selection is learnable end-to-end. This paper emphasizes architectural formulation, scaling analysis, and systems feasibility, and presents initial validation; comprehensive quality evaluations across diverse long-context tasks are left to future work.

