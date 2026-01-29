---
layout: default
title: AMA: Adaptive Memory via Multi-Agent Collaboration
---

# AMA: Adaptive Memory via Multi-Agent Collaboration
**arXiv**：[2601.20352v1](https://arxiv.org/abs/2601.20352) · [PDF](https://arxiv.org/pdf/2601.20352.pdf)  
**作者**：Weiquan Huang, Zixuan Wang, Hehai Lin, Sudong Wang, Bo Xu, Qian Li, Beier Zhu, Linyi Yang, Chengwei Qin  

**一句话要点**：提出AMA框架以解决LLM代理中记忆系统与任务需求不匹配的问题

**关键词**：大型语言模型代理, 自适应记忆系统, 多智能体协作, 分层记忆设计, 长期记忆一致性, 令牌效率优化

## 3 点简述
- 核心问题：现有LLM代理记忆系统存在检索粒度僵化、维护策略积累过重和更新机制粗粒度，导致信息与推理需求不匹配及逻辑不一致累积。
- 方法要点：AMA采用多智能体协作，通过分层记忆设计动态对齐检索粒度与任务复杂度，包括构造器、检索器、法官和刷新器协同工作。
- 实验或效果：在长上下文基准测试中显著优于现有方法，相比全上下文方法减少约80%令牌消耗，提升检索精度和长期记忆一致性。

## 摘要（原文）

> The rapid evolution of Large Language Model (LLM) agents has necessitated robust memory systems to support cohesive long-term interaction and complex reasoning. Benefiting from the strong capabilities of LLMs, recent research focus has shifted from simple context extension to the development of dedicated agentic memory systems. However, existing approaches typically rely on rigid retrieval granularity, accumulation-heavy maintenance strategies, and coarse-grained update mechanisms. These design choices create a persistent mismatch between stored information and task-specific reasoning demands, while leading to the unchecked accumulation of logical inconsistencies over time. To address these challenges, we propose Adaptive Memory via Multi-Agent Collaboration (AMA), a novel framework that leverages coordinated agents to manage memory across multiple granularities. AMA employs a hierarchical memory design that dynamically aligns retrieval granularity with task complexity. Specifically, the Constructor and Retriever jointly enable multi-granularity memory construction and adaptive query routing. The Judge verifies the relevance and consistency of retrieved content, triggering iterative retrieval when evidence is insufficient or invoking the Refresher upon detecting logical conflicts. The Refresher then enforces memory consistency by performing targeted updates or removing outdated entries. Extensive experiments on challenging long-context benchmarks show that AMA significantly outperforms state-of-the-art baselines while reducing token consumption by approximately 80% compared to full-context methods, demonstrating its effectiveness in maintaining retrieval precision and long-term memory consistency.

