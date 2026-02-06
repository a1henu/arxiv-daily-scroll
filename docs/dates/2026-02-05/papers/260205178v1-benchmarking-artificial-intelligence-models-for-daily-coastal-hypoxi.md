---
layout: default
title: Benchmarking Artificial Intelligence Models for Daily Coastal Hypoxia Forecasting
---

# Benchmarking Artificial Intelligence Models for Daily Coastal Hypoxia Forecasting
**arXiv**：[2602.05178v1](https://arxiv.org/abs/2602.05178) · [PDF](https://arxiv.org/pdf/2602.05178.pdf)  
**作者**：Magesh Rajasekaran, Md Saiful Sajol, Chris Alvin, Supratik Mukhopadhyay, Yanda Ou, Z. George Xue  

**一句话要点**：提出基于深度学习的日尺度沿海缺氧分类框架，以支持实时生态系统管理。

**关键词**：沿海缺氧预测, 深度学习分类, 时空Transformer, 日尺度建模, 生态系统管理

## 3 点简述
- 核心问题：墨西哥湾北部沿海缺氧的日尺度变异性预测不足，影响生态管理。
- 方法要点：比较BiLSTM、Medformer、ST-Transformer和TCN四种深度学习架构，结合水柱分层等特征。
- 实验或效果：ST-Transformer在所有指标和测试期表现最佳，AUC-ROC达0.982-0.992，提供可复现框架。

## 摘要（原文）

> Coastal hypoxia, especially in the northern part of Gulf of Mexico, presents a persistent ecological and economic concern. Seasonal models offer coarse forecasts that miss the fine-scale variability needed for daily, responsive ecosystem management. We present study that compares four deep learning architectures for daily hypoxia classification: Bidirectional Long Short-Term Memory (BiLSTM), Medformer (Medical Transformer), Spatio-Temporal Transformer (ST-Transformer), and Temporal Convolutional Network (TCN). We trained our models with twelve years of daily hindcast data from 2009-2020 Our training data consists of 2009-2020 hindcast data from a coupled hydrodynamic-biogeochemical model. Similarly, we use hindcast data from 2020 through 2024 as a test data. We constructed classification models incorporating water column stratification, sediment oxygen consumption, and temperature-dependent decomposition rates. We evaluated each architectures using the same data preprocessing, input/output formulation, and validation protocols. Each model achieved high classification accuracy and strong discriminative ability with ST-Transformer achieving the highest performance across all metrics and tests periods (AUC-ROC: 0.982-0.992). We also employed McNemar's method to identify statistically significant differences in model predictions. Our contribution is a reproducible framework for operational real-time hypoxia prediction that can support broader efforts in the environmental and ocean modeling systems community and in ecosystem resilience. The source code is available https://github.com/rmagesh148/hypoxia-ai/

