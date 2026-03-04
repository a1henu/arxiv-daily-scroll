---
layout: default
title: Torus embeddings
---

# Torus embeddings
**arXiv**：[2603.03135v1](https://arxiv.org/abs/2603.03135) · [PDF](https://arxiv.org/pdf/2603.03135.pdf)  
**作者**：Dan Stowell  

**一句话要点**：提出环面嵌入以匹配整数溢出表示，提升深度学习嵌入效率与实现简易性。

**关键词**：环面嵌入, 深度学习表示, 整数溢出, 量化嵌入, TinyML, 归一化策略

## 3 点简述
- 核心问题：现有计算机整数溢出表示与欧几里得或超球面嵌入不匹配，导致表示容量浪费。
- 方法要点：通过归一化策略，在深度学习框架中实现环面拓扑嵌入，保持训练稳定性和性能。
- 实验或效果：环面嵌入与超球面嵌入性能相当，并支持高效量化，便于TinyML嵌入式实现。

## 摘要（原文）

> Many data representations are vectors of continuous values. In particular, deep learning embeddings are data-driven representations, typically either unconstrained in Euclidean space, or constrained to a hypersphere. These may also be translated into integer representations (quantised) for efficient large-scale use. However, the fundamental (and most efficient) numeric representation in the overwhelming majority of existing computers is integers with overflow -- and vectors of these integers do not correspond to either of these spaces, but instead to the topology of a (hyper)torus. This mismatch can lead to wasted representation capacity. Here we show that common deep learning frameworks can be adapted, quite simply, to create representations with inherent toroidal topology. We investigate two alternative strategies, demonstrating that a normalisation-based strategy leads to training with desirable stability and performance properties, comparable to a standard hyperspherical L2 normalisation. We also demonstrate that a torus embedding maintains desirable quantisation properties. The torus embedding does not outperform hypersphere embeddings in general, but is comparable, and opens the possibility to train deep embeddings which have an extremely simple pathway to efficient `TinyML' embedded implementation.

