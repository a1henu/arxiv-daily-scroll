---
layout: default
title: Robust and Efficient MuJoCo-based Model Predictive Control via Web of Affine Spaces Derivatives
---

# Robust and Efficient MuJoCo-based Model Predictive Control via Web of Affine Spaces Derivatives
**arXiv**：[2512.21109v1](https://arxiv.org/abs/2512.21109) · [PDF](https://arxiv.org/pdf/2512.21109.pdf)  
**作者**：Chen Liang, Daniel Rakita  

**一句话要点**：提出基于WASP导数的MJPC方法，以提升MuJoCo MPC的效率和鲁棒性。

**关键词**：模型预测控制, MuJoCo模拟器, 导数计算, WASP方法, 机器人控制, 性能优化

## 3 点简述
- MJPC依赖有限差分计算导数，在高自由度系统中成为性能瓶颈。
- 引入WASP导数作为替代，通过重用先验信息加速和稳定导数计算。
- 实验显示WASP在MJPC任务中无缝集成，速度提升达2倍，优于随机采样规划器。

## 摘要（原文）

> MuJoCo is a powerful and efficient physics simulator widely used in robotics. One common way it is applied in practice is through Model Predictive Control (MPC), which uses repeated rollouts of the simulator to optimize future actions and generate responsive control policies in real time. To make this process more accessible, the open source library MuJoCo MPC (MJPC) provides ready-to-use MPC algorithms and implementations built directly on top of the MuJoCo simulator. However, MJPC relies on finite differencing (FD) to compute derivatives through the underlying MuJoCo simulator, which is often a key bottleneck that can make it prohibitively costly for time-sensitive tasks, especially in high-DOF systems or complex scenes. In this paper, we introduce the use of Web of Affine Spaces (WASP) derivatives within MJPC as a drop-in replacement for FD. WASP is a recently developed approach for efficiently computing sequences of accurate derivative approximations. By reusing information from prior, related derivative calculations, WASP accelerates and stabilizes the computation of new derivatives, making it especially well suited for MPC's iterative, fine-grained updates over time. We evaluate WASP across a diverse suite of MJPC tasks spanning multiple robot embodiments. Our results suggest that WASP derivatives are particularly effective in MJPC: it integrates seamlessly across tasks, delivers consistently robust performance, and achieves up to a 2$\mathsf{x}$ speedup compared to an FD backend when used with derivative-based planners, such as iLQG. In addition, WASP-based MPC outperforms MJPC's stochastic sampling-based planners on our evaluation tasks, offering both greater efficiency and reliability. To support adoption and future research, we release an open-source implementation of MJPC with WASP derivatives fully integrated.

