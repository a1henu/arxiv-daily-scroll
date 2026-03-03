---
layout: default
title: On the Stability Connection Between Discrete-Time Algorithms and Their Resolution ODEs: Applications to Min-Max Optimisation
---

# On the Stability Connection Between Discrete-Time Algorithms and Their Resolution ODEs: Applications to Min-Max Optimisation
**arXiv**：[2603.01430v1](https://arxiv.org/abs/2603.01430) · [PDF](https://arxiv.org/pdf/2603.01430.pdf)  
**作者**：Amir Ali Farzin, Yuen-Man Pun, Philipp Braun, Iman Shames  

**一句话要点**：建立离散时间算法与分辨率ODE的稳定性连接，应用于最小-最大优化分析

**关键词**：稳定性分析, 离散时间算法, 分辨率ODE, 最小-最大优化, 指数稳定性, 鞍点分析

## 3 点简述
- 核心问题：离散时间算法与连续时间ODE的稳定性关系缺乏严格理论连接
- 方法要点：通过O(s^r)-分辨率ODE，证明连续时间指数稳定性可传递到离散时间算法
- 实验或效果：应用于多种优化算法，分析鞍点稳定性，数值示例验证理论

## 摘要（原文）

> This work establishes a rigorous connection between stability properties of discrete-time algorithms (DTAs) and corresponding continuous-time dynamical systems derived through $ O(s^r) $-resolution ordinary differential equations (ODEs). We show that for discrete- and continuous-time dynamical systems satisfying a mild error assumption, exponential stability of a common equilibrium with respect to the continuous time dynamics implies exponential stability of the corresponding equilibrium for the discrete-time dynamics, provided that the step size is chosen sufficiently small. We extend this result to common compact invariant sets. We prove that if an equilibrium is exponentially stable for the $ O(s^r) $-resolution ODE, then it is also exponentially stable for the associated DTA. We apply this framework to analyse the limit point properties of several prominent optimisation algorithms, including Two-Timescale Gradient Descent--Ascent (TT-GDA), Generalised Extragradient (GEG), Two-Timescale Proximal Point (TT-PPM), Damped Newton (DN), Regularised Damped Newton (RDN), and the Jacobian method (JM), by studying their $ O(1) $- and $ O(s) $-resolution ODEs. We show that under a proper choice of hyperparameters, the set of saddle points of the objective function is a subset of the set of exponentially stable equilibria of GEG, TT-PPM, DN, and RDN. We relax the common Hessian invariance assumption through direct analysis of the resolution ODEs, broadening the applicability of our results. Numerical examples illustrate the theoretical findings.

