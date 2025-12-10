---
layout: default
title: Explainable Anomaly Detection for Industrial IoT Data Streams
---

# Explainable Anomaly Detection for Industrial IoT Data Streams
**arXiv**：[2512.08885v1](https://arxiv.org/abs/2512.08885) · [PDF](https://arxiv.org/pdf/2512.08885.pdf)  
**作者**：Ana Rita Paupério, Diogo Risca, Afonso Lourenço, Goreti Marreiros, Ricardo Martins  

**一句话要点**：提出协作数据流挖掘框架，集成无监督异常检测与交互式人机学习以支持工业物联网维护决策。

**关键词**：工业物联网, 数据流挖掘, 异常检测, 可解释性, 人机交互学习, 在线隔离森林

## 3 点简述
- 核心问题：工业物联网数据流中，真实标签常延迟或缺失，需实时自适应决策。
- 方法要点：使用在线隔离森林进行异常检测，增强可解释性通过增量部分依赖图和特征重要性评分。
- 实验或效果：在提花织机单元进行故障检测，提供初步结果，目标持续监测预测轴承故障。

## 摘要（原文）

> Industrial maintenance is being transformed by the Internet of Things and edge computing, generating continuous data streams that demand real-time, adaptive decision-making under limited computational resources. While data stream mining (DSM) addresses this challenge, most methods assume fully supervised settings, yet in practice, ground-truth labels are often delayed or unavailable. This paper presents a collaborative DSM framework that integrates unsupervised anomaly detection with interactive, human-in-the-loop learning to support maintenance decisions. We employ an online Isolation Forest and enhance interpretability using incremental Partial Dependence Plots and a feature importance score, derived from deviations of Individual Conditional Expectation curves from a fading average, enabling users to dynamically reassess feature relevance and adjust anomaly thresholds. We describe the real-time implementation and provide initial results for fault detection in a Jacquard loom unit. Ongoing work targets continuous monitoring to predict and explain imminent bearing failures.

