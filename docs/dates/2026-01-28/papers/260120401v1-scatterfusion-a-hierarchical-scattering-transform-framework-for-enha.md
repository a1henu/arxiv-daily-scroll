---
layout: default
title: ScatterFusion: A Hierarchical Scattering Transform Framework for Enhanced Time Series Forecasting
---

# ScatterFusion: A Hierarchical Scattering Transform Framework for Enhanced Time Series Forecasting
**arXiv**：[2601.20401v1](https://arxiv.org/abs/2601.20401) · [PDF](https://arxiv.org/pdf/2601.20401.pdf)  
**作者**：Wei Li  

**一句话要点**：提出ScatterFusion框架，结合散射变换与分层注意力机制以增强时间序列预测

**关键词**：时间序列预测, 散射变换, 分层注意力, 多尺度特征, 趋势季节分解

## 3 点简述
- 核心问题：时间序列预测面临多时间尺度复杂依赖的挑战
- 方法要点：通过分层散射变换提取多尺度特征，结合自适应增强与多分辨率注意力
- 实验或效果：在七个基准数据集上优于常见方法，显著降低预测误差

## 摘要（原文）

> Time series forecasting presents significant challenges due to the complex temporal dependencies at multiple time scales. This paper introduces ScatterFusion, a novel framework that synergistically integrates scattering transforms with hierarchical attention mechanisms for robust time series forecasting. Our approach comprises four key components: (1) a Hierarchical Scattering Transform Module (HSTM) that extracts multi-scale invariant features capturing both local and global patterns; (2) a Scale-Adaptive Feature Enhancement (SAFE) module that dynamically adjusts feature importance across different scales; (3) a Multi-Resolution Temporal Attention (MRTA) mechanism that learns dependencies at varying time horizons; and (4) a Trend-Seasonal-Residual (TSR) decomposition-guided structure-aware loss function. Extensive experiments on seven benchmark datasets demonstrate that ScatterFusion outperforms other common methods, achieving significant reductions in error metrics across various prediction horizons.

