---
layout: default
title: A Constrained RL Approach for Cost-Efficient Delivery of Latency-Sensitive Applications
---

# A Constrained RL Approach for Cost-Efficient Delivery of Latency-Sensitive Applications
**arXiv**：[2603.04353v1](https://arxiv.org/abs/2603.04353) · [PDF](https://arxiv.org/pdf/2603.04353.pdf)  
**作者**：Ozan Aygün, Vincenzo Norman Vitale, Antonia M. Tulino, Hao Feng, Elza Erkip, Jaime Llorca  

**一句话要点**：提出基于约束深度强化学习的方法，以最小化资源成本并满足延迟敏感应用的严格包延迟要求。

**关键词**：约束深度强化学习, 延迟敏感应用, 网络控制, 资源成本优化, 包延迟约束

## 3 点简述
- 核心问题：现有方法在严格包延迟要求下无法可靠交付，需在最小化成本的同时保证及时吞吐量。
- 方法要点：将最小成本延迟约束网络控制问题建模为约束马尔可夫决策过程，采用约束深度强化学习技术。
- 实验或效果：相比基线方法，该方法能确保及时包交付，且成本低于其他吞吐量最大化方法。

## 摘要（原文）

> Next-generation networks aim to provide performance guarantees to real-time interactive services that require timely and cost-efficient packet delivery. In this context, the goal is to reliably deliver packets with strict deadlines imposed by the application while minimizing overall resource allocation cost. A large body of work has leveraged stochastic optimization techniques to design efficient dynamic routing and scheduling solutions under average delay constraints; however, these methods fall short when faced with strict per-packet delay requirements. We formulate the minimum-cost delay-constrained network control problem as a constrained Markov decision process and utilize constrained deep reinforcement learning (CDRL) techniques to effectively minimize total resource allocation cost while maintaining timely throughput above a target reliability level. Results indicate that the proposed CDRL-based solution can ensure timely packet delivery even when existing baselines fall short, and it achieves lower cost compared to other throughput-maximizing methods.

