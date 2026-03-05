---
layout: default
title: A Dual-Helix Governance Approach Towards Reliable Agentic AI for WebGIS Development
---

# A Dual-Helix Governance Approach Towards Reliable Agentic AI for WebGIS Development
**arXiv**：[2603.04390v1](https://arxiv.org/abs/2603.04390) · [PDF](https://arxiv.org/pdf/2603.04390.pdf)  
**作者**：Boyuan, Guan, Wencong Cui, Levente Juhasz  

**一句话要点**：提出双螺旋治理框架以解决WebGIS开发中代理AI的可靠性问题

**关键词**：代理AI治理, WebGIS开发, 知识图谱, 代码重构, LLM可靠性

## 3 点简述
- 核心问题：LLM在WebGIS开发中因上下文限制、跨会话遗忘等五大限制导致代理AI频繁失败
- 方法要点：采用知识、行为、技能三轨架构，基于知识图谱外部化领域事实并强制执行协议
- 实验或效果：在FutureShorelines工具中，治理代理重构代码，复杂度降低51%，可维护性指数提升7点

## 摘要（原文）

> WebGIS development requires rigor, yet agentic AI frequently fails due to five large language model (LLM) limitations: context constraints, cross-session forgetting, stochasticity, instruction failure, and adaptation rigidity. We propose a dual-helix governance framework reframing these challenges as structural governance problems that model capacity alone cannot resolve. We implement the framework as a 3-track architecture (Knowledge, Behavior, Skills) that uses a knowledge graph substrate to stabilize execution by externalizing domain facts and enforcing executable protocols, complemented by a self-learning cycle for autonomous knowledge growth. Applying this to the FutureShorelines WebGIS tool, a governed agent refactored a 2,265-line monolithic codebase into modular ES6 components. Results demonstrated a 51\% reduction in cyclomatic complexity and a 7-point increase in maintainability index. A comparative experiment against a zero-shot LLM confirms that externalized governance, not just model capability, drives operational reliability in geospatial engineering. This approach is implemented in the open-source AgentLoom governance toolkit.

