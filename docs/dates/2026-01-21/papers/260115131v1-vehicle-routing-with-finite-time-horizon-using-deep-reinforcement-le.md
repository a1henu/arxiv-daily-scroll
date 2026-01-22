---
layout: default
title: Vehicle Routing with Finite Time Horizon using Deep Reinforcement Learning with Improved Network Embedding
---

# Vehicle Routing with Finite Time Horizon using Deep Reinforcement Learning with Improved Network Embedding
**arXiv**：[2601.15131v1](https://arxiv.org/abs/2601.15131) · [PDF](https://arxiv.org/pdf/2601.15131.pdf)  
**作者**：Ayan Maity, Sudeshna Sarkar  

**一句话要点**：提出改进网络嵌入的深度强化学习方法，以解决有限时间范围内的车辆路径规划问题。

**关键词**：车辆路径规划, 深度强化学习, 网络嵌入, 有限时间范围, 图表示学习

## 3 点简述
- 研究有限时间范围内的车辆路径规划问题，目标是在有限时间内最大化服务客户请求数量。
- 提出新颖的路由网络嵌入模块，结合局部节点嵌入和上下文感知的全局图表示，并整合剩余时间信息。
- 在真实和合成网络上验证，方法在客户服务率和求解时间上优于现有方法。

## 摘要（原文）

> In this paper, we study the vehicle routing problem with a finite time horizon. In this routing problem, the objective is to maximize the number of customer requests served within a finite time horizon. We present a novel routing network embedding module which creates local node embedding vectors and a context-aware global graph representation. The proposed Markov decision process for the vehicle routing problem incorporates the node features, the network adjacency matrix and the edge features as components of the state space. We incorporate the remaining finite time horizon into the network embedding module to provide a proper routing context to the embedding module. We integrate our embedding module with a policy gradient-based deep Reinforcement Learning framework to solve the vehicle routing problem with finite time horizon. We trained and validated our proposed routing method on real-world routing networks, as well as synthetically generated Euclidean networks. Our experimental results show that our method achieves a higher customer service rate than the existing routing methods. Additionally, the solution time of our method is significantly lower than that of the existing methods.

