---
layout: default
title: Architectures for Building Agentic AI
---

# Architectures for Building Agentic AI
**arXiv**：[2512.09458v1](https://arxiv.org/abs/2512.09458) · [PDF](https://arxiv.org/pdf/2512.09458.pdf)  
**作者**：Sławomir Nowaczyk  

**一句话要点**：提出基于架构的代理AI可靠性设计，通过组件化与接口规范提升系统稳定性。

**关键词**：代理AI架构, 系统可靠性, 组件化设计, 接口规范, 控制循环, 设计指南

## 3 点简述
- 核心问题：代理AI的可靠性主要依赖于系统架构设计，而非单一算法。
- 方法要点：定义代理系统组件（如目标管理器、规划器、工具路由器）和接口规范（如模式约束、权限控制）。
- 实验或效果：分析不同代理模式（如工具使用、记忆增强）对可靠性和故障模式的影响，提炼设计指南。

## 摘要（原文）

> This chapter argues that the reliability of agentic and generative AI is chiefly an architectural property. We define agentic systems as goal-directed, tool-using decision makers operating in closed loops, and show how reliability emerges from principled componentisation (goal manager, planner, tool-router, executor, memory, verifiers, safety monitor, telemetry), disciplined interfaces (schema-constrained, validated, least-privilege tool calls), and explicit control and assurance loops. Building on classical foundations, we propose a practical taxonomy-tool-using agents, memory-augmented agents, planning and self-improvement agents, multi-agent systems, and embodied or web agents - and analyse how each pattern reshapes the reliability envelope and failure modes. We distil design guidance on typed schemas, idempotency, permissioning, transactional semantics, memory provenance and hygiene, runtime governance (budgets, termination conditions), and simulate-before-actuate safeguards.

