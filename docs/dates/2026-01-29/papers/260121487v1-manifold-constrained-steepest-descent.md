---
layout: default
title: Manifold constrained steepest descent
---

# Manifold constrained steepest descent
**arXiv**：[2601.21487v1](https://arxiv.org/abs/2601.21487) · [PDF](https://arxiv.org/pdf/2601.21487.pdf)  
**作者**：Kaiwei Yang, Lexiao Lai  

**一句话要点**：提出流形约束最速下降法以解决流形优化中单循环框架的挑战

**关键词**：流形优化, 最速下降法, 线性最小化oracle, 黎曼梯度, Stiefel流形, 谱范数

## 3 点简述
- 核心问题：基于范数约束线性最小化oracle的优化器难以扩展到流形约束问题，常需嵌套循环
- 方法要点：通过黎曼梯度的LMO选择范数诱导的最速下降方向，再投影回流形，实现单循环优化
- 实验或效果：在PCA、正交约束CNN和LLM适配器调优中展示稳定性和竞争性能

## 摘要（原文）

> Norm-constrained linear minimization oracle (LMO)-based optimizers such as spectral gradient descent and Muon are attractive in large-scale learning, but extending them to manifold-constrained problems is nontrivial and often leads to nested-loop schemes that solve tangent-space subproblems iteratively. We propose \emph{Manifold Constrained Steepest Descent} (MCSD), a single-loop framework for optimization over manifolds that selects a norm-induced steepest-descent direction via an LMO applied to the Riemannian gradient, and then returns to the manifold via projection. Under standard smoothness assumptions, we establish convergence guarantees for MCSD and a stochastic momentum variant. We further introduce \emph{SPEL}, the spectral-norm specialization of MCSD on the Stiefel manifold, which admits scalable implementations via fast matrix sign computations. Experiments on PCA, orthogonality-constrained CNNs, and manifold-constrained LLM adapter tuning demonstrate improved stability and competitive performance relative to standard Riemannian baselines and existing manifold-aware LMO methods.

