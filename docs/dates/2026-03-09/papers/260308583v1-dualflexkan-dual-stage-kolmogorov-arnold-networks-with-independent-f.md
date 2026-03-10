---
layout: default
title: DualFlexKAN: Dual-stage Kolmogorov-Arnold Networks with Independent Function Control
---

# DualFlexKAN: Dual-stage Kolmogorov-Arnold Networks with Independent Function Control
**arXiv**：[2603.08583v1](https://arxiv.org/abs/2603.08583) · [PDF](https://arxiv.org/pdf/2603.08583.pdf)  
**作者**：Andrés Ortiz, Nicolás J. Gallego-Molina, Carmen Jiménez-Mesa, Juan M. Górriz, Javier Ramírez  

**一句话要点**：提出DualFlexKAN以解决KAN参数爆炸和架构僵化问题，适用于数据高效学习和科学应用。

**关键词**：Kolmogorov-Arnold网络, 双阶段架构, 自适应非线性, 参数优化, 函数逼近, 科学机器学习

## 3 点简述
- 核心问题：KAN参数二次增长且架构僵化，阻碍正则化集成。
- 方法要点：双阶段机制独立控制输入变换和输出激活，支持多种基函数和正则化。
- 实验或效果：在回归和函数逼近中优于MLP和KAN，参数减少1-2个数量级。

## 摘要（原文）

> Multi-Layer Perceptrons (MLPs) rely on pre-defined, fixed activation functions, imposing a static inductive bias that forces the network to approximate complex topologies solely through increased depth and width. Kolmogorov-Arnold Networks (KANs) address this limitation through edge-centric learnable functions, yet their formulation suffers from quadratic parameter scaling and architectural rigidity that hinders the effective integration of standard regularization techniques. This paper introduces the DualFlexKAN (DFKAN), a flexible architecture featuring a dual-stage mechanism that independently controls pre-linear input transformations and post-linear output activations. This decoupling enables hybrid networks that optimize the trade-off between expressiveness and computational cost. Unlike standard formulations, DFKAN supports diverse basis function families, including orthogonal polynomials, B-splines, and radial basis functions, integrated with configurable regularization strategies that stabilize training dynamics. Comprehensive evaluations across regression benchmarks, physics-informed tasks, and function approximation demonstrate that DFKAN outperforms both MLPs and conventional KANs in accuracy, convergence speed, and gradient fidelity. The proposed hybrid configurations achieve superior performance with one to two orders of magnitude fewer parameters than standard KANs, effectively mitigating the parameter explosion problem while preserving KAN-style expressiveness. DFKAN provides a principled, scalable framework for incorporating adaptive non-linearities, proving particularly advantageous for data-efficient learning and interpretable function discovery in scientific applications.

