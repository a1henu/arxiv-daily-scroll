---
layout: default
title: A Community-Enhanced Graph Representation Model for Link Prediction
---

# A Community-Enhanced Graph Representation Model for Link Prediction
**arXiv**：[2512.21166v1](https://arxiv.org/abs/2512.21166) · [PDF](https://arxiv.org/pdf/2512.21166.pdf)  
**作者**：Lei Wang, Darong Lai  

**一句话要点**：提出社区增强链接预测框架，通过整合社区结构提升图神经网络在链接预测中的性能。

**关键词**：链接预测, 图神经网络, 社区结构, 图表示学习, 多尺度特征

## 3 点简述
- 核心问题：现有图神经网络在链接预测中常因过度依赖局部信息而表现不佳，难以超越传统启发式方法。
- 方法要点：引入社区结构，通过社区感知的边完成与修剪增强图，并整合多尺度结构特征以建模局部与全局拓扑。
- 实验或效果：在多个基准数据集上验证了框架的优越性能，证实社区结构对提升链接预测准确性的关键作用。

## 摘要（原文）

> Although Graph Neural Networks (GNNs) have become the dominant approach for graph representation learning, their performance on link prediction tasks does not always surpass that of traditional heuristic methods such as Common Neighbors and Jaccard Coefficient. This is mainly because existing GNNs tend to focus on learning local node representations, making it difficult to effectively capture structural relationships between node pairs. Furthermore, excessive reliance on local neighborhood information can lead to over-smoothing. Prior studies have shown that introducing global structural encoding can partially alleviate this issue. To address these limitations, we propose a Community-Enhanced Link Prediction (CELP) framework that incorporates community structure to jointly model local and global graph topology. Specifically, CELP enhances the graph via community-aware, confidence-guided edge completion and pruning, while integrating multi-scale structural features to achieve more accurate link prediction. Experimental results across multiple benchmark datasets demonstrate that CELP achieves superior performance, validating the crucial role of community structure in improving link prediction accuracy.

