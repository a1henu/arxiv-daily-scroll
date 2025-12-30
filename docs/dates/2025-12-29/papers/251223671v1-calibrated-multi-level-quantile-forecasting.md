---
layout: default
title: Calibrated Multi-Level Quantile Forecasting
---

# Calibrated Multi-Level Quantile Forecasting
**arXiv**：[2512.23671v1](https://arxiv.org/abs/2512.23671) · [PDF](https://arxiv.org/pdf/2512.23671.pdf)  
**作者**：Tiffany Ding, Isaac Gibbs, Ryan J. Tibshirani  

**一句话要点**：提出MultiQT方法，在线保证多分位数预测的校准性，适用于对抗性分布偏移场景。

**关键词**：分位数预测, 在线校准, 对抗性学习, 预测保证, 轻量级方法

## 3 点简述
- 核心问题：多分位数预测的校准性难以保证，尤其在分布偏移下。
- 方法要点：轻量级包装方法，修正现有预测器，确保校准和分位数顺序。
- 实验或效果：在流行病和能源预测中显著提升校准性，不降低性能。

## 摘要（原文）

> We present an online method for guaranteeing calibration of quantile forecasts at multiple quantile levels simultaneously. A sequence of $α$-level quantile forecasts is calibrated if the forecasts are larger than the target value at an $α$-fraction of time steps. We introduce a lightweight method called Multi-Level Quantile Tracker (MultiQT) that wraps around any existing point or quantile forecaster to produce corrected forecasts guaranteed to achieve calibration, even against adversarial distribution shifts, while ensuring that the forecasts are ordered -- e.g., the 0.5-level quantile forecast is never larger than the 0.6-level forecast. Furthermore, the method comes with a no-regret guarantee that implies it will not worsen the performance of an existing forecaster, asymptotically, with respect to the quantile loss. In experiments, we find that MultiQT significantly improves the calibration of real forecasters in epidemic and energy forecasting problems.

