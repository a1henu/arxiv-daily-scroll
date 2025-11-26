---
layout: default
title: GED-Consistent Disentanglement of Aligned and Unaligned Substructures for Graph Similarity Learning
---

# GED-Consistent Disentanglement of Aligned and Unaligned Substructures for Graph Similarity Learning
**arXiv**：[2511.19837v1](https://arxiv.org/abs/2511.19837) · [PDF](https://arxiv.org/pdf/2511.19837.pdf)  
**作者**：Zhentao Zhan, Xiaoliang Xu, Jingjing Wang, Junmei Wang  

**一句话要点**：提出GCGSim框架以解决图相似性学习中的GED一致性问题

**关键词**：图相似性计算, 图编辑距离, 图神经网络, 子结构解耦, 图级匹配

## 3 点简述
- 核心问题：现有GNN方法在节点级匹配与GED原则不匹配，导致全局结构对应缺失和编辑成本误判
- 方法要点：基于图级匹配和子结构级编辑成本，实现对齐与非对齐子结构的解耦表示
- 实验或效果：在四个基准数据集上达到最优性能，验证了子结构表示的有效性

## 摘要（原文）

> Graph Similarity Computation (GSC) is a fundamental graph related task where Graph Edit Distance (GED) serves as a prevalent metric. GED is determined by an optimal alignment between a pair of graphs that partitions each into aligned (zero-cost) and unaligned (cost-incurring) substructures. Due to NP-hard nature of exact GED computation, GED approximations based on Graph Neural Network(GNN) have emerged. Existing GNN-based GED approaches typically learn node embeddings for each graph and then aggregate pairwise node similarities to estimate the final similarity. Despite their effectiveness, we identify a mismatch between this prevalent node-centric matching paradigm and the core principles of GED. This discrepancy leads to two critical limitations: (1) a failure to capture the global structural correspondence for optimal alignment, and (2) a misattribution of edit costs driven by spurious node level signals. To address these limitations, we propose GCGSim, a GED-consistent graph similarity learning framework centering on graph-level matching and substructure-level edit costs. Specifically, we make three core technical contributions. Extensive experiments on four benchmark datasets show that GCGSim achieves state-of-the-art performance. Our comprehensive analyses further validate that the framework effectively learns disentangled and semantically meaningful substructure representations.

