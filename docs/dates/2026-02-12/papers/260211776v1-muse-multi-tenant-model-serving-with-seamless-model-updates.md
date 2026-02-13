---
layout: default
title: MUSE: Multi-Tenant Model Serving With Seamless Model Updates
---

# MUSE: Multi-Tenant Model Serving With Seamless Model Updates
**arXiv**：[2602.11776v1](https://arxiv.org/abs/2602.11776) · [PDF](https://arxiv.org/pdf/2602.11776.pdf)  
**作者**：Cláudio Correia, Alberto E. A. Ferreira, Lucas Martins, Miguel P. Bento, Sofia Guerreiro, Ricardo Ribeiro Pereira, Ana Sofia Gomes, Jacopo Bono, Hugo Ferreira, Pedro Bizarro  

**一句话要点**：提出MUSE框架以解决多租户模型服务中模型更新导致的决策阈值失效问题

**关键词**：多租户模型服务, 模型更新, 分数变换, 决策阈值, 意图路由, 高可用性

## 3 点简述
- 核心问题：模型重训练导致分数分布变化，使客户端决策阈值失效，在多租户环境中协调更新成本高
- 方法要点：通过动态意图路由和两级分数变换，将模型输出映射到稳定参考分布，解耦分数与决策边界
- 实验或效果：在Feedzai部署，处理超千事件/秒，减少模型上线时间从周级到分钟级，节省数百万美元

## 摘要（原文）

> In binary classification systems, decision thresholds translate model scores into actions. Choosing suitable thresholds relies on the specific distribution of the underlying model scores but also on the specific business decisions of each client using that model. However, retraining models inevitably shifts score distributions, invalidating existing thresholds. In multi-tenant Score-as-a-Service environments, where decision boundaries reside in client-managed infrastructure, this creates a severe bottleneck: recalibration requires coordinating threshold updates across hundreds of clients, consuming excessive human hours and leading to model stagnation. We introduce MUSE, a model serving framework that enables seamless model updates by decoupling model scores from client decision boundaries. Designed for multi-tenancy, MUSE optimizes infrastructure re-use by sharing models via dynamic intent-based routing, combined with a two-level score transformation that maps model outputs to a stable, reference distribution. Deployed at scale by Feedzai, MUSE processes over a thousand events per second, and over 55 billion events in the last 12 months, across several dozens of tenants, while maintaining high-availability and low-latency guarantees. By reducing model lead time from weeks to minutes, MUSE promotes model resilience against shifting attacks, saving millions of dollars in fraud losses and operational costs.

