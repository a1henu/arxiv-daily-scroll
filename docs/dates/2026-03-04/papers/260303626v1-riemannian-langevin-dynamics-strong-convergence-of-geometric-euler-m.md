---
layout: default
title: Riemannian Langevin Dynamics: Strong Convergence of Geometric Euler-Maruyama Scheme
---

# Riemannian Langevin Dynamics: Strong Convergence of Geometric Euler-Maruyama Scheme
**arXiv**：[2603.03626v1](https://arxiv.org/abs/2603.03626) · [PDF](https://arxiv.org/pdf/2603.03626.pdf)  
**作者**：Zhiyuan Zhan, Masashi Sugiyama  

**一句话要点**：提出黎曼流形上的几何欧拉-丸山方案，证明强收敛性以支持流形扩散模型

**关键词**：黎曼流形, 随机微分方程, 数值方案, 强收敛性, 扩散模型, 流形采样

## 3 点简述
- 研究流形值随机微分方程的数值方案收敛性，作为流形扩散模型的基础
- 提出几何欧拉-丸山方案，在几何和正则条件下证明强收敛阶为1/2
- 应用至黎曼朗之万动力学，获得流形采样的Wasserstein界

## 摘要（原文）

> Low-dimensional structure in real-world data plays an important role in the success of generative models, which motivates diffusion models defined on intrinsic data manifolds. Such models are driven by stochastic differential equations (SDEs) on manifolds, which raises the need for convergence theory of numerical schemes for manifold-valued SDEs. In Euclidean space, the Euler--Maruyama (EM) scheme achieves strong convergence with order $1/2$, but an analogous result for manifold discretizations is less understood in general settings. In this work, we study a geometric version of the EM scheme for SDEs on Riemannian manifolds and prove strong convergence with order $1/2$ under geometric and regularity conditions. As an application, we obtain a Wasserstein bound for sampling on manifolds via the geometric EM discretization of Riemannian Langevin dynamics.

