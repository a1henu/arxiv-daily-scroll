---
layout: default
title: Better Learning-Augmented Spanning Tree Algorithms via Metric Forest Completion
---

# Better Learning-Augmented Spanning Tree Algorithms via Metric Forest Completion
**arXiv**：[2602.24232v1](https://arxiv.org/abs/2602.24232) · [PDF](https://arxiv.org/pdf/2602.24232.pdf)  
**作者**：Nate Veldt, Thomas Stanley, Benjamin W. Priest, Trevor Steil, Keita Iwabuchi, T. S. Jayram, Grace J. Li, Geoffrey Sanders  

**一句话要点**：提出基于度量森林补全的改进学习增强算法，以优化度量空间中近似最小生成树的计算。

**关键词**：学习增强算法, 度量森林补全, 近似最小生成树, 计算复杂度, 代表性点选择, 实验评估

## 3 点简述
- 核心问题：在任意度量空间中，学习增强的近似最小生成树算法面临高计算复杂度与近似比权衡。
- 方法要点：通过选择代表性点并插值现有算法，改进度量森林补全的近似比至2，并推广至实例特定优化。
- 实验或效果：理论分析证明紧界，并通过实验评估验证算法性能提升。

## 摘要（原文）

> We present improved learning-augmented algorithms for finding an approximate minimum spanning tree (MST) for points in an arbitrary metric space. Our work follows a recent framework called metric forest completion (MFC), where the learned input is a forest that must be given additional edges to form a full spanning tree. Veldt et al. (2025) showed that optimally completing the forest takes $Ω(n^2)$ time, but designed a 2.62-approximation for MFC with subquadratic complexity. The same method is a $(2γ+ 1)$-approximation for the original MST problem, where $γ\geq 1$ is a quality parameter for the initial forest. We introduce a generalized method that interpolates between this prior algorithm and an optimal $Ω(n^2)$-time MFC algorithm. Our approach considers only edges incident to a growing number of strategically chosen ``representative'' points. One corollary of our analysis is to improve the approximation factor of the previous algorithm from 2.62 for MFC and $(2γ+1)$ for metric MST to 2 and $2γ$ respectively. We prove this is tight for worst-case instances, but we still obtain better instance-specific approximations using our generalized method. We complement our theoretical results with a thorough experimental evaluation.

