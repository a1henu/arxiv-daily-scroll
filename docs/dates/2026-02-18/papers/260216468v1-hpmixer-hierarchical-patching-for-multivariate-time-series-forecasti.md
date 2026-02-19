---
layout: default
title: HPMixer: Hierarchical Patching for Multivariate Time Series Forecasting
---

# HPMixer: Hierarchical Patching for Multivariate Time Series Forecasting
**arXiv**：[2602.16468v1](https://arxiv.org/abs/2602.16468) · [PDF](https://arxiv.org/pdf/2602.16468.pdf)  
**作者**：Jung Min Choi, Vijaya Krishna Yalavarthi, Lars Schmidt-Thieme  

**一句话要点**：提出HPMixer，通过解耦建模周期性和残差，提升长期多元时间序列预测性能。

**关键词**：多元时间序列预测, 周期性建模, 残差学习, 分层补丁, 可学习小波变换, 通道混合

## 3 点简述
- 核心问题：长期多元时间序列预测需有效捕捉周期性模式和残差动态。
- 方法要点：使用可学习周期模块和可学习平稳小波变换，结合分层补丁机制建模多尺度残差。
- 实验或效果：在标准基准测试中，HPMixer达到竞争性或最先进的性能。

## 摘要（原文）

> In long-term multivariate time series forecasting, effectively capturing both periodic patterns and residual dynamics is essential. To address this within standard deep learning benchmark settings, we propose the Hierarchical Patching Mixer (HPMixer), which models periodicity and residuals in a decoupled yet complementary manner. The periodic component utilizes a learnable cycle module [7] enhanced with a nonlinear channel-wise MLP for greater expressiveness. The residual component is processed through a Learnable Stationary Wavelet Transform (LSWT) to extract stable, shift-invariant frequency-domain representations. Subsequently, a channel-mixing encoder models explicit inter-channel dependencies, while a two-level non-overlapping hierarchical patching mechanism captures coarse- and fine-scale residual variations. By integrating decoupled periodicity modeling with structured, multi-scale residual learning, HPMixer provides an effective framework. Extensive experiments on standard multivariate benchmarks demonstrate that HPMixer achieves competitive or state-of-the-art performance compared to recent baselines.

