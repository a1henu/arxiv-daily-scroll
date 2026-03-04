---
layout: default
title: Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning
---

# Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning
**arXiv**：[2603.03229v1](https://arxiv.org/abs/2603.03229) · [PDF](https://arxiv.org/pdf/2603.03229.pdf)  
**作者**：Adam Watts, Andrew Jeon, Destry Newton, Ryan Bowering  

**一句话要点**：提出条件变分自编码器以解决从冲击响应谱曲线反演时间序列的逆问题

**关键词**：冲击响应谱, 逆问题, 条件变分自编码器, 时间序列生成, 深度学习, 信号处理

## 3 点简述
- 核心问题：从冲击响应谱反演加速度时间序列是非线性、多对一的病态逆问题
- 方法要点：使用条件变分自编码器学习数据驱动的逆映射，无需迭代优化
- 实验或效果：相比传统方法，提高了谱保真度、泛化性强，推理速度快3-6个数量级

## 摘要（原文）

> The shock response spectrum (SRS) is widely used to characterize the response of single-degree-of-freedom (SDOF) systems to transient accelerations. Because the mapping from acceleration time history to SRS is nonlinear and many-to-one, reconstructing time-domain signals from a target spectrum is inherently ill-posed. Conventional approaches address this problem through iterative optimization, typically representing signals as sums of exponentially decayed sinusoids, but these methods are computationally expensive and constrained by predefined basis functions.
>   We propose a conditional variational autoencoder (CVAE) that learns a data-driven inverse mapping from SRS to acceleration time series. Once trained, the model generates signals consistent with prescribed target spectra without requiring iterative optimization. Experiments demonstrate improved spectral fidelity relative to classical techniques, strong generalization to unseen spectra, and inference speeds three to six orders of magnitude faster. These results establish deep generative modeling as a scalable and efficient approach for inverse SRS reconstruction.

