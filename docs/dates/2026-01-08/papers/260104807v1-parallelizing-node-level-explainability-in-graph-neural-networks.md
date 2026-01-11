---
layout: default
title: Parallelizing Node-Level Explainability in Graph Neural Networks
---

# Parallelizing Node-Level Explainability in Graph Neural Networks
**arXiv**：[2601.04807v1](https://arxiv.org/abs/2601.04807) · [PDF](https://arxiv.org/pdf/2601.04807.pdf)  
**作者**：Oscar Llorente, Jaime Boal, Eugenio F. Sánchez-Úbeda, Antonio Diaz-Cano, Miguel Familiar  

**一句话要点**：提出基于图划分的并行化方法以解决图神经网络中节点级可解释性计算效率低的问题

**关键词**：图神经网络, 节点级可解释性, 图划分, 并行计算, 可扩展性

## 3 点简述
- 核心问题：图神经网络节点级可解释性计算在大规模图中耗时严重，批处理策略常降低解释质量
- 方法要点：通过图划分将图分解为不相交子图，实现节点邻居可解释性的并行计算，提升可扩展性和效率
- 实验或效果：在真实数据集上实验显示显著加速，支持大规模图神经网络的可扩展和透明可解释性

## 摘要（原文）

> Graph Neural Networks (GNNs) have demonstrated remarkable performance in a wide range of tasks, such as node classification, link prediction, and graph classification, by exploiting the structural information in graph-structured data. However, in node classification, computing node-level explainability becomes extremely time-consuming as the size of the graph increases, while batching strategies often degrade explanation quality. This paper introduces a novel approach to parallelizing node-level explainability in GNNs through graph partitioning. By decomposing the graph into disjoint subgraphs, we enable parallel computation of explainability for node neighbors, significantly improving the scalability and efficiency without affecting the correctness of the results, provided sufficient memory is available. For scenarios where memory is limited, we further propose a dropout-based reconstruction mechanism that offers a controllable trade-off between memory usage and explanation fidelity. Experimental results on real-world datasets demonstrate substantial speedups, enabling scalable and transparent explainability for large-scale GNN models.

