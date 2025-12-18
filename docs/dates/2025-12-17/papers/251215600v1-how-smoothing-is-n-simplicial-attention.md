---
layout: default
title: How Smoothing is N-simplicial Attention?
---

# How Smoothing is N-simplicial Attention?
**arXiv**：[2512.15600v1](https://arxiv.org/abs/2512.15600) · [PDF](https://arxiv.org/pdf/2512.15600.pdf)  
**作者**：Alexandre Dussolle, Pietro Liò  

**一句话要点**：提出N-单纯形注意力以增强高阶交互，并分析其平滑性

**关键词**：N-单纯形注意力, 高阶交互, 图神经网络, 位置编码, 平滑性分析

## 3 点简述
- 核心问题：从MLP到图消息传递的演进中，如何引入高阶交互以提升模型性能
- 方法要点：引入N-单纯形注意力，结合RoPE，并提出成本有效的单纯形选择机制
- 实验或效果：推导Lipschitz上界，证明存在过平滑问题，未知具体应用效果

## 摘要（原文）

> Going from pure Multilayer Perceptron (MLP) to a learnable graph message-passing mechanism at each layer has been foundational to state-of-the-art results, despite the computational trade-off (e.g. GATs or Transformers). To go a step further, in this work, we introduce N-simplicial attention, going from pairwise token similarity to higher-order interactions, and adapt it for Rotary Position Embeddings (RoPE). To help manage the increased complexity, we propose a cost-effective simplex selection enabling the model to focus its computation load onto the more task-sensitive interactions. Beyond these core mechanisms, we study how smoothing N-simplicial attention is by deriving a Lipschitz upper-bound and by demonstrating that by itself it also suffers from over-smoothing, despite opening the attention message-passing to higher-order interactions.

