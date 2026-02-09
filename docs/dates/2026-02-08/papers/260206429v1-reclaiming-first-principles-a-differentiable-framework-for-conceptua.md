---
layout: default
title: Reclaiming First Principles: A Differentiable Framework for Conceptual Hydrologic Models
---

# Reclaiming First Principles: A Differentiable Framework for Conceptual Hydrologic Models
**arXiv**：[2602.06429v1](https://arxiv.org/abs/2602.06429) · [PDF](https://arxiv.org/pdf/2602.06429.pdf)  
**作者**：Jasper A. Vrugt, Jonathan M. Frame, Ethan Bollman  

**一句话要点**：提出基于精确参数敏感性的可微分水文模型框架，以解决概念水文模型校准缓慢和数值脆弱问题。

**关键词**：可微分建模, 水文模型校准, 参数敏感性, 梯度优化, ODE系统, 解析梯度

## 3 点简述
- 核心问题：概念水文模型校准依赖有限差分或自动微分，计算成本高且引入误差和不稳定性。
- 方法要点：通过扩展控制ODE系统，联合演化模型状态和雅可比矩阵，提供完全解析的梯度向量。
- 实验或效果：实现快速、稳定和透明的梯度校准，避免数值噪声和外部自动微分库的依赖。

## 摘要（原文）

> Conceptual hydrologic models remain the cornerstone of rainfall-runoff modeling, yet their calibration is often slow and numerically fragile. Most gradient-based parameter estimation methods rely on finite-difference approximations or automatic differentiation frameworks (e.g., JAX, PyTorch and TensorFlow), which are computationally demanding and introduce truncation errors, solver instabilities, and substantial overhead. These limitations are particularly acute for the ODE systems of conceptual watershed models. Here we introduce a fully analytic and computationally efficient framework for differentiable hydrologic modeling based on exact parameter sensitivities. By augmenting the governing ODE system with sensitivity equations, we jointly evolve the model states and the Jacobian matrix with respect to all parameters. This Jacobian then provides fully analytic gradient vectors for any differentiable loss function. These include classical objective functions such as the sum of absolute and squared residuals, widely used hydrologic performance metrics such as the Nash-Sutcliffe and Kling-Gupta efficiencies, robust loss functions that down-weight extreme events, and hydrograph-based functionals such as flow-duration and recession curves. The analytic sensitivities eliminate the step-size dependence and noise inherent to numerical differentiation, while avoiding the instability of adjoint methods and the overhead of modern machine-learning autodiff toolchains. The resulting gradients are deterministic, physically interpretable, and straightforward to embed in gradient-based optimizers. Overall, this work enables rapid, stable, and transparent gradient-based calibration of conceptual hydrologic models, unlocking the full potential of differentiable modeling without reliance on external, opaque, or CPU-intensive automatic-differentiation libraries.

