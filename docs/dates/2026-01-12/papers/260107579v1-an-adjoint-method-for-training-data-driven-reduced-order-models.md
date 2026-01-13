---
layout: default
title: An adjoint method for training data-driven reduced-order models
---

# An adjoint method for training data-driven reduced-order models
**arXiv**：[2601.07579v1](https://arxiv.org/abs/2601.07579) · [PDF](https://arxiv.org/pdf/2601.07579.pdf)  
**作者**：Donglin Liu, Francisco García Atienza, Mengwu Guo  

**一句话要点**：提出基于伴随方法的训练框架以提升数据驱动降阶模型在稀疏采样和噪声下的鲁棒性。

**关键词**：降阶建模, 伴随方法, 数据驱动模型, 算子推断, 偏微分方程, 鲁棒训练

## 3 点简述
- 核心问题：传统数据驱动降阶模型在稀疏采样和噪声数据下精度和稳定性不足。
- 方法要点：结合连续时间算子推断与伴随状态法，通过轨迹损失最小化避免时间导数估计并提供时间正则化。
- 实验或效果：在三个偏微分方程上验证，相比标准算子推断，在稀疏采样和噪声下具有更高精度和稳定性。

## 摘要（原文）

> Reduced-order modeling lies at the interface of numerical analysis and data-driven scientific computing, providing principled ways to compress high-fidelity simulations in science and engineering. We propose a training framework that couples a continuous-time form of operator inference with the adjoint-state method to obtain robust data-driven reduced-order models. This method minimizes a trajectory-based loss between reduced-order solutions and projected snapshot data, which removes the need to estimate time derivatives from noisy measurements and provides intrinsic temporal regularization through time integration. We derive the corresponding continuous adjoint equations to compute gradients efficiently and implement a gradient based optimizer to update the reduced model parameters. Each iteration only requires one forward reduced order solve and one adjoint solve, followed by inexpensive gradient assembly, making the method attractive for large-scale simulations. We validate the proposed method on three partial differential equations: viscous Burgers' equation, the two-dimensional Fisher-KPP equation, and an advection-diffusion equation. We perform systematic comparisons against standard operator inference under two perturbation regimes, namely reduced temporal snapshot density and additive Gaussian noise. For clean data, both approaches deliver similar accuracy, but in situations with sparse sampling and noise, the proposed adjoint-based training provides better accuracy and enhanced roll-out stability.

