---
layout: default
title: Better LMO-based Momentum Methods with Second-Order Information
---

# Better LMO-based Momentum Methods with Second-Order Information
**arXiv**：[2512.13227v1](https://arxiv.org/abs/2512.13227) · [PDF](https://arxiv.org/pdf/2512.13227.pdf)  
**作者**：Sarit Khirirat, Abdurakhmon Sadiev, Yury Demidovich, Peter Richtárik  

**一句话要点**：提出基于线性最小化预言机的二阶信息动量方法，以提升任意范数下的收敛速度

**关键词**：随机优化, 动量方法, 线性最小化预言机, 二阶信息, 收敛分析, 神经网络训练

## 3 点简述
- 传统随机动量方法收敛率受限，在任意范数问题中应用受限
- 扩展LMO框架，集成Hessian校正动量，提供改进的收敛保证
- 实验验证在MLP和LSTM训练中实现更快收敛

## 摘要（原文）

> The use of momentum in stochastic optimization algorithms has shown empirical success across a range of machine learning tasks. Recently, a new class of stochastic momentum algorithms has emerged within the Linear Minimization Oracle (LMO) framework--leading to state-of-the-art methods, such as Muon, Scion, and Gluon, that effectively solve deep neural network training problems. However, traditional stochastic momentum methods offer convergence guarantees no better than the ${O}(1/K^{1/4})$ rate. While several approaches--such as Hessian-Corrected Momentum (HCM)--have aimed to improve this rate, their theoretical results are generally restricted to the Euclidean norm setting. This limitation hinders their applicability in problems, where arbitrary norms are often required. In this paper, we extend the LMO-based framework by integrating HCM, and provide convergence guarantees under relaxed smoothness and arbitrary norm settings. We establish improved convergence rates of ${O}(1/K^{1/3})$ for HCM, which can adapt to the geometry of the problem and achieve a faster rate than traditional momentum. Experimental results on training Multi-Layer Perceptrons (MLPs) and Long Short-Term Memory (LSTM) networks verify our theoretical observations.

