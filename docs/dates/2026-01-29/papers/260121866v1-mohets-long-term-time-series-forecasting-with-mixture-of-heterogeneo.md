---
layout: default
title: MoHETS: Long-term Time Series Forecasting with Mixture-of-Heterogeneous-Experts
---

# MoHETS: Long-term Time Series Forecasting with Mixture-of-Heterogeneous-Experts
**arXiv**：[2601.21866v1](https://arxiv.org/abs/2601.21866) · [PDF](https://arxiv.org/pdf/2601.21866.pdf)  
**作者**：Evandro S. Ortigossa, Guy Lutsker, Eran Segal  

**一句话要点**：提出MoHETS模型，通过混合异构专家解决多元时间序列长期预测中的多尺度动态挑战。

**关键词**：长期时间序列预测, 混合异构专家, Transformer模型, 多尺度动态, 非平稳性处理, 参数效率优化

## 3 点简述
- 核心问题：现实世界多元时间序列具有复杂多尺度结构，如全局趋势和局部周期性，使长期预测困难。
- 方法要点：采用稀疏混合异构专家层，结合卷积专家和傅里叶专家，并引入外生信息增强鲁棒性。
- 实验或效果：在七个多元基准测试中，MoHETS平均MSE降低12%，实现最先进性能。

## 摘要（原文）

> Real-world multivariate time series can exhibit intricate multi-scale structures, including global trends, local periodicities, and non-stationary regimes, which makes long-horizon forecasting challenging. Although sparse Mixture-of-Experts (MoE) approaches improve scalability and specialization, they typically rely on homogeneous MLP experts that poorly capture the diverse temporal dynamics of time series data. We address these limitations with MoHETS, an encoder-only Transformer that integrates sparse Mixture-of-Heterogeneous-Experts (MoHE) layers. MoHE routes temporal patches to a small subset of expert networks, combining a shared depthwise-convolution expert for sequence-level continuity with routed Fourier-based experts for patch-level periodic structures. MoHETS further improves robustness to non-stationary dynamics by incorporating exogenous information via cross-attention over covariate patch embeddings. Finally, we replace parameter-heavy linear projection heads with a lightweight convolutional patch decoder, improving parameter efficiency, reducing training instability, and allowing a single model to generalize across arbitrary forecast horizons. We validate across seven multivariate benchmarks and multiple horizons, with MoHETS consistently achieving state-of-the-art performance, reducing the average MSE by $12\%$ compared to strong recent baselines, demonstrating effective heterogeneous specialization for long-term forecasting.

