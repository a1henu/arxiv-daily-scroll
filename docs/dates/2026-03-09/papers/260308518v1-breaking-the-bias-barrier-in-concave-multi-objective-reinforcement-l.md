---
layout: default
title: Breaking the Bias Barrier in Concave Multi-Objective Reinforcement Learning
---

# Breaking the Bias Barrier in Concave Multi-Objective Reinforcement Learning
**arXiv**：[2603.08518v1](https://arxiv.org/abs/2603.08518) · [PDF](https://arxiv.org/pdf/2603.08518.pdf)  
**作者**：Swetha Ganesh, Vaneet Aggarwal  

**一句话要点**：提出带多级蒙特卡洛估计的自然策略梯度算法，以解决凹多目标强化学习中的梯度偏差问题。

**关键词**：多目标强化学习, 凹标量化, 梯度偏差, 自然策略梯度, 多级蒙特卡洛, 样本复杂度

## 3 点简述
- 核心问题：非线性标量化导致策略梯度估计偏差，增加样本复杂度至O(ε^{-4})。
- 方法要点：结合自然策略梯度与多级蒙特卡洛估计器，控制偏差并降低采样成本。
- 实验或效果：算法实现最优O(ε^{-2})样本复杂度，二阶平滑时无需多级蒙特卡洛。

## 摘要（原文）

> While standard reinforcement learning optimizes a single reward signal, many applications require optimizing a nonlinear utility $f(J_1^π,\dots,J_M^π)$ over multiple objectives, where each $J_m^π$ denotes the expected discounted return of a distinct reward function. A common approach is concave scalarization, which captures important trade-offs such as fairness and risk sensitivity. However, nonlinear scalarization introduces a fundamental challenge for policy gradient methods: the gradient depends on $\partial f(J^π)$, while in practice only empirical return estimates $\hat J$ are available. Because $f$ is nonlinear, the plug-in estimator is biased ($\mathbb{E}[\partial f(\hat J)] \neq \partial f(\mathbb{E}[\hat J])$), leading to persistent gradient bias that degrades sample complexity.
>   In this work we identify and overcome this bias barrier in concave-scalarized multi-objective reinforcement learning. We show that existing policy-gradient methods suffer an intrinsic $\widetilde{\mathcal{O}}(ε^{-4})$ sample complexity due to this bias. To address this issue, we develop a Natural Policy Gradient (NPG) algorithm equipped with a multi-level Monte Carlo (MLMC) estimator that controls the bias of the scalarization gradient while maintaining low sampling cost. We prove that this approach achieves the optimal $\widetilde{\mathcal{O}}(ε^{-2})$ sample complexity for computing an $ε$-optimal policy. Furthermore, we show that when the scalarization function is second-order smooth, the first-order bias cancels automatically, allowing vanilla NPG to achieve the same $\widetilde{\mathcal{O}}(ε^{-2})$ rate without MLMC. Our results provide the first optimal sample complexity guarantees for concave multi-objective reinforcement learning under policy-gradient methods.

