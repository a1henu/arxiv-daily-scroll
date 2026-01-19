---
layout: default
title: Theoretically and Practically Efficient Resistance Distance Computation on Large Graphs
---

# Theoretically and Practically Efficient Resistance Distance Computation on Large Graphs
**arXiv**：[2601.11159v1](https://arxiv.org/abs/2601.11159) · [PDF](https://arxiv.org/pdf/2601.11159.pdf)  
**作者**：Yichun Yang, Longlong Lin, Rong-Hua Li, Meihao Liao, Guoren Wang  

**一句话要点**：提出Lanczos Iteration和Lanczos Push算法以高效计算大图上的电阻距离

**关键词**：电阻距离计算, 图分析, Lanczos方法, 全局算法, 局部算法, 图拉普拉斯矩阵

## 3 点简述
- 核心问题：现有方法在计算大图电阻距离时，因图拉普拉斯矩阵条件数大而收敛慢。
- 方法要点：基于Lanczos方法设计全局算法Lanczos Iteration和局部算法Lanczos Push，降低对条件数的依赖。
- 实验或效果：在八个真实数据集上验证，新算法在效率和精度上显著优于现有方法。

## 摘要（原文）

> The computation of resistance distance is pivotal in a wide range of graph analysis applications, including graph clustering, link prediction, and graph neural networks. Despite its foundational importance, efficient algorithms for computing resistance distances on large graphs are still lacking. Existing state-of-the-art (SOTA) methods, including power iteration-based algorithms and random walk-based local approaches, often struggle with slow convergence rates, particularly when the condition number of the graph Laplacian matrix, denoted by $κ$, is large. To tackle this challenge, we propose two novel and efficient algorithms inspired by the classic Lanczos method: Lanczos Iteration and Lanczos Push, both designed to reduce dependence on $κ$. Among them, Lanczos Iteration is a near-linear time global algorithm, whereas Lanczos Push is a local algorithm with a time complexity independent of the size of the graph. More specifically, we prove that the time complexity of Lanczos Iteration is $\tilde{O}(\sqrtκ m)$ ($m$ is the number of edges of the graph and $\tilde{O}$ means the complexity omitting the $\log$ terms) which achieves a speedup of $\sqrtκ$ compared to previous power iteration-based global methods. For Lanczos Push, we demonstrate that its time complexity is $\tilde{O}(κ^{2.75})$ under certain mild and frequently established assumptions, which represents a significant improvement of $κ^{0.25}$ over the SOTA random walk-based local algorithms. We validate our algorithms through extensive experiments on eight real-world datasets of varying sizes and statistical properties, demonstrating that Lanczos Iteration and Lanczos Push significantly outperform SOTA methods in terms of both efficiency and accuracy.

