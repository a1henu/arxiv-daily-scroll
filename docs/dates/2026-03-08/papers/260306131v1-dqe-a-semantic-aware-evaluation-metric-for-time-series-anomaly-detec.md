---
layout: default
title: DQE: A Semantic-Aware Evaluation Metric for Time Series Anomaly Detection
---

# DQE: A Semantic-Aware Evaluation Metric for Time Series Anomaly Detection
**arXiv**：[2603.06131v1](https://arxiv.org/abs/2603.06131) · [PDF](https://arxiv.org/pdf/2603.06131.pdf)  
**作者**：Yuewei Li, Dalin Zhang, Huan Li, Xinyi Gong, Hongjun Chu, Zhaohui Song  

**一句话要点**：提出DQE语义感知评估指标，以解决时间序列异常检测中现有评估指标的局限性。

**关键词**：时间序列异常检测, 评估指标, 语义感知, 阈值聚合, 检测语义分区

## 3 点简述
- 核心问题：现有评估指标存在点级覆盖偏差、近误检测不敏感、误报惩罚不足及阈值选择不一致等问题。
- 方法要点：基于检测语义划分异常局部时间区域为三个功能子区域，设计细粒度评分机制，并聚合全阈值谱检测质量。
- 实验或效果：在合成和真实数据上验证，DQE提供稳定、可区分且可解释的评估，优于十种常用指标。

## 摘要（原文）

> Time series anomaly detection has achieved remarkable progress in recent years. However, evaluation practices have received comparatively less attention, despite their critical importance. Existing metrics exhibit several limitations: (1) bias toward point-level coverage, (2) insensitivity or inconsistency in near-miss detections, (3) inadequate penalization of false alarms, and (4) inconsistency caused by threshold or threshold-interval selection. These limitations can produce unreliable or counterintuitive results, hindering objective progress. In this work, we revisit the evaluation of time series anomaly detection from the perspective of detection semantics and propose a novel metric for more comprehensive assessment. We first introduce a partitioning strategy grounded in detection semantics, which decomposes the local temporal region of each anomaly into three functionally distinct subregions. Using this partitioning, we evaluate overall detection behavior across events and design finer-grained scoring mechanisms for each subregion, enabling more reliable and interpretable assessment. Through a systematic study of existing metrics, we identify an evaluation bias associated with threshold-interval selection and adopt an approach that aggregates detection qualities across the full threshold spectrum, thereby eliminating evaluation inconsistency. Extensive experiments on synthetic and real-world data demonstrate that our metric provides stable, discriminative, and interpretable evaluation, while achieving robust assessment compared with ten widely used metrics.

