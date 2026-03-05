---
layout: default
title: TFWaveFormer: Temporal-Frequency Collaborative Multi-level Wavelet Transformer for Dynamic Link Prediction
---

# TFWaveFormer: Temporal-Frequency Collaborative Multi-level Wavelet Transformer for Dynamic Link Prediction
**arXiv**：[2603.03963v1](https://arxiv.org/abs/2603.03963) · [PDF](https://arxiv.org/pdf/2603.03963.pdf)  
**作者**：Hantong Feng, Yonggang Wu, Duxin Chen, Wenwu Yu  

**一句话要点**：提出TFWaveFormer，结合时频分析与小波分解以增强动态链接预测性能

**关键词**：动态链接预测, 时频分析, 小波分解, Transformer架构, 多尺度时间建模

## 3 点简述
- 核心问题：现有Transformer方法在捕捉动态图中复杂多尺度时间动态时性能受限
- 方法要点：通过时频协调机制、可学习多分辨率小波分解模块和混合Transformer模块融合局部与全局特征
- 实验或效果：在基准数据集上实现最先进性能，显著超越现有Transformer和混合模型

## 摘要（原文）

> Dynamic link prediction plays a crucial role in diverse applications including social network analysis, communication forecasting, and financial modeling. While recent Transformer-based approaches have demonstrated promising results in temporal graph learning, their performance remains limited when capturing complex multi-scale temporal dynamics. In this paper, we propose TFWaveFormer, a novel Transformer architecture that integrates temporal-frequency analysis with multi-resolution wavelet decomposition to enhance dynamic link prediction. Our framework comprises three key components: (i) a temporal-frequency coordination mechanism that jointly models temporal and spectral representations, (ii) a learnable multi-resolution wavelet decomposition module that adaptively extracts multi-scale temporal patterns through parallel convolutions, replacing traditional iterative wavelet transforms, and (iii) a hybrid Transformer module that effectively fuses local wavelet features with global temporal dependencies. Extensive experiments on benchmark datasets demonstrate that TFWaveFormer achieves state-of-the-art performance, outperforming existing Transformer-based and hybrid models by significant margins across multiple metrics. The superior performance of TFWaveFormer validates the effectiveness of combining temporal-frequency analysis with wavelet decomposition in capturing complex temporal dynamics for dynamic link prediction tasks.

