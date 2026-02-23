---
layout: default
title: FedZMG: Efficient Client-Side Optimization in Federated Learning
---

# FedZMG: Efficient Client-Side Optimization in Federated Learning
**arXiv**：[2602.18384v1](https://arxiv.org/abs/2602.18384) · [PDF](https://arxiv.org/pdf/2602.18384.pdf)  
**作者**：Fotios Zantalis, Evangelos Zervas, Grigorios Koulouras  

**一句话要点**：提出FedZMG以解决联邦学习中非独立同分布数据导致的客户端漂移问题

**关键词**：联邦学习, 客户端优化, 非独立同分布数据, 梯度中心化, 收敛加速

## 3 点简述
- 核心问题：非独立同分布数据导致客户端漂移，降低收敛速度和模型性能
- 方法要点：通过零均值梯度投影正则化优化空间，无需额外通信或超参数调优
- 实验或效果：在EMNIST、CIFAR100和Shakespeare数据集上优于FedAvg和FedAdam

## 摘要（原文）

> Federated Learning (FL) enables distributed model training on edge devices while preserving data privacy. However, clients tend to have non-Independent and Identically Distributed (non-IID) data, which often leads to client-drift, and therefore diminishing convergence speed and model performance. While adaptive optimizers have been proposed to mitigate these effects, they frequently introduce computational complexity or communication overhead unsuitable for resource-constrained IoT environments. This paper introduces Federated Zero Mean Gradients (FedZMG), a novel, parameter-free, client-side optimization algorithm designed to tackle client-drift by structurally regularizing the optimization space. Advancing the idea of Gradient Centralization, FedZMG projects local gradients onto a zero-mean hyperplane, effectively neutralizing the "intensity" or "bias" shifts inherent in heterogeneous data distributions without requiring additional communication or hyperparameter tuning. A theoretical analysis is provided, proving that FedZMG reduces the effective gradient variance and guarantees tighter convergence bounds compared to standard FedAvg. Extensive empirical evaluations on EMNIST, CIFAR100, and Shakespeare datasets demonstrate that FedZMG achieves better convergence speed and final validation accuracy compared to the baseline FedAvg and the adaptive optimizer FedAdam, particularly in highly non-IID settings.

