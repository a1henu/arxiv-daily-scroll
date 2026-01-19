---
layout: default
title: A Probabilistic Approach to Trajectory-Based Optimal Experimental Design
---

# A Probabilistic Approach to Trajectory-Based Optimal Experimental Design
**arXiv**：[2601.11473v1](https://arxiv.org/abs/2601.11473) · [PDF](https://arxiv.org/pdf/2601.11473.pdf)  
**作者**：Ahmed Attia  

**一句话要点**：提出基于轨迹的概率方法，用于静态导航网格上的最优实验设计。

**关键词**：最优实验设计, 轨迹优化, 概率方法, 随机优化, 参数识别, 导航网格

## 3 点简述
- 核心问题：在静态导航网格上定义离散路径优化问题，用于最优实验设计。
- 方法要点：将轨迹建模为参数化马尔可夫策略的随机变量，转化为策略参数的随机优化问题。
- 实验或效果：通过参数识别问题进行数值验证，适用于线性和非线性逆问题。

## 摘要（原文）

> We present a novel probabilistic approach for optimal path experimental design. In this approach a discrete path optimization problem is defined on a static navigation mesh, and trajectories are modeled as random variables governed by a parametric Markov policy. The discrete path optimization problem is then replaced with an equivalent stochastic optimization problem over the policy parameters, resulting in an optimal probability model that samples estimates of the optimal discrete path. This approach enables exploration of the utility function's distribution tail and treats the utility function of the design as a black box, making it applicable to linear and nonlinear inverse problems and beyond experimental design. Numerical verification and analysis are carried out by using a parameter identification problem widely used in model-based optimal experimental design.

