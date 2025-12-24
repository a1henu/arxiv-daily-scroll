---
layout: default
title: Avoiding the Price of Adaptivity: Inference in Linear Contextual Bandits via Stability
---

# Avoiding the Price of Adaptivity: Inference in Linear Contextual Bandits via Stability
**arXiv**：[2512.20368v1](https://arxiv.org/abs/2512.20368) · [PDF](https://arxiv.org/pdf/2512.20368.pdf)  
**作者**：Samya Praharaj, Koulik Khamaru  

**一句话要点**：提出惩罚EXP4算法以在线性上下文赌博机中实现稳定推断，避免适应性代价

**关键词**：线性上下文赌博机, 统计推断, 稳定性条件, 惩罚EXP4算法, 适应性代价, 置信区间

## 3 点简述
- 核心问题：自适应采样导致经典最小二乘推断失效，需支付适应性代价
- 方法要点：基于Lai-Wei稳定性条件，设计惩罚EXP4算法，满足稳定性并支持Wald型置信区间
- 实验或效果：算法实现最小化最优遗憾，模拟验证估计量正态性和置信区间锐度

## 摘要（原文）

> Statistical inference in contextual bandits is complicated by the adaptive, non-i.i.d. nature of the data. A growing body of work has shown that classical least-squares inference may fail under adaptive sampling, and that constructing valid confidence intervals for linear functionals of the model parameter typically requires paying an unavoidable inflation of order $\sqrt{d \log T}$. This phenomenon -- often referred to as the price of adaptivity -- highlights the inherent difficulty of reliable inference under general contextual bandit policies.
>   A key structural property that circumvents this limitation is the \emph{stability} condition of Lai and Wei, which requires the empirical feature covariance to concentrate around a deterministic limit. When stability holds, the ordinary least-squares estimator satisfies a central limit theorem, and classical Wald-type confidence intervals -- designed for i.i.d. data -- become asymptotically valid even under adaptation, \emph{without} incurring the $\sqrt{d \log T}$ price of adaptivity.
>   In this paper, we propose and analyze a penalized EXP4 algorithm for linear contextual bandits. Our first main result shows that this procedure satisfies the Lai--Wei stability condition and therefore admits valid Wald-type confidence intervals for linear functionals. Our second result establishes that the same algorithm achieves regret guarantees that are minimax optimal up to logarithmic factors, demonstrating that stability and statistical efficiency can coexist within a single contextual bandit method. Finally, we complement our theory with simulations illustrating the empirical normality of the resulting estimators and the sharpness of the corresponding confidence intervals.

