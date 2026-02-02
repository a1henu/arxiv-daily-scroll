---
layout: default
title: PEFT-MuTS: A Multivariate Parameter-Efficient Fine-Tuning Framework for Remaining Useful Life Prediction based on Cross-domain Time Series Representation Model
---

# PEFT-MuTS: A Multivariate Parameter-Efficient Fine-Tuning Framework for Remaining Useful Life Prediction based on Cross-domain Time Series Representation Model
**arXiv**：[2601.22631v1](https://arxiv.org/abs/2601.22631) · [PDF](https://arxiv.org/pdf/2601.22631.pdf)  
**作者**：En Fu, Yanyan Hu, Changhua Hu, Zengwang Jin, Kaixiang Peng  

**一句话要点**：提出PEFT-MuTS框架，基于跨域预训练时间序列模型，实现少样本剩余寿命预测。

**关键词**：剩余寿命预测, 参数高效微调, 跨域时间序列, 少样本学习, 多元融合

## 3 点简述
- 核心问题：数据驱动的剩余寿命预测受限于大量退化数据获取，现有方法依赖相似设备历史数据。
- 方法要点：开发独立特征调优网络和基于元变量的低秩多元融合机制，利用跨域预训练模型处理多元关系。
- 实验或效果：在航空发动机和工业轴承数据集上，使用少于1%目标样本实现有效预测，优于传统方法。

## 摘要（原文）

> The application of data-driven remaining useful life (RUL) prediction has long been constrained by the availability of large amount of degradation data. Mainstream solutions such as domain adaptation and meta-learning still rely on large amounts of historical degradation data from equipment that is identical or similar to the target, which imposes significant limitations in practical applications. This study investigates PEFT-MuTS, a Parameter-Efficient Fine-Tuning framework for few-shot RUL prediction, built on cross-domain pre-trained time-series representation models. Contrary to the widely held view that knowledge transfer in RUL prediction can only occur within similar devices, we demonstrate that substantial benefits can be achieved through pre-training process with large-scale cross-domain time series datasets. A independent feature tuning network and a meta-variable-based low rank multivariate fusion mechanism are developed to enable the pre-trained univariate time-series representation backbone model to fully exploit the multivariate relationships in degradation data for downstream RUL prediction task. Additionally, we introduce a zero-initialized regressor that stabilizes the fine-tuning process under few-shot conditions. Experiments on aero-engine and industrial bearing datasets demonstrate that our method can achieve effective RUL prediction even when less than 1\% of samples of target equipment are used. Meanwhile, it substantially outperforms conventional supervised and few-shot approaches while markedly reducing the data required to achieve high predictive accuracy. Our code is available at https://github.com/fuen1590/PEFT-MuTS.

