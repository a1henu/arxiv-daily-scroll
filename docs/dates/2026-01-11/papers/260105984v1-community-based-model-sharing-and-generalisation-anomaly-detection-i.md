---
layout: default
title: Community-Based Model Sharing and Generalisation: Anomaly Detection in IoT Temperature Sensor Networks
---

# Community-Based Model Sharing and Generalisation: Anomaly Detection in IoT Temperature Sensor Networks
**arXiv**：[2601.05984v1](https://arxiv.org/abs/2601.05984) · [PDF](https://arxiv.org/pdf/2601.05984.pdf)  
**作者**：Sahibzada Saadoon Hammad, Joaquín Huerta Guijarro, Francisco Ramos, Michael Gould Carlson, Sergio Trilles Oliver  

**一句话要点**：提出基于兴趣社区的异常检测框架，以降低物联网温度传感器网络的计算开销并分析模型泛化性。

**关键词**：物联网传感器网络, 异常检测, 兴趣社区, 自编码器, 贝叶斯优化, 模型泛化

## 3 点简述
- 核心问题：物联网传感器网络规模大且异构，异常检测面临计算和泛化挑战。
- 方法要点：通过融合相似性矩阵分组传感器社区，使用自编码器和贝叶斯优化训练模型。
- 实验或效果：实验显示社区内性能稳健，社区间存在差异，支持模型共享以减少计算开销。

## 摘要（原文）

> The rapid deployment of Internet of Things (IoT) devices has led to large-scale sensor networks that monitor environmental and urban phenomena in real time. Communities of Interest (CoIs) provide a promising paradigm for organising heterogeneous IoT sensor networks by grouping devices with similar operational and environmental characteristics. This work presents an anomaly detection framework based on the CoI paradigm by grouping sensors into communities using a fused similarity matrix that incorporates temporal correlations via Spearman coefficients, spatial proximity using Gaussian distance decay, and elevation similarities. For each community, representative stations based on the best silhouette are selected and three autoencoder architectures (BiLSTM, LSTM, and MLP) are trained using Bayesian hyperparameter optimization with expanding window cross-validation and tested on stations from the same cluster and the best representative stations of other clusters. The models are trained on normal temperature patterns of the data and anomalies are detected through reconstruction error analysis. Experimental results show a robust within-community performance across the evaluated configurations, while variations across communities are observed. Overall, the results support the applicability of community-based model sharing in reducing computational overhead and to analyse model generalisability across IoT sensor networks.

