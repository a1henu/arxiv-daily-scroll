---
layout: default
title: WADEPre: A Wavelet-based Decomposition Model for Extreme Precipitation Nowcasting with Multi-Scale Learning
---

# WADEPre: A Wavelet-based Decomposition Model for Extreme Precipitation Nowcasting with Multi-Scale Learning
**arXiv**：[2602.02096v1](https://arxiv.org/abs/2602.02096) · [PDF](https://arxiv.org/pdf/2602.02096.pdf)  
**作者**：Baitian Liu, Haiping Zhang, Huiling Yuan, Dongjing Wang, Ying Li, Feng Chen, Hao Wu  

**一句话要点**：提出WADEPre模型，基于小波分解解决极端降水临近预报中的重尾分布和空间定位问题。

**关键词**：极端降水临近预报, 小波分解, 多尺度学习, 双分支架构, 课程学习, 降水预测

## 3 点简述
- 核心问题：降水强度重尾分布导致标准模型回归到均值，模糊极端值，傅里叶方法缺乏空间定位能力。
- 方法要点：使用离散小波变换分解，双分支架构分别建模低频平流和高频对流，结合多尺度课程学习优化。
- 实验或效果：在SEVIR和上海雷达数据集上实现最先进性能，显著提升极端阈值捕获和结构保真度。

## 摘要（原文）

> The heavy-tailed nature of precipitation intensity impedes precise precipitation nowcasting. Standard models that optimize pixel-wise losses are prone to regression-to-the-mean bias, which blurs extreme values. Existing Fourier-based methods also lack the spatial localization needed to resolve transient convective cells. To overcome these intrinsic limitations, we propose WADEPre, a wavelet-based decomposition model for extreme precipitation that transitions the modeling into the wavelet domain. By leveraging the Discrete Wavelet Transform for explicit decomposition, WADEPre employs a dual-branch architecture: an Approximation Network to model stable, low-frequency advection, isolating deterministic trends from statistical bias, and a spatially localized Detail Network to capture high-frequency stochastic convection, resolving transient singularities and preserving sharp boundaries. A subsequent Refiner module then dynamically reconstructs these decoupled multi-scale components into the final high-fidelity forecast. To address optimization instability, we introduce a multi-scale curriculum learning strategy that progressively shifts supervision from coarse scales to fine-grained details. Extensive experiments on the SEVIR and Shanghai Radar datasets demonstrate that WADEPre achieves state-of-the-art performance, yielding significant improvements in capturing extreme thresholds and maintaining structural fidelity. Our code is available at https://github.com/sonderlau/WADEPre.

