---
layout: default
title: NN-OpInf: an operator inference approach using structure-preserving composable neural networks
---

# NN-OpInf: an operator inference approach using structure-preserving composable neural networks
**arXiv**：[2603.08488v1](https://arxiv.org/abs/2603.08488) · [PDF](https://arxiv.org/pdf/2603.08488.pdf)  
**作者**：Eric Parish, Anthony Gruber, Patrick Blonigan, Irina Tezaur  

**一句话要点**：提出NN-OpInf框架，用于非多项式非线性动力系统的非侵入式降阶建模

**关键词**：算子推断, 降阶建模, 神经网络, 结构保持, 非侵入式建模, 非线性动力系统

## 3 点简述
- 核心问题：传统多项式OpInf在非多项式非线性动力系统中建模精度和稳定性不足
- 方法要点：基于结构保持可组合神经网络，学习潜在动力学并强制局部算子结构
- 实验或效果：在多个非线性参数问题中，相比P-OpInf和先前NN-ROM，提高了准确性、稳定性和鲁棒性

## 摘要（原文）

> We propose neural network operator inference (NN-OpInf): a structure-preserving, composable, and minimally restrictive operator inference framework for the non-intrusive reduced-order modeling of dynamical systems. The approach learns latent dynamics from snapshot data, enforcing local operator structure such as skew-symmetry, (semi-)positive definiteness, and gradient preservation, while also reflecting complex dynamics by supporting additive compositions of heterogeneous operators. We present practical training strategies and analyze computational costs relative to linear and quadratic polynomial OpInf (P-OpInf). Numerical experiments across several nonlinear and parametric problems demonstrate improved accuracy, stability, and robustness over P-OpInf and prior NN-ROM formulations, particularly when the dynamics are not well represented by polynomial models. These results suggest that NN-OpInf can serve as an effective drop-in replacement for P-OpInf when the dynamics to be modeled contain non-polynomial nonlinearities, offering potential gains in accuracy and out-of-distribution performance at the expense of higher training computational costs and a more difficult, non-convex learning problem.

