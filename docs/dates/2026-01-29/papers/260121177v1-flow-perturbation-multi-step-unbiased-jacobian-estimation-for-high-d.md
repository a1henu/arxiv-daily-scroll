---
layout: default
title: Flow Perturbation++: Multi-Step Unbiased Jacobian Estimation for High-Dimensional Boltzmann Sampling
---

# Flow Perturbation++: Multi-Step Unbiased Jacobian Estimation for High-Dimensional Boltzmann Sampling
**arXiv**：[2601.21177v1](https://arxiv.org/abs/2601.21177) · [PDF](https://arxiv.org/pdf/2601.21177.pdf)  
**作者**：Xin Peng, Ang Gao  

**一句话要点**：提出Flow Perturbation++以解决高维玻尔兹曼采样中雅可比行列式估计的高方差问题

**关键词**：连续归一化流, 玻尔兹曼采样, 雅可比行列式估计, 无偏估计, 高维系统, 方差缩减

## 3 点简述
- 核心问题：连续归一化流在高维系统中因雅可比行列式计算成本高而受限，现有方法存在偏差或高方差
- 方法要点：基于Flow Perturbation，通过离散化概率流ODE进行多步无偏雅可比估计，降低方差
- 实验或效果：在1000D高斯混合模型和Chignolin蛋白质上，相比基线方法显著提升平衡采样效果

## 摘要（原文）

> The scalability of continuous normalizing flows (CNFs) for unbiased Boltzmann sampling remains limited in high-dimensional systems due to the cost of Jacobian-determinant evaluation, which requires $D$ backpropagation passes through the flow layers. Existing stochastic Jacobian estimators such as the Hutchinson trace estimator reduce computation but introduce bias, while the recently proposed Flow Perturbation method is unbiased yet suffers from high variance. We present \textbf{Flow Perturbation++}, a variance-reduced extension of Flow Perturbation that discretizes the probability-flow ODE and performs unbiased stepwise Jacobian estimation at each integration step. This multi-step construction retains the unbiasedness of Flow Perturbation while achieves substantially lower estimator variance. Integrated into a Sequential Monte Carlo framework, Flow Perturbation++ achieves significantly improved equilibrium sampling on a 1000D Gaussian Mixture Model and the all-atom Chignolin protein compared with Hutchinson-based and single-step Flow Perturbation baselines.

