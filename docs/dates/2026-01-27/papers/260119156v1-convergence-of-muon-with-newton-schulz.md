---
layout: default
title: Convergence of Muon with Newton-Schulz
---

# Convergence of Muon with Newton-Schulz
**arXiv**：[2601.19156v1](https://arxiv.org/abs/2601.19156) · [PDF](https://arxiv.org/pdf/2601.19156.pdf)  
**作者**：Gyu Yeol Kim, Min-hwan Oh  

**一句话要点**：证明Muon结合Newton-Schulz收敛至平稳点，匹配SVD理想化速率，缩小实践与理论差距。

**关键词**：Muon优化器, Newton-Schulz迭代, 动量正交化, 收敛分析, 矩阵优化, 实践理论差距

## 3 点简述
- 分析Muon优化器在实践中的关键步骤：使用动量正交化和Newton-Schulz近似正交方向。
- 证明Muon与Newton-Schulz收敛速率与基于SVD的理想化版本相同，常数因子随Newton-Schulz步数双指数收敛至1。
- 理论解释Muon通过Newton-Schulz在更短计算时间内匹配SVD行为，并优于基于向量的优化器如SGD with momentum。

## 摘要（原文）

> We analyze Muon as originally proposed and used in practice -- using the momentum orthogonalization with a few Newton-Schulz steps. The prior theoretical results replace this key step in Muon with an exact SVD-based polar factor. We prove that Muon with Newton-Schulz converges to a stationary point at the same rate as the SVD-polar idealization, up to a constant factor for a given number $q$ of Newton-Schulz steps. We further analyze this constant factor and prove that it converges to 1 doubly exponentially in $q$ and improves with the degree of the polynomial used in Newton-Schulz for approximating the orthogonalization direction. We also prove that Muon removes the typical square-root-of-rank loss compared to its vector-based counterpart, SGD with momentum. Our results explain why Muon with a few low-degree Newton-Schulz steps matches exact-polar (SVD) behavior at a much faster wall-clock time and explain how much momentum matrix orthogonalization via Newton-Schulz benefits over the vector-based optimizer. Overall, our theory justifies the practical Newton-Schulz design of Muon, narrowing its practice-theory gap.

