---
layout: default
title: Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration
---

# Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration
**arXiv**：[2603.01623v1](https://arxiv.org/abs/2603.01623) · [PDF](https://arxiv.org/pdf/2603.01623.pdf)  
**作者**：Jiaqi Han, Juntong Shi, Puheng Li, Haotian Ye, Qiushan Guo, Stefano Ermon  

**一句话要点**：提出自适应谱特征预测方法以加速扩散模型采样

**关键词**：扩散模型加速, 特征预测, 切比雪夫逼近, 训练免费方法, 采样优化

## 3 点简述
- 扩散模型采样速度受限于迭代计算，现有特征缓存方法在长步跳过时误差累积导致质量下降
- 基于切比雪夫多项式全局逼近去噪器特征，通过岭回归拟合系数预测未来多步特征，控制误差不随步长增长
- 在图像和视频扩散模型上实验验证，实现高达4.79倍加速，同时保持更高样本质量

## 摘要（原文）

> Diffusion models have become the dominant tool for high-fidelity image and video generation, yet are critically bottlenecked by their inference speed due to the numerous iterative passes of Diffusion Transformers. To reduce the exhaustive compute, recent works resort to the feature caching and reusing scheme that skips network evaluations at selected diffusion steps by using cached features in previous steps. However, their preliminary design solely relies on local approximation, causing errors to grow rapidly with large skips and leading to degraded sample quality at high speedups. In this work, we propose spectral diffusion feature forecaster (Spectrum), a training-free approach that enables global, long-range feature reuse with tightly controlled error. In particular, we view the latent features of the denoiser as functions over time and approximate them with Chebyshev polynomials. Specifically, we fit the coefficient for each basis via ridge regression, which is then leveraged to forecast features at multiple future diffusion steps. We theoretically reveal that our approach admits more favorable long-horizon behavior and yields an error bound that does not compound with the step size. Extensive experiments on various state-of-the-art image and video diffusion models consistently verify the superiority of our approach. Notably, we achieve up to 4.79$\times$ speedup on FLUX.1 and 4.67$\times$ speedup on Wan2.1-14B, while maintaining much higher sample quality compared with the baselines.

