---
layout: default
title: Training-free score-based diffusion for parameter-dependent stochastic dynamical systems
---

# Training-free score-based diffusion for parameter-dependent stochastic dynamical systems
**arXiv**：[2602.02113v1](https://arxiv.org/abs/2602.02113) · [PDF](https://arxiv.org/pdf/2602.02113.pdf)  
**作者**：Minglei Yang, Sicheng He  

**一句话要点**：提出免训练条件扩散模型框架，以加速参数依赖随机微分方程的模拟与参数研究。

**关键词**：条件扩散模型, 随机微分方程, 参数依赖系统, 免训练方法, 蒙特卡洛估计, 不确定性量化

## 3 点简述
- 核心问题：参数依赖随机微分方程模拟需为每个参数值单独高保真仿真，计算成本高。
- 方法要点：基于轨迹数据，使用联合核加权蒙特卡洛估计器近似条件分数函数，无需神经网络训练。
- 实验或效果：通过三个数值示例验证，能准确近似不同参数值的条件分布，加速参数研究和实时应用。

## 摘要（原文）

> Simulating parameter-dependent stochastic differential equations (SDEs) presents significant computational challenges, as separate high-fidelity simulations are typically required for each parameter value of interest. Despite the success of machine learning methods in learning SDE dynamics, existing approaches either require expensive neural network training for score function estimation or lack the ability to handle continuous parameter dependence. We present a training-free conditional diffusion model framework for learning stochastic flow maps of parameter-dependent SDEs, where both drift and diffusion coefficients depend on physical parameters. The key technical innovation is a joint kernel-weighted Monte Carlo estimator that approximates the conditional score function using trajectory data sampled at discrete parameter values, enabling interpolation across both state space and the continuous parameter domain. Once trained, the resulting generative model produces sample trajectories for any parameter value within the training range without retraining, significantly accelerating parameter studies, uncertainty quantification, and real-time filtering applications. The performance of the proposed approach is demonstrated via three numerical examples of increasing complexity, showing accurate approximation of conditional distributions across varying parameter values.

