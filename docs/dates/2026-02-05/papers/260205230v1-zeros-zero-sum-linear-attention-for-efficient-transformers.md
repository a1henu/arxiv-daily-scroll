---
layout: default
title: ZeroS: Zero-Sum Linear Attention for Efficient Transformers
---

# ZeroS: Zero-Sum Linear Attention for Efficient Transformers
**arXiv**：[2602.05230v1](https://arxiv.org/abs/2602.05230) · [PDF](https://arxiv.org/pdf/2602.05230.pdf)  
**作者**：Jiecheng Lu, Xu Han, Yan Sun, Viresh Pati, Yubin Kim, Siddhartha Somani, Shihao Yang  

**一句话要点**：提出ZeroS线性注意力以解决线性注意力在信息融合和长上下文中的性能限制

**关键词**：线性注意力, Transformer效率, 序列建模, 零和残差, 长上下文处理

## 3 点简述
- 核心问题：线性注意力受限于凸组合和均匀权重偏差，导致信息融合不足和长上下文注意力稀释
- 方法要点：通过移除常数项和重加权零和残差，实现数学稳定权重，支持正负值和对比操作
- 实验或效果：在保持O(N)复杂度下，理论扩展可表示函数集，实验匹配或超越标准softmax注意力

## 摘要（原文）

> Linear attention methods offer Transformers $O(N)$ complexity but typically underperform standard softmax attention. We identify two fundamental limitations affecting these approaches: the restriction to convex combinations that only permits additive information blending, and uniform accumulated weight bias that dilutes attention in long contexts. We propose Zero-Sum Linear Attention (ZeroS), which addresses these limitations by removing the constant zero-order term $1/t$ and reweighting the remaining zero-sum softmax residuals. This modification creates mathematically stable weights, enabling both positive and negative values and allowing a single attention layer to perform contrastive operations. While maintaining $O(N)$ complexity, ZeroS theoretically expands the set of representable functions compared to convex combinations. Empirically, it matches or exceeds standard softmax attention across various sequence modeling benchmarks.

