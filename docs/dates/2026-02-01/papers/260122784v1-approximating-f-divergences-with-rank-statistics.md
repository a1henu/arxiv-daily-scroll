---
layout: default
title: Approximating $f$-Divergences with Rank Statistics
---

# Approximating $f$-Divergences with Rank Statistics
**arXiv**：[2601.22784v1](https://arxiv.org/abs/2601.22784) · [PDF](https://arxiv.org/pdf/2601.22784.pdf)  
**作者**：Viktor Stein, José Manuel de Frutos  

**一句话要点**：提出基于秩统计的f-散度近似方法，避免显式密度比估计，用于分布比较与生成建模。

**关键词**：f-散度近似, 秩统计, 分布比较, 生成建模, 高维数据, 收敛分析

## 3 点简述
- 核心问题：传统f-散度估计依赖密度比，计算复杂且在高维中不稳定。
- 方法要点：通过秩直方图映射分布差异，用离散f-散度度量偏差，避免密度比估计。
- 实验或效果：理论证明收敛性，实验验证优于神经基线，适用于生成模型目标。

## 摘要（原文）

> We introduce a rank-statistic approximation of $f$-divergences that avoids explicit density-ratio estimation by working directly with the distribution of ranks. For a resolution parameter $K$, we map the mismatch between two univariate distributions $μ$ and $ν$ to a rank histogram on $\{ 0, \ldots, K\}$ and measure its deviation from uniformity via a discrete $f$-divergence, yielding a rank-statistic divergence estimator. We prove that the resulting estimator of the divergence is monotone in $K$, is always a lower bound of the true $f$-divergence, and we establish quantitative convergence rates for $K\to\infty$ under mild regularity of the quantile-domain density ratio. To handle high-dimensional data, we define the sliced rank-statistic $f$-divergence by averaging the univariate construction over random projections, and we provide convergence results for the sliced limit as well. We also derive finite-sample deviation bounds along with asymptotic normality results for the estimator. Finally, we empirically validate the approach by benchmarking against neural baselines and illustrating its use as a learning objective in generative modelling experiments.

