---
layout: default
title: Horizon Activation Mapping for Neural Networks in Time Series Forecasting
---

# Horizon Activation Mapping for Neural Networks in Time Series Forecasting
**arXiv**：[2601.02094v1](https://arxiv.org/abs/2601.02094) · [PDF](https://arxiv.org/pdf/2601.02094.pdf)  
**作者**：Hans Krupakar, V A Kandappan  

**一句话要点**：提出Horizon Activation Mapping以跨模型家族解释时间序列预测神经网络

**关键词**：时间序列预测, 神经网络解释, 梯度激活映射, 模型选择, 可视化技术

## 3 点简述
- 核心问题：现有模型选择方法依赖误差指标和架构特定解释，不适用于不同家族模型。
- 方法要点：引入HAM，一种基于梯度范数平均的可视化解释技术，受grad-CAM启发，支持因果和反因果模式。
- 实验或效果：在ETTm2数据集上测试多种模型，HAM可用于细粒度模型选择、验证集选择和跨模型比较。

## 摘要（原文）

> Neural networks for time series forecasting have relied on error metrics and architecture-specific interpretability approaches for model selection that don't apply across models of different families. To interpret forecasting models agnostic to the types of layers across state-of-the-art model families, we introduce Horizon Activation Mapping (HAM), a visual interpretability technique inspired by grad-CAM that uses gradient norm averages to study the horizon's subseries where grad-CAM studies attention maps over image data. We introduce causal and anti-causal modes to calculate gradient update norm averages across subseries at every timestep and lines of proportionality signifying uniform distributions of the norm averages. Optimization landscape studies with respect to changes in batch sizes, early stopping, train-val-test splits, univariate forecasting and dropouts are studied with respect to performances and subseries in HAM. Interestingly, batch size based differences in activities seem to indicate potential for existence of an exponential approximation across them per epoch relative to each other. Multivariate forecasting models including MLP-based CycleNet, N-Linear, N-HITS, self attention-based FEDformer, Pyraformer, SSM-based SpaceTime and diffusion-based Multi-Resolution DDPM over different horizon sizes trained over the ETTm2 dataset are used for HAM plots in this study. NHITS' neural approximation theorem and SpaceTime's exponential autoregressive activities have been attributed to trends in HAM plots over their training, validation and test sets. In general, HAM can be used for granular model selection, validation set choices and comparisons across different neural network model families.

