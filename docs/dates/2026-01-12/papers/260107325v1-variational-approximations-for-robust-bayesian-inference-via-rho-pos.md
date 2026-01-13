---
layout: default
title: Variational Approximations for Robust Bayesian Inference via Rho-Posteriors
---

# Variational Approximations for Robust Bayesian Inference via Rho-Posteriors
**arXiv**：[2601.07325v1](https://arxiv.org/abs/2601.07325) · [PDF](https://arxiv.org/pdf/2601.07325.pdf)  
**作者**：EL Mahdi Khribch, Pierre Alquier  

**一句话要点**：提出变分近似方法以解决ρ-后验框架的计算难题，实现鲁棒贝叶斯推断。

**关键词**：鲁棒贝叶斯推断, ρ-后验, 变分近似, PAC-Bayesian框架, 有限样本保证, 吉布斯后验

## 3 点简述
- 核心问题：ρ-后验框架虽具理论优势，但计算困难，因优化参考分布导致后验计算不可行。
- 方法要点：基于温度依赖的吉布斯后验，开发PAC-Bayesian框架，推导有限样本oracle不等式，并引入变分近似继承鲁棒性。
- 实验或效果：数值实验验证方法达到理论污染率，计算可行，首次实现ρ-后验推断的实用化。

## 摘要（原文）

> The $ρ$-posterior framework provides universal Bayesian estimation with explicit contamination rates and optimal convergence guarantees, but has remained computationally difficult due to an optimization over reference distributions that precludes intractable posterior computation. We develop a PAC-Bayesian framework that recovers these theoretical guarantees through temperature-dependent Gibbs posteriors, deriving finite-sample oracle inequalities with explicit rates and introducing tractable variational approximations that inherit the robustness properties of exact $ρ$-posteriors. Numerical experiments demonstrate that this approach achieves theoretical contamination rates while remaining computationally feasible, providing the first practical implementation of $ρ$-posterior inference with rigorous finite-sample guarantees.

