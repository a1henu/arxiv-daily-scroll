---
layout: default
title: Modeling high dimensional point clouds with the spherical cluster model
---

# Modeling high dimensional point clouds with the spherical cluster model
**arXiv**：[2512.21960v1](https://arxiv.org/abs/2512.21960) · [PDF](https://arxiv.org/pdf/2512.21960.pdf)  
**作者**：Frédéric Cazals, Antoine Commaret, Louis Goldenberg  

**一句话要点**：提出球形聚类模型以处理高维点云数据，提供参数化几何洞察和高效求解方法。

**关键词**：球形聚类模型, 高维点云, 参数化聚类, 精确求解, 几何数据分析, 高维中位数

## 3 点简述
- 核心问题：高维点云数据聚类中，传统方法如KMeans中心可能不稳健，需参数化模型提供几何解释。
- 方法要点：定义球形聚类模型，通过最小化球外点的幂距离成本来优化中心，使用Clarke梯度和分层单元复形进行精确求解。
- 实验效果：在维度9到10,000的数据集上，精确算法比BFGS启发式方法快多个数量级，中心表现为参数化高维中位数。

## 摘要（原文）

> A parametric cluster model is a statistical model providing geometric insights onto the points defining a cluster. The {\em spherical cluster model} (SC) approximates a finite point set $P\subset \mathbb{R}^d$ by a sphere $S(c,r)$ as follows. Taking $r$ as a fraction $η\in(0,1)$ (hyper-parameter) of the std deviation of distances between the center $c$ and the data points, the cost of the SC model is the sum over all data points lying outside the sphere $S$ of their power distance with respect to $S$. The center $c$ of the SC model is the point minimizing this cost. Note that $η=0$ yields the celebrated center of mass used in KMeans clustering. We make three contributions.
>   First, we show fitting a spherical cluster yields a strictly convex but not smooth combinatorial optimization problem. Second, we present an exact solver using the Clarke gradient on a suitable stratified cell complex defined from an arrangement of hyper-spheres. Finally, we present experiments on a variety of datasets ranging in dimension from $d=9$ to $d=10,000$, with two main observations. First, the exact algorithm is orders of magnitude faster than BFGS based heuristics for datasets of small/intermediate dimension and small values of $η$, and for high dimensional datasets (say $d>100$) whatever the value of $η$. Second, the center of the SC model behave as a parameterized high-dimensional median.
>   The SC model is of direct interest for high dimensional multivariate data analysis, and the application to the design of mixtures of SC will be reported in a companion paper.

