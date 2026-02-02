---
layout: default
title: Scalable Topology-Preserving Graph Coarsening with Graph Collapse
---

# Scalable Topology-Preserving Graph Coarsening with Graph Collapse
**arXiv**：[2601.22943v1](https://arxiv.org/abs/2601.22943) · [PDF](https://arxiv.org/pdf/2601.22943.pdf)  
**作者**：Xiang Wu, Rong-Hua Li, Xunkai Li, Kangfei Zhao, Hongchao Qin, Guoren Wang  

**一句话要点**：提出STPGC以解决图粗化中拓扑特征保持与可扩展性问题

**关键词**：图粗化, 拓扑保持, 图神经网络, 可扩展算法, 节点分类

## 3 点简述
- 现有图粗化方法多关注谱或空间特征，但拓扑特征对GNN性能重要且计算复杂
- 基于代数拓扑引入图强坍缩和边坍缩概念，设计三种算法消除支配节点和边
- 实验证明STPGC在节点分类任务中高效有效，并加速GNN训练

## 摘要（原文）

> Graph coarsening reduces the size of a graph while preserving certain properties. Most existing methods preserve either spectral or spatial characteristics. Recent research has shown that preserving topological features helps maintain the predictive performance of graph neural networks (GNNs) trained on the coarsened graph but suffers from exponential time complexity. To address these problems, we propose Scalable Topology-Preserving Graph Coarsening (STPGC) by introducing the concepts of graph strong collapse and graph edge collapse extended from algebraic topology. STPGC comprises three new algorithms, GStrongCollapse, GEdgeCollapse, and NeighborhoodConing based on these two concepts, which eliminate dominated nodes and edges while rigorously preserving topological features. We further prove that STPGC preserves the GNN receptive field and develop approximate algorithms to accelerate GNN training. Experiments on node classification with GNNs demonstrate the efficiency and effectiveness of STPGC.

