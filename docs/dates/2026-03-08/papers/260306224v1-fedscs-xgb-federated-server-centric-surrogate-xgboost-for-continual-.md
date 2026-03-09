---
layout: default
title: FedSCS-XGB -- Federated Server-centric surrogate XGBoost for continual health monitoring
---

# FedSCS-XGB -- Federated Server-centric surrogate XGBoost for continual health monitoring
**arXiv**：[2603.06224v1](https://arxiv.org/abs/2603.06224) · [PDF](https://arxiv.org/pdf/2603.06224.pdf)  
**作者**：Felix Walger, Mehdi Ejtehadi, Anke Schmeink, Diego Paez-Granados  

**一句话要点**：提出FedSCS-XGB分布式协议，用于可穿戴传感器的人体活动识别，以支持脊髓损伤的持续健康监测。

**关键词**：分布式机器学习, 可穿戴传感器, 人体活动识别, XGBoost, 健康监测, 脊髓损伤

## 3 点简述
- 核心问题：在分布式可穿戴传感器数据中，如何实现高效的人体活动识别以早期检测健康威胁，如脊髓损伤相关风险。
- 方法要点：基于XGBoost设计服务器中心化分布式协议，保留直方图分割和树集成等关键特性，理论分析显示可收敛至集中式训练效果。
- 实验或效果：在代表性数据集上评估，性能与集中式XGBoost差距小于1%，优于IBM PAX，验证了理论收敛性。

## 摘要（原文）

> Wearable sensors with local data processing can detect health threats early, enhance documentation, and support personalized therapy. In the context of spinal cord injury (SCI), which involves risks such as pressure injuries and blood pressure instability, continuous monitoring can help mitigate these by enabling early deDtection and intervention. In this work, we present a novel distributed machine learning (DML) protocol for human activity recognition (HAR) from wearable sensor data based on gradient-boosted decision trees (XGBoost). The proposed architecture is inspired by Party-Adaptive XGBoost (PAX) while explicitly preserving key structural and optimization properties of standard XGBoost, including histogram-based split construction and tree-ensemble dynamics. First, we provide a theoretical analysis showing that, under appropriate data conditions and suitable hyperparameter selection, the proposed distributed protocol can converge to solutions equivalent to centralized XGBoost training. Second, the protocol is empirically evaluated on a representative wearable-sensor HAR dataset, reflecting the heterogeneity and data fragmentation typical of remote monitoring scenarios. Benchmarking against centralized XGBoost and IBM PAX demonstrates that the theoretical convergence properties are reflected in practice. The results indicate that the proposed approach can match centralized performance up to a gap under 1\% while retaining the structural advantages of XGBoost in distributed wearable-based HAR settings.

