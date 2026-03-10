---
layout: default
title: Are We Winning the Wrong Game? Revisiting Evaluation Practices for Long-Term Time Series Forecasting
---

# Are We Winning the Wrong Game? Revisiting Evaluation Practices for Long-Term Time Series Forecasting
**arXiv**：[2603.08156v1](https://arxiv.org/abs/2603.08156) · [PDF](https://arxiv.org/pdf/2603.08156.pdf)  
**作者**：Thanapol Phungtua-eng, Yoshitaka Yamamoto  

**一句话要点**：提出多维度评估框架以解决长时序预测中指标单一化问题

**关键词**：长时序预测, 评估方法, 时间序列分析, 基准测试, 决策支持

## 3 点简述
- 核心问题：当前长时序预测评估过度依赖点误差指标，忽视结构属性和决策支持
- 方法要点：倡导整合统计保真度、结构一致性和决策相关性的多维度评估视角
- 实验或效果：挑战现有基准文化，旨在推动更具意义和上下文感知的预测研究

## 摘要（原文）

> Long-term time series forecasting (LTSF) is widely recognized as a central challenge in data mining and machine learning. LTSF has increasingly evolved into a benchmark-driven ''GAME,'' where models are ranked, compared, and declared state-of-the-art based primarily on marginal reductions in aggregated pointwise error metrics such as MSE and MAE. Across a small set of canonical datasets and fixed forecasting horizons, progress is communicated through leaderboard-style tables in which lower numerical scores define success. In this GAME, what is measured becomes what is optimized, and incremental error reduction becomes the dominant currency of advancement. We argue that this metric-centric regime is not merely incomplete, but structurally misaligned with the broader objectives of forecasting. In real-world settings, forecasting often prioritizes preserving temporal structure, trend stability, seasonal coherence, robustness to regime shifts, and supporting downstream decision processes. Optimizing aggregate pointwise error does not necessarily imply modeling these structural properties. As a result, leaderboard improvement may increasingly reflect specialization in benchmark configurations rather than a deeper understanding of temporal dynamics. This paper revisits LTSF evaluation as a foundational question in data science: what does it mean to measure forecasting progress? We propose a multi-dimensional evaluation perspective that integrates statistical fidelity, structural coherence, and decision-level relevance. By challenging the current metric monoculture, we aim to redirect attention from winning benchmark tables toward advancing meaningful, context-aware forecasting.

