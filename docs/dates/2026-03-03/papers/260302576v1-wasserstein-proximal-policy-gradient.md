---
layout: default
title: Wasserstein Proximal Policy Gradient
---

# Wasserstein Proximal Policy Gradient
**arXiv**：[2603.02576v1](https://arxiv.org/abs/2603.02576) · [PDF](https://arxiv.org/pdf/2603.02576.pdf)  
**作者**：Zhaoyu Zhu, Shuhan Zhang, Rui Gao, Shuang Li  

**一句话要点**：提出Wasserstein近端策略梯度方法，用于连续动作熵正则化强化学习。

**关键词**：强化学习, 策略梯度, Wasserstein距离, 连续动作控制, 熵正则化, 最优传输

## 3 点简述
- 研究连续动作熵正则化强化学习的策略梯度方法，基于Wasserstein几何视角。
- 通过算子分裂方案推导WPPG，交替最优传输更新与高斯卷积热步，避免评估策略对数密度或其梯度。
- 理论证明全局线性收敛率，实验显示在标准连续控制基准上实现竞争性能且易于实现。

## 摘要（原文）

> We study policy gradient methods for continuous-action, entropy-regularized reinforcement learning through the lens of Wasserstein geometry. Starting from a Wasserstein proximal update, we derive Wasserstein Proximal Policy Gradient (WPPG) via an operator-splitting scheme that alternates an optimal transport update with a heat step implemented by Gaussian convolution. This formulation avoids evaluating the policy's log density or its gradient, making the method directly applicable to expressive implicit stochastic policies specified as pushforward maps. We establish a global linear convergence rate for WPPG, covering both exact policy evaluation and actor-critic implementations with controlled approximation error. Empirically, WPPG is simple to implement and attains competitive performance on standard continuous-control benchmarks.

