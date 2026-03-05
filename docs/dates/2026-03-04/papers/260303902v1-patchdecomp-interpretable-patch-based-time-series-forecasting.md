---
layout: default
title: PatchDecomp: Interpretable Patch-Based Time Series Forecasting
---

# PatchDecomp: Interpretable Patch-Based Time Series Forecasting
**arXiv**：[2603.03902v1](https://arxiv.org/abs/2603.03902) · [PDF](https://arxiv.org/pdf/2603.03902.pdf)  
**作者**：Hiroki Tomioka, Genta Yoshimura  

**一句话要点**：提出PatchDecomp以实现高精度且可解释的时间序列预测

**关键词**：时间序列预测, 可解释性, 补丁分解, 神经网络, 归因分析

## 3 点简述
- 核心问题：复杂神经网络模型在时间序列预测中缺乏可解释性，限制人类理解预测依据。
- 方法要点：将输入时间序列划分为子序列（补丁），通过聚合每个补丁的贡献生成预测，实现清晰归因。
- 实验或效果：在多个基准数据集上预测性能与近期方法相当，并提供定量和定性的可解释性可视化。

## 摘要（原文）

> Time series forecasting, which predicts future values from past observations, plays a central role in many domains and has driven the development of highly accurate neural network models. However, the complexity of these models often limits human understanding of the rationale behind their predictions. We propose PatchDecomp, a neural network-based time series forecasting method that achieves both high accuracy and interpretability. PatchDecomp divides input time series into subsequences (patches) and generates predictions by aggregating the contributions of each patch. This enables clear attribution of each patch, including those from exogenous variables, to the final prediction. Experiments on multiple benchmark datasets demonstrate that PatchDecomp provides predictive performance comparable to recent forecasting methods. Furthermore, we show that the model's explanations not only influence predicted values quantitatively but also offer qualitative interpretability through visualization of patch-wise contributions.

