---
layout: default
title: Generalized Schrödinger Bridge on Graphs
---

# Generalized Schrödinger Bridge on Graphs
**arXiv**：[2602.04675v1](https://arxiv.org/abs/2602.04675) · [PDF](https://arxiv.org/pdf/2602.04675.pdf)  
**作者**：Panagiotis Theodoropoulos, Juno Nam, Evangelos Theodorou, Jaemoo Choi  

**一句话要点**：提出广义薛定谔桥图框架以解决图传输中可执行策略学习问题

**关键词**：图传输, 薛定谔桥, 连续时间马尔可夫链, 策略学习, 可扩展框架, 成本优化

## 3 点简述
- 核心问题：现有图传输方法缺乏可执行策略，假设限制多，泛化性和可扩展性差
- 方法要点：基于似然优化学习连续时间马尔可夫链策略，满足端点边际并优化中间状态成本
- 实验或效果：在真实世界图拓扑上验证，能学习准确、尊重拓扑的策略，优化应用特定成本

## 摘要（原文）

> Transportation on graphs is a fundamental challenge across many domains, where decisions must respect topological and operational constraints. Despite the need for actionable policies, existing graph-transport methods lack this expressivity. They rely on restrictive assumptions, fail to generalize across sparse topologies, and scale poorly with graph size and time horizon. To address these issues, we introduce Generalized Schrödinger Bridge on Graphs (GSBoG), a novel scalable data-driven framework for learning executable controlled continuous-time Markov chain (CTMC) policies on arbitrary graphs under state cost augmented dynamics. Notably, GSBoG learns trajectory-level policies, avoiding dense global solvers and thereby enhancing scalability. This is achieved via a likelihood optimization approach, satisfying the endpoint marginals, while simultaneously optimizing intermediate behavior under state-dependent running costs. Extensive experimentation on challenging real-world graph topologies shows that GSBoG reliably learns accurate, topology-respecting policies while optimizing application-specific intermediate state costs, highlighting its broad applicability and paving new avenues for cost-aware dynamical transport on general graphs.

