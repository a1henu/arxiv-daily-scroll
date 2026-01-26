---
layout: default
title: A Refinement of Vapnik--Chervonenkis' Theorem
---

# A Refinement of Vapnik--Chervonenkis' Theorem
**arXiv**：[2601.16411v1](https://arxiv.org/abs/2601.16411) · [PDF](https://arxiv.org/pdf/2601.16411.pdf)  
**作者**：A. Iosevich, A. Vagharshakyan, E. Wyman  

**一句话要点**：使用正态近似改进Vapnik-Chervonenkis定理，提升大样本下的均匀收敛率估计精度。

**关键词**：Vapnik-Chervonenkis定理, 均匀收敛, 正态近似, Berry-Esseen误差, 概率论证, 机器学习理论

## 3 点简述
- 核心问题：经典VC定理在概率论证中依赖Hoeffding不等式，可能导致收敛率估计不够精确。
- 方法要点：采用正态近似并控制Berry-Esseen误差，替代Hoeffding不等式，优化概率论证步骤。
- 实验或效果：在ε√n较大时，主导指数项增加(ε√n)^{-1}因子，实现中等偏差下的收敛率锐化。

## 摘要（原文）

> Vapnik--Chervonenkis' theorem is a seminal result in machine learning. It establishes sufficient conditions for empirical probabilities to converge to theoretical probabilities, uniformly over families of events. It also provides an estimate for the rate of such uniform convergence.
>   We revisit the probabilistic component of the classical argument. Instead of applying Hoeffding's inequality at the final step, we use a normal approximation with explicit Berry--Esseen error control. This yields a moderate-deviation sharpening of the usual VC estimate, with an additional factor of order $(\varepsilon\sqrt{n})^{-1}$ in the leading exponential term when $\varepsilon\sqrt{n}$ is large.

