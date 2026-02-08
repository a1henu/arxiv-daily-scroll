---
layout: default
title: Dimensionality Reduction on Riemannian Manifolds in Data Analysis
---

# Dimensionality Reduction on Riemannian Manifolds in Data Analysis
**arXiv**：[2602.05936v1](https://arxiv.org/abs/2602.05936) · [PDF](https://arxiv.org/pdf/2602.05936.pdf)  
**作者**：Alaa El Ichi, Khalide Jbilou  

**一句话要点**：研究黎曼流形降维方法，提升流形数据表示与分类性能

**关键词**：黎曼流形降维, 主测地线分析, 流形学习, 几何感知机器学习, 非线性降维

## 3 点简述
- 核心问题：数据位于黎曼流形时，传统欧氏降维方法可能失真，需几何感知降维。
- 方法要点：基于主测地线分析等，利用测地距离和切空间表示，扩展判别分析至流形。
- 实验效果：在超球面和对称正定流形等数据集上，黎曼方法优于欧氏方法，提升表示质量和分类性能。

## 摘要（原文）

> In this work, we investigate Riemannian geometry based dimensionality reduction methods that respect the underlying manifold structure of the data. In particular, we focus on Principal Geodesic Analysis (PGA) as a nonlinear generalization of PCA for manifold valued data, and extend discriminant analysis through Riemannian adaptations of other known dimensionality reduction methods. These approaches exploit geodesic distances, tangent space representations, and intrinsic statistical measures to achieve more faithful low dimensional embeddings. We also discuss related manifold learning techniques and highlight their theoretical foundations and practical advantages. Experimental results on representative datasets demonstrate that Riemannian methods provide improved representation quality and classification performance compared to their Euclidean counterparts, especially for data constrained to curved spaces such as hyperspheres and symmetric positive definite manifolds. This study underscores the importance of geometry aware dimensionality reduction in modern machine learning and data science applications.

