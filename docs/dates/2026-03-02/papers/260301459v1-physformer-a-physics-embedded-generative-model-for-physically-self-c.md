---
layout: default
title: PhysFormer: A Physics-Embedded Generative Model for Physically Self-Consistent Spectral Synthesis
---

# PhysFormer: A Physics-Embedded Generative Model for Physically Self-Consistent Spectral Synthesis
**arXiv**：[2603.01459v1](https://arxiv.org/abs/2603.01459) · [PDF](https://arxiv.org/pdf/2603.01459.pdf)  
**作者**：Siqi Wang, Mengmeng Zhang, Yude Bu, Chaozhou Mou  

**一句话要点**：提出PhysFormer以解决高维复杂系统物理一致性和数值稳定性问题

**关键词**：物理嵌入生成模型, 高维复杂系统建模, 光谱合成, 物理一致性, 反演稳定性

## 3 点简述
- 核心问题：高维复杂系统建模中物理一致性和数值稳定性挑战，现有方法如PINNs依赖已知物理场或系数，训练不稳定。
- 方法要点：PhysFormer通过低维物理可解释潜在空间学习关键物理量，将辐射通量生成物理过程嵌入网络，实现数据和物理层面的自一致性。
- 实验或效果：在高维退化反演任务中，PhysFormer约束生成在物理极限内，提升光谱保真度和反演稳定性，适应不同信噪比。

## 摘要（原文）

> In scientific and engineering domains, modeling high-dimensional complex systems governed by partial differential equations (PDEs) remains challenging in terms of physical consistency and numerical stability. However, existing approaches, such as physics-informed neural networks (PINNs), typically rely on known physical fields or coefficients and enforce physical constraints via external loss functions, which can lead to training instability and make it difficult to handle high-dimensional or unobservable scenarios. To this end, we propose PhysFormer, a generative modeling framework that is self-consistent at both the data and physical levels. PhysFormer leverages a low-dimensional, physically interpretable latent space to learn key physical quantities directly from data without requiring known high-dimensional physical field parameters, and embeds the physical process of radiative flux generation within the network to ensure the physical consistency of the generated spectra. In high-dimensional, degenerate inversion tasks, PhysFormer constrains generation within physical limits and enhances spectral fidelity and inversion stability under varying signal-to-noise ratios (SNRs). More broadly, this approach shifts the physical processes from external loss functions into the generative mechanism itself, providing a physically consistent generative modeling paradigm for complex systems involving unknown or unobservable physical quantities.

