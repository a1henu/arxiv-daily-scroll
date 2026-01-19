---
layout: default
title: Split-and-Conquer: Distributed Factor Modeling for High-Dimensional Matrix-Variate Time Series
---

# Split-and-Conquer: Distributed Factor Modeling for High-Dimensional Matrix-Variate Time Series
**arXiv**：[2601.11091v1](https://arxiv.org/abs/2601.11091) · [PDF](https://arxiv.org/pdf/2601.11091.pdf)  
**作者**：Hangjin Jiang, Yuzhou Li, Zhaoxing Gao  

**一句话要点**：提出分布式因子建模框架以处理高维矩阵时间序列的降维问题

**关键词**：矩阵时间序列, 分布式因子模型, 张量主成分分析, 高维降维, 非平稳时间序列

## 3 点简述
- 核心问题：高维、大规模、异构矩阵时间序列数据的降维与因子建模
- 方法要点：采用分而治之策略，通过分布式节点估计加载矩阵并聚合，保留矩阵结构
- 实验或效果：模拟评估计算效率与估计精度，真实数据验证预测性能

## 摘要（原文）

> In this paper, we propose a distributed framework for reducing the dimensionality of high-dimensional, large-scale, heterogeneous matrix-variate time series data using a factor model. The data are first partitioned column-wise (or row-wise) and allocated to node servers, where each node estimates the row (or column) loading matrix via two-dimensional tensor PCA. These local estimates are then transmitted to a central server and aggregated, followed by a final PCA step to obtain the global row (or column) loading matrix estimator. Given the estimated loading matrices, the corresponding factor matrices are subsequently computed. Unlike existing distributed approaches, our framework preserves the latent matrix structure, thereby improving computational efficiency and enhancing information utilization. We also discuss row- and column-wise clustering procedures for settings in which the group memberships are unknown. Furthermore, we extend the analysis to unit-root nonstationary matrix-variate time series. Asymptotic properties of the proposed method are derived for the diverging dimension of the data in each computing unit and the sample size $T$. Simulation results assess the computational efficiency and estimation accuracy of the proposed framework, and real data applications further validate its predictive performance.

