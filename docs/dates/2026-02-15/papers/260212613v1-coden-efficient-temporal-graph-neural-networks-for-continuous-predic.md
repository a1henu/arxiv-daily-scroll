---
layout: default
title: Coden: Efficient Temporal Graph Neural Networks for Continuous Prediction
---

# Coden: Efficient Temporal Graph Neural Networks for Continuous Prediction
**arXiv**：[2602.12613v1](https://arxiv.org/abs/2602.12613) · [PDF](https://arxiv.org/pdf/2602.12613.pdf)  
**作者**：Zulun Zhu, Siqiang Luo  

**一句话要点**：提出Coden模型以高效处理动态图中的连续预测问题

**关键词**：时序图神经网络, 连续预测, 动态图处理, 效率优化, 理论分析

## 3 点简述
- 现有TGNNs主要针对一次性预测，连续预测场景下存在计算开销大或预测质量低的问题
- Coden通过创新方法克服复杂度瓶颈，在保持预测准确性的同时提升效率
- 在五个动态数据集上的评估显示，Coden在效率和效果上均超越现有基准

## 摘要（原文）

> Temporal Graph Neural Networks (TGNNs) are pivotal in processing dynamic graphs. However, existing TGNNs primarily target one-time predictions for a given temporal span, whereas many practical applications require continuous predictions, that predictions are issued frequently over time. Directly adapting existing TGNNs to continuous-prediction scenarios introduces either significant computational overhead or prediction quality issues especially for large graphs. This paper revisits the challenge of { continuous predictions} in TGNNs, and introduces {\sc Coden}, a TGNN model designed for efficient and effective learning on dynamic graphs. {\sc Coden} innovatively overcomes the key complexity bottleneck in existing TGNNs while preserving comparable predictive accuracy. Moreover, we further provide theoretical analyses that substantiate the effectiveness and efficiency of {\sc Coden}, and clarify its duality relationship with both RNN-based and attention-based models. Our evaluations across five dynamic datasets show that {\sc Coden} surpasses existing performance benchmarks in both efficiency and effectiveness, establishing it as a superior solution for continuous prediction in evolving graph environments.

