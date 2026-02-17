---
layout: default
title: On the Stability of Nonlinear Dynamics in GD and SGD: Beyond Quadratic Potentials
---

# On the Stability of Nonlinear Dynamics in GD and SGD: Beyond Quadratic Potentials
**arXiv**：[2602.14789v1](https://arxiv.org/abs/2602.14789) · [PDF](https://arxiv.org/pdf/2602.14789.pdf)  
**作者**：Rotem Mulayoff, Sebastian U. Stich  

**一句话要点**：提出非线性动态稳定性准则，揭示GD和SGD在非二次势能下的稳定行为

**关键词**：梯度下降, 随机梯度下降, 非线性动态, 稳定性分析, 优化算法, 机器学习理论

## 3 点简述
- 研究梯度下降和随机梯度下降在训练中的非线性动态稳定性，超越线性化分析的局限性
- 推导多变量设置下GD稳定振荡的精确准则，依赖高阶导数，推广现有结果
- 证明SGD非线性动态可能因单个批次不稳定而发散，而所有批次线性稳定则确保期望稳定

## 摘要（原文）

> The dynamical stability of the iterates during training plays a key role in determining the minima obtained by optimization algorithms. For example, stable solutions of gradient descent (GD) correspond to flat minima, which have been associated with favorable features. While prior work often relies on linearization to determine stability, it remains unclear whether linearized dynamics faithfully capture the full nonlinear behavior. Recent work has shown that GD may stably oscillate near a linearly unstable minimum and still converge once the step size decays, indicating that linear analysis can be misleading. In this work, we explicitly study the effect of nonlinear terms. Specifically, we derive an exact criterion for stable oscillations of GD near minima in the multivariate setting. Our condition depends on high-order derivatives, generalizing existing results. Extending the analysis to stochastic gradient descent (SGD), we show that nonlinear dynamics can diverge in expectation even if a single batch is unstable. This implies that stability can be dictated by a single batch that oscillates unstably, rather than an average effect, as linear analysis suggests. Finally, we prove that if all batches are linearly stable, the nonlinear dynamics of SGD are stable in expectation.

