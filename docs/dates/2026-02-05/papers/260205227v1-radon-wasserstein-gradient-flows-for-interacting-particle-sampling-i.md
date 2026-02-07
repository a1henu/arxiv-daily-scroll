---
layout: default
title: Radon--Wasserstein Gradient Flows for Interacting-Particle Sampling in High Dimensions
---

# Radon--Wasserstein Gradient Flows for Interacting-Particle Sampling in High Dimensions
**arXiv**：[2602.05227v1](https://arxiv.org/abs/2602.05227) · [PDF](https://arxiv.org/pdf/2602.05227.pdf)  
**作者**：Elias Hess-Childs, Dejan Slepčev, Lantian Xu  

**一句话要点**：提出基于Radon-Wasserstein几何的梯度流，用于高维交互粒子采样，实现线性计算成本。

**关键词**：梯度流, 交互粒子采样, Radon-Wasserstein几何, 高维计算, KL散度, 数值实验

## 3 点简述
- 核心问题：高维空间中基于KL散度的梯度流采样方法计算成本高，难以高效实现交互粒子近似。
- 方法要点：引入Radon-Wasserstein几何，利用Radon变换使梯度流速度仅依赖一维投影，降低计算复杂度。
- 实验或效果：通过数值实验验证算法性能，提供理论保证如流的存在性和长期收敛性。

## 摘要（原文）

> Gradient flows of the Kullback--Leibler (KL) divergence, such as the Fokker--Planck equation and Stein Variational Gradient Descent, evolve a distribution toward a target density known only up to a normalizing constant. We introduce new gradient flows of the KL divergence with a remarkable combination of properties: they admit accurate interacting-particle approximations in high dimensions, and the per-step cost scales linearly in both the number of particles and the dimension. These gradient flows are based on new transportation-based Riemannian geometries on the space of probability measures: the Radon--Wasserstein geometry and the related Regularized Radon--Wasserstein (RRW) geometry. We define these geometries using the Radon transform so that the gradient-flow velocities depend only on one-dimensional projections. This yields interacting-particle-based algorithms whose per-step cost follows from efficient Fast Fourier Transform-based evaluation of the required 1D convolutions. We additionally provide numerical experiments that study the performance of the proposed algorithms and compare convergence behavior and quantization. Finally, we prove some theoretical results including well-posedness of the flows and long-time convergence guarantees for the RRW flow.

