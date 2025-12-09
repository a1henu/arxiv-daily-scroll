---
layout: default
title: RRAEDy: Adaptive Latent Linearization of Nonlinear Dynamical Systems
---

# RRAEDy: Adaptive Latent Linearization of Nonlinear Dynamical Systems
**arXiv**：[2512.07542v1](https://arxiv.org/abs/2512.07542) · [PDF](https://arxiv.org/pdf/2512.07542.pdf)  
**作者**：Jad Mounayer, Sebastian Rodriguez, Jerome Tomezyk, Chady Ghnatios, Francisco Chinesta  

**一句话要点**：提出RRAEDy模型，通过自适应潜在维度发现和线性化动态，解决非线性动力系统建模中的维度固定与正则化不足问题。

**关键词**：非线性动力系统, 潜在空间建模, 动态模式分解, 秩降自编码器, 自适应维度选择, 参数常微分方程

## 3 点简述
- 现有潜在空间模型需预先固定维度，依赖复杂损失平衡，且缺乏潜在变量正则化。
- RRAEDy基于秩降自编码器，自动发现潜在维度并学习线性动态模式分解算子，无需辅助损失或手动调参。
- 在Van der Pol振荡器、Burgers方程等基准测试中，模型实现准确稳健预测，并扩展处理参数常微分方程。

## 摘要（原文）

> Most existing latent-space models for dynamical systems require fixing the latent dimension in advance, they rely on complex loss balancing to approximate linear dynamics, and they don't regularize the latent variables. We introduce RRAEDy, a model that removes these limitations by discovering the appropriate latent dimension, while enforcing both regularized and linearized dynamics in the latent space. Built upon Rank-Reduction Autoencoders (RRAEs), RRAEDy automatically rank and prune latent variables through their singular values while learning a latent Dynamic Mode Decomposition (DMD) operator that governs their temporal progression. This structure-free yet linearly constrained formulation enables the model to learn stable and low-dimensional dynamics without auxiliary losses or manual tuning. We provide theoretical analysis demonstrating the stability of the learned operator and showcase the generality of our model by proposing an extension that handles parametric ODEs. Experiments on canonical benchmarks, including the Van der Pol oscillator, Burgers' equation, 2D Navier-Stokes, and Rotating Gaussians, show that RRAEDy achieves accurate and robust predictions. Our code is open-source and available at https://github.com/JadM133/RRAEDy. We also provide a video summarizing the main results at https://youtu.be/ox70mSSMGrM.

