---
layout: default
title: Formalizing the Sampling Design Space of Diffusion-Based Generative Models via Adaptive Solvers and Wasserstein-Bounded Timesteps
---

# Formalizing the Sampling Design Space of Diffusion-Based Generative Models via Adaptive Solvers and Wasserstein-Bounded Timesteps
**arXiv**：[2602.12624v1](https://arxiv.org/abs/2602.12624) · [PDF](https://arxiv.org/pdf/2602.12624.pdf)  
**作者**：Sangwoo Jo, Sungjoon Choi  

**一句话要点**：提出SDM框架，通过自适应求解器与Wasserstein有界时间步优化扩散模型采样设计。

**关键词**：扩散模型, 采样优化, 自适应求解器, Wasserstein距离, 数值求解, 生成模型

## 3 点简述
- 扩散模型采样成本高，现有方法依赖静态启发式，缺乏系统性设计。
- 基于几何分析，SDM根据扩散轨迹内在特性自适应选择求解器，并优化时间步以控制误差。
- 无需额外训练，SDM在CIFAR-10等基准上实现SOTA性能，减少函数评估次数。

## 摘要（原文）

> Diffusion-based generative models have achieved remarkable performance across various domains, yet their practical deployment is often limited by high sampling costs. While prior work focuses on training objectives or individual solvers, the holistic design of sampling, specifically solver selection and scheduling, remains dominated by static heuristics. In this work, we revisit this challenge through a geometric lens, proposing SDM, a principled framework that aligns the numerical solver with the intrinsic properties of the diffusion trajectory. By analyzing the ODE dynamics, we show that efficient low-order solvers suffice in early high-noise stages while higher-order solvers can be progressively deployed to handle the increasing non-linearity of later stages. Furthermore, we formalize the scheduling by introducing a Wasserstein-bounded optimization framework. This method systematically derives adaptive timesteps that explicitly bound the local discretization error, ensuring the sampling process remains faithful to the underlying continuous dynamics. Without requiring additional training or architectural modifications, SDM achieves state-of-the-art performance across standard benchmarks, including an FID of 1.93 on CIFAR-10, 2.41 on FFHQ, and 1.98 on AFHQv2, with a reduced number of function evaluations compared to existing samplers. Our code is available at https://github.com/aiimaginglab/sdm.

