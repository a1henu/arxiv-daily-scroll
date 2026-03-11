---
layout: default
title: PPO-Based Hybrid Optimization for RIS-Assisted Semantic Vehicular Edge Computing
---

# PPO-Based Hybrid Optimization for RIS-Assisted Semantic Vehicular Edge Computing
**arXiv**：[2603.09082v1](https://arxiv.org/abs/2603.09082) · [PDF](https://arxiv.org/pdf/2603.09082.pdf)  
**作者**：Wei Feng, Jingbo Zhang, Qiong Wu, Pingyi Fan, Qiang Fan  

**一句话要点**：提出基于PPO的混合优化方案，用于RIS辅助的语义车联网边缘计算，以降低延迟。

**关键词**：可重构智能表面, 语义通信, 车联网边缘计算, 近端策略优化, 混合优化

## 3 点简述
- 核心问题：动态环境和间歇性链路下，车联网应用对低延迟的需求。
- 方法要点：结合RIS优化无线连接和语义通信，采用PPO和LP的混合优化策略。
- 实验或效果：相比GA和QPSO，平均端到端延迟降低约40%至50%，支持30辆车的高可扩展性。

## 摘要（原文）

> To support latency-sensitive Internet of Vehicles (IoV) applications amidst dynamic environments and intermittent links, this paper proposes a Reconfigurable Intelligent Surface (RIS)-aided semantic-aware Vehicle Edge Computing (VEC) framework. This approach integrates RIS to optimize wireless connectivity and semantic communication to minimize latency by transmitting semantic features. We formulate a comprehensive joint optimization problem by optimizing offloading ratios, the number of semantic symbols, and RIS phase shifts. Considering the problem's high dimensionality and non-convexity, we propose a two-tier hybrid scheme that employs Proximal Policy Optimization (PPO) for discrete decision-making and Linear Programming (LP) for offloading optimization. {The simulation results have validated the proposed framework's superiority over existing methods. Specifically, the proposed PPO-based hybrid optimization scheme reduces the average end-to-end latency by approximately 40% to 50% compared to Genetic Algorithm (GA) and Quantum-behaved Particle Swarm Optimization (QPSO). Moreover, the system demonstrates strong scalability by maintaining low latency even in congested scenarios with up to 30 vehicles.

