---
layout: default
title: ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering
---

# ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering
**arXiv**：[2602.23193v1](https://arxiv.org/abs/2602.23193) · [PDF](https://arxiv.org/pdf/2602.23193.pdf)  
**作者**：Elzo Brito dos Santos Filho  

**一句话要点**：提出ESAA架构以解决基于LLM的自主代理在状态管理和确定性执行中的结构限制

**关键词**：事件溯源, 自主代理, 确定性编排, LLM软件工程, 状态管理, 并发代理

## 3 点简述
- 核心问题：LLM自主代理缺乏原生状态、长时上下文退化及概率生成与确定性执行间的差距
- 方法要点：采用事件溯源模式，分离认知意图与状态变更，通过确定性编排器验证并持久化事件
- 实验或效果：案例研究验证了架构在单代理和多代理场景下的可扩展性与可验证性

## 摘要（原文）

> Autonomous agents based on Large Language Models (LLMs) have evolved from reactive assistants to systems capable of planning, executing actions via tools, and iterating over environment observations. However, they remain vulnerable to structural limitations: lack of native state, context degradation over long horizons, and the gap between probabilistic generation and deterministic execution requirements. This paper presents the ESAA (Event Sourcing for Autonomous Agents) architecture, which separates the agent's cognitive intention from the project's state mutation, inspired by the Event Sourcing pattern. In ESAA, agents emit only structured intentions in validated JSON (agent.result or issue.report); a deterministic orchestrator validates, persists events in an append-only log (activity.jsonl), applies file-writing effects, and projects a verifiable materialized view (roadmap.json). The proposal incorporates boundary contracts (AGENT_CONTRACT.yaml), metaprompting profiles (PARCER), and replay verification with hashing (esaa verify), ensuring the immutability of completed tasks and forensic traceability. Two case studies validate the architecture: (i) a landing page project (9 tasks, 49 events, single-agent composition) and (ii) a clinical dashboard system (50 tasks, 86 events, 4 concurrent agents across 8 phases), both concluding with run.status=success and verify_status=ok. The multi-agent case study demonstrates real concurrent orchestration with heterogeneous LLMs (Claude Sonnet 4.6, Codex GPT-5, Antigravity/Gemini 3 Pro, and Claude Opus 4.6), providing empirical evidence of the architecture's scalability beyond single-agent scenarios.

