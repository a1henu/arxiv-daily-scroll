---
layout: default
title: HyperMLP: An Integrated Perspective for Sequence Modeling
---

# HyperMLP: An Integrated Perspective for Sequence Modeling
**arXiv**：[2602.12601v1](https://arxiv.org/abs/2602.12601) · [PDF](https://arxiv.org/pdf/2602.12601.pdf)  
**作者**：Jiecheng Lu, Shihao Yang  

**一句话要点**：提出HyperMLP/HyperGLU，将自注意力视为动态MLP以改进序列建模性能。

**关键词**：序列建模, 自注意力机制, 动态MLP, HyperMLP, HyperGLU, 表达性分析

## 3 点简述
- 核心问题：自注意力常被视为概率查询-键查找，限制了设计灵活性。
- 方法要点：将自注意力头视为动态两层MLP，引入HyperMLP/HyperGLU实现特征和序列空间的动态混合。
- 实验或效果：在匹配参数预算下，HyperMLP/HyperGLU持续优于强softmax注意力基线。

## 摘要（原文）

> Self-attention is often viewed as probabilistic query-key lookup, motivating designs that preserve normalized attention scores and fixed positional semantics. We advocate a simpler and more unified perspective: an autoregressive attention head can be viewed as a dynamic two-layer MLP whose weights are instantiated from the context history. From this view, attention scores form an ever-growing hidden representation, and standard MLP activations such as ReLU or GLU naturally implement input-conditioned selection over a context-dependent memory pool rather than a probability distribution. Based on this formulation, we introduce HyperMLP and HyperGLU, which learn dynamic mixing in both feature space and sequence space, using a reverse-offset (lag) layout to align temporal mixing with autoregressive semantics. We provide theoretical characterizations of the expressivity and implications of this structure, and empirically show that HyperMLP/HyperGLU consistently outperform strong softmax-attention baselines under matched parameter budgets.

