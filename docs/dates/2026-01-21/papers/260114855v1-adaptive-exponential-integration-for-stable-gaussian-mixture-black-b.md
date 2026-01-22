---
layout: default
title: Adaptive Exponential Integration for Stable Gaussian Mixture Black-Box Variational Inference
---

# Adaptive Exponential Integration for Stable Gaussian Mixture Black-Box Variational Inference
**arXiv**：[2601.14855v1](https://arxiv.org/abs/2601.14855) · [PDF](https://arxiv.org/pdf/2601.14855.pdf)  
**作者**：Baojun Che, Yifan Chen, Daniel Zhengyu Huang, Xinying Mao, Weijie Wang  

**一句话要点**：提出自适应指数积分框架以稳定高效地实现高斯混合黑盒变分推断

**关键词**：黑盒变分推断, 高斯混合模型, 自适应优化, 指数积分, 稳定性分析, 贝叶斯反问题

## 3 点简述
- 核心问题：高斯混合黑盒变分推断中标准数值优化方法存在不稳定和低效问题。
- 方法要点：结合仿射不变预处理、指数积分器和自适应时间步长，确保协方差矩阵正定性并适应不同优化阶段。
- 实验或效果：在噪声自由设置下证明指数收敛，并在多模态分布和PDE贝叶斯反问题中验证有效性。

## 摘要（原文）

> Black-box variational inference (BBVI) with Gaussian mixture families offers a flexible approach for approximating complex posterior distributions without requiring gradients of the target density. However, standard numerical optimization methods often suffer from instability and inefficiency. We develop a stable and efficient framework that combines three key components: (1) affine-invariant preconditioning via natural gradient formulations, (2) an exponential integrator that unconditionally preserves the positive definiteness of covariance matrices, and (3) adaptive time stepping to ensure stability and to accommodate distinct warm-up and convergence phases. The proposed approach has natural connections to manifold optimization and mirror descent. For Gaussian posteriors, we prove exponential convergence in the noise-free setting and almost-sure convergence under Monte Carlo estimation, rigorously justifying the necessity of adaptive time stepping. Numerical experiments on multimodal distributions, Neal's multiscale funnel, and a PDE-based Bayesian inverse problem for Darcy flow demonstrate the effectiveness of the proposed method.

