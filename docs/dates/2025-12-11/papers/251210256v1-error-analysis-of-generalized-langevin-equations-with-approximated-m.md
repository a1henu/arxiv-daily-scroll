---
layout: default
title: Error Analysis of Generalized Langevin Equations with Approximated Memory Kernels
---

# Error Analysis of Generalized Langevin Equations with Approximated Memory Kernels
**arXiv**：[2512.10256v1](https://arxiv.org/abs/2512.10256) · [PDF](https://arxiv.org/pdf/2512.10256.pdf)  
**作者**：Quanjun Lang, Jianfeng Lu  

**一句话要点**：分析广义朗之万方程在近似记忆核下的预测误差，建立轨迹误差与核估计误差的定量界限

**关键词**：广义朗之万方程, 记忆核, 预测误差分析, 随机Volterra方程, 加权范数, 数值验证

## 3 点简述
- 核心问题：研究具有记忆的随机动力系统（广义朗之万方程）中，近似记忆核导致的轨迹预测误差。
- 方法要点：结合同步噪声耦合和Volterra比较定理，在强凸势下推导误差衰减率，并利用加权范数量化核估计误差的影响。
- 实验或效果：通过数值示例验证理论结果，涵盖次指数和指数核类，适用于非平移不变核和白噪声强迫。

## 摘要（原文）

> We analyze prediction error in stochastic dynamical systems with memory, focusing on generalized Langevin equations (GLEs) formulated as stochastic Volterra equations. We establish that, under a strongly convex potential, trajectory discrepancies decay at a rate determined by the decay of the memory kernel and are quantitatively bounded by the estimation error of the kernel in a weighted norm. Our analysis integrates synchronized noise coupling with a Volterra comparison theorem, encompassing both subexponential and exponential kernel classes. For first-order models, we derive moment and perturbation bounds using resolvent estimates in weighted spaces. For second-order models with confining potentials, we prove contraction and stability under kernel perturbations using a hypocoercive Lyapunov-type distance. This framework accommodates non-translation-invariant kernels and white-noise forcing, explicitly linking improved kernel estimation to enhanced trajectory prediction. Numerical examples validate these theoretical findings.

