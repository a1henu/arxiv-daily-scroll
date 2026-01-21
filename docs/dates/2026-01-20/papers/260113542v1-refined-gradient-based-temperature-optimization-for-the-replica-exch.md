---
layout: default
title: Refined Gradient-Based Temperature Optimization for the Replica-Exchange Monte-Carlo Method
---

# Refined Gradient-Based Temperature Optimization for the Replica-Exchange Monte-Carlo Method
**arXiv**：[2601.13542v1](https://arxiv.org/abs/2601.13542) · [PDF](https://arxiv.org/pdf/2601.13542.pdf)  
**作者**：Tatsuya Miyata, Shunta Arai, Satoshi Takabe  

**一句话要点**：提出基于梯度优化的改进温度选择方法，以提升副本交换蒙特卡洛算法的采样效率。

**关键词**：副本交换蒙特卡洛, 温度优化, 梯度下降, 多模态分布采样, 自旋系统

## 3 点简述
- 核心问题：副本交换蒙特卡洛方法中温度选择影响采样效率，优化温度仍具挑战。
- 方法要点：扩展梯度优化框架，引入重参数化技术强制物理约束，如逆温度单调排序。
- 实验或效果：在自旋系统基准测试中实现均匀接受率，减少温度空间往返时间，优于需调参的策略梯度方法。

## 摘要（原文）

> The replica-exchange Monte-Carlo (RXMC) method is a powerful Markov-chain Monte-Carlo algorithm for sampling from multi-modal distributions, which are challenging for conventional methods. The sampling efficiency of the RXMC method depends highly on the selection of the temperatures, and finding optimal temperatures remains a challenge. In this study, we propose a refined online temperature selection method by extending the gradient-based optimization framework proposed previously. Building upon the existing temperature update approach, we introduce a reparameterization technique to strictly enforce physical constraints, such as the monotonic ordering of inverse temperatures, which were not explicitly addressed in the original formulation. The proposed method defines the variance of acceptance rates between adjacent replicas as a loss function, estimates its gradient using differential information from the sampling process, and optimizes the temperatures via gradient descent. We demonstrate the effectiveness of our method through experiments on benchmark spin systems, including the two-dimensional ferromagnetic Ising model, the two-dimensional ferromagnetic XY model, and the three-dimensional Edwards-Anderson model. Our results show that the method successfully achieves uniform acceptance rates and reduces round-trip times across the temperature space. Furthermore, our proposed method offers a significant advantage over recently proposed policy gradient method that require careful hyperparameter tuning, while simultaneously preventing the constraint violations that destabilize optimization.

