---
layout: default
title: Explicit Multi-head Attention for Inter-head Interaction in Large Language Models
---

# Explicit Multi-head Attention for Inter-head Interaction in Large Language Models
**arXiv**：[2601.19611v1](https://arxiv.org/abs/2601.19611) · [PDF](https://arxiv.org/pdf/2601.19611.pdf)  
**作者**：Runyu Peng, Yunhua Zhou, Demin Song, Kai Lv, Bo Wang, Qipeng Guo, Xipeng Qiu  

**一句话要点**：提出多头显式注意力以增强大语言模型中的头间交互

**关键词**：多头注意力, 头间交互, Transformer架构, KV缓存压缩, 大语言模型优化

## 3 点简述
- 针对Transformer多头注意力中头间交互不足的问题
- 引入头级线性组合模块和头级组归一化层显式建模跨头交互
- 实验显示MEA提升训练鲁棒性、加速收敛，并支持KV缓存压缩以减少内存使用

## 摘要（原文）

> In large language models built upon the Transformer architecture, recent studies have shown that inter-head interaction can enhance attention performance. Motivated by this, we propose Multi-head Explicit Attention (MEA), a simple yet effective attention variant that explicitly models cross-head interaction. MEA consists of two key components: a Head-level Linear Composition (HLC) module that separately applies learnable linear combinations to the key and value vectors across heads, thereby enabling rich inter-head communication; and a head-level Group Normalization layer that aligns the statistical properties of the recombined heads. MEA shows strong robustness in pretraining, which allows the use of larger learning rates that lead to faster convergence, ultimately resulting in lower validation loss and improved performance across a range of tasks. Furthermore, we explore the parameter efficiency of MEA by reducing the number of attention heads and leveraging HLC to reconstruct them using low-rank "virtual heads". This enables a practical key-value cache compression strategy that reduces KV-cache memory usage by 50% with negligible performance loss on knowledge-intensive and scientific reasoning tasks, and only a 3.59% accuracy drop for Olympiad-level mathematical benchmarks.

