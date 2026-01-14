---
layout: default
title: Semantic Laundering in AI Agent Architectures: Why Tool Boundaries Do Not Confer Epistemic Warrant
---

# Semantic Laundering in AI Agent Architectures: Why Tool Boundaries Do Not Confer Epistemic Warrant
**arXiv**：[2601.08333v1](https://arxiv.org/abs/2601.08333) · [PDF](https://arxiv.org/pdf/2601.08333.pdf)  
**作者**：Oleg Romanchuk, Roman Bondar  

**一句话要点**：提出语义清洗概念以揭示AI代理架构中工具边界无法保证认知正当性的问题

**关键词**：语义清洗, AI代理架构, 认知正当性, 盖梯尔问题, 工具边界, 自许可定理

## 3 点简述
- 核心问题：LLM代理架构混淆信息传输与认知正当性机制，导致无或弱正当性命题被系统接受
- 方法要点：形式化语义清洗为架构性失败模式，证明其构成盖梯尔问题的架构实现
- 实验或效果：提出不可避免自许可定理，显示扩展、模型改进等方案无法消除类型级问题

## 摘要（原文）

> LLM-based agent architectures systematically conflate information transport mechanisms with epistemic justification mechanisms. We formalize this class of architectural failures as semantic laundering: a pattern where propositions with absent or weak warrant are accepted by the system as admissible by crossing architecturally trusted interfaces. We show that semantic laundering constitutes an architectural realization of the Gettier problem: propositions acquire high epistemic status without a connection between their justification and what makes them true. Unlike classical Gettier cases, this effect is not accidental; it is architecturally determined and systematically reproducible. The central result is the Theorem of Inevitable Self-Licensing: under standard architectural assumptions, circular epistemic justification cannot be eliminated. We introduce the Warrant Erosion Principle as the fundamental explanation for this effect and show that scaling, model improvement, and LLM-as-judge schemes are structurally incapable of eliminating a problem that exists at the type level.

