---
layout: default
title: Which Graph Shift Operator? A Spectral Answer to an Empirical Question
---

# Which Graph Shift Operator? A Spectral Answer to an Empirical Question
**arXiv**：[2602.06557v1](https://arxiv.org/abs/2602.06557) · [PDF](https://arxiv.org/pdf/2602.06557.pdf)  
**作者**：Yassine Abbahaddou  

**一句话要点**：提出对齐增益度量，基于谱分析为图神经网络选择最优图移位算子提供理论依据。

**关键词**：图神经网络, 图移位算子, 谱分析, 泛化界, 对齐增益

## 3 点简述
- 核心问题：图神经网络中图移位算子的选择依赖经验，缺乏理论指导。
- 方法要点：引入对齐增益度量量化信号与标签子空间几何失真，连接谱代理与泛化界。
- 实验或效果：提供计算高效准则，训练前排序选择最优算子，减少搜索开销。

## 摘要（原文）

> Graph Neural Networks (GNNs) have established themselves as the leading models for learning on graph-structured data, generally categorized into spatial and spectral approaches. Central to these architectures is the Graph Shift Operator (GSO), a matrix representation of the graph structure used to filter node signals. However, selecting the optimal GSO, whether fixed or learnable, remains largely empirical. In this paper, we introduce a novel alignment gain metric that quantifies the geometric distortion between the input signal and label subspaces. Crucially, our theoretical analysis connects this alignment directly to generalization bounds via a spectral proxy for the Lipschitz constant. This yields a principled, computation-efficient criterion to rank and select the optimal GSO for any prediction task prior to training, eliminating the need for extensive search.

