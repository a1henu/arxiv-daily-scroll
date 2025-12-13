---
layout: default
title: LGAN: An Efficient High-Order Graph Neural Network via the Line Graph Aggregation
---

# LGAN: An Efficient High-Order Graph Neural Network via the Line Graph Aggregation
**arXiv**：[2512.10735v1](https://arxiv.org/abs/2512.10735) · [PDF](https://arxiv.org/pdf/2512.10735.pdf)  
**作者**：Lin Du, Lu Bai, Jincheng Li, Lixin Cui, Hangyuan Du, Lichi Zhang, Yuting Chen, Zhao Li  

**一句话要点**：提出LGAN通过线图聚合实现高效高阶图神经网络，以解决k-WL模型计算成本高和可解释性差的问题。

**关键词**：图神经网络, 高阶表达, 线图聚合, 可解释性, 图分类

## 3 点简述
- 核心问题：现有GNN表达能力受限于1-WL，k-WL模型计算成本高且缺乏节点或边级语义，导致可解释性不足。
- 方法要点：LGAN为每个节点构建诱导子图的线图进行高阶聚合，理论上表达能力超过2-WL且时间复杂度更低。
- 实验或效果：在基准测试中，LGAN优于当前最优k-WL基GNN，并提供更好的可解释性。

## 摘要（原文）

> Graph Neural Networks (GNNs) have emerged as a dominant paradigm for graph classification. Specifically, most existing GNNs mainly rely on the message passing strategy between neighbor nodes, where the expressivity is limited by the 1-dimensional Weisfeiler-Lehman (1-WL) test. Although a number of k-WL-based GNNs have been proposed to overcome this limitation, their computational cost increases rapidly with k, significantly restricting the practical applicability. Moreover, since the k-WL models mainly operate on node tuples, these k-WL-based GNNs cannot retain fine-grained node- or edge-level semantics required by attribution methods (e.g., Integrated Gradients), leading to the less interpretable problem. To overcome the above shortcomings, in this paper, we propose a novel Line Graph Aggregation Network (LGAN), that constructs a line graph from the induced subgraph centered at each node to perform the higher-order aggregation. We theoretically prove that the LGAN not only possesses the greater expressive power than the 2-WL under injective aggregation assumptions, but also has lower time complexity. Empirical evaluations on benchmarks demonstrate that the LGAN outperforms state-of-the-art k-WL-based GNNs, while offering better interpretability.

