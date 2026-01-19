---
layout: default
title: Contextual Distributionally Robust Optimization with Causal and Continuous Structure: An Interpretable and Tractable Approach
---

# Contextual Distributionally Robust Optimization with Causal and Continuous Structure: An Interpretable and Tractable Approach
**arXiv**：[2601.11016v1](https://arxiv.org/abs/2601.11016) · [PDF](https://arxiv.org/pdf/2601.11016.pdf)  
**作者**：Fenglin Zhang, Jie Wang  

**一句话要点**：提出因果Sinkhorn分布鲁棒优化框架，结合因果连续结构开发可解释决策规则

**关键词**：分布鲁棒优化, 因果推断, 可解释机器学习, 决策规则, Sinkhorn距离, 随机优化

## 3 点简述
- 核心问题：在上下文分布鲁棒优化中，考虑分布的因果和连续结构，以提升决策的鲁棒性和可解释性
- 方法要点：引入因果Sinkhorn距离构建模糊集，提出软回归森林决策规则，并开发高效随机组合梯度算法求解
- 实验或效果：在合成和真实数据集上验证了方法的优越性能和可解释性，收敛速率匹配标准随机梯度下降

## 摘要（原文）

> In this paper, we introduce a framework for contextual distributionally robust optimization (DRO) that considers the causal and continuous structure of the underlying distribution by developing interpretable and tractable decision rules that prescribe decisions using covariates. We first introduce the causal Sinkhorn discrepancy (CSD), an entropy-regularized causal Wasserstein distance that encourages continuous transport plans while preserving the causal consistency. We then formulate a contextual DRO model with a CSD-based ambiguity set, termed Causal Sinkhorn DRO (Causal-SDRO), and derive its strong dual reformulation where the worst-case distribution is characterized as a mixture of Gibbs distributions. To solve the corresponding infinite-dimensional policy optimization, we propose the Soft Regression Forest (SRF) decision rule, which approximates optimal policies within arbitrary measurable function spaces. The SRF preserves the interpretability of classical decision trees while being fully parametric, differentiable, and Lipschitz smooth, enabling intrinsic interpretation from both global and local perspectives. To solve the Causal-SDRO with parametric decision rules, we develop an efficient stochastic compositional gradient algorithm that converges to an $\varepsilon$-stationary point at a rate of $O(\varepsilon^{-4})$, matching the convergence rate of standard stochastic gradient descent. Finally, we validate our method through numerical experiments on synthetic and real-world datasets, demonstrating its superior performance and interpretability.

