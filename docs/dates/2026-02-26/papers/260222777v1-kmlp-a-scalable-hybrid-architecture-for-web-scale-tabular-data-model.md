---
layout: default
title: KMLP: A Scalable Hybrid Architecture for Web-Scale Tabular Data Modeling
---

# KMLP: A Scalable Hybrid Architecture for Web-Scale Tabular Data Modeling
**arXiv**：[2602.22777v1](https://arxiv.org/abs/2602.22777) · [PDF](https://arxiv.org/pdf/2602.22777.pdf)  
**作者**：Mingming Zhang, Pengfei Shi, Zhiqing Xiao, Feng Zhao, Guandong Sun, Yulin Kang, Ruizhe Gao, Ningtao Wang, Xing Fu, Weiqiang Wang, Junbo Zhao  

**一句话要点**：提出KMLP混合架构以解决大规模网络表格数据建模的可扩展性问题

**关键词**：表格数据建模, 可扩展架构, Kolmogorov-Arnold网络, 门控多层感知机, 深度学习

## 3 点简述
- 核心问题：网络表格数据规模大、特征异构且分布复杂，导致传统模型可扩展性差和特征工程繁琐
- 方法要点：结合KAN前端学习特征非线性变换和gMLP骨干捕获高阶交互，实现自动建模
- 实验或效果：在公开基准和工业数据集上验证了KMLP的先进性能，规模越大优势越明显

## 摘要（原文）

> Predictive modeling on web-scale tabular data with billions of instances and hundreds of heterogeneous numerical features faces significant scalability challenges. These features exhibit anisotropy, heavy-tailed distributions, and non-stationarity, creating bottlenecks for models like Gradient Boosting Decision Trees and requiring laborious manual feature engineering. We introduce KMLP, a hybrid deep architecture integrating a shallow Kolmogorov-Arnold Network (KAN) front-end with a Gated Multilayer Perceptron (gMLP) backbone. The KAN front-end uses learnable activation functions to automatically model complex non-linear transformations for each feature, while the gMLP backbone captures high-order interactions. Experiments on public benchmarks and an industrial dataset with billions of samples show KMLP achieves state-of-the-art performance, with advantages over baselines like GBDTs increasing at larger scales, validating KMLP as a scalable deep learning paradigm for large-scale web tabular data.

