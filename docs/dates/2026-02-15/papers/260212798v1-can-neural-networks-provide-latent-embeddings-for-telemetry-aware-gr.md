---
layout: default
title: Can Neural Networks Provide Latent Embeddings for Telemetry-Aware Greedy Routing?
---

# Can Neural Networks Provide Latent Embeddings for Telemetry-Aware Greedy Routing?
**arXiv**：[2602.12798v1](https://arxiv.org/abs/2602.12798) · [PDF](https://arxiv.org/pdf/2602.12798.pdf)  
**作者**：Andreas Boltres, Niklas Freymuth, Gerhard Neumann  

**一句话要点**：提出Placer算法，利用消息传递网络生成节点嵌入，实现网络状态感知的贪婪路由。

**关键词**：网络路由, 消息传递网络, 节点嵌入, 贪婪路由, 可解释性

## 3 点简述
- 核心问题：现有基于机器学习的路由方法牺牲了可解释性，难以理解网络状态与路由决策的复杂依赖关系。
- 方法要点：使用消息传递网络将网络状态转换为潜在节点嵌入，支持快速贪婪下一跳路由，无需直接求解全对最短路径问题。
- 实验或效果：嵌入可视化展示了网络事件如何影响路由决策，增强了路由决策的可解释性。

## 摘要（原文）

> Telemetry-Aware routing promises to increase efficacy and responsiveness to traffic surges in computer networks. Recent research leverages Machine Learning to deal with the complex dependency between network state and routing, but sacrifices explainability of routing decisions due to the black-box nature of the proposed neural routing modules. We propose \emph{Placer}, a novel algorithm using Message Passing Networks to transform network states into latent node embeddings. These embeddings facilitate quick greedy next-hop routing without directly solving the all-pairs shortest paths problem, and let us visualize how certain network events shape routing decisions.

