---
layout: default
title: On the geometry and topology of representations: the manifolds of modular addition
---

# On the geometry and topology of representations: the manifolds of modular addition
**arXiv**：[2512.25060v1](https://arxiv.org/abs/2512.25060) · [PDF](https://arxiv.org/pdf/2512.25060.pdf)  
**作者**：Gabriela Moisescu-Pareja, Gavin McCracken, Harley Wiltzer, Vincent Létourneau, Colin Daniels, Doina Precup, Jonathan Love  

**一句话要点**：揭示统一与可学习注意力架构在模加法中实现相同算法，基于拓扑几何分析表示流形

**关键词**：模加法, 注意力架构, 表示流形, 拓扑分析, 深度学习电路

## 3 点简述
- 核心问题：不同架构是否导致模加法的不同电路实现，Clock与Pizza解释引发争议
- 方法要点：超越单个神经元分析，识别表示对应神经元群，作为流形进行拓扑几何研究
- 实验或效果：统计分析数百个电路，证明常见深度学习范式下表示相似性

## 摘要（原文）

> The Clock and Pizza interpretations, associated with architectures differing in either uniform or learnable attention, were introduced to argue that different architectural designs can yield distinct circuits for modular addition. In this work, we show that this is not the case, and that both uniform attention and trainable attention architectures implement the same algorithm via topologically and geometrically equivalent representations. Our methodology goes beyond the interpretation of individual neurons and weights. Instead, we identify all of the neurons corresponding to each learned representation and then study the collective group of neurons as one entity. This method reveals that each learned representation is a manifold that we can study utilizing tools from topology. Based on this insight, we can statistically analyze the learned representations across hundreds of circuits to demonstrate the similarity between learned modular addition circuits that arise naturally from common deep learning paradigms.

