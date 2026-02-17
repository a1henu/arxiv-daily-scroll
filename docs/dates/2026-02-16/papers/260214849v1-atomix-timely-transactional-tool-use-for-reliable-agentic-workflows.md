---
layout: default
title: Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows
---

# Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows
**arXiv**：[2602.14849v1](https://arxiv.org/abs/2602.14849) · [PDF](https://arxiv.org/pdf/2602.14849.pdf)  
**作者**：Bardia Mohammadi, Nearchos Potamitis, Lars Klein, Akhil Arora, Laurent Bindschaedler  

**一句话要点**：提出Atomix运行时，为代理工具调用提供进度感知事务语义以解决副作用泄漏问题。

**关键词**：LLM代理, 事务语义, 工具调用, 副作用管理, 进度感知, 故障恢复

## 3 点简述
- 核心问题：LLM代理在故障、推测或争用下，工具调用可能泄漏意外副作用且无法安全回滚。
- 方法要点：Atomix通过纪元标记、资源前沿跟踪和进度谓词提交，支持可缓冲效果延迟和外部效果补偿。
- 实验或效果：在故障注入的真实工作负载中，事务重试提高任务成功率，前沿门控提交增强隔离性。

## 摘要（原文）

> LLM agents increasingly act on external systems, yet tool effects are immediate. Under failures, speculation, or contention, losing branches can leak unintended side effects with no safe rollback. We introduce Atomix, a runtime that provides progress-aware transactional semantics for agent tool calls. Atomix tags each call with an epoch, tracks per-resource frontiers, and commits only when progress predicates indicate safety; bufferable effects can be delayed, while externalized effects are tracked and compensated on abort. Across real workloads with fault injection, transactional retry improves task success, while frontier-gated commit strengthens isolation under speculation and contention.

