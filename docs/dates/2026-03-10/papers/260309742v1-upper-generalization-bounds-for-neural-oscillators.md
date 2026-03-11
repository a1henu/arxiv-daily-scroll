---
layout: default
title: Upper Generalization Bounds for Neural Oscillators
---

# Upper Generalization Bounds for Neural Oscillators
**arXiv**：[2603.09742v1](https://arxiv.org/abs/2603.09742) · [PDF](https://arxiv.org/pdf/2603.09742.pdf)  
**作者**：Zifeng Huang, Konstantin M. Zuev, Yong Xia, Michael Beer  

**一句话要点**：推导神经振荡器的上界泛化边界，以量化其在非线性结构系统动态映射中的泛化能力。

**关键词**：神经振荡器, 泛化边界, Rademacher复杂度, 二阶常微分方程, 非线性结构系统, PAC学习理论

## 3 点简述
- 核心问题：神经振荡器在动态负载与响应映射中表现良好，但缺乏理论泛化能力量化。
- 方法要点：基于Rademacher复杂度，推导因果连续算子近似和二阶动力系统近似的上界PAC泛化边界。
- 实验或效果：数值研究验证误差随样本量和时间长度呈幂律增长，约束MLP范数可提升泛化性能。

## 摘要（原文）

> Neural oscillators that originate from the second-order ordinary differential equations (ODEs) have shown competitive performance in learning mappings between dynamic loads and responses of complex nonlinear structural systems. Despite this empirical success, theoretically quantifying the generalization capacities of their neural network architectures remains undeveloped. In this study, the neural oscillator consisting of a second-order ODE followed by a multilayer perceptron (MLP) is considered. Its upper probably approximately correct (PAC) generalization bound for approximating causal and uniformly continuous operators between continuous temporal function spaces and that for approximating the uniformly asymptotically incrementally stable second-order dynamical systems are derived by leveraging the Rademacher complexity framework. The theoretical results show that the estimation errors grow polynomially with respect to both the MLP size and the time length, thereby avoiding the curse of parametric complexity. Furthermore, the derived error bounds demonstrate that constraining the Lipschitz constants of the MLPs via loss function regularization can improve the generalization ability of the neural oscillator. A numerical study considering a Bouc-Wen nonlinear system under stochastic seismic excitation validates the theoretically predicted power laws of the estimation errors with respect to the sample size and time length, and confirms the effectiveness of constraining MLPs' matrix and vector norms in enhancing the performance of the neural oscillator under limited training data.

