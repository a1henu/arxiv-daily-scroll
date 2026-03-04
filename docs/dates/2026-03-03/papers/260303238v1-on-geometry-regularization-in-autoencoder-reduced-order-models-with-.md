---
layout: default
title: On Geometry Regularization in Autoencoder Reduced-Order Models with Latent Neural ODE Dynamics
---

# On Geometry Regularization in Autoencoder Reduced-Order Models with Latent Neural ODE Dynamics
**arXiv**：[2603.03238v1](https://arxiv.org/abs/2603.03238) · [PDF](https://arxiv.org/pdf/2603.03238.pdf)  
**作者**：Mikhail Osipov  

**一句话要点**：研究几何正则化策略以改进自编码器降阶模型中的潜在表示学习

**关键词**：自编码器降阶模型, 几何正则化, 潜在神经ODE, Stiefel投影, 长时程推演

## 3 点简述
- 核心问题：自编码器降阶模型中潜在几何不匹配可能影响下游动力学训练性能
- 方法要点：在自编码器预训练中评估四种几何正则化方法，包括近等距正则化和Stiefel投影
- 实验或效果：Stiefel投影能改善潜在动力学条件，提升长时程推演性能，而其他正则化可能增加训练难度

## 摘要（原文）

> We investigate geometric regularization strategies for learned latent representations in encoder--decoder reduced-order models. In a fixed experimental setting for the advection--diffusion--reaction (ADR) equation, we model latent dynamics using a neural ODE and evaluate four regularization approaches applied during autoencoder pre-training: (a) near-isometry regularization of the decoder Jacobian, (b) a stochastic decoder gain penalty based on random directional gains, (c) a second-order directional curvature penalty, and (d) Stiefel projection of the first decoder layer. Across multiple seeds, we find that (a)--(c) often produce latent representations that make subsequent latent-dynamics training with a frozen autoencoder more difficult, especially for long-horizon rollouts, even when they improve local decoder smoothness or related sensitivity proxies. In contrast, (d) consistently improves conditioning-related diagnostics of the learned latent dynamics and tends to yield better rollout performance. We discuss the hypothesis that, in this setting, the downstream impact of latent-geometry mismatch outweighs the benefits of improved decoder smoothness.

