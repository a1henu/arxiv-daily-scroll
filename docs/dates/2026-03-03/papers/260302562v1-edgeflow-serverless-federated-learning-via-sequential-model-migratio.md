---
layout: default
title: EdgeFLow: Serverless Federated Learning via Sequential Model Migration in Edge Networks
---

# EdgeFLow: Serverless Federated Learning via Sequential Model Migration in Edge Networks
**arXiv**：[2603.02562v1](https://arxiv.org/abs/2603.02562) · [PDF](https://arxiv.org/pdf/2603.02562.pdf)  
**作者**：Yuchen Shi, Qijun Hou, Pingyi Fan, Khaled B. Letaief  

**一句话要点**：提出EdgeFLow框架，通过边缘基站间顺序模型迁移实现无服务器联邦学习，以降低通信开销。

**关键词**：联邦学习, 边缘计算, 模型迁移, 通信优化, 非独立同分布数据, 收敛分析

## 3 点简述
- 核心问题：传统联邦学习因客户端-服务器数据交换和长距离传输面临通信瓶颈。
- 方法要点：用边缘基站顺序迁移模型替代云服务器，仅在边缘集群进行聚合与传播。
- 实验或效果：在非凸目标和非独立同分布数据下验证收敛，显著减少通信成本并保持精度。

## 摘要（原文）

> Federated Learning (FL) has emerged as a transformative distributed learning paradigm in the era of Internet of Things (IoT), reconceptualizing data processing methodologies. However, FL systems face significant communication bottlenecks due to inevitable client-server data exchanges and long-distance transmissions. This work presents EdgeFLow, an innovative FL framework that redesigns the system topology by replacing traditional cloud servers with sequential model migration between edge base stations. By conducting model aggregation and propagation exclusively at edge clusters, EdgeFLow eliminates cloud-based transmissions and substantially reduces global communication overhead. We provide rigorous convergence analysis for EdgeFLow under non-convex objectives and non-IID data distributions, extending classical FL convergence theory. Experimental results across various configurations validate the theoretical analysis, demonstrating that EdgeFLow achieves comparable accuracy improvements while significantly reducing communication costs. As a systemic architectural innovation for communication-efficient FL, EdgeFLow establishes a foundational framework for future developments in IoT and edge-network learning systems.

