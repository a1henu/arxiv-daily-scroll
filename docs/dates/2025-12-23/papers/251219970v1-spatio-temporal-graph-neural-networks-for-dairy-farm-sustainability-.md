---
layout: default
title: Spatio-Temporal Graph Neural Networks for Dairy Farm Sustainability Forecasting and Counterfactual Policy Analysis
---

# Spatio-Temporal Graph Neural Networks for Dairy Farm Sustainability Forecasting and Counterfactual Policy Analysis
**arXiv**：[2512.19970v1](https://arxiv.org/abs/2512.19970) · [PDF](https://arxiv.org/pdf/2512.19970.pdf)  
**作者**：Surya Jayakumar, Kieran Sullivan, John McLaughlin, Christine O'Meara, Indrakshi Dey  

**一句话要点**：提出时空图神经网络框架，用于乳牛场可持续性预测与政策分析

**关键词**：时空图神经网络, 可持续性预测, 变分自编码器, 主成分分析, 乳牛场管理, 反事实分析

## 3 点简述
- 核心问题：基于牛群级数据预测县级可持续性指数，解决数据稀疏性和时空依赖建模挑战。
- 方法要点：使用变分自编码器增强数据，通过主成分分析构建加权指数，并设计STGNN编码地理依赖和非线性动态。
- 实验或效果：首次在县级尺度应用，生成2026-2030年多年预测，支持反事实政策分析。

## 摘要（原文）

> This study introduces a novel data-driven framework and the first-ever county-scale application of Spatio-Temporal Graph Neural Networks (STGNN) to forecast composite sustainability indices from herd-level operational records. The methodology employs a novel, end-to-end pipeline utilizing a Variational Autoencoder (VAE) to augment Irish Cattle Breeding Federation (ICBF) datasets, preserving joint distributions while mitigating sparsity. A first-ever pillar-based scoring formulation is derived via Principal Component Analysis, identifying Reproductive Efficiency, Genetic Management, Herd Health, and Herd Management, to construct weighted composite indices. These indices are modelled using a novel STGNN architecture that explicitly encodes geographic dependencies and non-linear temporal dynamics to generate multi-year forecasts for 2026-2030.

