---
layout: default
title: Minimax optimal differentially private synthetic data for smooth queries
---

# Minimax optimal differentially private synthetic data for smooth queries
**arXiv**：[2602.01607v1](https://arxiv.org/abs/2602.01607) · [PDF](https://arxiv.org/pdf/2602.01607.pdf)  
**作者**：Rundong Ding, Yiyun He, Yizhe Zhu  

**一句话要点**：提出多项式时间算法，为k-光滑查询生成差分隐私合成数据，实现极小极大最优误差率。

**关键词**：差分隐私, 合成数据, 光滑查询, 极小极大优化, 矩匹配, 效用保证

## 3 点简述
- 研究差分隐私合成数据生成，针对超立方体上k-光滑查询的效用保证问题。
- 基于Chebyshev矩匹配框架，提出算法在多项式时间内达到n^{-min{1, k/d}}误差率。
- 建立首个关于k-光滑查询的极小极大下界，揭示k=d处的相变现象。

## 摘要（原文）

> Differentially private synthetic data enables the sharing and analysis of sensitive datasets while providing rigorous privacy guarantees for individual contributors. A central challenge is to achieve strong utility guarantees for meaningful downstream analysis. Many existing methods ensure uniform accuracy over broad query classes, such as all Lipschitz functions, but this level of generality often leads to suboptimal rates for statistics of practical interest. Since many common data analysis queries exhibit smoothness beyond what worst-case Lipschitz bounds capture, we ask whether exploiting this additional structure can yield improved utility.
>   We study the problem of generating $(\varepsilon,δ)$-differentially private synthetic data from a dataset of size $n$ supported on the hypercube $[-1,1]^d$, with utility guarantees uniformly for all smooth queries having bounded derivatives up to order $k$. We propose a polynomial-time algorithm that achieves a minimax error rate of $n^{-\min \{1, \frac{k}{d}\}}$, up to a $\log(n)$ factor. This characterization uncovers a phase transition at $k=d$. Our results generalize the Chebyshev moment matching framework of (Musco et al., 2025; Wang et al., 2016) and strictly improve the error rates for $k$-smooth queries established in (Wang et al., 2016). Moreover, we establish the first minimax lower bound for the utility of $(\varepsilon,δ)$-differentially private synthetic data with respect to $k$-smooth queries, extending the Wasserstein lower bound for $\varepsilon$-differential privacy in (Boedihardjo et al., 2024).

