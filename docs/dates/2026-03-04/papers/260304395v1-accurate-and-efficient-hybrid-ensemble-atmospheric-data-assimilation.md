---
layout: default
title: Accurate and Efficient Hybrid-Ensemble Atmospheric Data Assimilation in Latent Space with Uncertainty Quantification
---

# Accurate and Efficient Hybrid-Ensemble Atmospheric Data Assimilation in Latent Space with Uncertainty Quantification
**arXiv**：[2603.04395v1](https://arxiv.org/abs/2603.04395) · [PDF](https://arxiv.org/pdf/2603.04395.pdf)  
**作者**：Hang Fan, Juan Nathaniel, Yi Xiao, Ce Bian, Fenghua Ling, Ben Fei, Lei Bai, Pierre Gentine  

**一句话要点**：提出HLOBA方法，在潜在空间实现高效混合集合数据同化，并量化不确定性。

**关键词**：数据同化, 潜在空间, 混合集合, 不确定性量化, 自编码器, 贝叶斯更新

## 3 点简述
- 核心问题：现有数据同化方法难以同时保证精度、效率和不确定性量化。
- 方法要点：使用自编码器将模型预测和观测映射到共享潜在空间，通过贝叶斯更新融合。
- 实验或效果：在理想和真实观测实验中匹配动态约束方法，实现端到端高效推理和不确定性估计。

## 摘要（原文）

> Data assimilation (DA) combines model forecasts and observations to estimate the optimal state of the atmosphere with its uncertainty, providing initial conditions for weather prediction and reanalyses for climate research. Yet, existing traditional and machine-learning DA methods struggle to achieve accuracy, efficiency and uncertainty quantification simultaneously. Here, we propose HLOBA (Hybrid-Ensemble Latent Observation-Background Assimilation), a three-dimensional hybrid-ensemble DA method that operates in an atmospheric latent space learned via an autoencoder (AE). HLOBA maps both model forecasts and observations into a shared latent space via the AE encoder and an end-to-end Observation-to-Latent-space mapping network (O2Lnet), respectively, and fuses them through a Bayesian update with weights inferred from time-lagged ensemble forecasts. Both idealized and real-observation experiments demonstrate that HLOBA matches dynamically constrained four-dimensional DA methods in both analysis and forecast skill, while achieving end-to-end inference-level efficiency and theoretical flexibility applies to any forecasting model. Moreover, by exploiting the error decorrelation property of latent variables, HLOBA enables element-wise uncertainty estimates for its latent analysis and propagates them to model space via the decoder. Idealized experiments show that this uncertainty highlights large-error regions and captures their seasonal variability.

