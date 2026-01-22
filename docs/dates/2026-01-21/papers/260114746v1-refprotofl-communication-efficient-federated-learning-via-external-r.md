---
layout: default
title: RefProtoFL: Communication-Efficient Federated Learning via External-Referenced Prototype Alignment
---

# RefProtoFL: Communication-Efficient Federated Learning via External-Referenced Prototype Alignment
**arXiv**：[2601.14746v1](https://arxiv.org/abs/2601.14746) · [PDF](https://arxiv.org/pdf/2601.14746.pdf)  
**作者**：Hongyue Wu, Hangyu Li, Guodong Fan, Haoran Zhu, Shizhan Chen, Zhiyong Feng  

**一句话要点**：提出RefProtoFL以解决通信受限下联邦学习的泛化问题

**关键词**：联邦学习, 原型对齐, 通信效率, 数据异构, 表示学习

## 3 点简述
- 核心问题：联邦学习在通信带宽有限和客户端数据异构时泛化性能受限
- 方法要点：通过外部参考原型对齐和自适应概率更新丢弃提升通信效率与表示一致性
- 实验或效果：在标准基准测试中优于现有原型联邦学习方法

## 摘要（原文）

> Federated learning (FL) enables collaborative model training without sharing raw data in edge environments, but is constrained by limited communication bandwidth and heterogeneous client data distributions. Prototype-based FL mitigates this issue by exchanging class-wise feature prototypes instead of full model parameters; however, existing methods still suffer from suboptimal generalization under severe communication constraints. In this paper, we propose RefProtoFL, a communication-efficient FL framework that integrates External-Referenced Prototype Alignment (ERPA) for representation consistency with Adaptive Probabilistic Update Dropping (APUD) for communication efficiency. Specifically, we decompose the model into a private backbone and a lightweight shared adapter, and restrict federated communication to the adapter parameters only. To further reduce uplink cost, APUD performs magnitude-aware Top-K sparsification, transmitting only the most significant adapter updates for server-side aggregation. To address representation inconsistency across heterogeneous clients, ERPA leverages a small server-held public dataset to construct external reference prototypes that serve as shared semantic anchors. For classes covered by public data, clients directly align local representations to public-induced prototypes, whereas for uncovered classes, alignment relies on server-aggregated global reference prototypes via weighted averaging. Extensive experiments on standard benchmarks demonstrate that RefProtoFL attains higher classification accuracy than state-of-the-art prototype-based FL baselines.

