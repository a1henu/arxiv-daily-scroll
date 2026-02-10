---
layout: default
title: Low Rank Transformer for Multivariate Time Series Anomaly Detection and Localization
---

# Low Rank Transformer for Multivariate Time Series Anomaly Detection and Localization
**arXiv**：[2602.08467v1](https://arxiv.org/abs/2602.08467) · [PDF](https://arxiv.org/pdf/2602.08467.pdf)  
**作者**：Charalampos Shimillas, Kleanthis Malialis, Konstantinos Fokianos, Marios M. Polycarpou  

**一句话要点**：提出ALoRa-T模型与ALoRa-Loc方法，用于多元时间序列异常检测与定位

**关键词**：多元时间序列, 异常检测, 异常定位, Transformer, 低秩正则化, 自注意力

## 3 点简述
- 核心问题：多元时间序列异常诊断缺乏理论洞察，尤其是定位任务未充分探索
- 方法要点：基于Transformer与统计时间序列理论，引入低秩正则化自注意力及关联量化
- 实验或效果：在检测和定位任务中显著优于现有方法，经广泛实验验证

## 摘要（原文）

> Multivariate time series (MTS) anomaly diagnosis, which encompasses both anomaly detection and localization, is critical for the safety and reliability of complex, large-scale real-world systems. The vast majority of existing anomaly diagnosis methods offer limited theoretical insights, especially for anomaly localization, which is a vital but largely unexplored area. The aim of this contribution is to study the learning process of a Transformer when applied to MTS by revealing connections to statistical time series methods. Based on these theoretical insights, we propose the Attention Low-Rank Transformer (ALoRa-T) model, which applies low-rank regularization to self-attention, and we introduce the Attention Low-Rank score, effectively capturing the temporal characteristics of anomalies. Finally, to enable anomaly localization, we propose the ALoRa-Loc method, a novel approach that associates anomalies to specific variables by quantifying interrelationships among time series. Extensive experiments and real data analysis, show that the proposed methodology significantly outperforms state-of-the-art methods in both detection and localization tasks.

