---
layout: default
title: Distributed Dynamic Associative Memory via Online Convex Optimization
---

# Distributed Dynamic Associative Memory via Online Convex Optimization
**arXiv**：[2511.23347v1](https://arxiv.org/abs/2511.23347) · [PDF](https://arxiv.org/pdf/2511.23347.pdf)  
**作者**：Bowen Wang, Matteo Zecchin, Osvaldo Simeone  

**一句话要点**：提出分布式动态关联记忆框架，通过在线凸优化解决多智能体时变数据流中的记忆更新问题。

**关键词**：分布式关联记忆, 在线凸优化, 动态环境, 通信树优化, 多智能体学习

## 3 点简述
- 核心问题：扩展经典关联记忆至多智能体时变环境，需本地记忆存储并选择性记忆其他智能体信息。
- 方法要点：设计基于树的分布式在线梯度下降算法，支持动态更新记忆并优化通信树以减少延迟。
- 实验或效果：理论分析提供性能保证，实验显示优于共识分布式优化基线，提升准确性和鲁棒性。

## 摘要（原文）

> An associative memory (AM) enables cue-response recall, and it has recently been recognized as a key mechanism underlying modern neural architectures such as Transformers. In this work, we introduce the concept of distributed dynamic associative memory (DDAM), which extends classical AM to settings with multiple agents and time-varying data streams. In DDAM, each agent maintains a local AM that must not only store its own associations but also selectively memorize information from other agents based on a specified interest matrix. To address this problem, we propose a novel tree-based distributed online gradient descent algorithm, termed DDAM-TOGD, which enables each agent to update its memory on the fly via inter-agent communication over designated routing trees. We derive rigorous performance guarantees for DDAM-TOGD, proving sublinear static regret in stationary environments and a path-length dependent dynamic regret bound in non-stationary environments. These theoretical results provide insights into how communication delays and network structure impact performance. Building on the regret analysis, we further introduce a combinatorial tree design strategy that optimizes the routing trees to minimize communication delays, thereby improving regret bounds. Numerical experiments demonstrate that the proposed DDAM-TOGD framework achieves superior accuracy and robustness compared to representative online learning baselines such as consensus-based distributed optimization, confirming the benefits of the proposed approach in dynamic, distributed environments.

