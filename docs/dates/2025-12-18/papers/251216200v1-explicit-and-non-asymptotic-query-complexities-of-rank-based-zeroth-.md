---
layout: default
title: Explicit and Non-asymptotic Query Complexities of Rank-Based Zeroth-order Algorithms on Smooth Functions
---

# Explicit and Non-asymptotic Query Complexities of Rank-Based Zeroth-order Algorithms on Smooth Functions
**arXiv**：[2512.16200v1](https://arxiv.org/abs/2512.16200) · [PDF](https://arxiv.org/pdf/2512.16200.pdf)  
**作者**：Haishan Ye  

**一句话要点**：提出基于排序的零阶算法，首次给出平滑函数上显式非渐近查询复杂度分析。

**关键词**：零阶优化, 排序算法, 查询复杂度, 平滑函数, 非渐近分析

## 3 点简述
- 核心问题：现有基于排序的零阶方法理论分析有限，缺乏显式收敛率。
- 方法要点：分析简单算法，针对平滑强凸和非凸函数建立显式查询复杂度。
- 实验或效果：算法在d维问题中达到特定复杂度，概率至少1-δ，提供新理论见解。

## 摘要（原文）

> Rank-based zeroth-order (ZO) optimization -- which relies only on the ordering of function evaluations -- offers strong robustness to noise and monotone transformations, and underlies many successful algorithms such as CMA-ES, natural evolution strategies, and rank-based genetic algorithms. Despite its widespread use, the theoretical understanding of rank-based ZO methods remains limited: existing analyses provide only asymptotic insights and do not yield explicit convergence rates for algorithms selecting the top-$k$ directions.
>   This work closes this gap by analyzing a simple rank-based ZO algorithm and establishing the first \emph{explicit}, and \emph{non-asymptotic} query complexities. For a $d$-dimension problem, if the function is $L$-smooth and $μ$-strongly convex, the algorithm achieves $\widetilde{\mathcal O}\!\left(\frac{dL}μ\log\!\frac{dL}{μδ}\log\!\frac{1}{\varepsilon}\right)$ to find an $\varepsilon$-suboptimal solution, and for smooth nonconvex objectives it reaches $\mathcal O\!\left(\frac{dL}{\varepsilon}\log\!\frac{1}{\varepsilon}\right)$. Notation $\cO(\cdot)$ hides constant terms and $\widetilde{\mathcal O}(\cdot)$ hides extra $\log\log\frac{1}{\varepsilon}$ term. These query complexities hold with a probability at least $1-δ$ with $0<δ<1$. The analysis in this paper is novel and avoids classical drift and information-geometric techniques. Our analysis offers new insight into why rank-based heuristics lead to efficient ZO optimization.

