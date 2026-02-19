---
layout: default
title: On the Hardness of Approximation of the Fair k-Center Problem
---

# On the Hardness of Approximation of the Fair k-Center Problem
**arXiv**：[2602.16688v1](https://arxiv.org/abs/2602.16688) · [PDF](https://arxiv.org/pdf/2602.16688.pdf)  
**作者**：Suhas Thejaswi  

**一句话要点**：证明公平k中心问题的(3-ε)近似是NP难的，确立3近似最优性

**关键词**：公平k中心问题, 近似硬度, NP难, 组合优化, 度量空间, 算法最优性

## 3 点简述
- 研究公平k中心问题的近似硬度，数据点分组需从每组选指定数量中心
- 证明在P≠NP下，对任意ε>0，(3-ε)近似是NP难的，即使仅两组且每组至少选一中心
- 结果扩展至每组选一中心的k组设置，表明现有3近似算法在一般度量空间最优

## 摘要（原文）

> In this work, we study the hardness of approximation of the fair $k$-center problem. Here the data points are partitioned into groups and the task is to choose a prescribed number of data points from each group, called centers, while minimizing the maximum distance from any point to its closest center. Although a polynomial-time $3$-approximation is known for this problem in general metrics, it has remained open whether this approximation guarantee is tight or could be further improved, especially since the unconstrained $k$-center problem admits a polynomial-time factor-$2$ approximation. We resolve this open question by proving that, for every $ε>0$, achieving a $(3-ε)$-approximation is NP-hard, assuming $\text{P} \neq \text{NP}$.
>   Our inapproximability results hold even when only two disjoint groups are present and at least one center must be chosen from each group. Further, it extends to the canonical one-per-group setting with $k$-groups (for arbitrary $k$), where exactly one center must be selected from each group. Consequently, the factor-$3$ barrier for fair $k$-center in general metric spaces is inherent, and existing $3$-approximation algorithms are optimal up to lower-order terms even in these restricted regimes. This result stands in sharp contrast to the $k$-supplier formulation, where both the unconstrained and fair variants admit factor-$3$ approximation in polynomial time.

