---
layout: default
title: KANFormer for Predicting Fill Probabilities via Survival Analysis in Limit Order Books
---

# KANFormer for Predicting Fill Probabilities via Survival Analysis in Limit Order Books
**arXiv**：[2512.05734v1](https://arxiv.org/abs/2512.05734) · [PDF](https://arxiv.org/pdf/2512.05734.pdf)  
**作者**：Jinfeng Zhong, Emmanuel Bacry, Agathe Guilloux, Jean-François Muzy  

**一句话要点**：提出KANFormer模型，结合市场与代理信息预测限价订单成交时间，提升填充概率预测准确性。

**关键词**：限价订单簿预测, 生存分析, 深度学习模型, 特征重要性分析, 时间序列预测

## 3 点简述
- 核心问题：现有模型仅依赖限价订单簿快照，难以有效预测订单成交时间与概率。
- 方法要点：结合扩张因果卷积网络与Transformer编码器，引入Kolmogorov-Arnold网络增强非线性近似能力。
- 实验或效果：在CAC 40指数期货数据上，校准与判别指标优于现有工作，并通过SHAP分析特征重要性。

## 摘要（原文）

> This paper introduces KANFormer, a novel deep-learning-based model for predicting the time-to-fill of limit orders by leveraging both market- and agent-level information. KANFormer combines a Dilated Causal Convolutional network with a Transformer encoder, enhanced by Kolmogorov-Arnold Networks (KANs), which improve nonlinear approximation. Unlike existing models that rely solely on a series of snapshots of the limit order book, KANFormer integrates the actions of agents related to LOB dynamics and the position of the order in the queue to more effectively capture patterns related to execution likelihood. We evaluate the model using CAC 40 index futures data with labeled orders. The results show that KANFormer outperforms existing works in both calibration (Right-Censored Log-Likelihood, Integrated Brier Score) and discrimination (C-index, time-dependent AUC). We further analyze feature importance over time using SHAP (SHapley Additive exPlanations). Our results highlight the benefits of combining rich market signals with expressive neural architectures to achieve accurate and interpretabl predictions of fill probabilities.

