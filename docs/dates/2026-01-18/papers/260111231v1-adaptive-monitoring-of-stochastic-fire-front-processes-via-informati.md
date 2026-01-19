---
layout: default
title: Adaptive Monitoring of Stochastic Fire Front Processes via Information-seeking Predictive Control
---

# Adaptive Monitoring of Stochastic Fire Front Processes via Information-seeking Predictive Control
**arXiv**：[2601.11231v1](https://arxiv.org/abs/2601.11231) · [PDF](https://arxiv.org/pdf/2601.11231.pdf)  
**作者**：Savvas Papaioannou, Panayiotis Kolios, Christos G. Panayiotou, Marios M. Polycarpou  

**一句话要点**：提出基于信息寻求预测控制的自适应监测方法，以优化无人机对随机火线过程的监控

**关键词**：自适应监测, 随机最优控制, 贝叶斯估计, 信息寻求控制, 无人机轨迹规划, 火线建模

## 3 点简述
- 核心问题：无人机轨迹规划需集成感知、估计与控制，以应对野火演化的随机性，现有方法常分离处理或缺乏性能保证
- 方法要点：将火线监测建模为随机最优控制问题，推导非线性椭圆增长模型的贝叶斯估计器，并设计基于置信下界的自适应搜索算法
- 实验或效果：算法渐近收敛至最优策略，提供性能保证，适用于随机非线性火线模型

## 摘要（原文）

> We consider the problem of adaptively monitoring a wildfire front using a mobile agent (e.g., a drone), whose trajectory determines where sensor data is collected and thus influences the accuracy of fire propagation estimation. This is a challenging problem, as the stochastic nature of wildfire evolution requires the seamless integration of sensing, estimation, and control, often treated separately in existing methods. State-of-the-art methods either impose linear-Gaussian assumptions to establish optimality or rely on approximations and heuristics, often without providing explicit performance guarantees. To address these limitations, we formulate the fire front monitoring task as a stochastic optimal control problem that integrates sensing, estimation, and control. We derive an optimal recursive Bayesian estimator for a class of stochastic nonlinear elliptical-growth fire front models. Subsequently, we transform the resulting nonlinear stochastic control problem into a finite-horizon Markov decision process and design an information-seeking predictive control law obtained via a lower confidence bound-based adaptive search algorithm with asymptotic convergence to the optimal policy.

