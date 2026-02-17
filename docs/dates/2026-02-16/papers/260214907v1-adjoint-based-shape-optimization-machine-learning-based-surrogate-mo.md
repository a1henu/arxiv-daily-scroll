---
layout: default
title: Adjoint-based Shape Optimization, Machine Learning based Surrogate Models, Conditional Variational Autoencoder (CVAE), Voith Schneider propulsion (VSP), Self-propelled Ship, Propulsion Model, Hull Optimization
---

# Adjoint-based Shape Optimization, Machine Learning based Surrogate Models, Conditional Variational Autoencoder (CVAE), Voith Schneider propulsion (VSP), Self-propelled Ship, Propulsion Model, Hull Optimization
**arXiv**：[2602.14907v1](https://arxiv.org/abs/2602.14907) · [PDF](https://arxiv.org/pdf/2602.14907.pdf)  
**作者**：Moloud Arian Maram, Georgios Bletsos, Thanh Tung Nguyen, Ahmed Hassan, Michael Palm, Thomas Rung  

**一句话要点**：提出基于条件变分自编码器的机器学习辅助优化框架，以解决船舶伴随形状优化中复杂推进系统带来的计算挑战。

**关键词**：伴随形状优化, 机器学习代理模型, 条件变分自编码器, 船舶推进系统, 计算流体动力学, 阻力优化

## 3 点简述
- 核心问题：船舶伴随形状优化应用于复杂推进系统时，因长时间瞬态模拟和反向传播导致存储与计算需求高，阻碍工业应用。
- 方法要点：使用条件变分自编码器构建推进系统的代理模型，替代几何和时间解析的推进器，实现数据驱动近似。
- 实验或效果：代理模型在保持精度的同时显著节省计算资源，优化后船体形状阻力降低超过8%。

## 摘要（原文）

> Adjoint-based shape optimization of ship hulls is a powerful tool for addressing high-dimensional design problems in naval architecture, particularly in minimizing the ship resistance. However, its application to vessels that employ complex propulsion systems introduces significant challenges. They arise from the need for transient simulations extending over long periods of time with small time steps and from the reverse temporal propagation of the primal and adjoint solutions. These challenges place considerable demands on the required storage and computing power, which significantly hamper the use of adjoint methods in the industry. To address this issue, we propose a machine learning-assisted optimization framework that employs a Conditional Variational Autoencoder-based surrogate model of the propulsion system. The surrogate model replicates the time-averaged flow field induced by a Voith Schneider Propeller and replaces the geometrically and time-resolved propeller with a data-driven approximation. Primal flow verification examples demonstrate that the surrogate model achieves significant computational savings while maintaining the necessary accuracy of the resolved propeller. Optimization studies show that ignoring the propulsion system can yield designs that perform worse than the initial shape. In contrast, the proposed method produces shapes that achieve more than an 8\% reduction in resistance.

