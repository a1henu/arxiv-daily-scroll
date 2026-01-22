---
layout: default
title: Calibrated uncertainty quantification for prosumer flexibility aggregation in ancillary service markets
---

# Calibrated uncertainty quantification for prosumer flexibility aggregation in ancillary service markets
**arXiv**：[2601.14663v1](https://arxiv.org/abs/2601.14663) · [PDF](https://arxiv.org/pdf/2601.14663.pdf)  
**作者**：Yogesh Pipada Sunil Kumar, S. Ali Pourmousavi, Jon A. R. Liisberg, Julian Lesmos-Vinasco  

**一句话要点**：提出集成蒙特卡洛丢弃与保形预测的框架，以解决聚合商在辅助服务市场中灵活性预测的不确定性校准问题。

**关键词**：不确定性量化, 保形预测, 蒙特卡洛丢弃, 需求响应聚合, 辅助服务市场, 机器学习代理模型

## 3 点简述
- 核心问题：聚合商在频率控制辅助服务市场中面临灵活性预测的认知不确定性，需满足P90可靠性标准。
- 方法要点：结合蒙特卡洛丢弃与保形预测，生成校准的有限样本预测区间，适用于大规模数据集。
- 实验或效果：在丹麦市场应用中，该框架减少过度投标风险，实现合规利润，优于传统方法。

## 摘要（原文）

> Reliable forecasting of prosumer flexibility is critical for demand response aggregators participating in frequency controlled ancillary services market, where strict reliability requirements such as the P90 standard are enforced. Limited historical data, dependence on exogeneous factors, and heterogenous prosumer behaviour introduce significant epistemic uncertainty, making deterministic or poorly calibrated probabilistic models unsuitable for market bidding. This paper proposes the use of scalable uncertainty quantification framework that integrates Monte Carlo dropout (MCD) with conformal prediction (CP) to produce calibrated, finite sample prediction intervals for aggregated prosumer flexibility. The proposed framework is applied to a behind-the-meter aggregator participating in the Danish manual frequency restoration reserve capacity market. A large-scale synthetic dataset is generated using a modified industry-grade home energy management system, combined with publicly available load, solar, price, activation and device-level data. The resulting machine learning surrogate model captures aggregate prosumer price responsiveness and provides uncertainty-aware estimates suitable for market bidding. Multiple multivariate CP strategies are evaluated and benchmarked against conventional MCD-based methods. Results show that standalone MCD systematically overestimates available flexibility and violates P90 compliance, whereas the proposed MCD-CP framework achieves reliable coverage with controlled conservatism. When embedded in aggregator bidding model, conformalised methods substantially reduce overbidding risk and achieve upto 70% of perfect-information profit while satisfying regulatory reliability constraints, providing practical, computationally efficient, and market-compliant solution for aggregator flexibility forecasting under uncertainty.

