---
layout: default
title: StackPlanner: A Centralized Hierarchical Multi-Agent System with Task-Experience Memory Management
---

# StackPlanner: A Centralized Hierarchical Multi-Agent System with Task-Experience Memory Management
**arXiv**：[2601.05890v1](https://arxiv.org/abs/2601.05890) · [PDF](https://arxiv.org/pdf/2601.05890.pdf)  
**作者**：Ruizhe Zhang, Xinke Jiang, Zhibang Yang, Zhixin Zhang, Jiaran Gao, Yuzhen Xiao, Hongbin Lai, Xu Chu, Junfeng Zhao, Yasha Wang  

**一句话要点**：提出StackPlanner框架，通过分层记忆管理解决多智能体协作中的记忆低效和泛化问题。

**关键词**：多智能体系统, 记忆管理, 分层框架, 强化学习, 任务协调

## 3 点简述
- 核心问题：集中式多智能体系统因缺乏记忆管理，导致上下文膨胀和跨任务泛化差。
- 方法要点：采用分层框架，分离高层协调与子任务执行，并利用结构化经验记忆和强化学习管理记忆。
- 实验或效果：在深度搜索和智能体系统基准测试中验证了长程协作的有效性。

## 摘要（原文）

> Multi-agent systems based on large language models, particularly centralized architectures, have recently shown strong potential for complex and knowledge-intensive tasks. However, central agents often suffer from unstable long-horizon collaboration due to the lack of memory management, leading to context bloat, error accumulation, and poor cross-task generalization. To address both task-level memory inefficiency and the inability to reuse coordination experience, we propose StackPlanner, a hierarchical multi-agent framework with explicit memory control. StackPlanner addresses these challenges by decoupling high-level coordination from subtask execution with active task-level memory control, and by learning to retrieve and exploit reusable coordination experience via structured experience memory and reinforcement learning. Experiments on multiple deep-search and agent system benchmarks demonstrate the effectiveness of our approach in enabling reliable long-horizon multi-agent collaboration.

