---
layout: default
title: Seg-MoE: Multi-Resolution Segment-wise Mixture-of-Experts for Time Series Forecasting Transformers
---

# Seg-MoE: Multi-Resolution Segment-wise Mixture-of-Experts for Time Series Forecasting Transformers
**arXiv**：[2601.21641v1](https://arxiv.org/abs/2601.21641) · [PDF](https://arxiv.org/pdf/2601.21641.pdf)  
**作者**：Evandro S. Ortigossa, Eran Segal  

**一句话要点**：提出Seg-MoE以解决时间序列预测中Transformer模型难以高效扩展并捕获长期动态的问题

**关键词**：时间序列预测, Transformer模型, 混合专家, 段级路由, 稀疏架构, 长期动态建模

## 3 点简述
- 核心问题：现有基于MoE的时间序列预测方法采用token-wise路由，未能充分利用时间数据的局部性和连续性
- 方法要点：Seg-MoE通过路由和处理连续时间步段，使专家直接建模段内交互，与时间模式自然对齐
- 实验或效果：在多个多元长期预测基准测试中，Seg-MoE几乎在所有预测范围上达到最先进精度，优于密集Transformer和先前token-wise MoE模型

## 摘要（原文）

> Transformer-based models have recently made significant advances in accurate time-series forecasting, but even these architectures struggle to scale efficiently while capturing long-term temporal dynamics. Mixture-of-Experts (MoE) layers are a proven solution to scaling problems in natural language processing. However, existing MoE approaches for time-series forecasting rely on token-wise routing mechanisms, which may fail to exploit the natural locality and continuity of temporal data. In this work, we introduce Seg-MoE, a sparse MoE design that routes and processes contiguous time-step segments rather than making independent expert decisions. Token segments allow each expert to model intra-segment interactions directly, naturally aligning with inherent temporal patterns. We integrate Seg-MoE layers into a time-series Transformer and evaluate it on multiple multivariate long-term forecasting benchmarks. Seg-MoE consistently achieves state-of-the-art forecasting accuracy across almost all prediction horizons, outperforming both dense Transformers and prior token-wise MoE models. Comprehensive ablation studies confirm that segment-level routing is the key factor driving these gains. Our results show that aligning the MoE routing granularity with the inherent structure of time series provides a powerful, yet previously underexplored, inductive bias, opening new avenues for conditionally sparse architectures in sequential data modeling.

