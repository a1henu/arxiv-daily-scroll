---
layout: default
title: A Behaviour-Aware Federated Forecasting Framework for Distributed Stand-Alone Wind Turbines
---

# A Behaviour-Aware Federated Forecasting Framework for Distributed Stand-Alone Wind Turbines
**arXiv**：[2603.05263v1](https://arxiv.org/abs/2603.05263) · [PDF](https://arxiv.org/pdf/2603.05263.pdf)  
**作者**：Bowen Li, Xiufeng Liu, Maria Sinziiana Astefanoaei  

**一句话要点**：提出行为感知联邦学习框架，通过聚类和FedAvg提升分布式独立风力涡轮机的短期功率预测准确性。

**关键词**：联邦学习, 风电预测, 行为聚类, LSTM模型, 数据隐私, 分布式系统

## 3 点简述
- 核心问题：集中化涡轮数据存在隐私、成本和异质性挑战，影响短期风电预测精度。
- 方法要点：采用两阶段联邦学习，先基于长期行为统计聚类涡轮，再训练集群特定LSTM模型。
- 实验或效果：在丹麦400台涡轮上验证，行为感知分组优于地理分区，匹配k-means++基准，保护数据本地性。

## 摘要（原文）

> Accurate short-term wind power forecasting is essential for grid dispatch and market operations, yet centralising turbine data raises privacy, cost, and heterogeneity concerns. We propose a two-stage federated learning framework that first clusters turbines by long-term behavioural statistics using Double Roulette Selection (DRS) initialisation with recursive Auto-split refinement, and then trains cluster-specific LSTM models via FedAvg. Experiments on 400 stand-alone turbines in Denmark show that DRS-auto discovers behaviourally coherent groups and achieves competitive forecasting accuracy while preserving data locality. Behaviour-aware grouping consistently outperforms geographic partitioning and matches strong k-means++ baselines, suggesting a practical privacy-friendly solution for heterogeneous distributed turbine fleets.

