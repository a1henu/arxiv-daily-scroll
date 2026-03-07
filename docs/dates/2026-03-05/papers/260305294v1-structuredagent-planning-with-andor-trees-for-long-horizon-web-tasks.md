---
layout: default
title: STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks
---

# STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks
**arXiv**：[2603.05294v1](https://arxiv.org/abs/2603.05294) · [PDF](https://arxiv.org/pdf/2603.05294.pdf)  
**作者**：ELita Lobo, Xu Chen, Jingjing Meng, Nan Xi, Yang Jiao, Chirag Agarwal, Yair Zick, Yan Gao  

**一句话要点**：提出STRUCTUREDAGENT框架，通过动态AND/OR树和结构化记忆解决长时程网页任务中的规划与约束满足问题。

**关键词**：网页代理, 分层规划, AND/OR树, 结构化记忆, 长时程任务, 约束满足

## 3 点简述
- 现有网页代理在复杂长时程任务中面临历史跟踪能力有限、规划能力弱和贪婪行为导致提前终止等核心问题。
- 方法采用在线分层规划器结合动态AND/OR树进行高效搜索，并引入结构化记忆模块以跟踪候选解提升约束满足。
- 在WebVoyager、WebArena和自定义购物基准测试中，该框架相比标准LLM代理提升了长时程网页浏览任务的性能。

## 摘要（原文）

> Recent advances in large language models (LLMs) have enabled agentic systems for sequential decision-making. Such agents must perceive their environment, reason across multiple time steps, and take actions that optimize long-term objectives. However, existing web agents struggle on complex, long-horizon tasks due to limited in-context memory for tracking history, weak planning abilities, and greedy behaviors that lead to premature termination. To address these challenges, we propose STRUCTUREDAGENT, a hierarchical planning framework with two core components: (1) an online hierarchical planner that uses dynamic AND/OR trees for efficient search and (2) a structured memory module that tracks and maintains candidate solutions to improve constraint satisfaction in information-seeking tasks. The framework also produces interpretable hierarchical plans, enabling easier debugging and facilitating human intervention when needed. Our results on WebVoyager, WebArena, and custom shopping benchmarks show that STRUCTUREDAGENT improves performance on long-horizon web-browsing tasks compared to standard LLM-based agents.

