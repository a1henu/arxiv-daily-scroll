---
layout: default
title: KMLP: A Scalable Hybrid Architecture for Web-Scale Tabular Data Modeling
---

# KMLP: A Scalable Hybrid Architecture for Web-Scale Tabular Data Modeling
**arXiv**：[2602.22777v1](https://arxiv.org/abs/2602.22777) · [PDF](https://arxiv.org/pdf/2602.22777.pdf)  
**作者**：Mingming Zhang, Pengfei Shi, Zhiqing Xiao, Feng Zhao, Guandong Sun, Yulin Kang, Ruizhe Gao, Ningtao Wang, Xing Fu, Weiqiang Wang, Junbo Zhao  

**一句话要点**：提出KMLP混合架构以解决大规模网络表格数据建模的可扩展性问题

**关键词**：表格数据建模, 可扩展深度学习, Kolmogorov-Arnold网络, 门控多层感知机, 大规模数据处理

## 3 点简述
- 核心问题：大规模网络表格数据存在各向异性、重尾分布和非平稳性，导致传统模型如梯度提升决策树面临可扩展性瓶颈和手动特征工程负担。
- 方法要点：结合浅层Kolmogorov-Arnold网络前端和门控多层感知机主干，前端学习激活函数自动建模特征非线性变换，主干捕获高阶交互。
- 实验或效果：在公开基准和工业数据集上验证，KMLP实现最先进性能，规模越大优势越明显，适用于大规模网络表格数据。

## 摘要（原文）

> Predictive modeling on web-scale tabular data with billions of instances and hundreds of heterogeneous numerical features faces significant scalability challenges. These features exhibit anisotropy, heavy-tailed distributions, and non-stationarity, creating bottlenecks for models like Gradient Boosting Decision Trees and requiring laborious manual feature engineering. We introduce KMLP, a hybrid deep architecture integrating a shallow Kolmogorov-Arnold Network (KAN) front-end with a Gated Multilayer Perceptron (gMLP) backbone. The KAN front-end uses learnable activation functions to automatically model complex non-linear transformations for each feature, while the gMLP backbone captures high-order interactions. Experiments on public benchmarks and an industrial dataset with billions of samples show KMLP achieves state-of-the-art performance, with advantages over baselines like GBDTs increasing at larger scales, validating KMLP as a scalable deep learning paradigm for large-scale web tabular data.

