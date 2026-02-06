---
layout: default
title: Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory
---

# Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory
**arXiv**：[2602.06025v1](https://arxiv.org/abs/2602.06025) · [PDF](https://arxiv.org/pdf/2602.06025.pdf)  
**作者**：Haozhen Zhang, Haodong Yue, Tao Feng, Quanyu Long, Jianzhu Bao, Bowen Jin, Weizhi Zhang, Xiao Li, Jiaxuan You, Chengwei Qin, Wenya Wang  

**一句话要点**：提出BudgetMem框架，通过查询感知的预算层级路由实现运行时代理内存的性能-成本控制。

**关键词**：运行时内存管理, 查询感知路由, 预算层级控制, 强化学习策略, 性能-成本权衡, LLM代理

## 3 点简述
- 核心问题：现有LLM代理内存系统依赖离线、查询无关构建，效率低且可能丢失关键信息。
- 方法要点：将内存处理模块化为三个预算层级，使用轻量级路由器进行强化学习训练的路由决策。
- 实验或效果：在多个基准测试中，BudgetMem在高预算下超越基线，在紧预算下提供更优的准确率-成本前沿。

## 摘要（原文）

> Memory is increasingly central to Large Language Model (LLM) agents operating beyond a single context window, yet most existing systems rely on offline, query-agnostic memory construction that can be inefficient and may discard query-critical information. Although runtime memory utilization is a natural alternative, prior work often incurs substantial overhead and offers limited explicit control over the performance-cost trade-off. In this work, we present \textbf{BudgetMem}, a runtime agent memory framework for explicit, query-aware performance-cost control. BudgetMem structures memory processing as a set of memory modules, each offered in three budget tiers (i.e., \textsc{Low}/\textsc{Mid}/\textsc{High}). A lightweight router performs budget-tier routing across modules to balance task performance and memory construction cost, which is implemented as a compact neural policy trained with reinforcement learning. Using BudgetMem as a unified testbed, we study three complementary strategies for realizing budget tiers: implementation (method complexity), reasoning (inference behavior), and capacity (module model size). Across LoCoMo, LongMemEval, and HotpotQA, BudgetMem surpasses strong baselines when performance is prioritized (i.e., high-budget setting), and delivers better accuracy-cost frontiers under tighter budgets. Moreover, our analysis disentangles the strengths and weaknesses of different tiering strategies, clarifying when each axis delivers the most favorable trade-offs under varying budget regimes.

