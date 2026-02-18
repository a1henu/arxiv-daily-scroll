---
layout: default
title: Random Wavelet Features for Graph Kernel Machines
---

# Random Wavelet Features for Graph Kernel Machines
**arXiv**：[2602.15711v1](https://arxiv.org/abs/2602.15711) · [PDF](https://arxiv.org/pdf/2602.15711.pdf)  
**作者**：Valentin de Bassompierre, Jean-Charles Delvenne, Laurent Jacques  

**一句话要点**：提出随机谱节点嵌入以估计图核，实现可扩展的图表示学习。

**关键词**：图核近似, 随机特征, 节点嵌入, 谱方法, 可扩展学习

## 3 点简述
- 核心问题：图核直接计算在大网络上不可行，需高效近似方法。
- 方法要点：基于随机特征方法，设计随机谱节点嵌入，点积估计图核低秩近似。
- 实验或效果：理论和实证显示，在谱局部化核上比现有方法更准确。

## 摘要（原文）

> Node embeddings map graph vertices into low-dimensional Euclidean spaces while preserving structural information. They are central to tasks such as node classification, link prediction, and signal reconstruction. A key goal is to design node embeddings whose dot products capture meaningful notions of node similarity induced by the graph. Graph kernels offer a principled way to define such similarities, but their direct computation is often prohibitive for large networks. Inspired by random feature methods for kernel approximation in Euclidean spaces, we introduce randomized spectral node embeddings whose dot products estimate a low-rank approximation of any specific graph kernel. We provide theoretical and empirical results showing that our embeddings achieve more accurate kernel approximations than existing methods, particularly for spectrally localized kernels. These results demonstrate the effectiveness of randomized spectral constructions for scalable and principled graph representation learning.

