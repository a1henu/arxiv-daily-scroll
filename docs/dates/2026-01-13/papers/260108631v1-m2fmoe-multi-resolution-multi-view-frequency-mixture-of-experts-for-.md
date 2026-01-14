---
layout: default
title: M$^2$FMoE: Multi-Resolution Multi-View Frequency Mixture-of-Experts for Extreme-Adaptive Time Series Forecasting
---

# M$^2$FMoE: Multi-Resolution Multi-View Frequency Mixture-of-Experts for Extreme-Adaptive Time Series Forecasting
**arXiv**：[2601.08631v1](https://arxiv.org/abs/2601.08631) · [PDF](https://arxiv.org/pdf/2601.08631.pdf)  
**作者**：Yaohui Huang, Runmin Zou, Yun Wang, Laeeq Aslam, Ruipeng Dong  

**一句话要点**：提出M²FMoE模型，通过多分辨率多视图频率建模解决极端事件时间序列预测问题。

**关键词**：时间序列预测, 极端事件建模, 频率分析, 专家混合, 多分辨率融合, 自适应学习

## 3 点简述
- 核心问题：现有方法在极端事件预测中性能下降，难以捕捉其复杂时间动态。
- 方法要点：结合多视图频率专家混合、多分辨率自适应融合和时序门控集成模块。
- 实验或效果：在真实水文数据集上优于现有基线，无需极端事件标签。

## 摘要（原文）

> Forecasting time series with extreme events is critical yet challenging due to their high variance, irregular dynamics, and sparse but high-impact nature. While existing methods excel in modeling dominant regular patterns, their performance degrades significantly during extreme events, constituting the primary source of forecasting errors in real-world applications. Although some approaches incorporate auxiliary signals to improve performance, they still fail to capture extreme events' complex temporal dynamics. To address these limitations, we propose M$^2$FMoE, an extreme-adaptive forecasting model that learns both regular and extreme patterns through multi-resolution and multi-view frequency modeling. It comprises three modules: (1) a multi-view frequency mixture-of-experts module assigns experts to distinct spectral bands in Fourier and Wavelet domains, with cross-view shared band splitter aligning frequency partitions and enabling inter-expert collaboration to capture both dominant and rare fluctuations; (2) a multi-resolution adaptive fusion module that hierarchically aggregates frequency features from coarse to fine resolutions, enhancing sensitivity to both short-term variations and sudden changes; (3) a temporal gating integration module that dynamically balances long-term trends and short-term frequency-aware features, improving adaptability to both regular and extreme temporal patterns. Experiments on real-world hydrological datasets with extreme patterns demonstrate that M$^2$FMoE outperforms state-of-the-art baselines without requiring extreme-event labels.

