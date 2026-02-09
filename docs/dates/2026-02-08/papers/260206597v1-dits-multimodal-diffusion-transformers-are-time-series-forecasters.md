---
layout: default
title: DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters
---

# DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters
**arXiv**：[2602.06597v1](https://arxiv.org/abs/2602.06597) · [PDF](https://arxiv.org/pdf/2602.06597.pdf)  
**作者**：Haoran Zhang, Haixuan Liu, Yong Liu, Yunzhong Qiu, Yuxuan Wang, Jianmin Wang, Mingsheng Long  

**一句话要点**：提出DiTS架构，将时间序列的内生和外生变量作为多模态处理，以改进概率预测。

**关键词**：时间序列预测, 扩散变换器, 多模态建模, 概率预测, 双流Transformer

## 3 点简述
- 现有生成模型未充分处理时间序列的多维特性，导致跨变量依赖利用不足。
- 设计双流Transformer块，包含时间注意力和变量注意力模块，以捕捉时序和跨变量依赖。
- 实验显示DiTS在基准测试中达到最先进性能，优于传统确定性深度预测模型。

## 摘要（原文）

> While generative modeling on time series facilitates more capable and flexible probabilistic forecasting, existing generative time series models do not address the multi-dimensional properties of time series data well. The prevalent architecture of Diffusion Transformers (DiT), which relies on simplistic conditioning controls and a single-stream Transformer backbone, tends to underutilize cross-variate dependencies in covariate-aware forecasting. Inspired by Multimodal Diffusion Transformers that integrate textual guidance into video generation, we propose Diffusion Transformers for Time Series (DiTS), a general-purpose architecture that frames endogenous and exogenous variates as distinct modalities. To better capture both inter-variate and intra-variate dependencies, we design a dual-stream Transformer block tailored for time-series data, comprising a Time Attention module for autoregressive modeling along the temporal dimension and a Variate Attention module for cross-variate modeling. Unlike the common approach for images, which flattens 2D token grids into 1D sequences, our design leverages the low-rank property inherent in multivariate dependencies, thereby reducing computational costs. Experiments show that DiTS achieves state-of-the-art performance across benchmarks, regardless of the presence of future exogenous variate observations, demonstrating unique generative forecasting strengths over traditional deterministic deep forecasting models.

