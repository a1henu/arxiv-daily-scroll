---
layout: default
title: Accelerated Online Risk-Averse Policy Evaluation in POMDPs with Theoretical Guarantees and Novel CVaR Bounds
---

# Accelerated Online Risk-Averse Policy Evaluation in POMDPs with Theoretical Guarantees and Novel CVaR Bounds
**arXiv**：[2602.23073v1](https://arxiv.org/abs/2602.23073) · [PDF](https://arxiv.org/pdf/2602.23073.pdf)  
**作者**：Yaacov Pariente, Vadim Indelman  

**一句话要点**：提出加速POMDP中CVaR策略评估的理论框架，通过新边界和动作剪枝实现计算加速。

**关键词**：部分可观测马尔可夫决策过程, 条件风险价值, 风险规避决策, 策略评估加速, 动作剪枝, 理论保证

## 3 点简述
- 核心问题：POMDP中风险规避策略评估计算复杂，CVaR作为风险度量难以高效求解。
- 方法要点：推导CVaR新边界，基于简化信念MDP建立上下界，设计带概率保证的估计器。
- 实验或效果：多领域验证边界可靠分离策略，在简化模型下实现显著计算加速。

## 摘要（原文）

> Risk-averse decision-making under uncertainty in partially observable domains is a central challenge in artificial intelligence and is essential for developing reliable autonomous agents. The formal framework for such problems is the partially observable Markov decision process (POMDP), where risk sensitivity is introduced through a risk measure applied to the value function, with Conditional Value-at-Risk (CVaR) being a particularly significant criterion. However, solving POMDPs is computationally intractable in general, and approximate methods rely on computationally expensive simulations of future agent trajectories. This work introduces a theoretical framework for accelerating CVaR value function evaluation in POMDPs with formal performance guarantees. We derive new bounds on the CVaR of a random variable X using an auxiliary random variable Y, under assumptions relating their cumulative distribution and density functions; these bounds yield interpretable concentration inequalities and converge as the distributional discrepancy vanishes. Building on this, we establish upper and lower bounds on the CVaR value function computable from a simplified belief-MDP, accommodating general simplifications of the transition dynamics. We develop estimators for these bounds within a particle-belief MDP framework with probabilistic guarantees, and employ them for acceleration via action elimination: actions whose bounds indicate suboptimality under the simplified model are safely discarded while ensuring consistency with the original POMDP. Empirical evaluation across multiple POMDP domains confirms that the bounds reliably separate safe from dangerous policies while achieving substantial computational speedups under the simplified model.

