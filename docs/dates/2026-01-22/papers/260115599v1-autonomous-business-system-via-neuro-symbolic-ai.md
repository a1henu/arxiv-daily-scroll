---
layout: default
title: Autonomous Business System via Neuro-symbolic AI
---

# Autonomous Business System via Neuro-symbolic AI
**arXiv**：[2601.15599v1](https://arxiv.org/abs/2601.15599) · [PDF](https://arxiv.org/pdf/2601.15599.pdf)  
**作者**：Cecil Pang, Hiroki Sayama  

**一句话要点**：提出AUTOBUS神经符号AI系统以整合LLM与逻辑编程，实现企业端到端业务自主编排。

**关键词**：神经符号AI, 企业自动化, 知识图谱, 逻辑编程, LLM智能体, 业务编排

## 3 点简述
- 当前企业系统部门孤岛化、流程僵化，难以适应动态业务重组需求。
- AUTOBUS结合LLM智能体、谓词逻辑编程和企业知识图谱，构建神经符号AI架构。
- 未知实验效果，但系统通过逻辑引擎执行任务，人类监督确保责任与适应性。

## 摘要（原文）

> Current business environments require organizations to continuously reconfigure cross-functional processes, yet enterprise systems are still organized around siloed departments, rigid workflows, and hard-coded automation. Meanwhile large language models (LLMs) excel at interpreting natural language and unstructured data but lack deterministic, verifiable execution of complex business logic. To address this gap, here we introduce AUTOBUS, an Autonomous Business System that integrates LLM-based AI agents, predicate-logic programming, and business-semantics-centric enterprise data into a coherent neuro-symbolic AI architecture for orchestrating end-to-end business initiatives. AUTOBUS models an initiative as a network of tasks with explicit pre/post conditions, required data, evaluation rules, and API-level actions. Enterprise data is organized as a knowledge graph whose entities, relationships, and constraints are translated into logic facts and foundational rules, providing the semantic grounding for task reasoning. Core AI agents synthesize task instructions, enterprise semantics, and available tools into task-specific logic programs, which are executed by a logic engine that enforces constraints, coordinates auxiliary tools, and orchestrate execution of actions and outcomes. Humans define and maintain the semantics, policies and task instructions, curate tools, and supervise high-impact or ambiguous decisions, ensuring accountability and adaptability. We detail the AUTOBUS architecture, the anatomy of the AI agent generated logic programs, and the role of humans and auxiliary tools in the lifecycle of a business initiative.

