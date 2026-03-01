---
layout: default
title: Physics-informed neural particle flow for the Bayesian update step
---

# Physics-informed neural particle flow for the Bayesian update step
**arXiv**：[2602.23089v1](https://arxiv.org/abs/2602.23089) · [PDF](https://arxiv.org/pdf/2602.23089.pdf)  
**作者**：Domonkos Csuzdi, Tamás Bécsi, Olivér Törő  

**一句话要点**：提出物理信息神经粒子流以解决高维非线性贝叶斯更新中的计算难题

**关键词**：贝叶斯更新, 粒子流滤波, 物理信息神经网络, 无监督学习, 高维非线性估计, 概率传输

## 3 点简述
- 核心问题：高维非线性贝叶斯更新计算复杂，现有方法常产生刚性微分方程或忽略概率传输的几何结构。
- 方法要点：结合对数同伦轨迹与连续性方程推导主PDE，通过物理约束训练神经网络近似传输速度场，实现无监督学习。
- 实验或效果：在多模态基准和挑战性非线性场景中验证，相比先进基线具有更好的模式覆盖和鲁棒性，降低在线计算复杂度。

## 摘要（原文）

> The Bayesian update step poses significant computational challenges in high-dimensional nonlinear estimation. While log-homotopy particle flow filters offer an alternative to stochastic sampling, existing formulations usually yield stiff differential equations. Conversely, existing deep learning approximations typically treat the update as a black-box task or rely on asymptotic relaxation, neglecting the exact geometric structure of the finite-horizon probability transport. In this work, we propose a physics-informed neural particle flow, which is an amortized inference framework. To construct the flow, we couple the log-homotopy trajectory of the prior to posterior density function with the continuity equation describing the density evolution. This derivation yields a governing partial differential equation (PDE), referred to as the master PDE. By embedding this PDE as a physical constraint into the loss function, we train a neural network to approximate the transport velocity field. This approach enables purely unsupervised training, eliminating the need for ground-truth posterior samples. We demonstrate that the neural parameterization acts as an implicit regularizer, mitigating the numerical stiffness inherent to analytic flows and reducing online computational complexity. Experimental validation on multimodal benchmarks and a challenging nonlinear scenario confirms better mode coverage and robustness compared to state-of-the-art baselines.

