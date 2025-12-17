---
layout: default
title: Maximum Mean Discrepancy with Unequal Sample Sizes via Generalized U-Statistics
---

# Maximum Mean Discrepancy with Unequal Sample Sizes via Generalized U-Statistics
**arXiv**：[2512.13997v1](https://arxiv.org/abs/2512.13997) · [PDF](https://arxiv.org/pdf/2512.13997.pdf)  
**作者**：Aaron Wei, Milad Jalali, Danica J. Sutherland  

**一句话要点**：提出基于广义U-统计量的最大均值差异方法，以解决不等样本量下的两样本测试问题。

**关键词**：最大均值差异, 两样本测试, 不等样本量, 广义U-统计量, 渐近分布, 测试功效优化

## 3 点简述
- 核心问题：现有最大均值差异方法假设等样本量，实际应用需丢弃数据，降低测试功效。
- 方法要点：扩展广义U-统计量理论，推导不等样本量下最大均值差异估计量的渐近分布。
- 实验或效果：新方法保留所有数据，提升测试准确性和适用性，并提供优化测试功效的新准则。

## 摘要（原文）

> Existing two-sample testing techniques, particularly those based on choosing a kernel for the Maximum Mean Discrepancy (MMD), often assume equal sample sizes from the two distributions. Applying these methods in practice can require discarding valuable data, unnecessarily reducing test power. We address this long-standing limitation by extending the theory of generalized U-statistics and applying it to the usual MMD estimator, resulting in new characterization of the asymptotic distributions of the MMD estimator with unequal sample sizes (particularly outside the proportional regimes required by previous partial results). This generalization also provides a new criterion for optimizing the power of an MMD test with unequal sample sizes. Our approach preserves all available data, enhancing test accuracy and applicability in realistic settings. Along the way, we give much cleaner characterizations of the variance of MMD estimators, revealing something that might be surprising to those in the area: while zero MMD implies a degenerate estimator, it is sometimes possible to have a degenerate estimator with nonzero MMD as well; we give a construction and a proof that it does not happen in common situations.

