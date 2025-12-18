---
layout: default
title: Label-consistent clustering for evolving data
---

# Label-consistent clustering for evolving data
**arXiv**：[2512.15210v1](https://arxiv.org/abs/2512.15210) · [PDF](https://arxiv.org/pdf/2512.15210.pdf)  
**作者**：Ameet Gadekar, Aristides Gionis, Thibault Marette  

**一句话要点**：提出标签一致k中心算法，以在数据演化中平衡聚类质量与解决方案一致性。

**关键词**：数据演化聚类, k中心问题, 标签一致性, 近似算法, 迭代优化

## 3 点简述
- 研究数据迭代分析中的聚类更新问题，要求新解在最小化聚类成本的同时限制与先前解的差异。
- 针对标签一致k中心问题，提出两种常数因子近似算法，确保理论性能保证。
- 在真实数据集上实验验证，展示方法在维持聚类质量和一致性方面的有效性。

## 摘要（原文）

> Data analysis often involves an iterative process, where solutions must be continuously refined in response to new data. Typically, as new data becomes available, an existing solution must be updated to incorporate the latest information. In addition to seeking a high-quality solution for the task at hand, it is also crucial to ensure consistency by minimizing drastic changes from previous solutions. Applying this approach across many iterations, ensures that the solution evolves gradually and smoothly.
>   In this paper, we study the above problem in the context of clustering, specifically focusing on the $k$-center problem. More precisely, we study the following problem: Given a set of points $X$, parameters $k$ and $b$, and a prior clustering solution $H$ for $X$, our goal is to compute a new solution $C$ for $X$, consisting of $k$ centers, which minimizes the clustering cost while introducing at most $b$ changes from $H$. We refer to this problem as label-consistent $k$-center, and we propose two constant-factor approximation algorithms for it. We complement our theoretical findings with an experimental evaluation demonstrating the effectiveness of our methods on real-world datasets.

