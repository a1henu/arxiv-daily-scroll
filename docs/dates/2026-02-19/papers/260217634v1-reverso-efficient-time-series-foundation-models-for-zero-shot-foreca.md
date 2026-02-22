---
layout: default
title: Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting
---

# Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting
**arXiv**：[2602.17634v1](https://arxiv.org/abs/2602.17634) · [PDF](https://arxiv.org/pdf/2602.17634.pdf)  
**作者**：Xinghong Fu, Yanhong Li, Georgios Papaioannou, Yoon Kim  

**一句话要点**：提出Reverso高效时间序列基础模型，用于零样本预测，显著提升性能-效率帕累托前沿。

**关键词**：时间序列基础模型, 零样本预测, 高效模型, 长卷积, 线性RNN, 性能-效率优化

## 3 点简述
- 核心问题：现有时间序列基础模型参数庞大，导致效率低下且使用成本高。
- 方法要点：采用小型混合模型，结合长卷积和线性RNN层（如DeltaNet），替代大型Transformer。
- 实验或效果：模型比基于Transformer的模型小百倍以上，性能相当，并辅以数据增强和推理策略提升效果。

## 摘要（原文）

> Learning time series foundation models has been shown to be a promising approach for zero-shot time series forecasting across diverse time series domains. Insofar as scaling has been a critical driver of performance of foundation models in other modalities such as language and vision, much recent work on time series foundation modeling has focused on scaling. This has resulted in time series foundation models with hundreds of millions of parameters that are, while performant, inefficient and expensive to use in practice. This paper describes a simple recipe for learning efficient foundation models for zero-shot time series forecasting that are orders of magnitude smaller. We show that large-scale transformers are not necessary: small hybrid models that interleave long convolution and linear RNN layers (in particular DeltaNet layers) can match the performance of larger transformer-based models while being more than a hundred times smaller. We also describe several data augmentation and inference strategies that further improve performance. This recipe results in Reverso, a family of efficient time series foundation models for zero-shot forecasting that significantly push the performance-efficiency Pareto frontier.

