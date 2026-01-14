---
layout: default
title: Multi-Preconditioned LBFGS for Training Finite-Basis PINNs
---

# Multi-Preconditioned LBFGS for Training Finite-Basis PINNs
**arXiv**：[2601.08709v1](https://arxiv.org/abs/2601.08709) · [PDF](https://arxiv.org/pdf/2601.08709.pdf)  
**作者**：Marc Salvadó-Benasco, Aymane Kssim, Alexander Heinlein, Rolf Krause, Serge Gratton, Alena Kopaničáková  

**一句话要点**：提出多预条件LBFGS算法以加速有限基物理信息神经网络的训练

**关键词**：物理信息神经网络, 有限基方法, 多预条件LBFGS, 域分解, 准牛顿法, 并行训练

## 3 点简述
- 核心问题：有限基物理信息神经网络训练中，标准LBFGS收敛慢且通信开销高。
- 方法要点：基于非线性加性Schwarz方法，利用域分解架构构建并行子域准牛顿校正，并通过低维子空间最小化优化组合。
- 实验或效果：数值实验显示，MP-LBFGS能提升收敛速度和模型精度，同时降低通信开销。

## 摘要（原文）

> A multi-preconditioned LBFGS (MP-LBFGS) algorithm is introduced for training finite-basis physics-informed neural networks (FBPINNs). The algorithm is motivated by the nonlinear additive Schwarz method and exploits the domain-decomposition-inspired additive architecture of FBPINNs, in which local neural networks are defined on subdomains, thereby localizing the network representation. Parallel, subdomain-local quasi-Newton corrections are then constructed on the corresponding local parts of the architecture. A key feature is a novel nonlinear multi-preconditioning mechanism, in which subdomain corrections are optimally combined through the solution of a low-dimensional subspace minimization problem. Numerical experiments indicate that MP-LBFGS can improve convergence speed, as well as model accuracy over standard LBFGS while incurring lower communication overhead.

