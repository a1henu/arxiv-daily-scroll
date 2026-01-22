---
layout: default
title: TRSVR: An Adaptive Stochastic Trust-Region Method with Variance Reduction
---

# TRSVR: An Adaptive Stochastic Trust-Region Method with Variance Reduction
**arXiv**：[2601.14647v1](https://arxiv.org/abs/2601.14647) · [PDF](https://arxiv.org/pdf/2601.14647.pdf)  
**作者**：Yuchen Fang, Xinshou Zheng, Javad Lavaei  

**一句话要点**：提出自适应随机信赖域方法TRSVR，结合SVRG加速非凸优化收敛。

**关键词**：随机优化, 信赖域方法, 方差缩减, 非凸优化, 机器学习任务

## 3 点简述
- 针对无约束非凸优化问题，仅依赖随机梯度信息，无需函数值评估。
- 自适应调整信赖域半径，基于半径控制参数和随机梯度估计，确保收敛到一阶驻点。
- 实验表明，结合SVRG加速收敛，信赖域和Hessian信息提升性能，优于SGD和Adam。

## 摘要（原文）

> We propose a stochastic trust-region method for unconstrained nonconvex optimization that incorporates stochastic variance-reduced gradients (SVRG) to accelerate convergence. Unlike classical trust-region methods, the proposed algorithm relies solely on stochastic gradient information and does not require function value evaluations. The trust-region radius is adaptively adjusted based on a radius-control parameter and the stochastic gradient estimate. Under mild assumptions, we establish that the algorithm converges in expectation to a first-order stationary point. Moreover, the method achieves iteration and sample complexity bounds that match those of SVRG-based first-order methods, while allowing stochastic and potentially gradient-dependent second-order information. Extensive numerical experiments demonstrate that incorporating SVRG accelerates convergence, and that the use of trust-region methods and Hessian information further improves performance. We also highlight the impact of batch size and inner-loop length on efficiency, and show that the proposed method outperforms SGD and Adam on several machine learning tasks.

