---
layout: default
title: Neural Diffusion Intensity Models for Point Process Data
---

# Neural Diffusion Intensity Models for Point Process Data
**arXiv**：[2602.24083v1](https://arxiv.org/abs/2602.24083) · [PDF](https://arxiv.org/pdf/2602.24083.pdf)  
**作者**：Xinlong Du, Harsha Honnappa, Vinayak Rao  

**一句话要点**：提出神经扩散强度模型，基于神经SDE的变分框架解决Cox过程强度估计与后验推理的难解问题。

**关键词**：点过程, Cox过程, 神经随机微分方程, 变分推理, 强度估计, 后验路径

## 3 点简述
- 核心问题：Cox过程强度模型的非参数估计和后验推理通常难解，依赖昂贵MCMC方法。
- 方法要点：基于滤波扩张理论，条件化点过程观测保持潜在强度的扩散结构，设计变分框架和摊销编码器。
- 实验或效果：在合成和真实数据上准确恢复强度动态和后验路径，相比MCMC方法实现数量级加速。

## 摘要（原文）

> Cox processes model overdispersed point process data via a latent stochastic intensity, but both nonparametric estimation of the intensity model and posterior inference over intensity paths are typically intractable, relying on expensive MCMC methods. We introduce Neural Diffusion Intensity Models, a variational framework for Cox processes driven by neural SDEs. Our key theoretical result, based on enlargement of filtrations, shows that conditioning on point process observations preserves the diffusion structure of the latent intensity with an explicit drift correction. This guarantees the variational family contains the true posterior, so that ELBO maximization coincides with maximum likelihood estimation under sufficient model capacity. We design an amortized encoder architecture that maps variable-length event sequences to posterior intensity paths by simulating the drift-corrected SDE, replacing repeated MCMC runs with a single forward pass. Experiments on synthetic and real-world data demonstrate accurate recovery of latent intensity dynamics and posterior paths, with orders-of-magnitude speedups over MCMC-based methods.

