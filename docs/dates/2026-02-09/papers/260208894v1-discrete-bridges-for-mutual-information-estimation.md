---
layout: default
title: Discrete Bridges for Mutual Information Estimation
---

# Discrete Bridges for Mutual Information Estimation
**arXiv**：[2602.08894v1](https://arxiv.org/abs/2602.08894) · [PDF](https://arxiv.org/pdf/2602.08894.pdf)  
**作者**：Iryna Zabarianska, Sergei Kholkin, Grigoriy Ksenofontov, Ivan Butakov, Alexander Korotin  

**一句话要点**：提出离散桥互信息估计器，以解决离散随机变量互信息估计问题。

**关键词**：互信息估计, 离散桥模型, 域转移, 生成建模, 信息理论

## 3 点简述
- 核心问题：传统互信息估计器难以处理离散数据，需新方法。
- 方法要点：利用离散桥匹配模型，将互信息估计框架为域转移问题。
- 实验或效果：在低维和基于图像的互信息估计设置中展示性能。

## 摘要（原文）

> Diffusion bridge models in both continuous and discrete state spaces have recently become powerful tools in the field of generative modeling. In this work, we leverage the discrete state space formulation of bridge matching models to address another important problem in machine learning and information theory: the estimation of the mutual information (MI) between discrete random variables. By neatly framing MI estimation as a domain transfer problem, we construct a Discrete Bridge Mutual Information (DBMI) estimator suitable for discrete data, which poses difficulties for conventional MI estimators. We showcase the performance of our estimator on two MI estimation settings: low-dimensional and image-based.

