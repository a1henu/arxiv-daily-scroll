---
layout: default
title: From Local Windows to Adaptive Candidates via Individualized Exploratory: Rethinking Attention for Image Super-Resolution
---

# From Local Windows to Adaptive Candidates via Individualized Exploratory: Rethinking Attention for Image Super-Resolution
**arXiv**：[2601.08341v1](https://arxiv.org/abs/2601.08341) · [PDF](https://arxiv.org/pdf/2601.08341.pdf)  
**作者**：Chunyu Meng, Wei Long, Shuhang Gu  

**一句话要点**：提出个体化探索Transformer以解决图像超分辨率中注意力计算效率与灵活性不足的问题

**关键词**：图像超分辨率, Transformer, 注意力机制, 计算效率, 令牌自适应

## 3 点简述
- 核心问题：现有Transformer方法在图像超分辨率中因固定分组注意力导致计算效率低且忽略令牌相似性不对称性
- 方法要点：引入个体化探索注意力机制，使每个令牌自适应选择内容感知的独立候选，实现令牌自适应和非对称设计
- 实验或效果：在标准超分辨率基准测试中，IET在可比计算复杂度下达到最先进性能

## 摘要（原文）

> Single Image Super-Resolution (SISR) is a fundamental computer vision task that aims to reconstruct a high-resolution (HR) image from a low-resolution (LR) input. Transformer-based methods have achieved remarkable performance by modeling long-range dependencies in degraded images. However, their feature-intensive attention computation incurs high computational cost. To improve efficiency, most existing approaches partition images into fixed groups and restrict attention within each group. Such group-wise attention overlooks the inherent asymmetry in token similarities, thereby failing to enable flexible and token-adaptive attention computation. To address this limitation, we propose the Individualized Exploratory Transformer (IET), which introduces a novel Individualized Exploratory Attention (IEA) mechanism that allows each token to adaptively select its own content-aware and independent attention candidates. This token-adaptive and asymmetric design enables more precise information aggregation while maintaining computational efficiency. Extensive experiments on standard SR benchmarks demonstrate that IET achieves state-of-the-art performance under comparable computational complexity.

