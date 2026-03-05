---
layout: default
title: Online Learning for Multi-Layer Hierarchical Inference under Partial and Policy-Dependent Feedback
---

# Online Learning for Multi-Layer Hierarchical Inference under Partial and Policy-Dependent Feedback
**arXiv**：[2603.04247v1](https://arxiv.org/abs/2603.04247) · [PDF](https://arxiv.org/pdf/2603.04247.pdf)  
**作者**：Haoran Zhang, Seohyeon Cha, Hasan Burhan Beytur, Kevin S Chan, Gustavo de Veciana, Haris Vikalo  

**一句话要点**：提出基于方差缩减EXP4与Lyapunov优化的在线学习算法，以解决多层分层推理中部分策略依赖反馈下的路由策略学习问题。

**关键词**：分层推理, 在线学习, 部分反馈, 路由策略, 方差缩减, Lyapunov优化

## 3 点简述
- 核心问题：多层分层推理系统中，仅终端层提供反馈，导致反馈稀疏且策略依赖，重要性加权估计器方差放大。
- 方法要点：结合方差缩减EXP4算法与Lyapunov优化，实现无偏损失估计，在稀疏反馈下稳定学习。
- 实验或效果：在大规模多任务工作负载上验证，相比标准重要性加权方法，提高了稳定性和性能。

## 摘要（原文）

> Hierarchical inference systems route tasks across multiple computational layers, where each node may either finalize a prediction locally or offload the task to a node in the next layer for further processing. Learning optimal routing policies in such systems is challenging: inference loss is defined recursively across layers, while feedback on prediction error is revealed only at a terminal oracle layer. This induces a partial, policy-dependent feedback structure in which observability probabilities decay with depth, causing importance-weighted estimators to suffer from amplified variance. We study online routing for multi-layer hierarchical inference under long-term resource constraints and terminal-only feedback. We formalize the recursive loss structure and show that naive importance-weighted contextual bandit methods become unstable as feedback probability decays along the hierarchy. To address this, we develop a variance-reduced EXP4-based algorithm integrated with Lyapunov optimization, yielding unbiased loss estimation and stable learning under sparse and policy-dependent feedback. We provide regret guarantees relative to the best fixed routing policy in hindsight and establish near-optimality under stochastic arrivals and resource constraints. Experiments on large-scale multi-task workloads demonstrate improved stability and performance compared to standard importance-weighted approaches.

