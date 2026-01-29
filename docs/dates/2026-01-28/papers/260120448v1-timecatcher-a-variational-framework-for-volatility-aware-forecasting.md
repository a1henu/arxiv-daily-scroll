---
layout: default
title: TimeCatcher: A Variational Framework for Volatility-Aware Forecasting of Non-Stationary Time Series
---

# TimeCatcher: A Variational Framework for Volatility-Aware Forecasting of Non-Stationary Time Series
**arXiv**：[2601.20448v1](https://arxiv.org/abs/2601.20448) · [PDF](https://arxiv.org/pdf/2601.20448.pdf)  
**作者**：Zhiyu Chen, Minhao Liu, Yanru Zhang  

**一句话要点**：提出TimeCatcher框架以解决非平稳时间序列中高波动性长期预测的挑战

**关键词**：时间序列预测, 非平稳性处理, 变分编码器, 波动感知机制, 长期预测

## 3 点简述
- 核心问题：现有轻量MLP模型依赖局部平稳性假设，在非平稳序列长期预测中易出错，尤其在突发波动场景。
- 方法要点：结合变分编码器捕捉历史数据的潜在动态模式，并引入波动感知增强机制检测和放大局部显著变化。
- 实验或效果：在九个真实世界数据集上验证，TimeCatcher在长期高波动预测中显著优于现有方法。

## 摘要（原文）

> Recent lightweight MLP-based models have achieved strong performance in time series forecasting by capturing stable trends and seasonal patterns. However, their effectiveness hinges on an implicit assumption of local stationarity assumption, making them prone to errors in long-term forecasting of highly non-stationary series, especially when abrupt fluctuations occur, a common challenge in domains like web traffic monitoring. To overcome this limitation, we propose TimeCatcher, a novel Volatility-Aware Variational Forecasting framework. TimeCatcher extends linear architectures with a variational encoder to capture latent dynamic patterns hidden in historical data and a volatility-aware enhancement mechanism to detect and amplify significant local variations. Experiments on nine real-world datasets from traffic, financial, energy, and weather domains show that TimeCatcher consistently outperforms state-of-the-art baselines, with particularly large improvements in long-term forecasting scenarios characterized by high volatility and sudden fluctuations. Our code is available at https://github.com/ColaPrinceCHEN/TimeCatcher.

