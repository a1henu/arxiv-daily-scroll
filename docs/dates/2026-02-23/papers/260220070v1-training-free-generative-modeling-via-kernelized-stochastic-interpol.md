---
layout: default
title: Training-Free Generative Modeling via Kernelized Stochastic Interpolants
---

# Training-Free Generative Modeling via Kernelized Stochastic Interpolants
**arXiv**：[2602.20070v1](https://arxiv.org/abs/2602.20070) · [PDF](https://arxiv.org/pdf/2602.20070.pdf)  
**作者**：Florentin Coeurdoux, Etienne Lempereur, Nathanaël Cuvelle-Magar, Thomas Eboli, Stéphane Mallat, Anastasia Borovykh, Eric Vanden-Eijnden  

**一句话要点**：提出基于核方法的训练自由生成建模，通过线性系统替代神经网络训练，适用于金融时间序列、湍流和图像生成。

**关键词**：训练自由生成建模, 核方法, 随机插值, 线性系统, 生成SDE, 特征映射

## 3 点简述
- 核心问题：传统生成模型依赖神经网络训练，计算成本高且复杂。
- 方法要点：在随机插值框架中，使用核方法将生成SDE的漂移项表示为线性系统，无需训练神经网络。
- 实验或效果：在金融时间序列、湍流和图像生成任务中展示训练自由生成能力，支持多种特征映射。

## 摘要（原文）

> We develop a kernel method for generative modeling within the stochastic interpolant framework, replacing neural network training with linear systems. The drift of the generative SDE is $\hat b_t(x) = \nablaφ(x)^\topη_t$, where $η_t\in\R^P$ solves a $P\times P$ system computable from data, with $P$ independent of the data dimension $d$. Since estimates are inexact, the diffusion coefficient $D_t$ affects sample quality; the optimal $D_t^*$ from Girsanov diverges at $t=0$, but this poses no difficulty and we develop an integrator that handles it seamlessly. The framework accommodates diverse feature maps -- scattering transforms, pretrained generative models etc. -- enabling training-free generation and model combination. We demonstrate the approach on financial time series, turbulence, and image generation.

