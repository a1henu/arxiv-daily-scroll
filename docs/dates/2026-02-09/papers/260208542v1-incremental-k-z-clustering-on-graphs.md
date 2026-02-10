---
layout: default
title: Incremental (k, z)-Clustering on Graphs
---

# Incremental (k, z)-Clustering on Graphs
**arXiv**：[2602.08542v1](https://arxiv.org/abs/2602.08542) · [PDF](https://arxiv.org/pdf/2602.08542.pdf)  
**作者**：Emilio Cruciani, Sebastian Forster, Antonis Skarlatos  

**一句话要点**：提出增量(k,z)-聚类算法，在动态图中维护常数近似解。

**关键词**：动态图聚类, 增量算法, 常数近似, 双准则近似, 最短路径度量

## 3 点简述
- 核心问题：动态图中(k,z)-聚类，需应对边插入更新。
- 方法要点：两阶段算法，先维护双准则近似解，再基于此动态聚类。
- 实验或效果：总更新时间为Õ(km^{1+o(1)}+k^{1+1/λ}m)，高概率常数近似。

## 摘要（原文）

> Given a weighted undirected graph, a number of clusters $k$, and an exponent $z$, the goal in the $(k, z)$-clustering problem on graphs is to select $k$ vertices as centers that minimize the sum of the distances raised to the power $z$ of each vertex to its closest center. In the dynamic setting, the graph is subject to adversarial edge updates, and the goal is to maintain explicitly an exact $(k, z)$-clustering solution in the induced shortest-path metric.
>   While efficient dynamic $k$-center approximation algorithms on graphs exist [Cruciani et al. SODA 2024], to the best of our knowledge, no prior work provides similar results for the dynamic $(k,z)$-clustering problem. As the main result of this paper, we develop a randomized incremental $(k, z)$-clustering algorithm that maintains with high probability a constant-factor approximation in a graph undergoing edge insertions with a total update time of $\tilde O(k m^{1+o(1)}+ k^{1+\frac{1}λ} m)$, where $λ\geq 1$ is an arbitrary fixed constant. Our incremental algorithm consists of two stages. In the first stage, we maintain a constant-factor bicriteria approximate solution of size $\tilde{O}(k)$ with a total update time of $m^{1+o(1)}$ over all adversarial edge insertions. This first stage is an intricate adaptation of the bicriteria approximation algorithm by Mettu and Plaxton [Machine Learning 2004] to incremental graphs. One of our key technical results is that the radii in their algorithm can be assumed to be non-decreasing while the approximation ratio remains constant, a property that may be of independent interest.
>   In the second stage, we maintain a constant-factor approximate $(k,z)$-clustering solution on a dynamic weighted instance induced by the bicriteria approximate solution. For this subproblem, we employ a dynamic spanner algorithm together with a static $(k,z)$-clustering algorithm.

