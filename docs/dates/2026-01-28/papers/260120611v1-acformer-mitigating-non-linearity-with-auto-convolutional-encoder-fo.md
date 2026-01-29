---
layout: default
title: ACFormer: Mitigating Non-linearity with Auto Convolutional Encoder for Time Series Forecasting
---

# ACFormer: Mitigating Non-linearity with Auto Convolutional Encoder for Time Series Forecasting
**arXiv**：[2601.20611v1](https://arxiv.org/abs/2601.20611) · [PDF](https://arxiv.org/pdf/2601.20611.pdf)  
**作者**：Gawon Lee, Hanbyeol Park, Minseop Kim, Dohee Kim, Hyerim Bae  

**一句话要点**：提出ACFormer以结合卷积的非线性特征提取与线性投影效率，用于时间序列预测。

**关键词**：时间序列预测, 卷积神经网络, 非线性建模, 感受野分析, 注意力机制

## 3 点简述
- 时间序列预测面临建模复杂时序依赖和通道相关性的挑战，线性模型常难以处理非线性信号。
- 通过系统分析卷积神经网络的感受野，引入个体感受野揭示卷积层作为特征提取器，具有对非线性波动的鲁棒性。
- 在多个基准数据集上实验表明，ACFormer能有效缓解线性模型捕获高频成分的不足，实现最先进性能。

## 摘要（原文）

> Time series forecasting (TSF) faces challenges in modeling complex intra-channel temporal dependencies and inter-channel correlations. Although recent research has highlighted the efficiency of linear architectures in capturing global trends, these models often struggle with non-linear signals. To address this gap, we conducted a systematic receptive field analysis of convolutional neural network (CNN) TSF models. We introduce the "individual receptive field" to uncover granular structural dependencies, revealing that convolutional layers act as feature extractors that mirror channel-wise attention while exhibiting superior robustness to non-linear fluctuations. Based on these insights, we propose ACFormer, an architecture designed to reconcile the efficiency of linear projections with the non-linear feature-extraction power of convolutions. ACFormer captures fine-grained information through a shared compression module, preserves temporal locality via gated attention, and reconstructs variable-specific temporal patterns using an independent patch expansion layer. Extensive experiments on multiple benchmark datasets demonstrate that ACFormer consistently achieves state-of-the-art performance, effectively mitigating the inherent drawbacks of linear models in capturing high-frequency components.

