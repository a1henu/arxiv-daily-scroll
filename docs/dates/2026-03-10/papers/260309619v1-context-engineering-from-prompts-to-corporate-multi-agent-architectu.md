---
layout: default
title: Context Engineering: From Prompts to Corporate Multi-Agent Architecture
---

# Context Engineering: From Prompts to Corporate Multi-Agent Architecture
**arXiv**：[2603.09619v1](https://arxiv.org/abs/2603.09619) · [PDF](https://arxiv.org/pdf/2603.09619.pdf)  
**作者**：Vera V. Vishnyakova  

**一句话要点**：提出上下文工程作为独立学科，以管理多智能体系统的信息环境，并构建累积式成熟度模型。

**关键词**：上下文工程, 多智能体系统, 意图工程, 规范工程, 企业人工智能, 成熟度模型

## 3 点简述
- 核心问题：提示工程不足以支持自主多步智能体，需扩展至上下文管理。
- 方法要点：定义上下文质量准则，并引入意图工程和规范工程作为高阶学科。
- 实验或效果：基于企业数据指出部署挑战，以Klarna案例说明上下文和意图双重缺陷。

## 摘要（原文）

> As artificial intelligence (AI) systems evolve from stateless chatbots to autonomous multi-step agents, prompt engineering (PE), the discipline of crafting individual queries, proves necessary but insufficient. This paper introduces context engineering (CE) as a standalone discipline concerned with designing, structuring, and managing the entire informational environment in which an AI agent makes decisions. Drawing on vendor architectures (Google ADK, Anthropic, LangChain), current academic work (ACE framework, Google DeepMind's intelligent delegation), enterprise research (Deloitte, 2026; KPMG, 2026), and the author's experience building a multi-agent system, the paper proposes five context quality criteria: relevance, sufficiency, isolation, economy, and provenance, and frames context as the agent's operating system. Two higher-order disciplines follow. Intent engineering (IE) encodes organizational goals, values, and trade-off hierarchies into agent infrastructure. Specification engineering (SE) creates a machine-readable corpus of corporate policies and standards enabling autonomous operation of multi-agent systems at scale. Together these four disciplines form a cumulative pyramid maturity model of agent engineering, in which each level subsumes the previous one as a necessary foundation. Enterprise data reveals a gap: while 75% of enterprises plan agentic AI deployment within two years (Deloitte, 2026), deployment has surged and retreated as organizations confront scaling complexity (KPMG, 2026). The Klarna case illustrates a dual deficit, contextual and intentional. Whoever controls the agent's context controls its behavior; whoever controls its intent controls its strategy; whoever controls its specifications controls its scale.

