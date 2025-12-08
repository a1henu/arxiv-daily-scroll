---
layout: default
title: Global stability of vehicle-with-driver dynamics via Sum-of-Squares programming
---

# Global stability of vehicle-with-driver dynamics via Sum-of-Squares programming
**arXiv**：[2512.05806v1](https://arxiv.org/abs/2512.05806) · [PDF](https://arxiv.org/pdf/2512.05806.pdf)  
**作者**：Martino Gulisano, Marco Gabiccini  

**一句话要点**：提出基于平方和规划的迭代方法，估计车辆-驾驶员系统的安全不变集，用于实时安全评估。

**关键词**：平方和规划, 车辆动力学, 李雅普诺夫函数, 安全不变集, 驾驶员模型, 实时安全评估

## 3 点简述
- 核心问题：估计七状态车辆-驾驶员系统的安全吸引区域，考虑渐近稳定性和状态安全约束。
- 方法要点：通过原创迭代平方和程序优化李雅普诺夫函数，计算多项式近似模型的安全集。
- 实验或效果：在转向不足和过度转向场景中验证，安全集与模拟参考边界一致，支持实时安全监控。

## 摘要（原文）

> This work estimates safe invariant subsets of the Region of Attraction (ROA) for a seven-state vehicle-with-driver system, capturing both asymptotic stability and the influence of state-safety bounds along the system trajectory. Safe sets are computed by optimizing Lyapunov functions through an original iterative Sum-of-Squares (SOS) procedure. The method is first demonstrated on a two-state benchmark, where it accurately recovers a prescribed safe region as the 1-level set of a polynomial Lyapunov function. We then describe the distinguishing characteristics of the studied vehicle-with-driver system: the control dynamics mimic human driver behavior through a delayed preview-tracking model that, with suitable parameter choices, can also emulate digital controllers. To enable SOS optimization, a polynomial approximation of the nonlinear vehicle model is derived, together with its operating-envelope constraints. The framework is then applied to understeering and oversteering scenarios, and the estimated safe sets are compared with reference boundaries obtained from exhaustive simulations. The results show that SOS techniques can efficiently deliver Lyapunov-defined safe regions, supporting their potential use for real-time safety assessment, for example as a supervisory layer for active vehicle control.

