---
layout: default
title: Least Restrictive Hyperplane Control Barrier Functions
---

# Least Restrictive Hyperplane Control Barrier Functions
**arXiv**：[2510.18643v1](https://arxiv.org/abs/2510.18643) · [PDF](https://arxiv.org/pdf/2510.18643.pdf)  
**作者**：Mattias Trende, Petter Ögren  

**一句话要点**：提出最小限制超平面控制屏障函数以优化安全控制，应对复杂不安全区域。

**关键词**：控制屏障函数, 安全控制, 超平面近似, 优化方法, 动态系统, 障碍物规避

## 3 点简述
- 核心问题：复杂不安全区域下高阶CBF设计困难，保守近似限制控制灵活性。
- 方法要点：联合优化CBF与安全控制，最小化与期望控制的偏差，确保安全。
- 实验或效果：在双积分器系统中验证，处理静态和动态任意形状障碍物。

## 摘要（原文）

> Control Barrier Functions (CBFs) can provide provable safety guarantees for
> dynamic systems. However, finding a valid CBF for a system of interest is often
> non-trivial, especially if the shape of the unsafe region is complex and the
> CBFs are of higher order. A common solution to this problem is to make a
> conservative approximation of the unsafe region in the form of a
> line/hyperplane, and use the corresponding conservative Hyperplane-CBF when
> deciding on safe control actions. In this letter, we note that conservative
> constraints are only a problem if they prevent us from doing what we want.
> Thus, instead of first choosing a CBF and then choosing a safe control with
> respect to the CBF, we optimize over a combination of CBFs and safe controls to
> get as close as possible to our desired control, while still having the safety
> guarantee provided by the CBF. We call the corresponding CBF the least
> restrictive Hyperplane-CBF. Finally, we also provide a way of creating a smooth
> parameterization of the CBF-family for the optimization, and illustrate the
> approach on a double integrator dynamical system with acceleration constraints,
> moving through a group of arbitrarily shaped static and moving obstacles.

