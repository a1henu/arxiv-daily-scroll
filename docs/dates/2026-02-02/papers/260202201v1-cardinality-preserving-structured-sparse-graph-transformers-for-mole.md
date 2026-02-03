---
layout: default
title: Cardinality-Preserving Structured Sparse Graph Transformers for Molecular Property Prediction
---

# Cardinality-Preserving Structured Sparse Graph Transformers for Molecular Property Prediction
**arXiv**：[2602.02201v1](https://arxiv.org/abs/2602.02201) · [PDF](https://arxiv.org/pdf/2602.02201.pdf)  
**作者**：Abhijit Gupta  

**一句话要点**：提出CardinalGraphFormer，通过结构化稀疏注意力与基数保持聚合，提升分子性质预测性能。

**关键词**：分子性质预测, 图变换器, 结构化稀疏注意力, 基数保持聚合, 自监督预训练, 药物发现

## 3 点简述
- 核心问题：药物发现中标记数据有限，需高效分子表示学习。
- 方法要点：结合Graphormer结构偏置与结构化稀疏注意力，引入基数保持聚合通道。
- 实验或效果：在11个基准任务中平均性能提升，10个任务有统计显著增益。

## 摘要（原文）

> Drug discovery motivates efficient molecular property prediction under limited labeled data. Chemical space is vast, often estimated at approximately 10^60 drug-like molecules, while only thousands of drugs have been approved. As a result, self-supervised pretraining on large unlabeled molecular corpora has become essential for data-efficient molecular representation learning. We introduce **CardinalGraphFormer**, a graph transformer that incorporates Graphormer-inspired structural biases, including shortest-path distance and centrality, as well as direct-bond edge bias, within a structured sparse attention regime limited to shortest-path distance <= 3. The model further augments this design with a cardinality-preserving unnormalized aggregation channel over the same support set. Pretraining combines contrastive graph-level alignment with masked attribute reconstruction. Under a fully matched evaluation protocol, CardinalGraphFormer improves mean performance across all 11 evaluated tasks and achieves statistically significant gains on 10 of 11 public benchmarks spanning MoleculeNet, OGB, and TDC ADMET tasks when compared to strong reproduced baselines.

