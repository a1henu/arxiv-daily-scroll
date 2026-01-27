---
layout: default
title: PolySHAP: Extending KernelSHAP with Interaction-Informed Polynomial Regression
---

# PolySHAP: Extending KernelSHAP with Interaction-Informed Polynomial Regression
**arXiv**：[2601.18608v1](https://arxiv.org/abs/2601.18608) · [PDF](https://arxiv.org/pdf/2601.18608.pdf)  
**作者**：Fabian Fumagalli, R. Teal Witter, Christopher Musco  

**一句话要点**：提出PolySHAP方法，通过多项式回归扩展KernelSHAP以捕捉特征交互，提升Shapley值估计精度。

**关键词**：可解释人工智能, Shapley值, 多项式回归, 特征交互, 配对采样

## 3 点简述
- 核心问题：KernelSHAP使用线性近似，忽略特征间非线性交互，可能导致Shapley值估计不准确。
- 方法要点：PolySHAP采用高阶多项式回归近似游戏函数，捕获特征交互，理论证明估计一致性。
- 实验或效果：在多个基准数据集上，PolySHAP实证优于KernelSHAP，并揭示配对采样与二阶多项式等价。

## 摘要（原文）

> Shapley values have emerged as a central game-theoretic tool in explainable AI (XAI). However, computing Shapley values exactly requires $2^d$ game evaluations for a model with $d$ features. Lundberg and Lee's KernelSHAP algorithm has emerged as a leading method for avoiding this exponential cost. KernelSHAP approximates Shapley values by approximating the game as a linear function, which is fit using a small number of game evaluations for random feature subsets.
>   In this work, we extend KernelSHAP by approximating the game via higher degree polynomials, which capture non-linear interactions between features. Our resulting PolySHAP method yields empirically better Shapley value estimates for various benchmark datasets, and we prove that these estimates are consistent.
>   Moreover, we connect our approach to paired sampling (antithetic sampling), a ubiquitous modification to KernelSHAP that improves empirical accuracy. We prove that paired sampling outputs exactly the same Shapley value approximations as second-order PolySHAP, without ever fitting a degree 2 polynomial. To the best of our knowledge, this finding provides the first strong theoretical justification for the excellent practical performance of the paired sampling heuristic.

