---
layout: default
title: BEACONS: Bounded-Error, Algebraically-Composable Neural Solvers for Partial Differential Equations
---

# BEACONS: Bounded-Error, Algebraically-Composable Neural Solvers for Partial Differential Equations
**arXiv**：[2602.14853v1](https://arxiv.org/abs/2602.14853) · [PDF](https://arxiv.org/pdf/2602.14853.pdf)  
**作者**：Jonathan Gorard, Ammar Hakim, James Juno  

**一句话要点**：提出BEACONS框架以构建形式验证的神经网络求解器，确保偏微分方程在训练域外求解的可靠性与有界误差。

**关键词**：偏微分方程求解, 形式验证, 神经网络外推, 有界误差, 组合学习, 计算物理

## 3 点简述
- 核心问题：神经网络在训练数据凸包外泛化不可靠，限制其在计算物理中求解偏微分方程的应用。
- 方法要点：利用特征线法预测解的性质，构建浅层网络的有界误差，并通过组合学习形成深层架构以抑制误差。
- 实验或效果：应用于线性和非线性偏微分方程，如线性平流方程和欧拉方程，在1D和2D中实现可靠外推求解。

## 摘要（原文）

> The traditional limitations of neural networks in reliably generalizing beyond the convex hulls of their training data present a significant problem for computational physics, in which one often wishes to solve PDEs in regimes far beyond anything which can be experimentally or analytically validated. In this paper, we show how it is possible to circumvent these limitations by constructing formally-verified neural network solvers for PDEs, with rigorous convergence, stability, and conservation properties, whose correctness can therefore be guaranteed even in extrapolatory regimes. By using the method of characteristics to predict the analytical properties of PDE solutions a priori (even in regions arbitrarily far from the training domain), we show how it is possible to construct rigorous extrapolatory bounds on the worst-case L^inf errors of shallow neural network approximations. Then, by decomposing PDE solutions into compositions of simpler functions, we show how it is possible to compose these shallow neural networks together to form deep architectures, based on ideas from compositional deep learning, in which the large L^inf errors in the approximations have been suppressed. The resulting framework, called BEACONS (Bounded-Error, Algebraically-COmposable Neural Solvers), comprises both an automatic code-generator for the neural solvers themselves, as well as a bespoke automated theorem-proving system for producing machine-checkable certificates of correctness. We apply the framework to a variety of linear and non-linear PDEs, including the linear advection and inviscid Burgers' equations, as well as the full compressible Euler equations, in both 1D and 2D, and illustrate how BEACONS architectures are able to extrapolate solutions far beyond the training data in a reliable and bounded way. Various advantages of the approach over the classical PINN approach are discussed.

