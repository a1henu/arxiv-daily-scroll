---
layout: default
title: Fixed Aggregation Features Can Rival GNNs
---

# Fixed Aggregation Features Can Rival GNNs
**arXiv**：[2601.19449v1](https://arxiv.org/abs/2601.19449) · [PDF](https://arxiv.org/pdf/2601.19449.pdf)  
**作者**：Celia Rubio-Madrigal, Rebekka Burkholz  

**一句话要点**：提出固定聚合特征以挑战图神经网络在节点表示学习中的主导地位。

**关键词**：图神经网络, 固定聚合特征, 节点表示学习, 表格方法, 可解释性, 基准测试

## 3 点简述
- 核心问题：质疑图神经网络通过可训练邻域聚合在节点表示学习中的优势。
- 方法要点：引入固定聚合特征，将图学习任务转化为表格问题，无需训练。
- 实验或效果：在14个基准测试中，固定聚合特征在12个任务上媲美或超越先进图神经网络。

## 摘要（原文）

> Graph neural networks (GNNs) are widely believed to excel at node representation learning through trainable neighborhood aggregations. We challenge this view by introducing Fixed Aggregation Features (FAFs), a training-free approach that transforms graph learning tasks into tabular problems. This simple shift enables the use of well-established tabular methods, offering strong interpretability and the flexibility to deploy diverse classifiers. Across 14 benchmarks, well-tuned multilayer perceptrons trained on FAFs rival or outperform state-of-the-art GNNs and graph transformers on 12 tasks -- often using only mean aggregation. The only exceptions are the Roman Empire and Minesweeper datasets, which typically require unusually deep GNNs. To explain the theoretical possibility of non-trainable aggregations, we connect our findings to Kolmogorov-Arnold representations and discuss when mean aggregation can be sufficient. In conclusion, our results call for (i) richer benchmarks benefiting from learning diverse neighborhood aggregations, (ii) strong tabular baselines as standard, and (iii) employing and advancing tabular models for graph data to gain new insights into related tasks.

