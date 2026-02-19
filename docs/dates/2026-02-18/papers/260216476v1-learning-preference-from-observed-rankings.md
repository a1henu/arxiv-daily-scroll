---
layout: default
title: Learning Preference from Observed Rankings
---

# Learning Preference from Observed Rankings
**arXiv**：[2602.16476v1](https://arxiv.org/abs/2602.16476) · [PDF](https://arxiv.org/pdf/2602.16476.pdf)  
**作者**：Yu-Chang Chen, Chen Chian Fuh, Shang En Tsai  

**一句话要点**：提出基于部分排序的偏好学习框架，通过逆概率加权校正曝光偏差，提升推荐性能。

**关键词**：偏好学习, 排序数据, 曝光偏差校正, 逆概率加权, 推荐系统, 随机梯度下降

## 3 点简述
- 核心问题：从部分排序数据估计消费者偏好，存在曝光偏差影响准确性。
- 方法要点：结合可解释属性、固定效应和低秩因子结构，用IPW加权和SGD优化估计。
- 实验或效果：在线葡萄酒交易数据中，相比流行度基准，提升未消费产品购买预测效果。

## 摘要（原文）

> Estimating consumer preferences is central to many problems in economics and marketing. This paper develops a flexible framework for learning individual preferences from partial ranking information by interpreting observed rankings as collections of pairwise comparisons with logistic choice probabilities. We model latent utility as the sum of interpretable product attributes, item fixed effects, and a low-rank user-item factor structure, enabling both interpretability and information sharing across consumers and items. We further correct for selection in which comparisons are observed: a comparison is recorded only if both items enter the consumer's consideration set, inducing exposure bias toward frequently encountered items. We model pair observability as the product of item-level observability propensities and estimate these propensities with a logistic model for the marginal probability that an item is observable. Preference parameters are then estimated by maximizing an inverse-probability-weighted (IPW), ridge-regularized log-likelihood that reweights observed comparisons toward a target comparison population. To scale computation, we propose a stochastic gradient descent (SGD) algorithm based on inverse-probability resampling, which draws comparisons in proportion to their IPW weights. In an application to transaction data from an online wine retailer, the method improves out-of-sample recommendation performance relative to a popularity-based benchmark, with particularly strong gains in predicting purchases of previously unconsumed products.

