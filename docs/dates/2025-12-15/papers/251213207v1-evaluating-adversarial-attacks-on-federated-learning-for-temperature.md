---
layout: default
title: Evaluating Adversarial Attacks on Federated Learning for Temperature Forecasting
---

# Evaluating Adversarial Attacks on Federated Learning for Temperature Forecasting
**arXiv**：[2512.13207v1](https://arxiv.org/abs/2512.13207) · [PDF](https://arxiv.org/pdf/2512.13207.pdf)  
**作者**：Karina Chichifoi, Fabio Merizzi, Michele Colajanni  

**一句话要点**：评估对抗攻击对联邦学习温度预测的影响，揭示空间依赖性放大威胁

**关键词**：联邦学习, 对抗攻击, 温度预测, 数据投毒, 空间依赖性, 防御机制

## 3 点简述
- 研究联邦学习在温度预测中面临的数据投毒攻击，特别是基于空间依赖性的威胁
- 模拟分布式客户端，评估全局偏置和基于补丁的攻击对区域预测的扭曲效果
- 实验显示少量中毒客户端可误导大面积预测，修剪均值聚合防御对全局攻击有效但对补丁攻击失败

## 摘要（原文）

> Deep learning and federated learning (FL) are becoming powerful partners for next-generation weather forecasting. Deep learning enables high-resolution spatiotemporal forecasts that can surpass traditional numerical models, while FL allows institutions in different locations to collaboratively train models without sharing raw data, addressing efficiency and security concerns. While FL has shown promise across heterogeneous regions, its distributed nature introduces new vulnerabilities. In particular, data poisoning attacks, in which compromised clients inject manipulated training data, can degrade performance or introduce systematic biases. These threats are amplified by spatial dependencies in meteorological data, allowing localized perturbations to influence broader regions through global model aggregation. In this study, we investigate how adversarial clients distort federated surface temperature forecasts trained on the Copernicus European Regional ReAnalysis (CERRA) dataset. We simulate geographically distributed clients and evaluate patch-based and global biasing attacks on regional temperature forecasts. Our results show that even a small fraction of poisoned clients can mislead predictions across large, spatially connected areas. A global temperature bias attack from a single compromised client shifts predictions by up to -1.7 K, while coordinated patch attacks more than triple the mean squared error and produce persistent regional anomalies exceeding +3.5 K. Finally, we assess trimmed mean aggregation as a defense mechanism, showing that it successfully defends against global bias attacks (2-13\% degradation) but fails against patch attacks (281-603\% amplification), exposing limitations of outlier-based defenses for spatially correlated data.

