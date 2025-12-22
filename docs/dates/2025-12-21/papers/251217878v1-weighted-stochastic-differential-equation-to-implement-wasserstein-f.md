---
layout: default
title: Weighted Stochastic Differential Equation to Implement Wasserstein-Fisher-Rao Gradient Flow
---

# Weighted Stochastic Differential Equation to Implement Wasserstein-Fisher-Rao Gradient Flow
**arXiv**：[2512.17878v1](https://arxiv.org/abs/2512.17878) · [PDF](https://arxiv.org/pdf/2512.17878.pdf)  
**作者**：Herlock Rahimi  

**一句话要点**：提出加权随机微分方程以实现Wasserstein-Fisher-Rao梯度流，用于改进非对数凹目标分布的采样

**关键词**：Wasserstein-Fisher-Rao梯度流, 加权随机微分方程, 生成建模, 采样算法, 信息几何

## 3 点简述
- 核心问题：基于分数的扩散模型在非凸或多模态分布中采样效率低，混合率指数下降
- 方法要点：通过信息几何工具引入显式校正项，利用Feynman-Kac表示实现加权随机微分方程
- 实验或效果：未知

## 摘要（原文）

> Score-based diffusion models currently constitute the state of the art in continuous generative modeling. These methods are typically formulated via overdamped or underdamped Ornstein--Uhlenbeck-type stochastic differential equations, in which sampling is driven by a combination of deterministic drift and Brownian diffusion, resulting in continuous particle trajectories in the ambient space. While such dynamics enjoy exponential convergence guarantees for strongly log-concave target distributions, it is well known that their mixing rates deteriorate exponentially in the presence of nonconvex or multimodal landscapes, such as double-well potentials. Since many practical generative modeling tasks involve highly non-log-concave target distributions, considerable recent effort has been devoted to developing sampling schemes that improve exploration beyond classical diffusion dynamics.
>   A promising line of work leverages tools from information geometry to augment diffusion-based samplers with controlled mass reweighting mechanisms. This perspective leads naturally to Wasserstein--Fisher--Rao (WFR) geometries, which couple transport in the sample space with vertical (reaction) dynamics on the space of probability measures. In this work, we formulate such reweighting mechanisms through the introduction of explicit correction terms and show how they can be implemented via weighted stochastic differential equations using the Feynman--Kac representation. Our study provides a preliminary but rigorous investigation of WFR-based sampling dynamics, and aims to clarify their geometric and operator-theoretic structure as a foundation for future theoretical and algorithmic developments.

