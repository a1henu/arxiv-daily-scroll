---
layout: default
title: A lightweight Spatial-Temporal Graph Neural Network for Long-term Time Series Forecasting
---

# A lightweight Spatial-Temporal Graph Neural Network for Long-term Time Series Forecasting
**arXiv**：[2512.17453v1](https://arxiv.org/abs/2512.17453) · [PDF](https://arxiv.org/pdf/2512.17453.pdf)  
**作者**：Henok Tenaw Moges, Deshendran Moodley  

**一句话要点**：提出Lite-STGNN，一种轻量级时空图神经网络，用于长期多元时间序列预测。

**关键词**：长期时间序列预测, 时空图神经网络, 趋势-季节分解, 可学习图结构, 参数高效模型

## 3 点简述
- 核心问题：长期多元时间序列预测，需高效建模时空依赖。
- 方法要点：集成趋势-季节分解的时间模块和可学习稀疏图结构的空间模块。
- 实验或效果：在四个基准数据集上达到最先进精度，参数高效且训练速度快。

## 摘要（原文）

> We propose Lite-STGNN, a lightweight spatial-temporal graph neural network for long-term multivariate forecasting that integrates decomposition-based temporal modeling with learnable sparse graph structure. The temporal module applies trend-seasonal decomposition, while the spatial module performs message passing with low-rank Top-$K$ adjacency learning and conservative horizon-wise gating, enabling spatial corrections that enhance a strong linear baseline. Lite-STGNN achieves state-of-the-art accuracy on four benchmark datasets for horizons up to 720 steps, while being parameter-efficient and substantially faster to train than transformer-based methods. Ablation studies show that the spatial module yields 4.6% improvement over the temporal baseline, Top-$K$ enhances locality by 3.3%, and learned adjacency matrices reveal domain-specific interaction dynamics. Lite-STGNN thus offers a compact, interpretable, and efficient framework for long-term multivariate time series forecasting.

