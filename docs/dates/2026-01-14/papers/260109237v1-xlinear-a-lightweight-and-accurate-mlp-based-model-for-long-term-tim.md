---
layout: default
title: XLinear: A Lightweight and Accurate MLP-Based Model for Long-Term Time Series Forecasting with Exogenous Inputs
---

# XLinear: A Lightweight and Accurate MLP-Based Model for Long-Term Time Series Forecasting with Exogenous Inputs
**arXiv**：[2601.09237v1](https://arxiv.org/abs/2601.09237) · [PDF](https://arxiv.org/pdf/2601.09237.pdf)  
**作者**：Xinyang Chen, Huidong Jin, Yu Huang, Zaiwen Feng  

**一句话要点**：提出XLinear，一种基于MLP的轻量级模型，用于利用外生输入进行长期时间序列预测。

**关键词**：长期时间序列预测, 外生输入, 多层感知机, 轻量级模型, 时间模式提取

## 3 点简述
- 核心问题：现有模型假设变量重要性均匀，但实际应用中存在不对称因果关系和数据获取成本差异。
- 方法要点：使用全局令牌作为枢纽与外生变量交互，通过带sigmoid激活的MLP提取时间和变量间依赖。
- 实验或效果：在多个基准和真实数据集上评估，相比先进模型，在准确性和效率上表现更优。

## 摘要（原文）

> Despite the prevalent assumption of uniform variable importance in long-term time series forecasting models, real world applications often exhibit asymmetric causal relationships and varying data acquisition costs. Specifically, cost-effective exogenous data (e.g., local weather) can unilaterally influence dynamics of endogenous variables, such as lake surface temperature. Exploiting these links enables more effective forecasts when exogenous inputs are readily available. Transformer-based models capture long-range dependencies but incur high computation and suffer from permutation invariance. Patch-based variants improve efficiency yet can miss local temporal patterns. To efficiently exploit informative signals across both the temporal dimension and relevant exogenous variables, this study proposes XLinear, a lightweight time series forecasting model built upon MultiLayer Perceptrons (MLPs). XLinear uses a global token derived from an endogenous variable as a pivotal hub for interacting with exogenous variables, and employs MLPs with sigmoid activation to extract both temporal patterns and variate-wise dependencies. Its prediction head then integrates these signals to forecast the endogenous series. We evaluate XLinear on seven standard benchmarks and five real-world datasets with exogenous inputs. Compared with state-of-the-art models, XLinear delivers superior accuracy and efficiency for both multivariate forecasts and univariate forecasts influenced by exogenous inputs.

