---
layout: default
title: PTOPOFL: Privacy-Preserving Personalised Federated Learning via Persistent Homology
---

# PTOPOFL: Privacy-Preserving Personalised Federated Learning via Persistent Homology
**arXiv**：[2603.04323v1](https://arxiv.org/abs/2603.04323) · [PDF](https://arxiv.org/pdf/2603.04323.pdf)  
**作者**：Kelly L Vomo-Donfack, Adryel Hoszu, Grégory Ginot, Ian Morilla  

**一句话要点**：提出PTOPOFL框架，通过持久同调解决联邦学习中隐私泄露与非IID数据聚合问题

**关键词**：联邦学习, 隐私保护, 持久同调, 个性化聚合, 非IID数据, 拓扑描述符

## 3 点简述
- 核心问题：联邦学习中梯度共享易导致数据重构攻击，非IID客户端分布降低聚合质量
- 方法要点：用持久同调生成拓扑描述符替代梯度传输，基于Wasserstein相似性进行个性化聚类与加权聚合
- 实验或效果：在非IID医疗场景和基准测试中，PTOPOFL实现最高AUC，重构风险降低4.5倍

## 摘要（原文）

> Federated learning (FL) faces two structural tensions: gradient sharing enables data-reconstruction attacks, while non-IID client distributions degrade aggregation quality. We introduce PTOPOFL, a framework that addresses both challenges simultaneously by replacing gradient communication with topological descriptors derived from persistent homology (PH). Clients transmit only 48-dimensional PH feature vectors-compact shape summaries whose many-to-one structure makes inversion provably ill-posed-rather than model gradients. The server performs topology-guided personalised aggregation: clients are clustered by Wasserstein similarity between their PH diagrams, intra-cluster models are topology-weighted,and clusters are blended with a global consensus. We prove an information-contraction theorem showing that PH descriptors leak strictly less mutual information per sample than gradients under strongly convex loss functions, and we establish linear convergence of the Wasserstein-weighted aggregation scheme with an error floor strictly smaller than FedAvg. Evaluated against FedAvg, FedProx, SCAFFOLD, and pFedMe on a non-IID healthcare scenario (8 hospitals, 2 adversarial) and a pathological benchmark (10 clients), PTOPOFL achieves AUC 0.841 and 0.910 respectively-the highest in both settings-while reducing reconstruction risk by a factor of 4.5 relative to gradient sharing. Code is publicly available at https://github.com/MorillaLab/TopoFederatedL and data at https://doi.org/10.5281/zenodo.18827595.

