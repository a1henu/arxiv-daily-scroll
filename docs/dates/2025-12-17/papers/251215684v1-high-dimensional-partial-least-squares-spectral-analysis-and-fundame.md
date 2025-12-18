---
layout: default
title: High-Dimensional Partial Least Squares: Spectral Analysis and Fundamental Limitations
---

# High-Dimensional Partial Least Squares: Spectral Analysis and Fundamental Limitations
**arXiv**：[2512.15684v1](https://arxiv.org/abs/2512.15684) · [PDF](https://arxiv.org/pdf/2512.15684.pdf)  
**作者**：Victor Léger, Florent Chatelain  

**一句话要点**：分析高维偏最小二乘的谱特性与理论局限，阐明其数据整合性能

**关键词**：高维数据分析, 偏最小二乘, 随机矩阵理论, 数据整合, 谱分析

## 3 点简述
- 研究高维数据整合中偏最小二乘的理论行为，模型包含共享低秩结构与个体特定成分
- 使用随机矩阵理论分析交叉协方差矩阵的奇异向量，推导估计方向与真实方向的渐近对齐
- 比较偏最小二乘与主成分分析，展示其在检测公共潜在子空间中的渐近优越性

## 摘要（原文）

> Partial Least Squares (PLS) is a widely used method for data integration, designed to extract latent components shared across paired high-dimensional datasets. Despite decades of practical success, a precise theoretical understanding of its behavior in high-dimensional regimes remains limited. In this paper, we study a data integration model in which two high-dimensional data matrices share a low-rank common latent structure while also containing individual-specific components. We analyze the singular vectors of the associated cross-covariance matrix using tools from random matrix theory and derive asymptotic characterizations of the alignment between estimated and true latent directions. These results provide a quantitative explanation of the reconstruction performance of the PLS variant based on Singular Value Decomposition (PLS-SVD) and identify regimes where the method exhibits counter-intuitive or limiting behavior. Building on this analysis, we compare PLS-SVD with principal component analysis applied separately to each dataset and show its asymptotic superiority in detecting the common latent subspace. Overall, our results offer a comprehensive theoretical understanding of high-dimensional PLS-SVD, clarifying both its advantages and fundamental limitations.

