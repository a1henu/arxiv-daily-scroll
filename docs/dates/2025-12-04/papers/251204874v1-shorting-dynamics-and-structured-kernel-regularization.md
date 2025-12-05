---
layout: default
title: Shorting Dynamics and Structured Kernel Regularization
---

# Shorting Dynamics and Structured Kernel Regularization
**arXiv**：[2512.04874v1](https://arxiv.org/abs/2512.04874) · [PDF](https://arxiv.org/pdf/2512.04874.pdf)  
**作者**：James Tian  

**一句话要点**：提出非线性算子动态以构建不变核并实现结构化正则化

**关键词**：算子动态, 再生核希尔伯特空间, 核岭回归, 结构化正则化, 不变核构造

## 3 点简述
- 核心问题：如何在再生核希尔伯特空间中去除指定特征子空间影响并保留最大结构
- 方法要点：通过单调算子序列收敛到短算子，诱导核族实现核岭回归的规范形式
- 实验或效果：未知

## 摘要（原文）

> This paper develops a nonlinear operator dynamic that progressively removes the influence of a prescribed feature subspace while retaining maximal structure elsewhere. The induced sequence of positive operators is monotone, admits an exact residual decomposition, and converges to the classical shorted operator. Transporting this dynamic to reproducing kernel Hilbert spaces yields a corresponding family of kernels that converges to the largest kernel dominated by the original one and annihilating the given subspace. In the finite-sample setting, the associated Gram operators inherit a structured residual decomposition that leads to a canonical form of kernel ridge regression and a principled way to enforce nuisance invariance. This gives a unified operator-analytic approach to invariant kernel construction and structured regularization in data analysis.

