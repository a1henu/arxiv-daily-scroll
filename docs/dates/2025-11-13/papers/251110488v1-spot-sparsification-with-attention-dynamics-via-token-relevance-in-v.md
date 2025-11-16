---
layout: default
title: SPOT: Sparsification with Attention Dynamics via Token Relevance in Vision Transformers
---

# SPOT: Sparsification with Attention Dynamics via Token Relevance in Vision Transformers
**arXiv**：[2511.10488v1](https://arxiv.org/abs/2511.10488) · [PDF](https://arxiv.org/pdf/2511.10488.pdf)  
**作者**：Oded Schlesinger, Amirhossein Farzam, J. Matias Di Martino, Guillermo Sapiro  

**一句话要点**：提出SPOT框架以解决视觉Transformer计算效率低的问题

**关键词**：视觉Transformer, token稀疏化, 注意力机制, 计算效率, 模型优化

## 3 点简述
- 视觉Transformer计算需求随token数二次增长，效率低下
- SPOT利用token嵌入和注意力动态早期检测冗余token
- 实验显示效率提升达40%，同时保持或提高准确率

## 摘要（原文）

> While Vision Transformers (ViT) have demonstrated remarkable performance across diverse tasks, their computational demands are substantial, scaling quadratically with the number of processed tokens. Compact attention representations, reflecting token interaction distributions, can guide early detection and reduction of less salient tokens prior to attention computation. Motivated by this, we present SParsification with attentiOn dynamics via Token relevance (SPOT), a framework for early detection of redundant tokens within ViTs that leverages token embeddings, interactions, and attention dynamics across layers to infer token importance, resulting in a more context-aware and interpretable relevance detection process. SPOT informs token sparsification and facilitates the elimination of such tokens, improving computational efficiency without sacrificing performance. SPOT employs computationally lightweight predictors that can be plugged into various ViT architectures and learn to derive effective input-specific token prioritization across layers. Its versatile design supports a range of performance levels adaptable to varying resource constraints. Empirical evaluations demonstrate significant efficiency gains of up to 40% compared to standard ViTs, while maintaining or even improving accuracy. Code and models are available at https://github.com/odedsc/SPOT .

