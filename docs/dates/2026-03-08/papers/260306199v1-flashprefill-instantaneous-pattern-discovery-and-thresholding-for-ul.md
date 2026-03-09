---
layout: default
title: FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling
---

# FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling
**arXiv**：[2603.06199v1](https://arxiv.org/abs/2603.06199) · [PDF](https://arxiv.org/pdf/2603.06199.pdf)  
**作者**：Qihang Fan, Huaibo Huang, Zhiying Wu, Juqiu Wang, Bingning Wang, Ran He  

**一句话要点**：提出FlashPrefill框架，通过即时模式发现与阈值化实现超快长上下文预填充

**关键词**：长上下文建模, 注意力机制, 预填充加速, 稀疏注意力, 动态阈值化, 块搜索技术

## 3 点简述
- 核心问题：长上下文建模中注意力二次复杂度是预填充阶段的关键瓶颈，现有稀疏方法存在搜索延迟或稀疏度不足问题
- 方法要点：采用快速块搜索技术动态定位垂直、斜线和块稀疏注意力模式，并引入动态阈值化机制避免排序开销以增强稀疏性
- 实验或效果：在256K序列上实现27.78倍加速，4K上下文长度下保持1.71倍加速，展示跨序列规模的鲁棒性

## 摘要（原文）

> Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase. While various sparse attention mechanisms have been explored, they typically suffer from either significant search latency or insufficient sparsity. In this paper, we propose FlashPrefill, a framework enabling ultra-fast prefilling via instantaneous pattern discovery and thresholding. FlashPrefill leverages a fast block-searching technique to simultaneously locate dynamic vertical, slash, and block-sparse attention patterns. Crucially, it introduces a dynamic thresholding mechanism that bypasses the prohibitive overhead of sorting or accumulating attention scores while effectively eliminating the long-tail distribution to enhance sparsity. Extensive evaluations demonstrate that FlashPrefill achieves a substantial leap in efficiency, delivering an unprecedented 27.78x speedup on 256K sequences. Notably, unlike existing methods that incur efficiency degradation on shorter contexts, FlashPrefill maintains a 1.71x speedup even at a 4K context length, demonstrating its robustness and practical utility across varying sequence scales.

