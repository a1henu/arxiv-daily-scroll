---
layout: default
title: Switch-Hurdle: A MoE Encoder with AR Hurdle Decoder for Intermittent Demand Forecasting
---

# Switch-Hurdle: A MoE Encoder with AR Hurdle Decoder for Intermittent Demand Forecasting
**arXiv**：[2602.22685v1](https://arxiv.org/abs/2602.22685) · [PDF](https://arxiv.org/pdf/2602.22685.pdf)  
**作者**：Fabian Muşat, Simona Căbuz  

**一句话要点**：提出Switch-Hurdle框架，结合MoE编码器与AR Hurdle解码器，以解决零售间歇性需求预测难题。

**关键词**：间歇性需求预测, 混合专家模型, Hurdle模型, 零售预测, 稀疏序列处理, 自回归解码器

## 3 点简述
- 间歇性需求预测面临零值序列长、非零值稀疏的挑战，传统和现代方法常表现不佳。
- Switch-Hurdle采用稀疏MoE编码器与Hurdle解码器，分离销售概率和数量预测，提升模型适应性。
- 在M5基准和零售数据集上，Switch-Hurdle实现最优预测性能，同时保持可扩展性。

## 摘要（原文）

> Intermittent demand, a pattern characterized by long sequences of zero sales punctuated by sporadic, non-zero values, poses a persistent challenge in retail and supply chain forecasting. Both traditional methods, such as ARIMA, exponential smoothing, or Croston variants, as well as modern neural architectures such as DeepAR and Transformer-based models often underperform on such data, as they treat demand as a single continuous process or become computationally expensive when scaled across many sparse series. To address these limitations, we introduce Switch-Hurdle: a new framework that integrates a Mixture-of-Experts (MoE) encoder with a Hurdle-based probabilistic decoder. The encoder uses a sparse Top-1 expert routing during the forward pass yet approximately dense in the backward pass via a straight-through estimator (STE). The decoder follows a cross-attention autoregressive design with a shared hurdle head that explicitly separates the forecasting task into two components: a binary classification component estimating the probability of a sale, and a conditional regression component, predicting the quantity given a sale. This structured separation enables the model to capture both occurrence and magnitude processes inherent to intermittent demand. Empirical results on the M5 benchmark and a large proprietary retail dataset show that Switch-Hurdle achieves state-of-the-art prediction performance while maintaining scalability.

