---
layout: default
title: Scalable Uncertainty Quantification for Black-Box Density-Based Clustering
---

# Scalable Uncertainty Quantification for Black-Box Density-Based Clustering
**arXiv**：[2603.03188v1](https://arxiv.org/abs/2603.03188) · [PDF](https://arxiv.org/pdf/2603.03188.pdf)  
**作者**：Nicola Bariletto, Stephen G. Walker  

**一句话要点**：提出基于鞅后验与密度聚类的可扩展不确定性量化框架，适用于高维不规则数据。

**关键词**：不确定性量化, 密度聚类, 鞅后验, 神经密度估计, 可扩展计算, 高维数据

## 3 点简述
- 核心问题：聚类中的不确定性量化，传统方法难以处理高维不规则数据。
- 方法要点：结合鞅后验范式与密度聚类，利用神经密度估计器和GPU并行计算实现可扩展性。
- 实验或效果：建立频率论一致性保证，在合成和真实数据上验证了方法的有效性。

## 摘要（原文）

> We introduce a novel framework for uncertainty quantification in clustering. By combining the martingale posterior paradigm with density-based clustering, uncertainty in the estimated density is naturally propagated to the clustering structure. The approach scales effectively to high-dimensional and irregularly shaped data by leveraging modern neural density estimators and GPU-friendly parallel computation. We establish frequentist consistency guarantees and validate the methodology on synthetic and real data.

