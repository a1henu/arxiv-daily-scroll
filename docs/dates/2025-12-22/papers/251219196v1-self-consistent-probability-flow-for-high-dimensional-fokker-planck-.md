---
layout: default
title: Self-Consistent Probability Flow for High-Dimensional Fokker-Planck Equations
---

# Self-Consistent Probability Flow for High-Dimensional Fokker-Planck Equations
**arXiv**：[2512.19196v1](https://arxiv.org/abs/2512.19196) · [PDF](https://arxiv.org/pdf/2512.19196.pdf)  
**作者**：Xiaolong Wu, Qifeng Liao  

**一句话要点**：提出自洽概率流方法以解决高维Fokker-Planck方程的计算难题

**关键词**：Fokker-Planck方程, 概率流方法, 连续归一化流, 高维计算, 自适应采样, 深度学习

## 3 点简述
- 高维Fokker-Planck方程求解面临维度灾难和二阶项计算瓶颈
- 将二阶方程转化为一阶概率流ODE约束，避免显式Hessian计算
- 结合连续归一化流和Hutchinson迹估计器，实现线性复杂度训练

## 摘要（原文）

> Solving high-dimensional Fokker-Planck (FP) equations is a challenge in computational physics and stochastic dynamics, due to the curse of dimensionality (CoD) and the bottleneck of evaluating second-order diffusion terms. Existing deep learning approaches, such as Physics-Informed Neural Networks (PINNs), face computational challenges as dimensionality increases, driven by the $O(D^2)$ complexity of automatic differentiation for second-order derivatives. While recent probability flow approaches bypass this by learning score functions or matching velocity fields, they often involve serial computational operations or depend on sampling efficiency in complex distributions. To address these issues, we propose the Self-Consistent Probability Flow (SCPF) method. We reformulate the second-order FP equation into an equivalent first-order deterministic Probability Flow ODE (PF-ODE) constraint. Unlike score matching or velocity matching, SCPF solves this problem by minimizing the residual of the PF-ODE continuity equation, which avoids explicit Hessian computation. We leverage Continuous Normalizing Flows (CNF) combined with the Hutchinson Trace Estimator (HTE) to reduce the training complexity to linear scale $O(D)$, achieving an effective $O(1)$ wall-clock time on GPUs. To address data sparsity in high dimensions, we apply a generative adaptive sampling strategy and theoretically prove that dynamically aligning collocation points with the evolving probability mass is a necessary condition to bound the approximation error. Experiments on diverse benchmarks -- ranging from anisotropic Ornstein-Uhlenbeck (OU) processes and high-dimensional Brownian motions with time-varying diffusion terms, to Geometric OU processes featuring non-Gaussian solutions -- demonstrate that SCPF effectively mitigates the CoD, maintaining high accuracy and constant computational cost for problems up to 100 dimensions.

