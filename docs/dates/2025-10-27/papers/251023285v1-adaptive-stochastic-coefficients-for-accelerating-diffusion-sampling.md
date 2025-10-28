---
layout: default
title: Adaptive Stochastic Coefficients for Accelerating Diffusion Sampling
---

# Adaptive Stochastic Coefficients for Accelerating Diffusion Sampling
**arXiv**：[2510.23285v1](https://arxiv.org/abs/2510.23285) · [PDF](https://arxiv.org/pdf/2510.23285.pdf)  
**作者**：Ruoyu Wang, Beier Zhu, Junzhi Li, Liangyu Yuan, Chi Zhang  

**一句话要点**：提出AdaSDE以加速扩散采样，平衡ODE与SDE的误差问题

**关键词**：扩散模型, 采样加速, 误差修正, 轻量蒸馏, SDE求解器

## 3 点简述
- 核心问题：ODE和SDE求解器在扩散采样中存在梯度误差和离散化误差的互补弱点
- 方法要点：引入可学习系数动态调节误差修正强度，通过轻量蒸馏估计
- 实验或效果：在5 NFE下，CIFAR-10 FID为4.18，FFHQ为8.05，LSUN Bedroom为6.96

## 摘要（原文）

> Diffusion-based generative processes, formulated as differential equation
> solving, frequently balance computational speed with sample quality. Our
> theoretical investigation of ODE- and SDE-based solvers reveals complementary
> weaknesses: ODE solvers accumulate irreducible gradient error along
> deterministic trajectories, while SDE methods suffer from amplified
> discretization errors when the step budget is limited. Building upon this
> insight, we introduce AdaSDE, a novel single-step SDE solver that aims to unify
> the efficiency of ODEs with the error resilience of SDEs. Specifically, we
> introduce a single per-step learnable coefficient, estimated via lightweight
> distillation, which dynamically regulates the error correction strength to
> accelerate diffusion sampling. Notably, our framework can be integrated with
> existing solvers to enhance their capabilities. Extensive experiments
> demonstrate state-of-the-art performance: at 5 NFE, AdaSDE achieves FID scores
> of 4.18 on CIFAR-10, 8.05 on FFHQ and 6.96 on LSUN Bedroom. Codes are available
> in https://github.com/WLU-wry02/AdaSDE.

