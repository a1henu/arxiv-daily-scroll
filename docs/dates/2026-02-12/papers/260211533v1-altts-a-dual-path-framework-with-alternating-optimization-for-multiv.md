---
layout: default
title: AltTS: A Dual-Path Framework with Alternating Optimization for Multivariate Time Series Forecasting
---

# AltTS: A Dual-Path Framework with Alternating Optimization for Multivariate Time Series Forecasting
**arXiv**：[2602.11533v1](https://arxiv.org/abs/2602.11533) · [PDF](https://arxiv.org/pdf/2602.11533.pdf)  
**作者**：Zhihang Yuan, Zhiyuan Liu, Mahesh K. Marina  

**一句话要点**：提出AltTS双路径框架，通过交替优化解决多变量时间序列预测中的优化冲突问题。

**关键词**：多变量时间序列预测, 双路径框架, 交替优化, 自回归建模, 跨关系建模, 长时预测

## 3 点简述
- 核心问题：单模型同时捕捉自回归动态和跨维度交互导致优化冲突，影响长时预测精度。
- 方法要点：采用双路径设计，线性预测器处理自回归，Transformer处理跨关系，通过交替优化隔离梯度噪声。
- 实验或效果：在多个基准测试中表现优于现有方法，长时预测改进尤为显著。

## 摘要（原文）

> Multivariate time series forecasting involves two qualitatively distinct factors: (i) stable within-series autoregressive (AR) dynamics, and (ii) intermittent cross-dimension interactions that can become spurious over long horizons. We argue that fitting a single model to capture both effects creates an optimization conflict: the high-variance updates needed for cross-dimension modeling can corrupt the gradients that support autoregression, resulting in brittle training and degraded long-horizon accuracy. To address this, we propose ALTTS, a dual-path framework that explicitly decouples autoregression and cross-relation (CR) modeling. In ALTTS, the AR path is instantiated with a linear predictor, while the CR path uses a Transformer equipped with Cross-Relation Self-Attention (CRSA); the two branches are coordinated via alternating optimization to isolate gradient noise and reduce cross-block interference. Extensive experiments on multiple benchmarks show that ALTTS consistently outperforms prior methods, with the most pronounced improvements on long-horizon forecasting. Overall, our results suggest that carefully designed optimization strategies, rather than ever more complex architectures, can be a key driver of progress in multivariate time series forecasting.

