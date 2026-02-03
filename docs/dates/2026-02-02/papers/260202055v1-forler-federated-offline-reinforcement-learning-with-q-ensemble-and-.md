---
layout: default
title: FORLER: Federated Offline Reinforcement Learning with Q-Ensemble and Actor Rectification
---

# FORLER: Federated Offline Reinforcement Learning with Q-Ensemble and Actor Rectification
**arXiv**：[2602.02055v1](https://arxiv.org/abs/2602.02055) · [PDF](https://arxiv.org/pdf/2602.02055.pdf)  
**作者**：Nan Qiao, Sheng Yue  

**一句话要点**：提出FORLER，结合服务器Q-集成聚合与设备演员校正，以解决物联网中离线联邦强化学习的策略污染问题。

**关键词**：联邦学习, 离线强化学习, Q-集成, 演员校正, 策略污染, 物联网系统

## 3 点简述
- 核心问题：离线联邦强化学习在低质量异构数据下易陷入局部最优，导致策略污染。
- 方法要点：服务器通过Q-集成聚合稳健合并设备Q函数，设备采用演员校正增强策略梯度。
- 实验或效果：理论提供安全策略改进保证，实验显示在不同数据质量和异构性下优于基线。

## 摘要（原文）

> In Internet-of-Things systems, federated learning has advanced online reinforcement learning (RL) by enabling parallel policy training without sharing raw data. However, interacting with real environments online can be risky and costly, motivating offline federated RL (FRL), where local devices learn from fixed datasets. Despite its promise, offline FRL may break down under low-quality, heterogeneous data. Offline RL tends to get stuck in local optima, and in FRL, one device's suboptimal policy can degrade the aggregated model, i.e., policy pollution. We present FORLER, combining Q-ensemble aggregation on the server with actor rectification on devices. The server robustly merges device Q-functions to curb policy pollution and shift heavy computation off resource-constrained hardware without compromising privacy. Locally, actor rectification enriches policy gradients via a zeroth-order search for high-Q actions plus a bespoke regularizer that nudges the policy toward them. A $δ$-periodic strategy further reduces local computation. We theoretically provide safe policy improvement performance guarantees. Extensive experiments show FORLER consistently outperforms strong baselines under varying data quality and heterogeneity.

