---
layout: default
title: Computing Fixpoints of Learned Functions: Chaotic Iteration and Simple Stochastic Games
---

# Computing Fixpoints of Learned Functions: Chaotic Iteration and Simple Stochastic Games
**arXiv**：[2601.16142v1](https://arxiv.org/abs/2601.16142) · [PDF](https://arxiv.org/pdf/2601.16142.pdf)  
**作者**：Paolo Baldan, Sebastian Gurke, Barbara König, Florian Wittbold  

**一句话要点**：提出改进的阻尼Mann迭代以计算未知函数的定点，适用于高维系统和概率模型。

**关键词**：定点计算, 阻尼Mann迭代, 混沌迭代, 函数近似, 简单随机游戏, 概率模型

## 3 点简述
- 核心问题：计算非负实数上高维函数的定点，但函数仅能近似已知。
- 方法要点：推广阻尼Mann迭代，放宽参数序列约束，支持混沌迭代和零收敛学习率。
- 实验或效果：方法可直接应用于简单随机游戏等概率模型的期望收益计算。

## 摘要（原文）

> The problem of determining the (least) fixpoint of (higher-dimensional) functions over the non-negative reals frequently occurs when dealing with systems endowed with a quantitative semantics. We focus on the situation in which the functions of interest are not known precisely but can only be approximated. As a first contribution we generalize an iteration scheme called dampened Mann iteration, recently introduced in the literature. The improved scheme relaxes previous constraints on parameter sequences, allowing learning rates to converge to zero or not converge at all. While seemingly minor, this flexibility is essential to enable the implementation of chaotic iterations, where only a subset of components is updated in each step, allowing to tackle higher-dimensional problems. Additionally, by allowing learning rates to converge to zero, we can relax conditions on the convergence speed of function approximations, making the method more adaptable to various scenarios. We also show that dampened Mann iteration applies immediately to compute the expected payoff in various probabilistic models, including simple stochastic games, not covered by previous work.

