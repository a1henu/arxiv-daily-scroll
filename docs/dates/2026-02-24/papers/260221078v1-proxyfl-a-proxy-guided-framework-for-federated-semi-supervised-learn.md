---
layout: default
title: ProxyFL: A Proxy-Guided Framework for Federated Semi-Supervised Learning
---

# ProxyFL: A Proxy-Guided Framework for Federated Semi-Supervised Learning
**arXiv**：[2602.21078v1](https://arxiv.org/abs/2602.21078) · [PDF](https://arxiv.org/pdf/2602.21078.pdf)  
**作者**：Duowen Chen, Yan Wang  

**一句话要点**：提出ProxyFL框架，通过代理机制同时缓解联邦半监督学习中的外部和内部异构性问题。

**关键词**：联邦学习, 半监督学习, 数据异构性, 代理机制, 模型聚合

## 3 点简述
- 核心问题：联邦半监督学习中存在跨客户端和客户端内的数据异构性，影响模型性能。
- 方法要点：使用可学习的分类器权重作为代理，优化全局代理以处理外部异构，并通过正负代理池重新纳入被丢弃样本以缓解内部异构。
- 实验或效果：实验和理论分析显示ProxyFL在性能和收敛性方面表现显著。

## 摘要（原文）

> Federated Semi-Supervised Learning (FSSL) aims to collaboratively train a global model across clients by leveraging partially-annotated local data in a privacy-preserving manner. In FSSL, data heterogeneity is a challenging issue, which exists both across clients and within clients. External heterogeneity refers to the data distribution discrepancy across different clients, while internal heterogeneity represents the mismatch between labeled and unlabeled data within clients. Most FSSL methods typically design fixed or dynamic parameter aggregation strategies to collect client knowledge on the server (external) and / or filter out low-confidence unlabeled samples to reduce mistakes in local client (internal). But, the former is hard to precisely fit the ideal global distribution via direct weights, and the latter results in fewer data participation into FL training. To this end, we propose a proxy-guided framework called ProxyFL that focuses on simultaneously mitigating external and internal heterogeneity via a unified proxy. I.e., we consider the learnable weights of classifier as proxy to simulate the category distribution both locally and globally. For external, we explicitly optimize global proxy against outliers instead of direct weights; for internal, we re-include the discarded samples into training by a positive-negative proxy pool to mitigate the impact of potentially-incorrect pseudo-labels. Insight experiments & theoretical analysis show our significant performance and convergence in FSSL.

