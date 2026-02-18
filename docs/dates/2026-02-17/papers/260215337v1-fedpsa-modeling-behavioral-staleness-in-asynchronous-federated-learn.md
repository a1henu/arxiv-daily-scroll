---
layout: default
title: FedPSA: Modeling Behavioral Staleness in Asynchronous Federated Learning
---

# FedPSA: Modeling Behavioral Staleness in Asynchronous Federated Learning
**arXiv**：[2602.15337v1](https://arxiv.org/abs/2602.15337) · [PDF](https://arxiv.org/pdf/2602.15337.pdf)  
**作者**：Chaoyi Lu  

**一句话要点**：提出FedPSA以解决异步联邦学习中行为陈旧性问题，通过参数敏感度动态调整容忍度。

**关键词**：异步联邦学习, 参数敏感度, 陈旧性建模, 动态动量队列, 性能优化

## 3 点简述
- 核心问题：异步联邦学习因陈旧性导致性能下降，现有方法仅用轮次差衡量，粒度粗且忽略模型本身。
- 方法要点：利用参数敏感度细粒度衡量模型陈旧性，建立动态动量队列实时评估训练阶段，动态调整陈旧信息容忍度。
- 实验或效果：在多个数据集上验证，相比基线方法提升达6.37%，优于当前最优方法1.93%。

## 摘要（原文）

> Asynchronous Federated Learning (AFL) has emerged as a significant research area in recent years. By not waiting for slower clients and executing the training process concurrently, it achieves faster training speed compared to traditional federated learning. However, due to the staleness introduced by the asynchronous process, its performance may degrade in some scenarios. Existing methods often use the round difference between the current model and the global model as the sole measure of staleness, which is coarse-grained and lacks observation of the model itself, thereby limiting the performance ceiling of asynchronous methods. In this paper, we propose FedPSA (Parameter Sensitivity-based Asynchronous Federated Learning), a more fine-grained AFL framework that leverages parameter sensitivity to measure model obsolescence and establishes a dynamic momentum queue to assess the current training phase in real time, thereby adjusting the tolerance for outdated information dynamically. Extensive experiments on multiple datasets and comparisons with various methods demonstrate the superior performance of FedPSA, achieving up to 6.37\% improvement over baseline methods and 1.93\% over the current state-of-the-art method.

