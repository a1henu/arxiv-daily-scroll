---
layout: default
title: GShield: Mitigating Poisoning Attacks in Federated Learning
---

# GShield: Mitigating Poisoning Attacks in Federated Learning
**arXiv**：[2512.19286v1](https://arxiv.org/abs/2512.19286) · [PDF](https://arxiv.org/pdf/2512.19286.pdf)  
**作者**：Sameera K. M., Serena Nicolazzo, Antonino Nocera, Vinod P., Rafidha Rehiman K. A  

**一句话要点**：提出GShield防御机制以缓解联邦学习中的数据投毒攻击

**关键词**：联邦学习, 数据投毒攻击, 梯度聚类, 非独立同分布数据, 模型鲁棒性

## 3 点简述
- 联邦学习易受数据投毒攻击，恶意客户端注入操纵数据损害模型性能
- GShield通过聚类和高斯建模学习良性梯度分布，选择性聚合符合预期的更新
- 实验表明GShield显著提升模型鲁棒性，在非独立同分布数据下保持高准确率

## 摘要（原文）

> Federated Learning (FL) has recently emerged as a revolutionary approach to collaborative training Machine Learning models. In particular, it enables decentralized model training while preserving data privacy, but its distributed nature makes it highly vulnerable to a severe attack known as Data Poisoning. In such scenarios, malicious clients inject manipulated data into the training process, thereby degrading global model performance or causing targeted misclassification. In this paper, we present a novel defense mechanism called GShield, designed to detect and mitigate malicious and low-quality updates, especially under non-independent and identically distributed (non-IID) data scenarios. GShield operates by learning the distribution of benign gradients through clustering and Gaussian modeling during an initial round, enabling it to establish a reliable baseline of trusted client behavior. With this benign profile, GShield selectively aggregates only those updates that align with the expected gradient patterns, effectively isolating adversarial clients and preserving the integrity of the global model. An extensive experimental campaign demonstrates that our proposed defense significantly improves model robustness compared to the state-of-the-art methods while maintaining a high accuracy of performance across both tabular and image datasets. Furthermore, GShield improves the accuracy of the targeted class by 43\% to 65\% after detecting malicious and low-quality clients.

