---
layout: default
title: A Scalable Approach to Solving Simulation-Based Network Security Games
---

# A Scalable Approach to Solving Simulation-Based Network Security Games
**arXiv**：[2602.16564v1](https://arxiv.org/abs/2602.16564) · [PDF](https://arxiv.org/pdf/2602.16564.pdf)  
**作者**：Michael Lanier, Yevgeniy Vorobeychik  

**一句话要点**：提出MetaDOAR以解决大规模网络环境中多智能体强化学习的可扩展性问题

**关键词**：多智能体强化学习, 网络游戏, 可扩展性, 元控制器, Q值缓存, 分层策略学习

## 3 点简述
- 核心问题：大规模网络环境下的多智能体强化学习面临计算和内存可扩展性挑战
- 方法要点：通过元控制器结合分区感知过滤和Q值缓存，实现高效的分层策略学习
- 实验或效果：在大型网络拓扑上获得比现有方法更高的玩家收益，无显著内存或训练时间扩展问题

## 摘要（原文）

> We introduce MetaDOAR, a lightweight meta-controller that augments the Double Oracle / PSRO paradigm with a learned, partition-aware filtering layer and Q-value caching to enable scalable multi-agent reinforcement learning on very large cyber-network environments. MetaDOAR learns a compact state projection from per node structural embeddings to rapidly score and select a small subset of devices (a top-k partition) on which a conventional low-level actor performs focused beam search utilizing a critic agent. Selected candidate actions are evaluated with batched critic forwards and stored in an LRU cache keyed by a quantized state projection and local action identifiers, dramatically reducing redundant critic computation while preserving decision quality via conservative k-hop cache invalidation. Empirically, MetaDOAR attains higher player payoffs than SOTA baselines on large network topologies, without significant scaling issues in terms of memory usage or training time. This contribution provide a practical, theoretically motivated path to efficient hierarchical policy learning for large-scale networked decision problems.

