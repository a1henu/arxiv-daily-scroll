---
layout: default
title: Disco: Densely-overlapping Cell Instance Segmentation via Adjacency-aware Collaborative Coloring
---

# Disco: Densely-overlapping Cell Instance Segmentation via Adjacency-aware Collaborative Coloring
**arXiv**：[2602.05420v1](https://arxiv.org/abs/2602.05420) · [PDF](https://arxiv.org/pdf/2602.05420.pdf)  
**作者**：Rui Sun, Yiwen Yang, Kaiyu Guo, Chen Jiang, Dongli Xu, Zhaonan Liu, Tan Pan, Limei Han, Xue Jiang, Wu Wei, Yuan Cheng  

**一句话要点**：提出Disco框架，通过邻接感知协同着色解决密集重叠细胞实例分割问题

**关键词**：细胞实例分割, 图着色, 密集重叠, 邻接感知, 深度学习, 病理分析

## 3 点简述
- 核心问题：现有方法在处理密集重叠细胞区域时面临挑战，图着色方法在复杂拓扑中有效性未知
- 方法要点：基于数据驱动拓扑标记和约束深度学习，分解细胞图并解决邻接冲突
- 实验或效果：发布GBC-FS 2025数据集，分析细胞图色性，验证模型在复杂组织中的性能

## 摘要（原文）

> Accurate cell instance segmentation is foundational for digital pathology analysis. Existing methods based on contour detection and distance mapping still face significant challenges in processing complex and dense cellular regions. Graph coloring-based methods provide a new paradigm for this task, yet the effectiveness of this paradigm in real-world scenarios with dense overlaps and complex topologies has not been verified. Addressing this issue, we release a large-scale dataset GBC-FS 2025, which contains highly complex and dense sub-cellular nuclear arrangements. We conduct the first systematic analysis of the chromatic properties of cell adjacency graphs across four diverse datasets and reveal an important discovery: most real-world cell graphs are non-bipartite, with a high prevalence of odd-length cycles (predominantly triangles). This makes simple 2-coloring theory insufficient for handling complex tissues, while higher-chromaticity models would cause representational redundancy and optimization difficulties. Building on this observation of complex real-world contexts, we propose Disco (Densely-overlapping Cell Instance Segmentation via Adjacency-aware COllaborative Coloring), an adjacency-aware framework based on the "divide and conquer" principle. It uniquely combines a data-driven topological labeling strategy with a constrained deep learning system to resolve complex adjacency conflicts. First, "Explicit Marking" strategy transforms the topological challenge into a learnable classification task by recursively decomposing the cell graph and isolating a "conflict set." Second, "Implicit Disambiguation" mechanism resolves ambiguities in conflict regions by enforcing feature dissimilarity between different instances, enabling the model to learn separable feature representations.

