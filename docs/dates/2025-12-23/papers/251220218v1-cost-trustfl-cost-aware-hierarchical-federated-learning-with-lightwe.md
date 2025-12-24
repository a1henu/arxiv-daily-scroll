---
layout: default
title: Cost-TrustFL: Cost-Aware Hierarchical Federated Learning with Lightweight Reputation Evaluation across Multi-Cloud
---

# Cost-TrustFL: Cost-Aware Hierarchical Federated Learning with Lightweight Reputation Evaluation across Multi-Cloud
**arXiv**：[2512.20218v1](https://arxiv.org/abs/2512.20218) · [PDF](https://arxiv.org/pdf/2512.20218.pdf)  
**作者**：Jixiao Yang, Jinyu Chen, Zixiao Huang, Chengda Xu, Chi Zhang, Sijia Li  

**一句话要点**：提出Cost-TrustFL框架，以优化多云联邦学习中的模型性能与通信成本，并防御投毒攻击。

**关键词**：多云联邦学习, 成本优化, 信誉评估, 投毒攻击防御, 非独立同分布数据, 通信效率

## 3 点简述
- 核心问题：多云联邦学习面临非独立同分布数据、恶意参与者检测和高昂跨云通信成本（如出口费）的挑战。
- 方法要点：采用基于梯度的近似Shapley值计算，复杂度从指数降至线性，实现轻量级信誉评估；成本感知聚合策略优先云内通信以减少跨云传输。
- 实验或效果：在CIFAR-10和FEMNIST数据集上，Cost-TrustFL在30%恶意客户端下达到86.7%准确率，通信成本比基线降低32%，性能在不同非独立同分布程度和攻击强度下保持稳定。

## 摘要（原文）

> Federated learning across multi-cloud environments faces critical challenges, including non-IID data distributions, malicious participant detection, and substantial cross-cloud communication costs (egress fees). Existing Byzantine-robust methods focus primarily on model accuracy while overlooking the economic implications of data transfer across cloud providers. This paper presents Cost-TrustFL, a hierarchical federated learning framework that jointly optimizes model performance and communication costs while providing robust defense against poisoning attacks. We propose a gradient-based approximate Shapley value computation method that reduces the complexity from exponential to linear, enabling lightweight reputation evaluation. Our cost-aware aggregation strategy prioritizes intra-cloud communication to minimize expensive cross-cloud data transfers. Experiments on CIFAR-10 and FEMNIST datasets demonstrate that Cost-TrustFL achieves 86.7% accuracy under 30% malicious clients while reducing communication costs by 32% compared to baseline methods. The framework maintains stable performance across varying non-IID degrees and attack intensities, making it practical for real-world multi-cloud deployments.

