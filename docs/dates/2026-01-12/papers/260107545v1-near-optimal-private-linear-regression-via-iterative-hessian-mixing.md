---
layout: default
title: Near-Optimal Private Linear Regression via Iterative Hessian Mixing
---

# Near-Optimal Private Linear Regression via Iterative Hessian Mixing
**arXiv**：[2601.07545v1](https://arxiv.org/abs/2601.07545) · [PDF](https://arxiv.org/pdf/2601.07545.pdf)  
**作者**：Omri Lev, Moshe Shenfeld, Vishwak Srinivasan, Katrina Ligett, Ashia C. Wilson  

**一句话要点**：提出迭代Hessian混合算法，用于差分隐私线性回归，超越现有方法性能。

**关键词**：差分隐私, 线性回归, 高斯草图, 迭代Hessian混合, 自适应充分统计扰动

## 3 点简述
- 研究差分隐私普通最小二乘问题，关注有界数据下的最优精度。
- 引入基于高斯草图的迭代Hessian混合算法，改进先前高斯草图方法的分析。
- 实验表明新算法在标准基准上优于自适应充分统计扰动等基线方法。

## 摘要（原文）

> We study differentially private ordinary least squares (DP-OLS) with bounded data. The dominant approach, adaptive sufficient-statistics perturbation (AdaSSP), adds an adaptively chosen perturbation to the sufficient statistics, namely, the matrix $X^{\top}X$ and the vector $X^{\top}Y$, and is known to achieve near-optimal accuracy and to have strong empirical performance. In contrast, methods that rely on Gaussian-sketching, which ensure differential privacy by pre-multiplying the data with a random Gaussian matrix, are widely used in federated and distributed regression, yet remain relatively uncommon for DP-OLS. In this work, we introduce the iterative Hessian mixing, a novel DP-OLS algorithm that relies on Gaussian sketches and is inspired by the iterative Hessian sketch algorithm. We provide utility analysis for the iterative Hessian mixing as well as a new analysis for the previous methods that rely on Gaussian sketches. Then, we show that our new approach circumvents the intrinsic limitations of the prior methods and provides non-trivial improvements over AdaSSP. We conclude by running an extensive set of experiments across standard benchmarks to demonstrate further that our approach consistently outperforms these prior baselines.

