---
layout: default
title: TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation
---

# TiCard: Deployable EXPLAIN-only Residual Learning for Cardinality Estimation
**arXiv**：[2512.14358v1](https://arxiv.org/abs/2512.14358) · [PDF](https://arxiv.org/pdf/2512.14358.pdf)  
**作者**：Qizhi Wang  

**一句话要点**：提出TiCard框架，通过残差学习增强数据库原生基数估计器，提升部署性。

**关键词**：基数估计, 残差学习, 查询优化, 部署性增强, 梯度提升回归, TabPFN模型

## 3 点简述
- 核心问题：基数估计是查询优化的瓶颈，传统方法忽略相关性，学习型方法部署困难。
- 方法要点：基于EXPLAIN-only特征学习乘法残差校正，低侵入性增强而非替换原生估计器。
- 实验效果：在TiDB上，TiCard显著降低尾部误差，如P90 Q-error从312.85降至13.69。

## 摘要（原文）

> Cardinality estimation is a key bottleneck for cost-based query optimization, yet deployable improvements remain difficult: classical estimators miss correlations, while learned estimators often require workload-specific training pipelines and invasive integration into the optimizer. This paper presents TiCard, a low intrusion, correction-based framework that augments (rather than replaces) a database's native estimator. TiCard learns multiplicative residual corrections using EXPLAIN-only features, and uses EXPLAIN ANALYZE only for offline labels. We study two practical instantiations: (i) a Gradient Boosting Regressor for sub-millisecond inference, and (ii) TabPFN, an in-context tabular foundation model that adapts by refreshing a small reference set without gradient retraining. On TiDB with TPCH and the Join Order Benchmark, in a low-trace setting (263 executions total; 157 used for learning), TiCard improves operator-level tail accuracy substantially: P90 Q-error drops from 312.85 (native) to 13.69 (TiCard-GBR), and P99 drops from 37,974.37 to 3,416.50 (TiCard-TabPFN), while a join-only policy preserves near-perfect median behavior. We position TiCard as an AI4DB building block focused on deployability: explicit scope, conservative integration policies, and an integration roadmap from offline correction to in-optimizer use.

