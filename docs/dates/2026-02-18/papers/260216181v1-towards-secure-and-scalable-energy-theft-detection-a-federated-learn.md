---
layout: default
title: Towards Secure and Scalable Energy Theft Detection: A Federated Learning Approach for Resource-Constrained Smart Meters
---

# Towards Secure and Scalable Energy Theft Detection: A Federated Learning Approach for Resource-Constrained Smart Meters
**arXiv**：[2602.16181v1](https://arxiv.org/abs/2602.16181) · [PDF](https://arxiv.org/pdf/2602.16181.pdf)  
**作者**：Diego Labate, Dipanwita Thakur, Giancarlo Fortino  

**一句话要点**：提出基于联邦学习的轻量级隐私保护框架，以解决智能电表中能源盗窃检测的隐私与计算约束问题。

**关键词**：能源盗窃检测, 联邦学习, 差分隐私, 智能电表, 轻量级模型, 智能电网安全

## 3 点简述
- 核心问题：能源盗窃威胁智能电网稳定，传统集中式方法存在隐私泄露风险，且智能电表资源受限难以运行重模型。
- 方法要点：采用轻量级多层感知机模型，结合高斯噪声注入实现差分隐私，在本地更新后聚合，确保隐私与性能平衡。
- 实验或效果：在真实数据集上评估，IID和非IID分布下均实现高准确率、精确率、召回率和AUC，验证了方法的实用性与可扩展性。

## 摘要（原文）

> Energy theft poses a significant threat to the stability and efficiency of smart grids, leading to substantial economic losses and operational challenges. Traditional centralized machine learning approaches for theft detection require aggregating user data, raising serious concerns about privacy and data security. These issues are further exacerbated in smart meter environments, where devices are often resource-constrained and lack the capacity to run heavy models. In this work, we propose a privacy-preserving federated learning framework for energy theft detection that addresses both privacy and computational constraints. Our approach leverages a lightweight multilayer perceptron (MLP) model, suitable for deployment on low-power smart meters, and integrates basic differential privacy (DP) by injecting Gaussian noise into local model updates before aggregation. This ensures formal privacy guarantees without compromising learning performance. We evaluate our framework on a real-world smart meter dataset under both IID and non-IID data distributions. Experimental results demonstrate that our method achieves competitive accuracy, precision, recall, and AUC scores while maintaining privacy and efficiency. This makes the proposed solution practical and scalable for secure energy theft detection in next-generation smart grid infrastructures.

