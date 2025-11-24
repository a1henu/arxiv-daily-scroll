---
layout: default
title: Spanning Tree Autoregressive Visual Generation
---

# Spanning Tree Autoregressive Visual Generation
**arXiv**：[2511.17089v1](https://arxiv.org/abs/2511.17089) · [PDF](https://arxiv.org/pdf/2511.17089.pdf)  
**作者**：Sangkyu Lee, Changho Lee, Janghoon Han, Hosung Song, Tackgeun You, Hwasup Lim, Stanley Jungkyu Choi, Honglak Lee, Youngjae Yu  

**一句话要点**：提出Spanning Tree Autoregressive建模，以在视觉生成中结合先验知识，保持采样性能并支持灵活序列编辑。

**关键词**：视觉生成, 自回归建模, 序列顺序优化, 图像编辑, 生成树遍历

## 3 点简述
- 核心问题：传统自回归模型在视觉生成中，随机序列顺序导致性能下降或推理灵活性受限。
- 方法要点：利用均匀生成树的遍历顺序，通过广度优先搜索和拒绝采样构建序列，确保部分观察作为前缀。
- 实验或效果：在保持采样性能的同时，提供灵活序列顺序，无需显著改变模型架构。

## 摘要（原文）

> We present Spanning Tree Autoregressive (STAR) modeling, which can incorporate prior knowledge of images, such as center bias and locality, to maintain sampling performance while also providing sufficiently flexible sequence orders to accommodate image editing at inference. Approaches that expose randomly permuted sequence orders to conventional autoregressive (AR) models in visual generation for bidirectional context either suffer from a decline in performance or compromise the flexibility in sequence order choice at inference. Instead, STAR utilizes traversal orders of uniform spanning trees sampled in a lattice defined by the positions of image patches. Traversal orders are obtained through breadth-first search, allowing us to efficiently construct a spanning tree whose traversal order ensures that the connected partial observation of the image appears as a prefix in the sequence through rejection sampling. Through the tailored yet structured randomized strategy compared to random permutation, STAR preserves the capability of postfix completion while maintaining sampling performance without any significant changes to the model architecture widely adopted in the language AR modeling.

