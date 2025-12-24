---
layout: default
title: HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training
---

# HGAN-SDEs: Learning Neural Stochastic Differential Equations with Hermite-Guided Adversarial Training
**arXiv**：[2512.20272v1](https://arxiv.org/abs/2512.20272) · [PDF](https://arxiv.org/pdf/2512.20272.pdf)  
**作者**：Yuanjian Xu, Yuan Shuai, Jianing Hao, Guang Zhang  

**一句话要点**：提出HGAN-SDEs，利用Hermite函数构建高效判别器以解决神经随机微分方程生成对抗训练中的计算与稳定性问题。

**关键词**：神经随机微分方程, 生成对抗网络, Hermite函数, 对抗训练, 路径分布建模, 计算效率

## 3 点简述
- 核心问题：现有基于神经控制微分方程的判别器计算成本高且加剧对抗训练不稳定性。
- 方法要点：引入Hermite函数作为轻量级基础，构建结构化判别器以近似路径级动态。
- 实验或效果：在合成和真实系统上验证了优越的样本质量和学习效率。

## 摘要（原文）

> Neural Stochastic Differential Equations (Neural SDEs) provide a principled framework for modeling continuous-time stochastic processes and have been widely adopted in fields ranging from physics to finance. Recent advances suggest that Generative Adversarial Networks (GANs) offer a promising solution to learning the complex path distributions induced by SDEs. However, a critical bottleneck lies in designing a discriminator that faithfully captures temporal dependencies while remaining computationally efficient. Prior works have explored Neural Controlled Differential Equations (CDEs) as discriminators due to their ability to model continuous-time dynamics, but such architectures suffer from high computational costs and exacerbate the instability of adversarial training. To address these limitations, we introduce HGAN-SDEs, a novel GAN-based framework that leverages Neural Hermite functions to construct a structured and efficient discriminator. Hermite functions provide an expressive yet lightweight basis for approximating path-level dynamics, enabling both reduced runtime complexity and improved training stability. We establish the universal approximation property of our framework for a broad class of SDE-driven distributions and theoretically characterize its convergence behavior. Extensive empirical evaluations on synthetic and real-world systems demonstrate that HGAN-SDEs achieve superior sample quality and learning efficiency compared to existing generative models for SDEs

