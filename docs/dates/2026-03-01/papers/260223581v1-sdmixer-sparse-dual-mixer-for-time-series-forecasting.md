---
layout: default
title: SDMixer: Sparse Dual-Mixer for Time Series Forecasting
---

# SDMixer: Sparse Dual-Mixer for Time Series Forecasting
**arXiv**：[2602.23581v1](https://arxiv.org/abs/2602.23581) · [PDF](https://arxiv.org/pdf/2602.23581.pdf)  
**作者**：Xiang Ao  

**一句话要点**：提出SDMixer稀疏双流混合器框架，以解决多变量时间序列预测中的多尺度、弱相关和噪声问题。

**关键词**：时间序列预测, 多变量分析, 稀疏机制, 频域特征提取, 时域特征提取, 双流框架

## 3 点简述
- 核心问题：多变量时间序列数据存在多尺度特征、弱相关性和噪声干扰，限制预测性能。
- 方法要点：采用双流稀疏Mixer框架，在频域和时域分别提取全局趋势和局部动态特征，通过稀疏机制过滤无效信息。
- 实验或效果：在多个真实场景数据集上实现领先性能，验证了方法的有效性和泛化能力。

## 摘要（原文）

> Multivariate time series forecasting is widely applied in fields such as transportation, energy, and finance. However, the data commonly suffers from issues of multi-scale characteristics, weak correlations, and noise interference, which limit the predictive performance of existing models. This paper proposes a dual-stream sparse Mixer prediction framework that extracts global trends and local dynamic features from sequences in both the frequency and time domains, respectively. It employs a sparsity mechanism to filter out invalid information, thereby enhancing the accuracy of cross-variable dependency modeling. Experimental results demonstrate that this method achieves leading performance on multiple real-world scenario datasets, validating its effectiveness and generality. The code is available at https://github.com/SDMixer/SDMixer

