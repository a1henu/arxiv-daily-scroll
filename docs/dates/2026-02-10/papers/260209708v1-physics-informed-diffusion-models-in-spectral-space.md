---
layout: default
title: Physics-informed diffusion models in spectral space
---

# Physics-informed diffusion models in spectral space
**arXiv**：[2602.09708v1](https://arxiv.org/abs/2602.09708) · [PDF](https://arxiv.org/pdf/2602.09708.pdf)  
**作者**：Davide Gallon, Philippe von Wurstemberger, Patrick Cheridito, Arnulf Jentzen  

**一句话要点**：提出基于谱空间物理信息扩散模型的方法，以解决参数偏微分方程的条件生成问题。

**关键词**：物理信息机器学习, 潜在扩散模型, 谱空间表示, 参数偏微分方程, 条件生成, 扩散后验采样

## 3 点简述
- 核心问题：结合生成模型与物理约束，处理参数偏微分方程在部分观测下的正反问题。
- 方法要点：在谱空间潜在表示中学习扩散过程，利用Adam更新在推理时强制物理信息约束。
- 实验或效果：在Poisson、Helmholtz和Navier-Stokes方程上验证，相比现有方法提升精度与效率。

## 摘要（原文）

> We propose a methodology that combines generative latent diffusion models with physics-informed machine learning to generate solutions of parametric partial differential equations (PDEs) conditioned on partial observations, which includes, in particular, forward and inverse PDE problems. We learn the joint distribution of PDE parameters and solutions via a diffusion process in a latent space of scaled spectral representations, where Gaussian noise corresponds to functions with controlled regularity. This spectral formulation enables significant dimensionality reduction compared to grid-based diffusion models and ensures that the induced process in function space remains within a class of functions for which the PDE operators are well defined. Building on diffusion posterior sampling, we enforce physics-informed constraints and measurement conditions during inference, applying Adam-based updates at each diffusion step. We evaluate the proposed approach on Poisson, Helmholtz, and incompressible Navier--Stokes equations, demonstrating improved accuracy and computational efficiency compared with existing diffusion-based PDE solvers, which are state of the art for sparse observations. Code is available at https://github.com/deeplearningmethods/PISD.

