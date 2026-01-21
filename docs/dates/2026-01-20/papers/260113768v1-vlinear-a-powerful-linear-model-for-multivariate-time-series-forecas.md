---
layout: default
title: vLinear: A Powerful Linear Model for Multivariate Time Series Forecasting
---

# vLinear: A Powerful Linear Model for Multivariate Time Series Forecasting
**arXiv**：[2601.13768v1](https://arxiv.org/abs/2601.13768) · [PDF](https://arxiv.org/pdf/2601.13768.pdf)  
**作者**：Wenzhen Yue, Ruohao Guo, Ji Shi, Zihan Hao, Shiyu Hu, Xianghua Ying  

**一句话要点**：提出vLinear线性模型，通过vecTrans模块和WFMLoss目标提升多元时间序列预测效率与精度。

**关键词**：多元时间序列预测, 线性模型, 计算复杂度优化, 流匹配损失, 变量相关性建模, 预测精度提升

## 3 点简述
- 针对多元时间序列预测中自注意力计算复杂度高的问题，提出vecTrans模块，用可学习向量建模变量相关性，将复杂度降至O(N)。
- 引入WFMLoss目标，采用最终序列导向的流匹配损失，结合路径和时域加权策略，提升预测准确性。
- 在22个基准和124个预测设置中实现最优性能，WFMLoss可作为即插即用目标改进现有预测器。

## 摘要（原文）

> In this paper, we present \textbf{vLinear}, an effective yet efficient \textbf{linear}-based multivariate time series forecaster featuring two components: the \textbf{v}ecTrans module and the WFMLoss objective. Many state-of-the-art forecasters rely on self-attention or its variants to capture multivariate correlations, typically incurring $\mathcal{O}(N^2)$ computational complexity with respect to the number of variates $N$. To address this, we propose vecTrans, a lightweight module that utilizes a learnable vector to model multivariate correlations, reducing the complexity to $\mathcal{O}(N)$. Notably, vecTrans can be seamlessly integrated into Transformer-based forecasters, delivering up to 5$\times$ inference speedups and consistent performance gains. Furthermore, we introduce WFMLoss (Weighted Flow Matching Loss) as the objective. In contrast to typical \textbf{velocity-oriented} flow matching objectives, we demonstrate that a \textbf{final-series-oriented} formulation yields significantly superior forecasting accuracy. WFMLoss also incorporates path- and horizon-weighted strategies to focus learning on more reliable paths and horizons. Empirically, vLinear achieves state-of-the-art performance across 22 benchmarks and 124 forecasting settings. Moreover, WFMLoss serves as an effective plug-and-play objective, consistently improving existing forecasters. The code is available at https://anonymous.4open.science/r/vLinear.

