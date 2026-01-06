---
layout: default
title: Distributed Federated Learning by Alternating Periods of Training
---

# Distributed Federated Learning by Alternating Periods of Training
**arXiv**：[2601.01793v1](https://arxiv.org/abs/2601.01793) · [PDF](https://arxiv.org/pdf/2601.01793.pdf)  
**作者**：Shamik Bhattacharyya, Rachel Kalpana Kalaimani  

**一句话要点**：提出分布式联邦学习算法以解决单服务器可扩展性和容错性问题

**关键词**：分布式联邦学习, 可扩展性, 容错性, 服务器间通信, 交替训练, 模型收敛

## 3 点简述
- 核心问题：传统联邦学习依赖单服务器，面临可扩展性差和单点故障风险
- 方法要点：设计多服务器分布式框架，通过交替本地训练和服务器间全局训练实现去中心化
- 实验或效果：理论分析表明算法能收敛到理想模型，数值模拟验证了有效性

## 摘要（原文）

> Federated learning is a privacy-focused approach towards machine learning where models are trained on client devices with locally available data and aggregated at a central server. However, the dependence on a single central server is challenging in the case of a large number of clients and even poses the risk of a single point of failure. To address these critical limitations of scalability and fault-tolerance, we present a distributed approach to federated learning comprising multiple servers with inter-server communication capabilities. While providing a fully decentralized approach, the designed framework retains the core federated learning structure where each server is associated with a disjoint set of clients with server-client communication capabilities. We propose a novel DFL (Distributed Federated Learning) algorithm which uses alternating periods of local training on the client data followed by global training among servers. We show that the DFL algorithm, under a suitable choice of parameters, ensures that all the servers converge to a common model value within a small tolerance of the ideal model, thus exhibiting effective integration of local and global training models. Finally, we illustrate our theoretical claims through numerical simulations.

