---
layout: default
title: Conflict-Aware Client Selection for Multi-Server Federated Learning
---

# Conflict-Aware Client Selection for Multi-Server Federated Learning
**arXiv**：[2602.02458v1](https://arxiv.org/abs/2602.02458) · [PDF](https://arxiv.org/pdf/2602.02458.pdf)  
**作者**：Mingwei Hong, Zheng Lin, Zehang Lin, Lin Li, Miao Yang, Xia Du, Zihan Fang, Zhaolu Kang, Dianxin Luan, Shunzhi Zhu  

**一句话要点**：提出基于强化学习与冲突风险预测的客户端选择方法，以优化多服务器联邦学习中的资源争用问题。

**关键词**：多服务器联邦学习, 客户端选择, 强化学习, 冲突预测, 隐马尔可夫模型, 公平性奖励

## 3 点简述
- 核心问题：多服务器联邦学习中客户端覆盖重叠与选择不协调导致带宽冲突和训练失败。
- 方法要点：使用分类隐马尔可夫模型预测冲突风险，结合公平性奖励机制优化客户端选择。
- 实验或效果：实验表明该方法有效减少服务器间冲突，提升收敛速度和通信效率。

## 摘要（原文）

> Federated learning (FL) has emerged as a promising distributed machine learning (ML) that enables collaborative model training across clients without exposing raw data, thereby preserving user privacy and reducing communication costs. Despite these benefits, traditional single-server FL suffers from high communication latency due to the aggregation of models from a large number of clients. While multi-server FL distributes workloads across edge servers, overlapping client coverage and uncoordinated selection often lead to resource contention, causing bandwidth conflicts and training failures. To address these limitations, we propose a decentralized reinforcement learning with conflict risk prediction, named RL CRP, to optimize client selection in multi-server FL systems. Specifically, each server estimates the likelihood of client selection conflicts using a categorical hidden Markov model based on its sparse historical client selection sequence. Then, a fairness-aware reward mechanism is incorporated to promote long-term client participation for minimizing training latency and resource contention. Extensive experiments demonstrate that the proposed RL-CRP framework effectively reduces inter-server conflicts and significantly improves training efficiency in terms of convergence speed and communication cost.

