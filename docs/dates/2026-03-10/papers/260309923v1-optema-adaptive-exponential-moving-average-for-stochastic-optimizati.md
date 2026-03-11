---
layout: default
title: OptEMA: Adaptive Exponential Moving Average for Stochastic Optimization with Zero-Noise Optimality
---

# OptEMA: Adaptive Exponential Moving Average for Stochastic Optimization with Zero-Noise Optimality
**arXiv**：[2603.09923v1](https://arxiv.org/abs/2603.09923) · [PDF](https://arxiv.org/pdf/2603.09923.pdf)  
**作者**：Ganzhao Yuan  

**一句话要点**：提出OptEMA自适应指数移动平均优化器，在零噪声场景下实现近最优收敛

**关键词**：自适应优化, 指数移动平均, 零噪声收敛, 随机优化, 理论分析, 梯度下降

## 3 点简述
- 现有Adam类方法理论分析存在零噪声下非最优、依赖有界条件或Lipschitz常数等局限
- OptEMA引入自适应EMA系数，变体OptEMA-M和OptEMA-V分别调整一阶和二阶矩，实现闭环无Lipschitz参数化
- 在标准SGD假设下，达到噪声自适应收敛率，零噪声时无需超参数调整即获近最优确定性速率

## 摘要（原文）

> The Exponential Moving Average (EMA) is a cornerstone of widely used optimizers such as Adam. However, existing theoretical analyses of Adam-style methods have notable limitations: their guarantees can remain suboptimal in the zero-noise regime, rely on restrictive boundedness conditions (e.g., bounded gradients or objective gaps), use constant or open-loop stepsizes, or require prior knowledge of Lipschitz constants. To overcome these bottlenecks, we introduce OptEMA and analyze two novel variants: OptEMA-M, which applies an adaptive, decreasing EMA coefficient to the first-order moment with a fixed second-order decay, and OptEMA-V, which swaps these roles. Crucially, OptEMA is closed-loop and Lipschitz-free in the sense that its effective stepsizes are trajectory-dependent and do not require the Lipschitz constant for parameterization. Under standard stochastic gradient descent (SGD) assumptions, namely smoothness, a lower-bounded objective, and unbiased gradients with bounded variance, we establish rigorous convergence guarantees. Both variants achieve a noise-adaptive convergence rate of $\widetilde{\mathcal{O}}(T^{-1/2}+σ^{1/2} T^{-1/4})$ for the average gradient norm, where $σ$ is the noise level. In particular, in the zero-noise regime where $σ=0$, our bounds reduce to the nearly optimal deterministic rate $\widetilde{\mathcal{O}}(T^{-1/2})$ without manual hyperparameter retuning.

