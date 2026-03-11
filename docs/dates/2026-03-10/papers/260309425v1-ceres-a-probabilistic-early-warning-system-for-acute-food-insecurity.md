---
layout: default
title: CERES: A Probabilistic Early Warning System for Acute Food Insecurity
---

# CERES: A Probabilistic Early Warning System for Acute Food Insecurity
**arXiv**：[2603.09425v1](https://arxiv.org/abs/2603.09425) · [PDF](https://arxiv.org/pdf/2603.09425.pdf)  
**作者**：Tom Danny S. Pedersen  

**一句话要点**：提出CERES概率预警系统，用于预测全球高风险国家的急性粮食不安全状况。

**关键词**：概率预测, 粮食安全预警, 数据融合, 逻辑回归模型, 公开验证

## 3 点简述
- 核心问题：预测急性粮食不安全，如危机、紧急和饥荒阶段，以提供早期预警。
- 方法要点：融合降水异常、植被指数、冲突事件等六类数据，通过逻辑评分模型生成90天概率估计。
- 实验或效果：历史回验中，对四个选定事件均给出TIER-1分类，但仅为样本内检查，非前瞻性能声明。

## 摘要（原文）

> We present CERES (Calibrated Early-warning and Risk Estimation System), an automated probabilistic forecasting system for acute food insecurity. CERES generates 90-day ahead probability estimates of IPC Phase 3+ (Crisis), Phase 4+ (Emergency), and Phase 5 (Famine) conditions for 43 high-risk countries globally, updated weekly. The system fuses six data streams, precipitation anomalies (CHIRPS), vegetation indices (MODIS NDVI), conflict events (ACLED), IPC classifications, food consumption scores (WFP), and cereal price indices (FAO/WFP) - through a logistic scoring model with author-specified initial coefficients and parametric input-perturbation intervals (n=2,000 draws). In historical back-validation against four IPC Phase 4-5 events selected for data completeness, CERES assigned TIER-1 classification in all four cases; these are in-sample sanity checks only, not prospective performance claims. All prospective predictions are timestamped, cryptographically identified, and archived for public verification against IPC outcome data at the T+90 horizon. To the author's knowledge, CERES is the first famine early warning system that is simultaneously: (1) probabilistic, (2) open-access, (3) continuously running, (4) machine-readable at prediction level, and (5) committed to public prospective verification of every prediction made.

