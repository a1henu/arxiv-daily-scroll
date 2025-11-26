---
layout: default
title: Zero-Shot Transfer Capabilities of the Sundial Foundation Model for Leaf Area Index Forecasting
---

# Zero-Shot Transfer Capabilities of the Sundial Foundation Model for Leaf Area Index Forecasting
**arXiv**：[2511.20004v1](https://arxiv.org/abs/2511.20004) · [PDF](https://arxiv.org/pdf/2511.20004.pdf)  
**作者**：Peining Zhang, Hongchen Qin, Haochen Zhang, Ziqi Guo, Guiling Wang, Jinbo Bi  

**一句话要点**：探索Sundial基础模型在叶面积指数预测中的零样本迁移能力

**关键词**：叶面积指数预测, 零样本学习, 时间序列基础模型, 农业监测, 远程感知

## 3 点简述
- 核心问题：评估时间序列基础模型在农业监测中零样本预测叶面积指数的能力。
- 方法要点：使用HiQ数据集，比较统计基线、全监督LSTM和Sundial模型。
- 实验或效果：Sundial在长输入窗口下零样本超越全监督LSTM，无需任务特定调优。

## 摘要（原文）

> This work investigates the zero-shot forecasting capability of time-series foundation models for Leaf Area Index (LAI) forecasting in agricultural monitoring. Using the HiQ dataset (U.S., 2000-2022), we systematically compare statistical baselines, a fully supervised LSTM, and the Sundial foundation model under multiple evaluation protocols. We find that Sundial, in the zero-shot setting, can outperform a fully trained LSTM provided that the input context window is sufficiently long-specifically, when covering more than one or two full seasonal cycles. This demonstrates, for the first time, that a general-purpose foundation model can surpass specialized supervised models on remote-sensing time series prediction without any task-specific tuning. These results highlight the strong potential of pretrained time-series foundation models to serve as effective plug-and-play forecasters in agricultural and environmental applications.

