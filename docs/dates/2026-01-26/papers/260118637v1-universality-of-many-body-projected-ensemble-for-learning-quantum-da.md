---
layout: default
title: Universality of Many-body Projected Ensemble for Learning Quantum Data Distribution
---

# Universality of Many-body Projected Ensemble for Learning Quantum Data Distribution
**arXiv**：[2601.18637v1](https://arxiv.org/abs/2601.18637) · [PDF](https://arxiv.org/pdf/2601.18637.pdf)  
**作者**：Quoc Hoan Tran, Koki Chinzei, Yasuhiro Endo, Hirotaka Oshima  

**一句话要点**：证明多体投影系综在量子机器学习中的普适性，以近似任意纯态分布。

**关键词**：量子机器学习, 多体投影系综, 普适性定理, 量子态设计, 1-Wasserstein距离, 量子数据分布

## 3 点简述
- 核心问题：量子机器学习中参数化模型能否近似任意量子分布的普适性问题。
- 方法要点：提出多体投影系综框架，证明其能在1-Wasserstein距离内近似任意纯态分布。
- 实验或效果：通过聚类量子态和量子化学数据集验证框架学习复杂量子数据分布的有效性。

## 摘要（原文）

> Generating quantum data by learning the underlying quantum distribution poses challenges in both theoretical and practical scenarios, yet it is a critical task for understanding quantum systems. A fundamental question in quantum machine learning (QML) is the universality of approximation: whether a parameterized QML model can approximate any quantum distribution. We address this question by proving a universality theorem for the Many-body Projected Ensemble (MPE) framework, a method for quantum state design that uses a single many-body wave function to prepare random states. This demonstrates that MPE can approximate any distribution of pure states within a 1-Wasserstein distance error. This theorem provides a rigorous guarantee of universal expressivity, addressing key theoretical gaps in QML. For practicality, we propose an Incremental MPE variant with layer-wise training to improve the trainability. Numerical experiments on clustered quantum states and quantum chemistry datasets validate MPE's efficacy in learning complex quantum data distributions.

