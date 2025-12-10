---
layout: default
title: Secure and Privacy-Preserving Federated Learning for Next-Generation Underground Mine Safety
---

# Secure and Privacy-Preserving Federated Learning for Next-Generation Underground Mine Safety
**arXiv**：[2512.08862v1](https://arxiv.org/abs/2512.08862) · [PDF](https://arxiv.org/pdf/2512.08862.pdf)  
**作者**：Mohamed Elmahallawy, Sanjay Madria, Samuel Frimpong  

**一句话要点**：提出FedMining框架，通过去中心化功能加密和平衡聚合机制，解决地下矿山联邦学习中的隐私安全与数据异构问题。

**关键词**：联邦学习, 隐私保护, 地下矿山安全, 去中心化功能加密, 数据异构性, 模型收敛

## 3 点简述
- 核心问题：地下矿山传感器数据集中训练引发隐私安全风险，且非独立同分布数据与噪声阻碍模型收敛。
- 方法要点：采用去中心化功能加密保护本地模型更新，结合平衡聚合机制缓解数据异构性。
- 实验或效果：在真实数据集上验证了隐私保护能力，同时保持高模型精度和快速收敛，降低通信与计算开销。

## 摘要（原文）

> Underground mining operations depend on sensor networks to monitor critical parameters such as temperature, gas concentration, and miner movement, enabling timely hazard detection and safety decisions. However, transmitting raw sensor data to a centralized server for machine learning (ML) model training raises serious privacy and security concerns. Federated Learning (FL) offers a promising alternative by enabling decentralized model training without exposing sensitive local data. Yet, applying FL in underground mining presents unique challenges: (i) Adversaries may eavesdrop on shared model updates to launch model inversion or membership inference attacks, compromising data privacy and operational safety; (ii) Non-IID data distributions across mines and sensor noise can hinder model convergence. To address these issues, we propose FedMining--a privacy-preserving FL framework tailored for underground mining. FedMining introduces two core innovations: (1) a Decentralized Functional Encryption (DFE) scheme that keeps local models encrypted, thwarting unauthorized access and inference attacks; and (2) a balancing aggregation mechanism to mitigate data heterogeneity and enhance convergence. Evaluations on real-world mining datasets demonstrate FedMining's ability to safeguard privacy while maintaining high model accuracy and achieving rapid convergence with reduced communication and computation overhead. These advantages make FedMining both secure and practical for real-time underground safety monitoring.

