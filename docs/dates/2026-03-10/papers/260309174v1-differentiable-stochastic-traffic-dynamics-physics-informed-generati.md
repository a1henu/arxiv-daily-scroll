---
layout: default
title: Differentiable Stochastic Traffic Dynamics: Physics-Informed Generative Modelling in Transportation
---

# Differentiable Stochastic Traffic Dynamics: Physics-Informed Generative Modelling in Transportation
**arXiv**：[2603.09174v1](https://arxiv.org/abs/2603.09174) · [PDF](https://arxiv.org/pdf/2603.09174.pdf)  
**作者**：Wuping Xin  

**一句话要点**：提出可微随机交通动力学框架，以物理信息生成建模解决宏观交通流随机性建模问题

**关键词**：随机交通流, 物理信息生成建模, 可微动力学, 得分网络, 分布估计, 交通状态分析

## 3 点简述
- 核心问题：现有物理信息深度学习方法嵌入确定性PDE，忽略交通流随机性，导致点值输出无法捕捉分布特性
- 方法要点：基于Ito型LWR模型推导边际密度前向方程，构建概率流ODE作为物理约束，结合得分网络与去噪得分匹配训练
- 实验或效果：模型生成数据条件密度分布，支持点估计、置信区间和拥堵风险计算，为分布交通状态估计提供基础

## 摘要（原文）

> Macroscopic traffic flow is stochastic, but the physics-informed deep learning methods currently used in transportation literature embed deterministic PDEs and produce point-valued outputs; the stochasticity of the governing dynamics plays no role in the learned representation. This work develops a framework in which the physics constraint itself is distributional and directly derived from stochastic traffic-flow dynamics. Starting from an Ito-type Lighthill-Whitham-Richards model with Brownian forcing, we derive a one-point forward equation for the marginal traffic density at each spatial location. The spatial coupling induced by the conservation law appears as an explicit conditional drift term, which makes the closure requirement transparent. Based on this formulation, we derive an equivalent deterministic Probability Flow ODE that is pointwise evaluable and differentiable once a closure is specified. Incorporating this as a physics constraint, we then propose a score network with an advection-closure module, trainable by denoising score matching together with a Fokker-Planck residual loss. The resulting model targets a data-conditioned density distribution, from which point estimates, credible intervals, and congestion-risk measures can be computed. The framework provides a basis for distributional traffic-state estimation and for stochastic fundamental-diagram analysis in a physics-informed generative setting.

