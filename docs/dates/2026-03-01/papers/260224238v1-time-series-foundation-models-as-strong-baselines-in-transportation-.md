---
layout: default
title: Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis
---

# Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis
**arXiv**：[2602.24238v1](https://arxiv.org/abs/2602.24238) · [PDF](https://arxiv.org/pdf/2602.24238.pdf)  
**作者**：Javier Pulido, Filipe Rodrigues  

**一句话要点**：评估时间序列基础模型在交通预测中的零样本性能，作为强基线

**关键词**：时间序列预测, 交通预测, 基础模型, 零样本学习, 概率预测, 基准分析

## 3 点简述
- 核心问题：交通预测需数据集特定训练，通用模型能否替代？
- 方法要点：用Chronos-2模型在10个真实数据集进行零样本基准测试
- 实验或效果：Chronos-2在多数数据集上达到SOTA或竞争性精度，尤其在长时预测

## 摘要（原文）

> Accurate forecasting of transportation dynamics is essential for urban mobility and infrastructure planning. Although recent work has achieved strong performance with deep learning models, these methods typically require dataset-specific training, architecture design and hyper-parameter tuning. This paper evaluates whether general-purpose time-series foundation models can serve as forecasters for transportation tasks by benchmarking the zero-shot performance of the state-of-the-art model, Chronos-2, across ten real-world datasets covering highway traffic volume and flow, urban traffic speed, bike-sharing demand, and electric vehicle charging station data. Under a consistent evaluation protocol, we find that, even without any task-specific fine-tuning, Chronos-2 delivers state-of-the-art or competitive accuracy across most datasets, frequently outperforming classical statistical baselines and specialized deep learning architectures, particularly at longer horizons. Beyond point forecasting, we evaluate its native probabilistic outputs using prediction-interval coverage and sharpness, demonstrating that Chronos-2 also provides useful uncertainty quantification without dataset-specific training. In general, this study supports the adoption of time-series foundation models as a key baseline for transportation forecasting research.

