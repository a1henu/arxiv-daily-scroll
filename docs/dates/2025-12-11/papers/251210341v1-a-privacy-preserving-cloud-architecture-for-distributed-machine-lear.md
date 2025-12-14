---
layout: default
title: A Privacy-Preserving Cloud Architecture for Distributed Machine Learning at Scale
---

# A Privacy-Preserving Cloud Architecture for Distributed Machine Learning at Scale
**arXiv**：[2512.10341v1](https://arxiv.org/abs/2512.10341) · [PDF](https://arxiv.org/pdf/2512.10341.pdf)  
**作者**：Vinoth Punniyamoorthy, Ashok Gadi Parthi, Mayilsamy Palanigounder, Ravi Kiran Kodali, Bikesh Kumar, Kabilan Kannan  

**一句话要点**：提出云原生隐私保护架构以解决分布式机器学习中的隐私、合规与可扩展性问题

**关键词**：隐私保护架构, 联邦学习, 差分隐私, 零知识证明, 自适应治理, 多云部署

## 3 点简述
- 核心问题：分布式机器学习需在异构多云环境中保障隐私、合规与可扩展部署
- 方法要点：集成联邦学习、差分隐私、零知识合规证明和基于强化学习的自适应治理
- 实验或效果：原型部署显示降低成员推断风险，保持模型性能，并实现低开销的持续治理

## 摘要（原文）

> Distributed machine learning systems require strong privacy guarantees, verifiable compliance, and scalable deployment across heterogeneous and multi-cloud environments. This work introduces a cloud-native privacy-preserving architecture that integrates federated learning, differential privacy, zero-knowledge compliance proofs, and adaptive governance powered by reinforcement learning. The framework supports secure model training and inference without centralizing sensitive data, while enabling cryptographically verifiable policy enforcement across institutions and cloud platforms. A full prototype deployed across hybrid Kubernetes clusters demonstrates reduced membership-inference risk, consistent enforcement of formal privacy budgets, and stable model performance under differential privacy. Experimental evaluation across multi-institution workloads shows that the architecture maintains utility with minimal overhead while providing continuous, risk-aware governance. The proposed framework establishes a practical foundation for deploying trustworthy and compliant distributed machine learning systems at scale.

