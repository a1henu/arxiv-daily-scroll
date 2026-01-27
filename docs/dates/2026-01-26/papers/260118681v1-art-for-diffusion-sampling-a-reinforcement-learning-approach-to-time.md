---
layout: default
title: ART for Diffusion Sampling: A Reinforcement Learning Approach to Timestep Schedule
---

# ART for Diffusion Sampling: A Reinforcement Learning Approach to Timestep Schedule
**arXiv**：[2601.18681v1](https://arxiv.org/abs/2601.18681) · [PDF](https://arxiv.org/pdf/2601.18681.pdf)  
**作者**：Yilie Huang, Wenpin Tang, Xunyu Zhou  

**一句话要点**：提出ART-RL方法，通过强化学习优化扩散模型采样时间步调度以提升样本质量。

**关键词**：扩散模型, 时间步调度, 强化学习, 自适应采样, 样本生成, 连续时间控制

## 3 点简述
- 核心问题：均匀或手动设计的时间步调度在有限步数下可能非最优，影响扩散模型采样精度。
- 方法要点：引入自适应重参数化时间（ART），将时间变化建模为连续时间强化学习问题，使用高斯策略学习最优调度。
- 实验或效果：基于EDM框架，ART-RL在CIFAR-10上提升Fréchet Inception Distance，并迁移至AFHQv2、FFHQ和ImageNet无需重训练。

## 摘要（原文）

> We consider time discretization for score-based diffusion models to generate samples from a learned reverse-time dynamic on a finite grid. Uniform and hand-crafted grids can be suboptimal given a budget on the number of time steps. We introduce Adaptive Reparameterized Time (ART) that controls the clock speed of a reparameterized time variable, leading to a time change and uneven timesteps along the sampling trajectory while preserving the terminal time. The objective is to minimize the aggregate error arising from the discretized Euler scheme. We derive a randomized control companion, ART-RL, and formulate time change as a continuous-time reinforcement learning (RL) problem with Gaussian policies. We then prove that solving ART-RL recovers the optimal ART schedule, which in turn enables practical actor--critic updates to learn the latter in a data-driven way. Empirically, based on the official EDM pipeline, ART-RL improves Fréchet Inception Distance on CIFAR-10 over a wide range of budgets and transfers to AFHQv2, FFHQ, and ImageNet without the need of retraining.

