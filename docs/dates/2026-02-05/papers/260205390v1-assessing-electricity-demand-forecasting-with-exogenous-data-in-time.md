---
layout: default
title: Assessing Electricity Demand Forecasting with Exogenous Data in Time Series Foundation Models
---

# Assessing Electricity Demand Forecasting with Exogenous Data in Time Series Foundation Models
**arXiv**：[2602.05390v1](https://arxiv.org/abs/2602.05390) · [PDF](https://arxiv.org/pdf/2602.05390.pdf)  
**作者**：Wei Soon Cheong, Lian Lian Jiang, Jamie Ng Suat Ling  

**一句话要点**：评估时间序列基础模型在电力需求预测中利用外生特征的有效性

**关键词**：时间序列预测, 电力需求预测, 外生特征, 基础模型评估, 地理气候影响, 模型架构分析

## 3 点简述
- 核心问题：时间序列基础模型能否有效利用外生特征进行电力需求预测，其性能与地理气候和模型架构的关系未知。
- 方法要点：在星澳电力市场，对比MOIRAI等基础模型与LSTM基线，评估三种特征配置下的零样本预测性能。
- 实验或效果：基础模型在多变气候中表现更佳，但基线模型在稳定气候中常更优，模型架构如分组注意力对特征利用至关重要。

## 摘要（原文）

> Time-series foundation models have emerged as a new paradigm for forecasting, yet their ability to effectively leverage exogenous features -- critical for electricity demand forecasting -- remains unclear. This paper empirically evaluates foundation models capable of modeling cross-channel correlations against a baseline LSTM with reversible instance normalization across Singaporean and Australian electricity markets at hourly and daily granularities. We systematically assess MOIRAI, MOMENT, TinyTimeMixers, ChronosX, and Chronos-2 under three feature configurations: all features, selected features, and target-only. Our findings reveal highly variable effectiveness: while Chronos-2 achieves the best performance among foundation models (in zero-shot settings), the simple baseline frequently outperforms all foundation models in Singapore's stable climate, particularly for short-term horizons. Model architecture proves critical, with synergistic architectural implementations (TTM's channel-mixing, Chronos-2's grouped attention) consistently leveraging exogenous features, while other approaches show inconsistent benefits. Geographic context emerges as equally important, with foundation models demonstrating advantages primarily in variable climates. These results challenge assumptions about universal foundation model superiority and highlight the need for domain-specific models, specifically in the energy domain.

