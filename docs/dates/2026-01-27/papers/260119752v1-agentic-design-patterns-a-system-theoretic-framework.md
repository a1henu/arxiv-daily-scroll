---
layout: default
title: Agentic Design Patterns: A System-Theoretic Framework
---

# Agentic Design Patterns: A System-Theoretic Framework
**arXiv**：[2601.19752v1](https://arxiv.org/abs/2601.19752) · [PDF](https://arxiv.org/pdf/2601.19752.pdf)  
**作者**：Minh-Dung Dao, Quy Minh Le, Hoang Thanh Lam, Duc-Trong Le, Quoc-Viet Pham, Barry O'Sullivan, Hoang D. Nguyen  

**一句话要点**：提出基于系统理论的框架和12种设计模式，以解决智能体系统设计中的不可靠性和随意性问题。

**关键词**：智能体系统设计, 系统理论框架, 设计模式, 自主系统, 模块化架构

## 3 点简述
- 核心问题：现有智能体设计模式缺乏系统理论基础，导致应用不可靠和脆弱。
- 方法要点：将智能体系统解构为五个核心功能子系统，并映射出12种可重用设计模式。
- 实验或效果：通过ReAct框架案例研究，展示模式如何纠正系统架构缺陷。

## 摘要（原文）

> With the development of foundation model (FM), agentic AI systems are getting more attention, yet their inherent issues like hallucination and poor reasoning, coupled with the frequent ad-hoc nature of system design, lead to unreliable and brittle applications. Existing efforts to characterise agentic design patterns often lack a rigorous systems-theoretic foundation, resulting in high-level or convenience-based taxonomies that are difficult to implement. This paper addresses this gap by introducing a principled methodology for engineering robust AI agents. We propose two primary contributions: first, a novel system-theoretic framework that deconstructs an agentic AI system into five core, interacting functional subsystems: Reasoning & World Model, Perception & Grounding, Action Execution, Learning & Adaptation, and Inter-Agent Communication. Second, derived from this architecture and directly mapped to a comprehensive taxonomy of agentic challenges, we present a collection of 12 agentic design patterns. These patterns - categorised as Foundational, Cognitive & Decisional, Execution & Interaction, and Adaptive & Learning - offer reusable, structural solutions to recurring problems in agent design. The utility of the framework is demonstrated by a case study on the ReAct framework, showing how the proposed patterns can rectify systemic architectural deficiencies. This work provides a foundational language and a structured methodology to standardise agentic design communication among researchers and engineers, leading to more modular, understandable, and reliable autonomous systems.

