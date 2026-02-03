---
layout: default
title: Finite-Sample Wasserstein Error Bounds and Concentration Inequalities for Nonlinear Stochastic Approximation
---

# Finite-Sample Wasserstein Error Bounds and Concentration Inequalities for Nonlinear Stochastic Approximation
**arXiv**：[2602.02445v1](https://arxiv.org/abs/2602.02445) · [PDF](https://arxiv.org/pdf/2602.02445.pdf)  
**作者**：Seo Taek Kong, R. Srikant  

**一句话要点**：提出非线性随机逼近算法的有限样本Wasserstein误差界与集中不等式

**关键词**：非线性随机逼近, Wasserstein距离, 有限样本分析, Ornstein-Uhlenbeck过程, Polyak-Ruppert平均, 集中不等式

## 3 点简述
- 核心问题：推导非线性随机逼近算法在Wasserstein距离下的非渐近误差界，以提供有限样本保证。
- 方法要点：通过耦合离散时间过程与极限Ornstein-Uhlenbeck过程，分析末次迭代和Polyak-Ruppert平均的收敛速率。
- 实验或效果：应用于线性随机逼近和随机梯度下降，量化迭代从重尾到高斯行为的过渡，并建立收敛到中心极限定理的速率。

## 摘要（原文）

> This paper derives non-asymptotic error bounds for nonlinear stochastic approximation algorithms in the Wasserstein-$p$ distance. To obtain explicit finite-sample guarantees for the last iterate, we develop a coupling argument that compares the discrete-time process to a limiting Ornstein-Uhlenbeck process. Our analysis applies to algorithms driven by general noise conditions, including martingale differences and functions of ergodic Markov chains. Complementing this result, we handle the convergence rate of the Polyak-Ruppert average through a direct analysis that applies under the same general setting.
>   Assuming the driving noise satisfies a non-asymptotic central limit theorem, we show that the normalized last iterates converge to a Gaussian distribution in the $p$-Wasserstein distance at a rate of order $γ_n^{1/6}$, where $γ_n$ is the step size. Similarly, the Polyak-Ruppert average is shown to converge in the Wasserstein distance at a rate of order $n^{-1/6}$. These distributional guarantees imply high-probability concentration inequalities that improve upon those derived from moment bounds and Markov's inequality. We demonstrate the utility of this approach by considering two applications: (1) linear stochastic approximation, where we explicitly quantify the transition from heavy-tailed to Gaussian behavior of the iterates, thereby bridging the gap between recent finite-sample analyses and asymptotic theory and (2) stochastic gradient descent, where we establish rate of convergence to the central limit theorem.

