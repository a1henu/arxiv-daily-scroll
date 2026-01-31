---
layout: default
title: Differentiable Knapsack and Top-k Operators via Dynamic Programming
---

# Differentiable Knapsack and Top-k Operators via Dynamic Programming
**arXiv**：[2601.21775v1](https://arxiv.org/abs/2601.21775) · [PDF](https://arxiv.org/pdf/2601.21775.pdf)  
**作者**：Germain Vivier-Ardisson, Michaël E. Sander, Axel Parmentier, Mathieu Blondel  

**一句话要点**：提出基于动态规划的可微背包与Top-k算子框架，以集成离散选择算子到神经网络中。

**关键词**：可微优化, 动态规划, 离散选择算子, 神经网络集成, 并行算法, 决策聚焦学习

## 3 点简述
- 核心问题：背包和Top-k算子在神经网络中因分段常数特性导致梯度几乎为零，难以集成。
- 方法要点：通过动态规划统一框架，平滑递归实现可微松弛，并开发高效并行算法支持前向和后向传播。
- 实验或效果：在决策聚焦学习、约束动态品类强化学习和离散VAE扩展等基准上验证框架有效性。

## 摘要（原文）

> Knapsack and Top-k operators are useful for selecting discrete subsets of variables. However, their integration into neural networks is challenging as they are piecewise constant, yielding gradients that are zero almost everywhere. In this paper, we propose a unified framework casting these operators as dynamic programs, and derive differentiable relaxations by smoothing the underlying recursions. On the algorithmic side, we develop efficient parallel algorithms supporting both deterministic and stochastic forward passes, and vector-Jacobian products for the backward pass. On the theoretical side, we prove that Shannon entropy is the unique regularization choice yielding permutation-equivariant operators, and characterize regularizers inducing sparse selections. Finally, on the experimental side, we demonstrate our framework on a decision-focused learning benchmark, a constrained dynamic assortment RL problem, and an extension of discrete VAEs.

