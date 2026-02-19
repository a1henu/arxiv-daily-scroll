---
layout: default
title: Ratio Covers of Convex Sets and Optimal Mixture Density Estimation
---

# Ratio Covers of Convex Sets and Optimal Mixture Density Estimation
**arXiv**：[2602.16142v1](https://arxiv.org/abs/2602.16142) · [PDF](https://arxiv.org/pdf/2602.16142.pdf)  
**作者**：Spencer Compton, Gábor Lugosi, Jaouad Mourtada, Jian Qian, Nikita Zhivotovskiy  

**一句话要点**：提出比率覆盖定理与最优混合密度估计方法，解决字典密度无界比与不同支撑下的KL散度估计问题。

**关键词**：密度估计, KL散度, 混合模型, 比率覆盖, 凸集几何, 多目标优化

## 3 点简述
- 研究KL散度下的密度估计，针对字典密度无界比与不同支撑的模型聚合与混合估计问题。
- 通过局部Hellinger熵上界与凸集比率覆盖定理，推导出最优高概率保证率。
- 在混合密度估计中，匹配离散分布下现有下界，几何结果独立应用于多目标优化近似Pareto集。

## 摘要（原文）

> We study density estimation in Kullback-Leibler divergence: given an i.i.d. sample from an unknown density $p$, the goal is to construct an estimator $\widehat p$ such that $\mathrm{KL}(p,\widehat p)$ is small with high probability. We consider two settings involving a finite dictionary of $M$ densities: (i) model aggregation, where $p$ belongs to the dictionary, and (ii) convex aggregation (mixture density estimation), where $p$ is a mixture of densities from the dictionary. Crucially, we make no assumption on the base densities: their ratios may be unbounded and their supports may differ. For both problems, we identify the best possible high-probability guarantees in terms of the dictionary size, sample size, and confidence level. These optimal rates are higher than those achievable when density ratios are bounded by absolute constants; for mixture density estimation, they match existing lower bounds in the special case of discrete distributions.
>   Our analysis of the mixture case hinges on two new covering results. First, we provide a sharp, distribution-free upper bound on the local Hellinger entropy of the class of mixtures of $M$ distributions. Second, we prove an optimal ratio covering theorem for convex sets: for every convex compact set $K\subset \mathbb{R}_+^d$, there exists a subset $A\subset K$ with at most $2^{8d}$ elements such that each element of $K$ is coordinate-wise dominated by an element of $A$ up to a universal constant factor. This geometric result is of independent interest; notably, it yields new cardinality estimates for $\varepsilon$-approximate Pareto sets in multi-objective optimization when the attainable set of objective vectors is convex.

