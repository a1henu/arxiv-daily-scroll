---
layout: default
title: Ensemble-size-dependence of deep-learning post-processing methods that minimize an (un)fair score: motivating examples and a proof-of-concept solution
---

# Ensemble-size-dependence of deep-learning post-processing methods that minimize an (un)fair score: motivating examples and a proof-of-concept solution
**arXiv**：[2602.15830v1](https://arxiv.org/abs/2602.15830) · [PDF](https://arxiv.org/pdf/2602.15830.pdf)  
**作者**：Christopher David Roberts  

**一句话要点**：提出轨迹变换器以解决深度学习后处理方法在最小化公平分数时对集合大小的依赖问题

**关键词**：集合预报后处理, 公平分数, 深度学习, 变换器, 集合大小依赖性, 条件独立性

## 3 点简述
- 公平分数如aCRPS在集合成员可交换时独立于集合大小，但依赖结构的方法可能违反此假设
- 线性逐成员校准和基于变换器的方法因成员耦合导致集合大小敏感性和系统不可靠性
- 轨迹变换器通过沿时间维自注意力保持条件独立性，在ECMWF次季节预报中改善偏差和可靠性

## 摘要（原文）

> Fair scores reward ensemble forecast members that behave like samples from the same distribution as the verifying observations. They are therefore an attractive choice as loss functions to train data-driven ensemble forecasts or post-processing methods when large training ensembles are either unavailable or computationally prohibitive. The adjusted continuous ranked probability score (aCRPS) is fair and unbiased with respect to ensemble size, provided forecast members are exchangeable and interpretable as conditionally independent draws from an underlying predictive distribution. However, distribution-aware post-processing methods that introduce structural dependency between members can violate this assumption, rendering aCRPS unfair. We demonstrate this effect using two approaches designed to minimize the expected aCRPS of a finite ensemble: (1) a linear member-by-member calibration, which couples members through a common dependency on the sample ensemble mean, and (2) a deep-learning method, which couples members via transformer self-attention across the ensemble dimension. In both cases, the results are sensitive to ensemble size and apparent gains in aCRPS can correspond to systematic unreliability characterized by over-dispersion. We introduce trajectory transformers as a proof-of-concept that ensemble-size independence can be achieved. This approach is an adaptation of the Post-processing Ensembles with Transformers (PoET) framework and applies self-attention over lead time while preserving the conditional independence required by aCRPS. When applied to weekly mean $T_{2m}$ forecasts from the ECMWF subseasonal forecasting system, this approach successfully reduces systematic model biases whilst also improving or maintaining forecast reliability regardless of the ensemble size used in training (3 vs 9 members) or real-time forecasts (9 vs 100 members).

