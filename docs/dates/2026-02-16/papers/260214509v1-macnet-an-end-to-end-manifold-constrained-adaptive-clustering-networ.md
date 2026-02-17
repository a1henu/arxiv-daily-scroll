---
layout: default
title: MacNet: An End-to-End Manifold-Constrained Adaptive Clustering Network for Interpretable Whole Slide Image Classification
---

# MacNet: An End-to-End Manifold-Constrained Adaptive Clustering Network for Interpretable Whole Slide Image Classification
**arXiv**：[2602.14509v1](https://arxiv.org/abs/2602.14509) · [PDF](https://arxiv.org/pdf/2602.14509.pdf)  
**作者**：Mingrui Ma, Chentao Li, Pan Huang, Jing Qin  

**一句话要点**：提出端到端流形约束自适应聚类网络，以提升全切片图像分类的准确性和可解释性。

**关键词**：全切片图像分类, 多实例学习, 流形聚类, 可解释性, 端到端学习

## 3 点简述
- 针对全切片图像分类中现有方法特征维度高、聚类中心语义模糊的问题。
- 集成Grassmann重嵌入和流形自适应聚类，利用几何结构增强聚类鲁棒性。
- 实验表明模型在分级准确性和可解释性上优于基线，且计算资源需求可接受。

## 摘要（原文）

> Whole slide images (WSIs) are the gold standard for pathological diagnosis and sub-typing. Current main-stream two-step frameworks employ offline feature encoders trained without domain-specific knowledge. Among them, attention-based multiple instance learning (MIL) methods are outcome-oriented and offer limited interpretability. Clustering-based approaches can provide explainable decision-making process but suffer from high dimension features and semantically ambiguous centroids. To this end, we propose an end-to-end MIL framework that integrates Grassmann re-embedding and manifold adaptive clustering, where the manifold geometric structure facilitates robust clustering results. Furthermore, we design a prior knowledge guiding proxy instance labeling and aggregation strategy to approximate patch labels and focus on pathologically relevant tumor regions. Experiments on multicentre WSI datasets demonstrate that: 1) our cluster-incorporated model achieves superior performance in both grading accuracy and interpretability; 2) end-to-end learning refines better feature representations and it requires acceptable computation resources.

