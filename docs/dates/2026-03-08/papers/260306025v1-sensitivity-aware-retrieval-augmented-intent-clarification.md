---
layout: default
title: Sensitivity-Aware Retrieval-Augmented Intent Clarification
---

# Sensitivity-Aware Retrieval-Augmented Intent Clarification
**arXiv**：[2603.06025v1](https://arxiv.org/abs/2603.06025) · [PDF](https://arxiv.org/pdf/2603.06025.pdf)  
**作者**：Maik Larooij  

**一句话要点**：提出敏感感知检索增强意图澄清方法，以保护敏感领域信息并平衡系统效用

**关键词**：检索增强意图澄清, 敏感信息保护, 攻击模型, 防御机制, 系统效用评估, 对话搜索系统

## 3 点简述
- 核心问题：在敏感领域如医疗、政府中，检索增强意图澄清可能泄露敏感信息，需保护隐私。
- 方法要点：通过定义攻击模型、设计检索级敏感感知防御机制，开发评估方法权衡保护与效用。
- 实验或效果：未知具体实验，但旨在提升澄清性能同时确保敏感数据安全，适用于LLM知识不足的领域。

## 摘要（原文）

> In conversational search systems, a key component is to determine and clarify the intent behind complex queries. We view intent clarification in light of the exploratory search paradigm, where users, through an iterative, evolving process of selection, exploration and retrieval, transform a visceral or conscious need into a formalized one. Augmenting the clarification component with a retrieval step (retrieval-augmented intent clarification) can seriously enhance clarification performance, especially in domains where Large Language Models (LLMs) lack parametric knowledge. However, in more sensitive domains, such as healthcare, government (e.g. FOIA search) or legal contexts, the retrieval database may contain sensitive information that needs protection. In this paper, we explore the research challenge of developing a retrieval-augmented conversational agent that can act as a mediator and gatekeeper for the sensitive collection. To do that, we also need to know what we are protecting and against what. We propose to tackle this research challenge in three steps: 1) define an attack model, 2) design sensitivity-aware defenses on the retrieval level and 3) develop evaluation methods to measure the trade-off between the level of protection and the system's utility.

