---
layout: default
title: A Circular Argument : Does RoPE need to be Equivariant for Vision?
---

# A Circular Argument : Does RoPE need to be Equivariant for Vision?
**arXiv**：[2511.08368v1](https://arxiv.org/abs/2511.08368) · [PDF](https://arxiv.org/pdf/2511.08368.pdf)  
**作者**：Chase van de Geijn, Timo Lüddecke, Polina Turishcheva, Alexander S. Ecker  

**一句话要点**：提出Spherical RoPE以质疑位置等变性在视觉任务中的必要性

**关键词**：旋转位置编码, 位置等变性, 视觉任务, 相对位置嵌入, 非交换生成器

## 3 点简述
- 核心问题：RoPE的成功是否依赖于位置等变性，尤其在视觉数据中。
- 方法要点：引入Spherical RoPE，使用非交换生成器，不强制等变性。
- 实验或效果：Spherical RoPE在视觉任务中表现等同或优于等变方法。

## 摘要（原文）

> Rotary Positional Encodings (RoPE) have emerged as a highly effective technique for one-dimensional sequences in Natural Language Processing spurring recent progress towards generalizing RoPE to higher-dimensional data such as images and videos. The success of RoPE has been thought to be due to its positional equivariance, i.e. its status as a relative positional encoding. In this paper, we mathematically show RoPE to be one of the most general solutions for equivariant positional embedding in one-dimensional data. Moreover, we show Mixed RoPE to be the analogously general solution for M-dimensional data, if we require commutative generators -- a property necessary for RoPE's equivariance. However, we question whether strict equivariance plays a large role in RoPE's performance. We propose Spherical RoPE, a method analogous to Mixed RoPE, but assumes non-commutative generators. Empirically, we find Spherical RoPE to have the equivalent or better learning behavior compared to its equivariant analogues. This suggests that relative positional embeddings are not as important as is commonly believed, at least within computer vision. We expect this discovery to facilitate future work in positional encodings for vision that can be faster and generalize better by removing the preconception that they must be relative.

