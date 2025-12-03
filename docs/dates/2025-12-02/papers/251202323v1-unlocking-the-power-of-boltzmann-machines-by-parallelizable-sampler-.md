---
layout: default
title: Unlocking the Power of Boltzmann Machines by Parallelizable Sampler and Efficient Temperature Estimation
---

# Unlocking the Power of Boltzmann Machines by Parallelizable Sampler and Efficient Temperature Estimation
**arXiv**：[2512.02323v1](https://arxiv.org/abs/2512.02323) · [PDF](https://arxiv.org/pdf/2512.02323.pdf)  
**作者**：Kentaro Kubo, Hayato Goto  

**一句话要点**：提出朗之万模拟分岔采样器和条件期望匹配方法，以解决玻尔兹曼机训练中采样并行化和温度控制问题。

**关键词**：玻尔兹曼机, 并行采样, 温度估计, 能量基生成模型, 采样器自适应学习

## 3 点简述
- 玻尔兹曼机训练成本高，采样难以并行化，限制了其应用超越受限玻尔兹曼机。
- 基于模拟分岔提出朗之万模拟分岔采样器，实现并行采样，适用于一般耦合玻尔兹曼机。
- 结合条件期望匹配估计逆温度，建立采样器自适应学习框架，提升生成建模性能。

## 摘要（原文）

> Boltzmann machines (BMs) are powerful energy-based generative models, but their heavy training cost has largely confined practical use to Restricted BMs (RBMs) trained with an efficient learning method called contrastive divergence. More accurate learning typically requires Markov chain Monte Carlo (MCMC) Boltzmann sampling, but it is time-consuming due to the difficulty of parallelization for more expressive models. To address this limitation, we first propose a new Boltzmann sampler inspired by a quantum-inspired combinatorial optimization called simulated bifurcation (SB). This SB-inspired approach, which we name Langevin SB (LSB), enables parallelized sampling while maintaining accuracy comparable to MCMC. Furthermore, this is applicable not only to RBMs but also to BMs with general couplings. However, LSB cannot control the inverse temperature of the output Boltzmann distribution, which hinders learning and degrades performance. To overcome this limitation, we also developed an efficient method for estimating the inverse temperature during the learning process, which we call conditional expectation matching (CEM). By combining LSB and CEM, we establish an efficient learning framework for BMs with greater expressive power than RBMs. We refer to this framework as sampler-adaptive learning (SAL). SAL opens new avenues for energy-based generative modeling beyond RBMs.

