---
layout: default
title: Investigating GNN Convergence on Large Randomly Generated Graphs with Realistic Node Feature Correlations
---

# Investigating GNN Convergence on Large Randomly Generated Graphs with Realistic Node Feature Correlations
**arXiv**：[2602.16145v1](https://arxiv.org/abs/2602.16145) · [PDF](https://arxiv.org/pdf/2602.16145.pdf)  
**作者**：Mohammed Zain Ali Ahmed  

**一句话要点**：提出生成具有相关节点特征的随机图方法，以研究图神经网络在现实图上的收敛行为与表达能力。

**关键词**：图神经网络收敛, 随机图生成, 节点特征相关性, Barabási-Albert模型, 表达能力分析

## 3 点简述
- 现有研究分析图神经网络在大随机图上的收敛行为，但常忽略节点特征相关性，导致对表达能力的评估不准确。
- 引入新方法生成具有相关节点特征的随机图，基于Barabási-Albert模型模拟现实图属性，确保相邻节点特征相关。
- 理论分析表明收敛在某些情况下可避免，并通过大随机图实验验证发散行为，支持图神经网络在现实图上更具表达力。

## 摘要（原文）

> There are a number of existing studies analysing the convergence behaviour of graph neural networks on large random graphs. Unfortunately, the majority of these studies do not model correlations between node features, which would naturally exist in a variety of real-life networks. Consequently, the derived limitations of GNNs, resulting from such convergence behaviour, is not truly reflective of the expressive power of GNNs when applied to realistic graphs. In this paper, we will introduce a novel method to generate random graphs that have correlated node features. The node features will be sampled in such a manner to ensure correlation between neighbouring nodes. As motivation for our choice of sampling scheme, we will appeal to properties exhibited by real-life graphs, particularly properties that are captured by the Barabási-Albert model. A theoretical analysis will strongly indicate that convergence can be avoided in some cases, which we will empirically validate on large random graphs generated using our novel method. The observed divergent behaviour provides evidence that GNNs may be more expressive than initial studies would suggest, especially on realistic graphs.

