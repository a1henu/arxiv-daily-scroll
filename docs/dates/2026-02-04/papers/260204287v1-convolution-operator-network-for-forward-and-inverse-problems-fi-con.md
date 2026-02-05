---
layout: default
title: Convolution Operator Network for Forward and Inverse Problems (FI-Conv): Application to Plasma Turbulence Simulations
---

# Convolution Operator Network for Forward and Inverse Problems (FI-Conv): Application to Plasma Turbulence Simulations
**arXiv**：[2602.04287v1](https://arxiv.org/abs/2602.04287) · [PDF](https://arxiv.org/pdf/2602.04287.pdf)  
**作者**：Xingzhuo Chen, Anthony Poole, Ionut-Gabriel Farcas, David R. Hatch, Ulisses Braga-Neto  

**一句话要点**：提出FI-Conv卷积算子网络，用于等离子体湍流模拟中的正反问题预测与参数估计。

**关键词**：卷积算子网络, 等离子体湍流模拟, 正反问题求解, U-Net架构, ConvNext V2块, 梯度下降反演

## 3 点简述
- 核心问题：解决复杂时空动力学系统（如湍流）的演化预测和参数估计难题。
- 方法要点：基于U-Net架构，用ConvNext V2块替换卷积层，保持高频输入性能并降低计算复杂度。
- 实验或效果：在Hasegawa-Wakatani方程上实现短期准确预测和长期统计特性捕捉，并基于梯度下降进行参数反演。

## 摘要（原文）

> We propose the Convolutional Operator Network for Forward and Inverse Problems (FI-Conv), a framework capable of predicting system evolution and estimating parameters in complex spatio-temporal dynamics, such as turbulence. FI-Conv is built on a U-Net architecture, in which most convolutional layers are replaced by ConvNeXt V2 blocks. This design preserves U-Net performance on inputs with high-frequency variations while maintaining low computational complexity. FI-Conv uses an initial state, PDE parameters, and evolution time as input to predict the system future state. As a representative example of a system exhibiting complex dynamics, we evaluate the performance of FI-Conv on the task of predicting turbulent plasma fields governed by the Hasegawa-Wakatani (HW) equations. The HW system models two-dimensional electrostatic drift-wave turbulence and exhibits strongly nonlinear behavior, making accurate approximation and long-term prediction particularly challenging. Using an autoregressive forecasting procedure, FI-Conv achieves accurate forward prediction of the plasma state evolution over short times (t ~ 3) and captures the statistic properties of derived physical quantities of interest over longer times (t ~ 100). Moreover, we develop a gradient-descent-based inverse estimation method that accurately infers PDE parameters from plasma state evolution data, without modifying the trained model weights. Collectively, our results demonstrate that FI-Conv can be an effective alternative to existing physics-informed machine learning methods for systems with complex spatio-temporal dynamics.

