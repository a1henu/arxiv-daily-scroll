---
layout: default
title: Harmonic Dataset Distillation for Time Series Forecasting
---

# Harmonic Dataset Distillation for Time Series Forecasting
**arXiv**：[2603.03760v1](https://arxiv.org/abs/2603.03760) · [PDF](https://arxiv.org/pdf/2603.03760.pdf)  
**作者**：Seungha Hong, Sanghwan Jang, Wonbin Kweon, Suyeon Kim, Gyuseok Lee, Hwanjo Yu  

**一句话要点**：提出谐波数据集蒸馏方法以解决时间序列预测中的计算存储挑战

**关键词**：时间序列预测, 数据集蒸馏, 谐波分解, 频域处理, 跨架构泛化

## 3 点简述
- 核心问题：传统数据集蒸馏方法不适用于时间序列，存在架构过拟合和可扩展性限制
- 方法要点：通过FFT分解时间序列为谐波基，使用谐波匹配对齐周期性结构，在频域进行全局更新
- 实验或效果：实验显示HDT具有强跨架构泛化能力和可扩展性，适用于大规模实际应用

## 摘要（原文）

> Time Series forecasting (TSF) in the modern era faces significant computational and storage cost challenges due to the massive scale of real-world data. Dataset Distillation (DD), a paradigm that synthesizes a small, compact dataset to achieve training performance comparable to that of the original dataset, has emerged as a promising solution. However, conventional DD methods are not tailored for time series and suffer from architectural overfitting and limited scalability. To address these issues, we propose Harmonic Dataset Distillation for Time Series Forecasting (HDT). HDT decomposes the time series into its sinusoidal basis through the FFT and aligns the core periodic structure by Harmonic Matching. Since this process operates in the frequency domain, all updates during distillation are applied globally without disrupting temporal dependencies of time series. Extensive experiments demonstrate that HDT achieves strong cross-architecture generalization and scalability, validating its practicality for large-scale, real-world applications.

