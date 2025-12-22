---
layout: default
title: Spatially-informed transformers: Injecting geostatistical covariance biases into self-attention for spatio-temporal forecasting
---

# Spatially-informed transformers: Injecting geostatistical covariance biases into self-attention for spatio-temporal forecasting
**arXiv**：[2512.17696v1](https://arxiv.org/abs/2512.17696) · [PDF](https://arxiv.org/pdf/2512.17696.pdf)  
**作者**：Yuri Calleo  

**一句话要点**：提出空间感知Transformer，通过可学习协方差核将地统计偏置注入自注意力机制，以提升时空预测性能。

**关键词**：时空预测, Transformer, 地统计偏置, 自注意力机制, 概率建模

## 3 点简述
- 核心问题：传统Transformer缺乏空间几何偏置，难以有效建模高维时空过程。
- 方法要点：将自注意力分解为静态物理先验和非静态数据驱动残差，注入地统计协方差偏置。
- 实验或效果：在合成高斯随机场和真实交通数据上超越图神经网络，实现校准良好的概率预测。

## 摘要（原文）

> The modeling of high-dimensional spatio-temporal processes presents a fundamental dichotomy between the probabilistic rigor of classical geostatistics and the flexible, high-capacity representations of deep learning. While Gaussian processes offer theoretical consistency and exact uncertainty quantification, their prohibitive computational scaling renders them impractical for massive sensor networks. Conversely, modern transformer architectures excel at sequence modeling but inherently lack a geometric inductive bias, treating spatial sensors as permutation-invariant tokens without a native understanding of distance. In this work, we propose a spatially-informed transformer, a hybrid architecture that injects a geostatistical inductive bias directly into the self-attention mechanism via a learnable covariance kernel. By formally decomposing the attention structure into a stationary physical prior and a non-stationary data-driven residual, we impose a soft topological constraint that favors spatially proximal interactions while retaining the capacity to model complex dynamics. We demonstrate the phenomenon of ``Deep Variography'', where the network successfully recovers the true spatial decay parameters of the underlying process end-to-end via backpropagation. Extensive experiments on synthetic Gaussian random fields and real-world traffic benchmarks confirm that our method outperforms state-of-the-art graph neural networks. Furthermore, rigorous statistical validation confirms that the proposed method delivers not only superior predictive accuracy but also well-calibrated probabilistic forecasts, effectively bridging the gap between physics-aware modeling and data-driven learning.

