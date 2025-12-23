---
layout: default
title: An Inverse Scattering Inspired Fourier Neural Operator for Time-Dependent PDE Learning
---

# An Inverse Scattering Inspired Fourier Neural Operator for Time-Dependent PDE Learning
**arXiv**：[2512.19439v1](https://arxiv.org/abs/2512.19439) · [PDF](https://arxiv.org/pdf/2512.19439.pdf)  
**作者**：Rixin Yu  

**一句话要点**：提出逆散射启发的傅里叶神经算子以增强非线性偏微分方程长期预测稳定性

**关键词**：傅里叶神经算子, 逆散射变换, 非线性偏微分方程学习, 长期稳定性, 谱演化, 可逆神经网络

## 3 点简述
- 核心问题：现有神经算子方法在非线性偏微分方程长期预测中稳定性不足，受限于无约束潜在表示和累积误差。
- 方法要点：引入逆散射变换启发的可逆神经变换和指数傅里叶层，强制提升与投影映射的近似可逆配对，编码谱动力学。
- 实验或效果：在多个基准偏微分方程上验证，IS-FNO实现更低短期误差和显著改善的长期稳定性，尤其在非刚性区域。

## 摘要（原文）

> Learning accurate and stable time-advancement operators for nonlinear partial differential equations (PDEs) remains challenging, particularly for chaotic, stiff, and long-horizon dynamical systems. While neural operator methods such as the Fourier Neural Operator (FNO) and Koopman-inspired extensions achieve good short-term accuracy, their long-term stability is often limited by unconstrained latent representations and cumulative rollout errors. In this work, we introduce an inverse scattering inspired Fourier Neural Operator(IS-FNO), motivated by the reversibility and spectral evolution structure underlying the classical inverse scattering transform. The proposed architecture enforces a near-reversible pairing between lifting and projection maps through an explicitly invertible neural transformation, and models latent temporal evolution using exponential Fourier layers that naturally encode linear and nonlinear spectral dynamics. We systematically evaluate IS-FNO against baseline FNO and Koopman-based models on a range of benchmark PDEs, including the Michelson-Sivashinsky and Kuramoto-Sivashinsky equations (in one and two dimensions), as well as the integrable Korteweg-de Vries and Kadomtsev-Petviashvili equations. The results demonstrate that IS-FNO achieves lower short-term errors and substantially improved long-horizon stability in non-stiff regimes. For integrable systems, reduced IS-FNO variants that embed analytical scattering structure retain competitive long-term accuracy despite limited model capacity. Overall, this work shows that incorporating physical structure -- particularly reversibility and spectral evolution -- into neural operator design significantly enhances robustness and long-term predictive fidelity for nonlinear PDE dynamics.

