---
layout: default
title: An Efficient Gradient-Based Inference Attack for Federated Learning
---

# An Efficient Gradient-Based Inference Attack for Federated Learning
**arXiv**：[2512.15143v1](https://arxiv.org/abs/2512.15143) · [PDF](https://arxiv.org/pdf/2512.15143.pdf)  
**作者**：Pablo Montaña-Fernández, Ines Ortega-Fernandez  

**一句话要点**：提出基于梯度的联邦学习推理攻击方法，利用多轮梯度时序演化进行成员与属性推断

**关键词**：联邦学习隐私攻击, 梯度推理攻击, 成员推断, 属性推断, 多轮时序分析

## 3 点简述
- 针对联邦学习中模型更新交换仍可能泄露敏感信息的问题
- 利用影子技术学习训练记录的轮次梯度模式，无需访问私有数据集
- 在CIFAR-100等数据集上验证攻击效果，揭示多轮联邦学习增加推理攻击风险

## 摘要（原文）

> Federated Learning is a machine learning setting that reduces direct data exposure, improving the privacy guarantees of machine learning models. Yet, the exchange of model updates between the participants and the aggregator can still leak sensitive information. In this work, we present a new gradient-based membership inference attack for federated learning scenarios that exploits the temporal evolution of last-layer gradients across multiple federated rounds. Our method uses the shadow technique to learn round-wise gradient patterns of the training records, requiring no access to the private dataset, and is designed to consider both semi-honest and malicious adversaries (aggregators or data owners). Beyond membership inference, we also provide a natural extension of the proposed attack to discrete attribute inference by contrasting gradient responses under alternative attribute hypotheses. The proposed attacks are model-agnostic, and therefore applicable to any gradient-based model and can be applied to both classification and regression settings. We evaluate the attack on CIFAR-100 and Purchase100 datasets for membership inference and on Breast Cancer Wisconsin for attribute inference. Our findings reveal strong attack performance and comparable computational and memory overhead in membership inference when compared to another attack from the literature. The obtained results emphasize that multi-round federated learning can increase the vulnerability to inference attacks, that aggregators pose a more substantial threat than data owners, and that attack performance is strongly influenced by the nature of the training dataset, with richer, high-dimensional data leading to stronger leakage than simpler tabular data.

