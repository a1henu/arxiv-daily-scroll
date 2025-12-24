---
layout: default
title: DecoKAN: Interpretable Decomposition for Forecasting Cryptocurrency Market Dynamics
---

# DecoKAN: Interpretable Decomposition for Forecasting Cryptocurrency Market Dynamics
**arXiv**：[2512.20028v1](https://arxiv.org/abs/2512.20028) · [PDF](https://arxiv.org/pdf/2512.20028.pdf)  
**作者**：Yuan Gao, Zhenguo Dong, Xuelong Wang, Zhiqiang Wang, Yong Zhang, Shaofan Wang  

**一句话要点**：提出DecoKAN框架，通过分解与可解释建模提升加密货币市场预测的准确性与透明度

**关键词**：加密货币预测, 时间序列分解, 可解释深度学习, 离散小波变换, Kolmogorov-Arnold网络

## 3 点简述
- 加密货币数据包含长期趋势与高频振荡，现有深度学习模型难以解耦且缺乏可解释性
- DecoKAN结合离散小波变换分解时间序列与KAN混合器进行可解释非线性建模
- 在BTC、ETH、XMR数据集上实现最低平均均方误差，优于现有先进基线

## 摘要（原文）

> Accurate and interpretable forecasting of multivariate time series is crucial for understanding the complex dynamics of cryptocurrency markets in digital asset systems. Advanced deep learning methodologies, particularly Transformer-based and MLP-based architectures, have achieved competitive predictive performance in cryptocurrency forecasting tasks. However, cryptocurrency data is inherently composed of long-term socio-economic trends and local high-frequency speculative oscillations. Existing deep learning-based 'black-box' models fail to effectively decouple these composite dynamics or provide the interpretability needed for trustworthy financial decision-making. To overcome these limitations, we propose DecoKAN, an interpretable forecasting framework that integrates multi-level Discrete Wavelet Transform (DWT) for decoupling and hierarchical signal decomposition with Kolmogorov-Arnold Network (KAN) mixers for transparent and interpretable nonlinear modeling. The DWT component decomposes complex cryptocurrency time series into distinct frequency components, enabling frequency-specific analysis, while KAN mixers provide intrinsically interpretable spline-based mappings within each decomposed subseries. Furthermore, interpretability is enhanced through a symbolic analysis pipeline involving sparsification, pruning, and symbolization, which produces concise analytical expressions offering symbolic representations of the learned patterns. Extensive experiments demonstrate that DecoKAN achieves the lowest average Mean Squared Error on all tested real-world cryptocurrency datasets (BTC, ETH, XMR), consistently outperforming a comprehensive suite of competitive state-of-the-art baselines. These results validate DecoKAN's potential to bridge the gap between predictive accuracy and model transparency, advancing trustworthy decision support within complex cryptocurrency markets.

