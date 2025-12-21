---
layout: default
title: Learning Confidence Ellipsoids and Applications to Robust Subspace Recovery
---

# Learning Confidence Ellipsoids and Applications to Robust Subspace Recovery
**arXiv**：[2512.16875v1](https://arxiv.org/abs/2512.16875) · [PDF](https://arxiv.org/pdf/2512.16875.pdf)  
**作者**：Chao Gao, Liren Shan, Vaidehi Srinivas, Aravindan Vijayaraghavan  

**一句话要点**：提出高效算法以解决高维分布中置信椭球体的体积近似问题

**关键词**：置信椭球体, 高维统计, 鲁棒子空间恢复, 多项式时间算法, 体积近似, 条件数

## 3 点简述
- 研究高维分布中最小体积置信椭球体的计算问题，关注条件数有界时的近似保证
- 开发多项式时间算法，在体积上提供与最佳β条件椭球体的近似因子，并覆盖指定概率质量
- 算法基于最小体积包围椭球体的原始对偶结构和几何Brascamp-Lieb不等式，应用于鲁棒子空间恢复

## 摘要（原文）

> We study the problem of finding confidence ellipsoids for an arbitrary distribution in high dimensions. Given samples from a distribution $D$ and a confidence parameter $α$, the goal is to find the smallest volume ellipsoid $E$ which has probability mass $\Pr_{D}[E] \ge 1-α$. Ellipsoids are a highly expressive class of confidence sets as they can capture correlations in the distribution, and can approximate any convex set. This problem has been studied in many different communities. In statistics, this is the classic minimum volume estimator introduced by Rousseeuw as a robust non-parametric estimator of location and scatter. However in high dimensions, it becomes NP-hard to obtain any non-trivial approximation factor in volume when the condition number $β$ of the ellipsoid (ratio of the largest to the smallest axis length) goes to $\infty$. This motivates the focus of our paper: can we efficiently find confidence ellipsoids with volume approximation guarantees when compared to ellipsoids of bounded condition number $β$?
>   Our main result is a polynomial time algorithm that finds an ellipsoid $E$ whose volume is within a $O(β^{γd})$ multiplicative factor of the volume of best $β$-conditioned ellipsoid while covering at least $1-O(α/γ)$ probability mass for any $γ< α$. We complement this with a computational hardness result that shows that such a dependence seems necessary up to constants in the exponent. The algorithm and analysis uses the rich primal-dual structure of the minimum volume enclosing ellipsoid and the geometric Brascamp-Lieb inequality. As a consequence, we obtain the first polynomial time algorithm with approximation guarantees on worst-case instances of the robust subspace recovery problem.

