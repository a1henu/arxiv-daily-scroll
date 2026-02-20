---
layout: default
title: MGD: Moment Guided Diffusion for Maximum Entropy Generation
---

# MGD: Moment Guided Diffusion for Maximum Entropy Generation
**arXiv**：[2602.17211v1](https://arxiv.org/abs/2602.17211) · [PDF](https://arxiv.org/pdf/2602.17211.pdf)  
**作者**：Etienne Lempereur, Nathanaël Cuvelle--Magar, Florentin Coeurdoux, Stéphane Mallat, Eric Vanden-Eijnden  

**一句话要点**：提出MGD方法，结合最大熵与扩散模型，高效生成高维多尺度过程样本。

**关键词**：最大熵生成, 扩散模型, 矩引导, 高维采样, 多尺度过程, 负熵估计

## 3 点简述
- 核心问题：从有限信息生成样本，传统最大熵方法在高维下采样效率低。
- 方法要点：基于随机插值框架，通过SDE引导矩在有限时间内达到预设值。
- 实验或效果：应用于金融时间序列、湍流和宇宙学场，估计高维过程负熵。

## 摘要（原文）

> Generating samples from limited information is a fundamental problem across scientific domains. Classical maximum entropy methods provide principled uncertainty quantification from moment constraints but require sampling via MCMC or Langevin dynamics, which typically exhibit exponential slowdown in high dimensions. In contrast, generative models based on diffusion and flow matching efficiently transport noise to data but offer limited theoretical guarantees and can overfit when data is scarce. We introduce Moment Guided Diffusion (MGD), which combines elements of both approaches. Building on the stochastic interpolant framework, MGD samples maximum entropy distributions by solving a stochastic differential equation that guides moments toward prescribed values in finite time, thereby avoiding slow mixing in equilibrium-based methods. We formally obtain, in the large-volatility limit, convergence of MGD to the maximum entropy distribution and derive a tractable estimator of the resulting entropy computed directly from the dynamics. Applications to financial time series, turbulent flows, and cosmological fields using wavelet scattering moments yield estimates of negentropy for high-dimensional multiscale processes.

