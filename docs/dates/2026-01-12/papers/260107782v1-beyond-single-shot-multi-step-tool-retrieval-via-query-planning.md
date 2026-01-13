---
layout: default
title: Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning
---

# Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning
**arXiv**：[2601.07782v1](https://arxiv.org/abs/2601.07782) · [PDF](https://arxiv.org/pdf/2601.07782.pdf)  
**作者**：Wei Fang, James Glass  

**一句话要点**：提出TOOLQP框架，通过迭代查询规划解决大工具库中复杂指令的检索问题。

**关键词**：工具检索, 查询规划, 强化学习, 语义鸿沟, 代理系统

## 3 点简述
- 核心问题：单次密集检索器难以处理抽象用户目标与工具文档间的语义鸿沟及组合工具建模。
- 方法要点：将检索建模为迭代查询规划，分解指令为子任务并动态生成查询以桥接语义。
- 实验或效果：使用合成轨迹和RLVR训练，在零样本泛化、检索器鲁棒性和下游代理执行上表现优异。

## 摘要（原文）

> LLM agents operating over massive, dynamic tool libraries rely on effective retrieval, yet standard single-shot dense retrievers struggle with complex requests. These failures primarily stem from the disconnect between abstract user goals and technical documentation, and the limited capacity of fixed-size embeddings to model combinatorial tool compositions. To address these challenges, we propose TOOLQP, a lightweight framework that models retrieval as iterative query planning. Instead of single-shot matching, TOOLQP decomposes instructions into sub-tasks and dynamically generates queries to interact with the retriever, effectively bridging the semantic gap by targeting the specific sub-tasks required for composition. We train TOOLQP using synthetic query trajectories followed by optimization via Reinforcement Learning with Verifiable Rewards (RLVR). Experiments demonstrate that TOOLQP achieves state-of-the-art performance, exhibiting superior zero-shot generalization, robustness across diverse retrievers, and significant improvements in downstream agentic execution.

