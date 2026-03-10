---
layout: default
title: FedPrism: Adaptive Personalized Federated Learning under Non-IID Data
---

# FedPrism: Adaptive Personalized Federated Learning under Non-IID Data
**arXiv**：[2603.08252v1](https://arxiv.org/abs/2603.08252) · [PDF](https://arxiv.org/pdf/2603.08252.pdf)  
**作者**：Prakash Kumbhakar, Shrey Srivastava, Haroon R Lone  

**一句话要点**：提出FedPrism框架以解决非独立同分布数据下的联邦学习性能下降问题

**关键词**：联邦学习, 非独立同分布数据, 个性化模型, 自适应聚类, 双流架构

## 3 点简述
- 核心问题：联邦学习在非独立同分布数据中性能下降，全局聚合策略难以适应本地数据多样性
- 方法要点：采用Prism分解构建全局、共享组和私有模型部分，结合双流设计基于置信度路由预测
- 实验或效果：在非独立同分布数据上超越静态聚合和硬聚类基线，高异质性下实现显著准确率提升

## 摘要（原文）

> Federated Learning (FL) suffers significant performance degradation in real-world deployments characterized by moderate to extreme statistical heterogeneity (non-IID client data). While global aggregation strategies promote broad generalization, they often fail to capture the diversity of local data distributions, leading to suboptimal personalization.
>   We address this problem with FedPrism, a framework that uses two main strategies. First, it uses a Prism Decomposition method that builds each client's model from three parts: a global foundation, a shared group part for similar clients, and a private part for unique local data. This allows the system to group similar users together automatically and adapt if their data changes. Second, we include a Dual-Stream design that runs a general model alongside a local specialist. The system routes predictions between the general model and the local specialist based on the specialist's confidence.
>   Through systematic experiments on non-IID data partitions, we demonstrate that FedPrism exceeds static aggregation and hard-clustering baselines, achieving significant accuracy gains under high heterogeneity. These results establish FedPrism as a robust and flexible solution for federated learning in heterogeneous environments, effectively balancing generalizable knowledge with adaptive personalization.

