---
layout: default
title: Time Series Foundation Models for Process Model Forecasting
---

# Time Series Foundation Models for Process Model Forecasting
**arXiv**：[2512.07624v1](https://arxiv.org/abs/2512.07624) · [PDF](https://arxiv.org/pdf/2512.07624.pdf)  
**作者**：Yongbo Yu, Jari Peeperkorn, Johannes De Smedt, Jochen De Weerdt  

**一句话要点**：评估时间序列基础模型在过程模型预测中的零样本与微调性能

**关键词**：过程模型预测, 时间序列基础模型, 零样本学习, 微调, 直接跟随关系, 预测性能评估

## 3 点简述
- 过程模型预测面临直接跟随关系时间序列的稀疏性和异质性挑战
- 研究采用时间序列基础模型进行零样本预测和微调，与传统方法对比
- 实验显示基础模型在多数数据集上优于传统模型，零样本使用效果稳定

## 摘要（原文）

> Process Model Forecasting (PMF) aims to predict how the control-flow structure of a process evolves over time by modeling the temporal dynamics of directly-follows (DF) relations, complementing predictive process monitoring that focuses on single-case prefixes. Prior benchmarks show that machine learning and deep learning models provide only modest gains over statistical baselines, mainly due to the sparsity and heterogeneity of the DF time series. We investigate Time Series Foundation Models (TSFMs), large pre-trained models for generic time series, as an alternative for PMF. Using DF time series derived from real-life event logs, we compare zero-shot use of TSFMs, without additional training, with fine-tuned variants adapted on PMF-specific data. TSFMs generally achieve lower forecasting errors (MAE and RMSE) than traditional and specialized models trained from scratch on the same logs, indicating effective transfer of temporal structure from non-process domains. While fine-tuning can further improve accuracy, the gains are often small and may disappear on smaller or more complex datasets, so zero-shot use remains a strong default. Our study highlights the generalization capability and data efficiency of TSFMs for process-related time series and, to the best of our knowledge, provides the first systematic evaluation of temporal foundation models for PMF.

