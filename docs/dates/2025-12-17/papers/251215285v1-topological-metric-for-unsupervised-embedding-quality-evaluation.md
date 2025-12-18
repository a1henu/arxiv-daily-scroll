---
layout: default
title: Topological Metric for Unsupervised Embedding Quality Evaluation
---

# Topological Metric for Unsupervised Embedding Quality Evaluation
**arXiv**：[2512.15285v1](https://arxiv.org/abs/2512.15285) · [PDF](https://arxiv.org/pdf/2512.15285.pdf)  
**作者**：Aleksei Shestov, Anton Klenitskiy, Daria Denisova, Amurkhan Dzagkoev, Daniil Petrovich, Andrey Savchenko, Maksim Makarenko  

**一句话要点**：提出Persistence拓扑度量，以无监督方式评估嵌入质量

**关键词**：无监督评估, 持久同调, 嵌入质量, 拓扑度量, 表示学习

## 3 点简述
- 核心问题：无标签下评估嵌入质量是开放挑战
- 方法要点：基于持久同调，量化嵌入空间的几何与拓扑结构
- 实验或效果：在多个领域与下游性能高度相关，优于现有无监督度量

## 摘要（原文）

> Modern representation learning increasingly relies on unsupervised and self-supervised methods trained on large-scale unlabeled data. While these approaches achieve impressive generalization across tasks and domains, evaluating embedding quality without labels remains an open challenge. In this work, we propose Persistence, a topology-aware metric based on persistent homology that quantifies the geometric structure and topological richness of embedding spaces in a fully unsupervised manner. Unlike metrics that assume linear separability or rely on covariance structure, Persistence captures global and multi-scale organization. Empirical results across diverse domains show that Persistence consistently achieves top-tier correlations with downstream performance, outperforming existing unsupervised metrics and enabling reliable model and hyperparameter selection.

