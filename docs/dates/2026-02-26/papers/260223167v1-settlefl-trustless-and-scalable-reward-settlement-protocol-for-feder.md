---
layout: default
title: SettleFL: Trustless and Scalable Reward Settlement Protocol for Federated Learning on Permissionless Blockchains (Extended version)
---

# SettleFL: Trustless and Scalable Reward Settlement Protocol for Federated Learning on Permissionless Blockchains (Extended version)
**arXiv**：[2602.23167v1](https://arxiv.org/abs/2602.23167) · [PDF](https://arxiv.org/pdf/2602.23167.pdf)  
**作者**：Shuang Liang, Yang Hua, Linshan Jiang, Peishen Yan, Tao Song, Bin Yao, Haibing Guan  

**一句话要点**：提出SettleFL协议以解决无许可区块链上联邦学习的去中心化奖励结算成本高和可扩展性差的问题

**关键词**：联邦学习, 区块链奖励结算, 去中心化协议, 可扩展性优化, 乐观执行, 有效性证明

## 3 点简述
- 核心问题：无许可区块链的高成本与联邦学习高频迭代训练冲突，现有方案牺牲去中心化或可扩展性
- 方法要点：基于共享电路架构，提供乐观执行和有效性证明两种策略，灵活适应延迟与成本约束
- 实验或效果：结合真实联邦学习负载和模拟实验，在800参与者规模下显著降低gas成本，保持实用性

## 摘要（原文）

> In open Federated Learning (FL) environments where no central authority exists, ensuring collaboration fairness relies on decentralized reward settlement, yet the prohibitive cost of permissionless blockchains directly clashes with the high-frequency, iterative nature of model training. Existing solutions either compromise decentralization or suffer from scalability bottlenecks due to linear on-chain costs. To address this, we present SettleFL, a trustless and scalable reward settlement protocol designed to minimize total economic friction by offering a family of two interoperable protocols. Leveraging a shared domain-specific circuit architecture, SettleFL offers two interoperable strategies: (1) a Commit-and-Challenge variant that minimizes on-chain costs via optimistic execution and dispute-driven arbitration, and (2) a Commit-with-Proof variant that guarantees instant finality through per-round validity proofs. This design allows the protocol to flexibly adapt to varying latency and cost constraints while enforcing rational robustness without trusted coordination. We conduct extensive experiments combining real FL workloads and controlled simulations. Results show that SettleFL remains practical when scaling to 800 participants, achieving substantially lower gas cost.

