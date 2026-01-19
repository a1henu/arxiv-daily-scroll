---
layout: default
title: Latent Space Inference via Paired Autoencoders
---

# Latent Space Inference via Paired Autoencoders
**arXiv**：[2601.11397v1](https://arxiv.org/abs/2601.11397) · [PDF](https://arxiv.org/pdf/2601.11397.pdf)  
**作者**：Emma Hart, Bas Peters, Julianne Chung, Matthias Chung  

**一句话要点**：提出基于配对自编码器的潜在空间推断框架，以处理反问题中的观测不一致性。

**关键词**：潜在空间推断, 配对自编码器, 反问题求解, 数据不一致处理, 正则化优化, 科学计算应用

## 3 点简述
- 核心问题：解决反问题中观测数据不一致（如部分、噪声或分布外数据）导致的参数估计困难。
- 方法要点：使用参数空间和观测空间的两个自编码器，通过潜在空间映射实现正则化反演和优化。
- 实验或效果：在医学层析成像和地球物理地震波形反演中验证，相比单独配对自编码器和端到端编码器-解码器，能更准确重建参数。

## 摘要（原文）

> This work describes a novel data-driven latent space inference framework built on paired autoencoders to handle observational inconsistencies when solving inverse problems. Our approach uses two autoencoders, one for the parameter space and one for the observation space, connected by learned mappings between the autoencoders' latent spaces. These mappings enable a surrogate for regularized inversion and optimization in low-dimensional, informative latent spaces. Our flexible framework can work with partial, noisy, or out-of-distribution data, all while maintaining consistency with the underlying physical models. The paired autoencoders enable reconstruction of corrupted data, and then use the reconstructed data for parameter estimation, which produces more accurate reconstructions compared to paired autoencoders alone and end-to-end encoder-decoders of the same architecture, especially in scenarios with data inconsistencies. We demonstrate our approaches on two imaging examples in medical tomography and geophysical seismic-waveform inversion, but the described approaches are broadly applicable to a variety of inverse problems in scientific and engineering applications.

