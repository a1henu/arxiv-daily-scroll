---
layout: default
title: FreqCycle: A Multi-Scale Time-Frequency Analysis Method for Time Series Forecasting
---

# FreqCycle: A Multi-Scale Time-Frequency Analysis Method for Time Series Forecasting
**arXiv**：[2603.09661v1](https://arxiv.org/abs/2603.09661) · [PDF](https://arxiv.org/pdf/2603.09661.pdf)  
**作者**：Boya Zhang, Shuaijie Yin, Huiwen Zhu, Xing He  

**一句话要点**：提出FreqCycle框架，通过多尺度时频分析解决时间序列预测中中高频特征建模不足的问题。

**关键词**：时间序列预测, 时频分析, 多周期建模, 深度学习, 高效推理

## 3 点简述
- 核心问题：现有方法主要关注低频模式，忽略中高频特征，限制了深度学习模型的性能提升。
- 方法要点：结合FECF模块提取低频周期性特征，SFPL模块增强中高频能量比例，并扩展为MFreqCycle处理耦合多周期性和长回溯窗口。
- 实验或效果：在七个基准测试中实现最优精度，同时保持快速推理速度，平衡性能与效率。

## 摘要（原文）

> Mining time-frequency features is critical for time series forecasting. Existing research has predominantly focused on modeling low-frequency patterns, where most time series energy is concentrated. The overlooking of mid to high frequency continues to limit further performance gains in deep learning models. We propose FreqCycle, a novel framework integrating: (i) a Filter-Enhanced Cycle Forecasting (FECF) module to extract low-frequency features by explicitly learning shared periodic patterns in the time domain, and (ii) a Segmented Frequency-domain Pattern Learning (SFPL) module to enhance mid to high frequency energy proportion via learnable filters and adaptive weighting. Furthermore, time series data often exhibit coupled multi-periodicity, such as intertwined weekly and daily cycles. To address coupled multi-periodicity as well as long lookback window challenges, we extend FreqCycle hierarchically into MFreqCycle, which decouples nested periodic features through cross-scale interactions. Extensive experiments on seven diverse domain benchmarks demonstrate that FreqCycle achieves state-of-the-art accuracy while maintaining faster inference speeds, striking an optimal balance between performance and efficiency.

