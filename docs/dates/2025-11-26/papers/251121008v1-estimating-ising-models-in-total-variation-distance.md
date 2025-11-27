---
layout: default
title: Estimating Ising Models in Total Variation Distance
---

# Estimating Ising Models in Total Variation Distance
**arXiv**：[2511.21008v1](https://arxiv.org/abs/2511.21008) · [PDF](https://arxiv.org/pdf/2511.21008.pdf)  
**作者**：Constantinos Daskalakis, Vardis Kandiros, Rui Yao  

**一句话要点**：提出最大伪似然估计器统一分析，用于总变差距离下的伊辛模型估计

**关键词**：伊辛模型估计, 总变差距离, 最大伪似然估计器, 算子范数有界, 无穷范数有界, 样本复杂度

## 3 点简述
- 核心问题：估计伊辛模型在总变差距离下的计算与统计效率挑战
- 方法要点：分析MPLE在算子范数有界和无穷范数有界模型类中的性能
- 实验或效果：获得多项式时间算法和最优或近最优样本复杂度保证

## 摘要（原文）

> We consider the problem of estimating Ising models over $n$ variables in Total Variation (TV) distance, given $l$ independent samples from the model. While the statistical complexity of the problem is well-understood [DMR20], identifying computationally and statistically efficient algorithms has been challenging. In particular, remarkable progress has occurred in several settings, such as when the underlying graph is a tree [DP21, BGPV21], when the entries of the interaction matrix follow a Gaussian distribution [GM24, CK24], or when the bulk of its eigenvalues lie in a small interval [AJK+24, KLV24], but no unified framework for polynomial-time estimation in TV exists so far. Our main contribution is a unified analysis of the Maximum Pseudo-Likelihood Estimator (MPLE) for two general classes of Ising models. The first class includes models that have bounded operator norm and satisfy the Modified Log-Sobolev Inequality (MLSI), a functional inequality that was introduced to study the convergence of the associated Glauber dynamics to stationarity. In the second class of models, the interaction matrix has bounded infinity norm (or bounded width), which is the most common assumption in the literature for structure learning of Ising models. We show how our general results for these classes yield polynomial-time algorithms and optimal or near-optimal sample complexity guarantees in a variety of settings. Our proofs employ a variety of tools from tensorization inequalities to measure decompositions and concentration bounds.

