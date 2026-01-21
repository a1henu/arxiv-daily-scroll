---
layout: default
title: Unified Unbiased Variance Estimation for MMD: Robust Finite-Sample Performance with Imbalanced Data and Exact Acceleration under Null and Alternative Hypotheses
---

# Unified Unbiased Variance Estimation for MMD: Robust Finite-Sample Performance with Imbalanced Data and Exact Acceleration under Null and Alternative Hypotheses
**arXiv**：[2601.13874v1](https://arxiv.org/abs/2601.13874) · [PDF](https://arxiv.org/pdf/2601.13874.pdf)  
**作者**：Shijie Zhong, Jiangfeng Fu, Yikun Yang  

**一句话要点**：提出统一无偏方差估计与精确加速方法，提升MMD在非平衡数据下的鲁棒性与计算效率。

**关键词**：最大均值差异, 方差估计, 两样本检验, 非平衡数据, 计算加速, 拉普拉斯核

## 3 点简述
- 核心问题：MMD方差估计在零假设、备择假设及非平衡采样下缺乏统一有限样本表征。
- 方法要点：基于U统计量与Hoeffding分解，建立统一方差表征，并针对拉普拉斯核提出精确加速算法。
- 实验或效果：在单变量拉普拉斯核下，计算复杂度从O(n²)降至O(n log n)，增强鲁棒性。

## 摘要（原文）

> The maximum mean discrepancy (MMD) is a kernel-based nonparametric statistic for two-sample testing, whose inferential accuracy depends critically on variance characterization. Existing work provides various finite-sample estimators of the MMD variance, often differing under the null and alternative hypotheses and across balanced or imbalanced sampling schemes. In this paper, we study the variance of the MMD statistic through its U-statistic representation and Hoeffding decomposition, and establish a unified finite-sample characterization covering different hypotheses and sample configurations. Building on this analysis, we propose an exact acceleration method for the univariate case under the Laplacian kernel, which reduces the overall computational complexity from $\mathcal O(n^2)$ to $\mathcal O(n \log n)$.

