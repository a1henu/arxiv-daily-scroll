---
layout: default
title: A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation
---

# A Graphop Analysis of Graph Neural Networks on Sparse Graphs: Generalization and Universal Approximation
**arXiv**：[2602.08785v1](https://arxiv.org/abs/2602.08785) · [PDF](https://arxiv.org/pdf/2602.08785.pdf)  
**作者**：Ofek Amran, Tom Gilat, Ron Levie  

**一句话要点**：提出基于图算子分析的统一度量框架，以增强消息传递图神经网络在稀疏图上的泛化与逼近能力。

**关键词**：图神经网络, 泛化理论, 逼近定理, 图算子分析, 稀疏图, 度量空间

## 3 点简述
- 核心问题：现有理论在分析消息传递图神经网络时，对稀疏图仅适用于大小有界图，对稠密图则限制较少，缺乏统一框架。
- 方法要点：定义适用于所有大小图的紧凑度量空间，基于图算子分析扩展理论，证明网络在该度量下具有Hölder连续性。
- 实验或效果：理论推导出更强大的通用逼近定理和泛化界，优于先前工作，适用于稀疏和稠密图。

## 摘要（原文）

> Generalization and approximation capabilities of message passing graph neural networks (MPNNs) are often studied by defining a compact metric on a space of input graphs under which MPNNs are Hölder continuous. Such analyses are of two varieties: 1) when the metric space includes graphs of unbounded sizes, the theory is only appropriate for dense graphs, and, 2) when studying sparse graphs, the metric space only includes graphs of uniformly bounded size. In this work, we present a unified approach, defining a compact metric on the space of graphs of all sizes, both sparse and dense, under which MPNNs are Hölder continuous. This leads to more powerful universal approximation theorems and generalization bounds than previous works. The theory is based on, and extends, a recent approach to graph limit theory called graphop analysis.

