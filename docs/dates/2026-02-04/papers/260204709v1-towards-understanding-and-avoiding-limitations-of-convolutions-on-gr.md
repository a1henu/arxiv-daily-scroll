---
layout: default
title: Towards Understanding and Avoiding Limitations of Convolutions on Graphs
---

# Towards Understanding and Avoiding Limitations of Convolutions on Graphs
**arXiv**：[2602.04709v1](https://arxiv.org/abs/2602.04709) · [PDF](https://arxiv.org/pdf/2602.04709.pdf)  
**作者**：Andreas Roth  

**一句话要点**：提出多关系分割和个性化PageRank变体以解决图卷积中的共享组件放大和组件主导问题

**关键词**：图神经网络, 消息传递网络, 过平滑现象, 多关系图卷积, 个性化PageRank, 秩崩溃

## 3 点简述
- 核心问题：MPNNs存在共享组件放大和组件主导，导致节点表示秩崩溃，限制性能。
- 方法要点：引入多关系分割框架和MIMO-GC，利用多计算图避免共享组件放大；基于个性化PageRank设计变体，防止组件主导。
- 实验或效果：理论分析深化理解，框架提升MPNNs性能，支持无限消息传递迭代。

## 摘要（原文）

> While message-passing neural networks (MPNNs) have shown promising results, their real-world impact remains limited. Although various limitations have been identified, their theoretical foundations remain poorly understood, leading to fragmented research efforts. In this thesis, we provide an in-depth theoretical analysis and identify several key properties limiting the performance of MPNNs. Building on these findings, we propose several frameworks that address these shortcomings. We identify two properties exhibited by many MPNNs: shared component amplification (SCA), where each message-passing iteration amplifies the same components across all feature channels, and component dominance (CD), where a single component gets increasingly amplified as more message-passing steps are applied. These properties lead to the observable phenomenon of rank collapse of node representations, which generalizes the established over-smoothing phenomenon. By generalizing and decomposing over-smoothing, we enable a deeper understanding of MPNNs, more targeted solutions, and more precise communication within the field. To avoid SCA, we show that utilizing multiple computational graphs or edge relations is necessary. Our multi-relational split (MRS) framework transforms any existing MPNN into one that leverages multiple edge relations. Additionally, we introduce the spectral graph convolution for multiple feature channels (MIMO-GC), which naturally uses multiple computational graphs. A localized variant, LMGC, approximates the MIMO-GC while inheriting its beneficial properties. To address CD, we demonstrate a close connection between MPNNs and the PageRank algorithm. Based on personalized PageRank, we propose a variant of MPNNs that allows for infinitely many message-passing iterations, while preserving initial node features. Collectively, these results deepen the theoretical understanding of MPNNs.

