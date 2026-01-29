---
layout: default
title: AWGformer: Adaptive Wavelet-Guided Transformer for Multi-Resolution Time Series Forecasting
---

# AWGformer: Adaptive Wavelet-Guided Transformer for Multi-Resolution Time Series Forecasting
**arXiv**：[2601.20409v1](https://arxiv.org/abs/2601.20409) · [PDF](https://arxiv.org/pdf/2601.20409.pdf)  
**作者**：Wei Li  

**一句话要点**：提出AWGformer，通过自适应小波引导的Transformer解决多分辨率时间序列预测问题。

**关键词**：时间序列预测, 自适应小波分解, 跨尺度注意力, 多分辨率预测, 非平稳时间序列

## 3 点简述
- 核心问题：时间序列预测需捕捉多时间尺度模式，同时保持计算效率。
- 方法要点：集成自适应小波分解与跨尺度注意力机制，包括动态小波基选择、频率感知注意力等模块。
- 实验或效果：在基准数据集上显著优于现有方法，尤其适用于多尺度和非平稳时间序列。

## 摘要（原文）

> Time series forecasting requires capturing patterns across multiple temporal scales while maintaining computational efficiency. This paper introduces AWGformer, a novel architecture that integrates adaptive wavelet decomposition with cross-scale attention mechanisms for enhanced multi-variate time series prediction. Our approach comprises: (1) an Adaptive Wavelet Decomposition Module (AWDM) that dynamically selects optimal wavelet bases and decomposition levels based on signal characteristics; (2) a Cross-Scale Feature Fusion (CSFF) mechanism that captures interactions between different frequency bands through learnable coupling matrices; (3) a Frequency-Aware Multi-Head Attention (FAMA) module that weights attention heads according to their frequency selectivity; (4) a Hierarchical Prediction Network (HPN) that generates forecasts at multiple resolutions before reconstruction. Extensive experiments on benchmark datasets demonstrate that AWGformer achieves significant average improvements over state-of-the-art methods, with particular effectiveness on multi-scale and non-stationary time series. Theoretical analysis provides convergence guarantees and establishes the connection between our wavelet-guided attention and classical signal processing principles.

