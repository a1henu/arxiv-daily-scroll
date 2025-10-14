---
layout: default
title: Topological Alignment of Shared Vision-Language Embedding Space
---

# Topological Alignment of Shared Vision-Language Embedding Space
**arXiv**：[2510.10889v1](https://arxiv.org/abs/2510.10889) · [PDF](https://arxiv.org/pdf/2510.10889.pdf)  
**作者**：Junwon You, Dasol Kang, Jae-Hun Jung  

**一句话要点**：提出ToMCLIP框架以解决多语言视觉-语言模型嵌入空间全局几何对齐问题

**关键词**：多语言视觉-语言模型, 拓扑对齐, 持久同调, 图稀疏化, 零样本学习, 跨模态检索

## 3 点简述
- 核心问题：多语言视觉-语言模型嵌入空间存在英语偏见，且现有方法忽视全局几何结构。
- 方法要点：引入拓扑对齐损失，使用持久同调和图稀疏化策略保持嵌入空间拓扑。
- 实验或效果：在CIFAR-100和xFlickr&CO上提升零样本准确率和多语言检索性能。

## 摘要（原文）

> Contrastive Vision-Language Models (VLMs) have demonstrated strong zero-shot
> capabilities. However, their cross-modal alignment remains biased toward
> English due to limited multilingual multimodal data. Recent multilingual
> extensions have alleviated this gap but enforce instance-level alignment while
> neglecting the global geometry of the shared embedding space. We address this
> problem by introducing ToMCLIP (Topological Alignment for Multilingual CLIP), a
> topology-aware framework aligning embedding spaces with topology-preserving
> constraints. The proposed method applies persistent homology to define a
> topological alignment loss and approximates persistence diagram with
> theoretical error bounds using graph sparsification strategy. This work
> validates the proposed approach, showing enhanced structural coherence of
> multilingual representations, higher zero-shot accuracy on the CIFAR-100, and
> stronger multilingual retrieval performance on the xFlickr&CO. Beyond VLMs, the
> proposed approach provides a general method for incorporating topological
> alignment into representation learning.

