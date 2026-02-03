---
layout: default
title: Spatio-Temporal Transformers for Long-Term NDVI Forecasting
---

# Spatio-Temporal Transformers for Long-Term NDVI Forecasting
**arXiv**：[2602.01799v1](https://arxiv.org/abs/2602.01799) · [PDF](https://arxiv.org/pdf/2602.01799.pdf)  
**作者**：Ido Faran, Nathan S. Netanyahu, Maxim Shoshany  

**一句话要点**：提出STT-LTF框架，通过时空Transformer整合空间上下文与时间序列，用于长期NDVI预测以应对异质景观挑战。

**关键词**：时空Transformer, 长期NDVI预测, 卫星图像时间序列, 自监督学习, 异质景观分析

## 3 点简述
- 核心问题：长期卫星图像时间序列分析在异质景观中面临空间模式复杂、季节变化和多年代环境变化交互的挑战。
- 方法要点：采用统一Transformer架构处理多尺度空间块和时间序列，结合自监督学习策略，直接预测任意未来时间点。
- 实验或效果：在Landsat数据上，STT-LTF在次年预测中MAE为0.0328，R^2为0.8412，优于传统方法。

## 摘要（原文）

> Long-term satellite image time series (SITS) analysis in heterogeneous landscapes faces significant challenges, particularly in Mediterranean regions where complex spatial patterns, seasonal variations, and multi-decade environmental changes interact across different scales. This paper presents the Spatio-Temporal Transformer for Long Term Forecasting (STT-LTF ), an extended framework that advances beyond purely temporal analysis to integrate spatial context modeling with temporal sequence prediction. STT-LTF processes multi-scale spatial patches alongside temporal sequences (up to 20 years) through a unified transformer architecture, capturing both local neighborhood relationships and regional climate influences. The framework employs comprehensive self-supervised learning with spatial masking, temporal masking, and horizon sampling strategies, enabling robust model training from 40 years of unlabeled Landsat imagery. Unlike autoregressive approaches, STT-LTF directly predicts arbitrary future time points without error accumulation, incorporating spatial patch embeddings, cyclical temporal encoding, and geographic coordinates to learn complex dependencies across heterogeneous Mediterranean ecosystems. Experimental evaluation on Landsat data (1984-2024) demonstrates that STT-LTF achieves a Mean Absolute Error (MAE) of 0.0328 and R^2 of 0.8412 for next-year predictions, outperforming traditional statistical methods, CNN-based approaches, LSTM networks, and standard transformers. The framework's ability to handle irregular temporal sampling and variable prediction horizons makes it particularly suitable for analysis of heterogeneous landscapes experiencing rapid ecological transitions.

