---
layout: default
title: Hierarchical Persistence Velocity for Network Anomaly Detection: Theory and Applications to Cryptocurrency Markets
---

# Hierarchical Persistence Velocity for Network Anomaly Detection: Theory and Applications to Cryptocurrency Markets
**arXiv**：[2512.14615v1](https://arxiv.org/abs/2512.14615) · [PDF](https://arxiv.org/pdf/2512.14615.pdf)  
**作者**：Omid Khormali  

**一句话要点**：提出基于拓扑速度的异常检测方法OW-HNPV，应用于加密货币市场预测

**关键词**：拓扑数据分析, 网络异常检测, 持久图速度, 加密货币市场, 动态网络

## 3 点简述
- 核心问题：现有方法基于累积拓扑特征，难以有效检测时变网络中的结构异常。
- 方法要点：引入首个基于持久图速度的视角，通过重叠加权自动降噪，并证明数学稳定性。
- 实验或效果：在以太坊交易网络中，OW-HNPV在7天价格预测上AUC提升达10.4%，优于基线模型。

## 摘要（原文）

> We introduce the Overlap-Weighted Hierarchical Normalized Persistence Velocity (OW-HNPV), a novel topological data analysis method for detecting anomalies in time-varying networks. Unlike existing methods that measure cumulative topological presence, we introduce the first velocity-based perspective on persistence diagrams, measuring the rate at which features appear and disappear, automatically downweighting noise through overlap-based weighting. We also prove that OW-HNPV is mathematically stable. It behaves in a controlled, predictable way, even when comparing persistence diagrams from networks with different feature types. Applied to Ethereum transaction networks (May 2017-May 2018), OW-HNPV demonstrates superior performance for cryptocurrency anomaly detection, achieving up to 10.4% AUC gain over baseline models for 7-day price movement predictions. Compared with established methods, including Vector of Averaged Bettis (VAB), persistence landscapes, and persistence images, velocity-based summaries excel at medium- to long-range forecasting (4-7 days), with OW-HNPV providing the most consistent and stable performance across prediction horizons. Our results show that modeling topological velocity is crucial for detecting structural anomalies in dynamic networks.

