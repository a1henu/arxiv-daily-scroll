---
layout: default
title: Thermodynamic Regulation of Finite-Time Gibbs Training in Energy-Based Models: A Restricted Boltzmann Machine Study
---

# Thermodynamic Regulation of Finite-Time Gibbs Training in Energy-Based Models: A Restricted Boltzmann Machine Study
**arXiv**：[2603.02525v1](https://arxiv.org/abs/2603.02525) · [PDF](https://arxiv.org/pdf/2603.02525.pdf)  
**作者**：Görkem Can Süleymanoğlu  

**一句话要点**：提出内源性热力学调控框架，以解决受限玻尔兹曼机有限时间训练中的采样不稳定问题。

**关键词**：受限玻尔兹曼机, 热力学调控, 有限时间训练, 采样稳定性, 非凸能量模型, 吉布斯采样

## 3 点简述
- 核心问题：固定温度有限时间训练在非凸能量模型中可能导致吉布斯采样器冻结和参数漂移。
- 方法要点：引入温度作为动态状态变量，基于采样统计进行调控，确保参数有界性和局部稳定性。
- 实验或效果：在MNIST上验证，自调控RBM提升归一化稳定性和有效样本量，保持重建性能。

## 摘要（原文）

> Restricted Boltzmann Machines (RBMs) are typically trained using finite-length Gibbs chains under a fixed sampling temperature. This practice implicitly assumes that the stochastic regime remains valid as the energy landscape evolves during learning. We argue that this assumption can become structurally fragile under finite-time training dynamics. This fragility arises because, in nonconvex energy-based models, fixed-temperature finite-time training can generate admissible trajectories with effective-field amplification and conductance collapse. As a result, the Gibbs sampler may asymptotically freeze, the negative phase may localize, and, without sufficiently strong regularization, parameters may exhibit deterministic linear drift. To address this instability, we introduce an endogenous thermodynamic regulation framework in which temperature evolves as a dynamical state variable coupled to measurable sampling statistics. Under standard local Lipschitz conditions and a two-time-scale separation regime, we establish global parameter boundedness under strictly positive L2 regularization. We further prove local exponential stability of the thermodynamic subsystem and show that the regulated regime mitigates inverse-temperature blow-up and freezing-induced degeneracy within a forward-invariant neighborhood. Experiments on MNIST demonstrate that the proposed self-regulated RBM substantially improves normalization stability and effective sample size relative to fixed-temperature baselines, while preserving reconstruction performance. Overall, the results reinterpret RBM training as a controlled non-equilibrium dynamical process rather than a static equilibrium approximation.

