---
layout: default
title: Intermittent time series forecasting: local vs global models
---

# Intermittent time series forecasting: local vs global models
**arXiv**：[2601.14031v1](https://arxiv.org/abs/2601.14031) · [PDF](https://arxiv.org/pdf/2601.14031.pdf)  
**作者**：Stefano Damato, Nicolò Rubattu, Dario Azzimonti, Giorgio Corani  

**一句话要点**：比较局部与全局模型在间歇性时间序列预测中的性能，发现D-Linear全局模型优于局部模型。

**关键词**：间歇性时间序列预测, 局部模型, 全局模型, D-Linear, Tweedie分布, 供应链库存规划

## 3 点简述
- 间歇性时间序列预测需处理大量零值和长尾分布，用于供应链库存规划。
- 首次系统比较局部模型（iETS、TweedieGP）与全局模型（D-Linear、DeepAR、Transformers）在间歇性序列上的表现。
- 实验基于5个大型数据集，D-Linear在准确性和计算效率上表现最佳，Tweedie分布头在高分位数估计中效果最好。

## 摘要（原文）

> Intermittent time series, characterised by the presence of a significant amount of zeros, constitute a large percentage of inventory items in supply chain. Probabilistic forecasts are needed to plan the inventory levels; the predictive distribution should cover non-negative values, have a mass in zero and a long upper tail. Intermittent time series are commonly forecast using local models, which are trained individually on each time series. In the last years global models, which are trained on a large collection of time series, have become popular for time series forecasting. Global models are often based on neural networks. However, they have not yet been exhaustively tested on intermittent time series. We carry out the first study comparing state-of-the-art local (iETS, TweedieGP) and global models (D-Linear, DeepAR, Transformers) on intermittent time series. For neural networks models we consider three different distribution heads suitable for intermittent time series: negative binomial, hurdle-shifted negative binomial and Tweedie. We use, for the first time, the last two distribution heads with neural networks. We perform experiments on five large datasets comprising more than 40'000 real-world time series. Among neural networks D-Linear provides best accuracy; it also consistently outperforms the local models. Moreover, it has also low computational requirements. Transformers-based architectures are instead much more computationally demanding and less accurate. Among the distribution heads, the Tweedie provides the best estimates of the highest quantiles, while the negative binomial offers overall the best performance.

