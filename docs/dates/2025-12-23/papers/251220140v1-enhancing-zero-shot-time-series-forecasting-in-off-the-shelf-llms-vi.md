---
layout: default
title: Enhancing Zero-Shot Time Series Forecasting in Off-the-Shelf LLMs via Noise Injection
---

# Enhancing Zero-Shot Time Series Forecasting in Off-the-Shelf LLMs via Noise Injection
**arXiv**：[2512.20140v1](https://arxiv.org/abs/2512.20140) · [PDF](https://arxiv.org/pdf/2512.20140.pdf)  
**作者**：Xingyou Yin, Ceyao Zhang, Min Hu, Kai Chen  

**一句话要点**：提出噪声注入策略以增强零样本时间序列预测中现成LLMs的鲁棒性

**关键词**：零样本学习, 时间序列预测, 大型语言模型, 噪声注入, 推理时增强, 现成模型

## 3 点简述
- 核心问题：现成LLMs在零样本时间序列预测中，对输入数据的文本表示高度敏感，易受分布偏移影响。
- 方法要点：在时间序列数据tokenization前注入噪声，作为推理时增强，促使模型基于稳健时间模式而非数值伪影进行预测。
- 实验或效果：理论分析支持，并在多个基准测试中实证有效，包括引入新数据集以避免预训练数据污染偏差。

## 摘要（原文）

> Large Language Models (LLMs) have demonstrated effectiveness as zero-shot time series (TS) forecasters. The key challenge lies in tokenizing TS data into textual representations that align with LLMs' pre-trained knowledge. While existing work often relies on fine-tuning specialized modules to bridge this gap, a distinct, yet challenging, paradigm aims to leverage truly off-the-shelf LLMs without any fine-tuning whatsoever, relying solely on strategic tokenization of numerical sequences. The performance of these fully frozen models is acutely sensitive to the textual representation of the input data, as their parameters cannot adapt to distribution shifts. In this paper, we introduce a simple yet highly effective strategy to overcome this brittleness: injecting noise into the raw time series before tokenization. This non-invasive intervention acts as a form of inference-time augmentation, compelling the frozen LLM to extrapolate based on robust underlying temporal patterns rather than superficial numerical artifacts. We theoretically analyze this phenomenon and empirically validate its effectiveness across diverse benchmarks. Notably, to fully eliminate potential biases from data contamination during LLM pre-training, we introduce two novel TS datasets that fall outside all utilized LLMs' pre-training scopes, and consistently observe improved performance. This study provides a further step in directly leveraging off-the-shelf LLMs for time series forecasting.

