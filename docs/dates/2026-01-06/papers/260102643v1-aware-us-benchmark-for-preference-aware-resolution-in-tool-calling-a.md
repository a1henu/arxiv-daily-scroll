---
layout: default
title: AWARE-US: Benchmark for Preference-Aware Resolution in Tool-Calling Agents
---

# AWARE-US: Benchmark for Preference-Aware Resolution in Tool-Calling Agents
**arXiv**：[2601.02643v1](https://arxiv.org/abs/2601.02643) · [PDF](https://arxiv.org/pdf/2601.02643.pdf)  
**作者**：Mehmet Kurmaz  

**一句话要点**：提出AWARE-US基准和偏好感知查询修复方法，以解决工具调用代理中的查询不完整与不可行问题。

**关键词**：工具调用代理, 查询修复, 偏好感知, LLM方法, 基准测试, 对话系统

## 3 点简述
- 核心问题：工具调用代理在查询结构化数据库时面临查询不完整和不可行性，现有方法可能违反用户意图。
- 方法要点：基于LLM推断约束重要性，包括局部加权、全局一次性加权和成对排序三种方法。
- 实验或效果：局部加权在偏好对齐上表现最佳，全局加权在正确约束松弛上最优，并引入AWARE-US基准进行评估。

## 摘要（原文）

> Tool-calling conversational agents querying structured databases often face two linked failures: underspecification (missing constraints needed to run a precise query) and infeasibility (the fully specified query returns an empty set because no item satisfies all constraints). Existing work often responds with "no results" or relaxes constraints using ad hoc rules, which can violate user intent by discarding requirements the user cares about most. We frame infeasibility handling as a preference-aware query repair problem: when a query is unsatisfiable, the agent should relax the least important constraints to the user. We propose three LLM-based methods for inferring relative constraint importance from dialogue: (1) local weighting, (2) global one-shot weighting, and (3) pairwise ranking. Experiments show local weighting achieves the best preference alignment, while global weighting performs best on correct constraint relaxation. We also introduce AWARE-US, a benchmark of persona-grounded queries requiring agents to disambiguate requests via conversation and resolve infeasibility in a way consistent with persona-implied preferences.

