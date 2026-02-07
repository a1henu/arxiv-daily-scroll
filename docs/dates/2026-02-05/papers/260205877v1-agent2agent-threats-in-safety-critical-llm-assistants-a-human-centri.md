---
layout: default
title: Agent2Agent Threats in Safety-Critical LLM Assistants: A Human-Centric Taxonomy
---

# Agent2Agent Threats in Safety-Critical LLM Assistants: A Human-Centric Taxonomy
**arXiv**：[2602.05877v1](https://arxiv.org/abs/2602.05877) · [PDF](https://arxiv.org/pdf/2602.05877.pdf)  
**作者**：Lukas Stappen, Ahmet Erkan Turan, Johann Hagerer, Georg Groh  

**一句话要点**：提出AgentHeLLM威胁建模框架，以解决车载LLM助手在代理间通信中的安全挑战。

**关键词**：代理间威胁, 威胁建模, 车载LLM助手, 人本资产分类, 攻击路径分析, 安全关键系统

## 3 点简述
- 核心问题：现有AI安全框架在安全关键系统中缺乏资产与攻击路径的严格分离，导致车载LLM助手面临代理间威胁。
- 方法要点：基于人本资产分类和形式化图模型，区分毒化路径与触发路径，实现资产识别与攻击路径分析的分离。
- 实验或效果：开发开源攻击路径生成工具，通过双层搜索策略自动化多阶段威胁发现，验证框架实用性。

## 摘要（原文）

> The integration of Large Language Model (LLM)-based conversational agents into vehicles creates novel security challenges at the intersection of agentic AI, automotive safety, and inter-agent communication. As these intelligent assistants coordinate with external services via protocols such as Google's Agent-to-Agent (A2A), they establish attack surfaces where manipulations can propagate through natural language payloads, potentially causing severe consequences ranging from driver distraction to unauthorized vehicle control. Existing AI security frameworks, while foundational, lack the rigorous "separation of concerns" standard in safety-critical systems engineering by co-mingling the concepts of what is being protected (assets) with how it is attacked (attack paths). This paper addresses this methodological gap by proposing a threat modeling framework called AgentHeLLM (Agent Hazard Exploration for LLM Assistants) that formally separates asset identification from attack path analysis. We introduce a human-centric asset taxonomy derived from harm-oriented "victim modeling" and inspired by the Universal Declaration of Human Rights, and a formal graph-based model that distinguishes poison paths (malicious data propagation) from trigger paths (activation actions). We demonstrate the framework's practical applicability through an open-source attack path suggestion tool AgentHeLLM Attack Path Generator that automates multi-stage threat discovery using a bi-level search strategy.

