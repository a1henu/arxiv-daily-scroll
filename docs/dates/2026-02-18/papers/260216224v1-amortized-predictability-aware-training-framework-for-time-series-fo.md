---
layout: default
title: Amortized Predictability-aware Training Framework for Time Series Forecasting and Classification
---

# Amortized Predictability-aware Training Framework for Time Series Forecasting and Classification
**arXiv**：[2602.16224v1](https://arxiv.org/abs/2602.16224) · [PDF](https://arxiv.org/pdf/2602.16224.pdf)  
**作者**：Xu Zhang, Peng Wang, Yichen Li, Wei Wang  

**一句话要点**：提出APTF框架以解决时间序列预测和分类中低可预测性样本的负面影响

**关键词**：时间序列预测, 时间序列分类, 可预测性感知训练, 分层损失, 摊销模型, 深度学习框架

## 3 点简述
- 核心问题：时间序列数据常含低可预测性样本，导致训练不稳定或收敛至差局部最优
- 方法要点：引入分层可预测性感知损失和摊销模型，动态识别并惩罚低可预测性样本
- 实验或效果：未知，但代码已开源，旨在提升模型性能

## 摘要（原文）

> Time series data are prone to noise in various domains, and training samples may contain low-predictability patterns that deviate from the normal data distribution, leading to training instability or convergence to poor local minima. Therefore, mitigating the adverse effects of low-predictability samples is crucial for time series analysis tasks such as time series forecasting (TSF) and time series classification (TSC). While many deep learning models have achieved promising performance, few consider how to identify and penalize low-predictability samples to improve model performance from the training perspective. To fill this gap, we propose a general Amortized Predictability-aware Training Framework (APTF) for both TSF and TSC. APTF introduces two key designs that enable the model to focus on high-predictability samples while still learning appropriately from low-predictability ones: (i) a Hierarchical Predictability-aware Loss (HPL) that dynamically identifies low-predictability samples and progressively expands their loss penalty as training evolves, and (ii) an amortization model that mitigates predictability estimation errors caused by model bias, further enhancing HPL's effectiveness. The code is available at https://github.com/Meteor-Stars/APTF.

