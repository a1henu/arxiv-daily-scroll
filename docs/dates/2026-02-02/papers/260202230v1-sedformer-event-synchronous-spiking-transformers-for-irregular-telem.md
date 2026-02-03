---
layout: default
title: SEDformer: Event-Synchronous Spiking Transformers for Irregular Telemetry Time Series Forecasting
---

# SEDformer: Event-Synchronous Spiking Transformers for Irregular Telemetry Time Series Forecasting
**arXiv**：[2602.02230v1](https://arxiv.org/abs/2602.02230) · [PDF](https://arxiv.org/pdf/2602.02230.pdf)  
**作者**：Ziyu Zhou, Yuchen Fang, Weilin Ruan, Shiyu Wang, James Kwok, Yuxuan Liang  

**一句话要点**：提出SEDformer以解决不规则遥测时间序列预测中的稀疏-事件二重性问题

**关键词**：不规则时间序列预测, 脉冲神经网络, 稀疏-事件二重性, 遥测数据, 事件驱动计算, Transformer模型

## 3 点简述
- 核心问题：不规则遥测时间序列存在稀疏-事件二重性，现有方法因填充或关系重构而忽略此特性。
- 方法要点：基于脉冲神经网络的SEDformer，通过事件对齐编码、事件保留下采样和脉冲Transformer块实现自然建模。
- 实验或效果：在公开数据集上达到最先进预测精度，同时降低能耗和内存使用。

## 摘要（原文）

> Telemetry streams from large-scale Internet-connected systems (e.g., IoT deployments and online platforms) naturally form an irregular multivariate time series (IMTS) whose accurate forecasting is operationally vital. A closer examination reveals a defining Sparsity-Event Duality (SED) property of IMTS, i.e., long stretches with sparse or no observations are punctuated by short, dense bursts where most semantic events (observations) occur. However, existing Graph- and Transformer-based forecasters ignore SED: pre-alignment to uniform grids with heavy padding violates sparsity by inflating sequences and forcing computation at non-informative steps, while relational recasting weakens event semantics by disrupting local temporal continuity. These limitations motivate a more faithful and natural modeling paradigm for IMTS that aligns with its SED property. We find that Spiking Neural Networks meet this requirement, as they communicate via sparse binary spikes and update in an event-driven manner, aligning naturally with the SED nature of IMTS. Therefore, we present SEDformer, an SED-enhanced Spiking Transformer for telemetry IMTS forecasting that couples: (1) a SED-based Spike Encoder converts raw observations into event synchronous spikes using an Event-Aligned LIF neuron, (2) an Event-Preserving Temporal Downsampling module compresses long gaps while retaining salient firings and (3) a stack of SED-based Spike Transformer blocks enable intra-series dependency modeling with a membrane-based linear attention driven by EA-LIF spiking features. Experiments on public telemetry IMTS datasets show that SEDformer attains state-of-the-art forecasting accuracy while reducing energy and memory usage, providing a natural and efficient path for modeling IMTS.

