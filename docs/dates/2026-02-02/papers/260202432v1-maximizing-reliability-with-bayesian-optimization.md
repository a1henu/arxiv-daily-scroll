---
layout: default
title: Maximizing Reliability with Bayesian Optimization
---

# Maximizing Reliability with Bayesian Optimization
**arXiv**：[2602.02432v1](https://arxiv.org/abs/2602.02432) · [PDF](https://arxiv.org/pdf/2602.02432.pdf)  
**作者**：Jack M. Buckingham, Ivo Couckuyt, Juergen Branke  

**一句话要点**：提出基于汤普森采样和知识梯度的贝叶斯优化方法，以最大化制造设计可靠性并处理极低失效概率。

**关键词**：贝叶斯优化, 可靠性最大化, 极低失效概率, 重要性采样, 汤普森采样, 知识梯度

## 3 点简述
- 核心问题：在制造中最大化设计可靠性，涉及随机扰动和极低失效概率（10^-6至10^-8）。
- 方法要点：基于汤普森采样和知识梯度开发贝叶斯优化方法，后者近似最小化失效概率对数的一步贝叶斯最优策略，并集成重要性采样。
- 实验或效果：经验结果显示，所提方法在极端和非极端失效概率场景下均优于现有方法。

## 摘要（原文）

> Bayesian optimization (BO) is a popular, sample-efficient technique for expensive, black-box optimization. One such problem arising in manufacturing is that of maximizing the reliability, or equivalently minimizing the probability of a failure, of a design which is subject to random perturbations - a problem that can involve extremely rare failures ($P_\mathrm{fail} = 10^{-6}-10^{-8}$). In this work, we propose two BO methods based on Thompson sampling and knowledge gradient, the latter approximating the one-step Bayes-optimal policy for minimizing the logarithm of the failure probability. Both methods incorporate importance sampling to target extremely small failure probabilities. Empirical results show the proposed methods outperform existing methods in both extreme and non-extreme regimes.

