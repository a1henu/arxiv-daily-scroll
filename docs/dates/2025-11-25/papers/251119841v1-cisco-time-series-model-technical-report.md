---
layout: default
title: Cisco Time Series Model Technical Report
---

# Cisco Time Series Model Technical Report
**arXiv**：[2511.19841v1](https://arxiv.org/abs/2511.19841) · [PDF](https://arxiv.org/pdf/2511.19841.pdf)  
**作者**：Liang Gou, Archit Khare, Praneet Pabolu, Prachi Patel, Joseph Ross, Hercy Shen, Yuhan, Song, Jingze Sun, Kristal Curtis, Vedant Dharnidharka, Abhinav Mathur, Hao Yang  

**一句话要点**：提出多分辨率解码器时间序列模型，提升可观测性数据预测精度。

**关键词**：时间序列预测, 多分辨率输入, 解码器模型, 可观测性数据, 零样本学习

## 3 点简述
- 核心问题：传统时间序列模型难以处理多分辨率输入，影响长上下文预测准确性。
- 方法要点：基于TimesFM架构创新，引入多分辨率输入能力，训练超3000亿数据点。
- 实验效果：在可观测性数据集上表现优异，通用基准性能保持相似。

## 摘要（原文）

> We introduce the Cisco Time Series Model, a univariate zero-shot forecaster. This time series foundation model is the result of a general architectural innovation to a time series model enabling it to accept multiresolution input, applied to a popular decoder-only time series model (TimesFM). The resulting multiresolution decoder-only model is trained on over 300B unique data points, with more than half coming from the observability domain. Quantitative and qualitative evaluations demonstrate that the resulting model achieves superior performance on observability datasets while retaining very similar performance on a standard general-purpose forecasting benchmark (GIFT-Eval), and suggest that the multiresolution structure enables the model to make more accurate predictions on long context input.

