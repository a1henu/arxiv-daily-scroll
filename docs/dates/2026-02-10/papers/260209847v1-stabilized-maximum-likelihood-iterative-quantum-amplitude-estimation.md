---
layout: default
title: Stabilized Maximum-Likelihood Iterative Quantum Amplitude Estimation for Structural CVaR under Correlated Random Fields
---

# Stabilized Maximum-Likelihood Iterative Quantum Amplitude Estimation for Structural CVaR under Correlated Random Fields
**arXiv**：[2602.09847v1](https://arxiv.org/abs/2602.09847) · [PDF](https://arxiv.org/pdf/2602.09847.pdf)  
**作者**：Alireza Tabarraei  

**一句话要点**：提出稳定最大似然迭代量子振幅估计方法，用于相关随机场下结构CVaR的高效计算

**关键词**：量子振幅估计, 条件风险价值, 结构力学, 最大似然推断, 相关随机场, 计算复杂度

## 3 点简述
- 核心问题：高维空间相关材料不确定性下，结构条件风险价值（CVaR）的经典蒙特卡洛计算成本过高
- 方法要点：基于量子振幅估计，结合最大似然推断和区间跟踪，引入多假设可行性跟踪和重启机制以增强稳定性
- 实验或效果：在Nyström低秩高斯核模型生成的对数正态杨氏模量场基准问题上，相比经典方法显著降低计算复杂度并保持统计可靠性

## 摘要（原文）

> Conditional Value-at-Risk (CVaR) is a central tail-risk measure in stochastic structural mechanics, yet its accurate evaluation under high-dimensional, spatially correlated material uncertainty remains computationally prohibitive for classical Monte Carlo methods. Leveraging bounded-expectation reformulations of CVaR compatible with quantum amplitude estimation, we develop a quantum-enhanced inference framework that casts CVaR evaluation as a statistically consistent, confidence-constrained maximum-likelihood amplitude estimation problem. The proposed method extends iterative quantum amplitude estimation (IQAE) by embedding explicit maximum-likelihood inference within a rigorously controlled interval-tracking architecture. To ensure global correctness under finite-shot noise and the non-injective oscillatory response induced by Grover amplification, we introduce a stabilized inference scheme incorporating multi-hypothesis feasibility tracking, periodic low-depth disambiguation, and a bounded restart mechanism governed by an explicit failure-probability budget. This formulation preserves the quadratic oracle-complexity advantage of amplitude estimation while providing finite-sample confidence guarantees and reduced estimator variance. The framework is demonstrated on benchmark problems with spatially correlated lognormal Young's modulus fields generated using a Nystrom low-rank Gaussian kernel model. Numerical results show that the proposed estimator achieves substantially lower oracle complexity than classical Monte Carlo CVaR estimation at comparable confidence levels, while maintaining rigorous statistical reliability. This work establishes a practically robust and theoretically grounded quantum-enhanced methodology for tail-risk quantification in stochastic continuum mechanics.

