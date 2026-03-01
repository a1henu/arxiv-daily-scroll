---
layout: default
title: General Agent Evaluation
---

# General Agent Evaluation
**arXiv**：[2602.22953v1](https://arxiv.org/abs/2602.22953) · [PDF](https://arxiv.org/pdf/2602.22953.pdf)  
**作者**：Elron Bandel, Asaf Yehudai, Lilach Eden, Yehoshua Sagron, Yotam Perlitz, Elad Venezian, Natalia Razinkov, Natan Ergas, Shlomit Shachor Ifergan, Segev Shlomov, Michal Jacovi, Leshem Choshen, Liat Ein-Dor, Yoav Katz, Michal Shmueli-Scheuer  

**一句话要点**：提出通用智能体评估框架以解决跨环境性能系统评测问题

**关键词**：通用智能体评估, 统一协议, Exgentic框架, 性能基准, 跨环境泛化, 智能体评测

## 3 点简述
- 核心问题：现有智能体多为专用，缺乏通用性能的系统评估方法
- 方法要点：提出统一协议和Exgentic框架，支持智能体与基准的无缝集成
- 实验或效果：在六个环境中评测五个智能体，显示通用智能体性能接近专用智能体

## 摘要（原文）

> The promise of general-purpose agents - systems that perform tasks in unfamiliar environments without domain-specific engineering - remains largely unrealized. Existing agents are predominantly specialized, and while emerging implementations like OpenAI SDK Agent and Claude Code hint at broader capabilities, no systematic evaluation of their general performance has been pursued. Current agentic benchmarks assume domain-specific integration, encoding task information in ways that preclude fair evaluation of general agents. This paper frames general-agent evaluation as a first-class research objective. We propose conceptual principles for such evaluation, a Unified Protocol enabling agent-benchmark integration, and Exgentic - a practical framework for general agent evaluation. We benchmark five prominent agent implementations across six environments as the first Open General Agent Leaderboard. Our experiments show that general agents generalize across diverse environments, achieving performance comparable to domain-specific agents without any environment-specific tuning. We release our evaluation protocol, framework, and leaderboard to establish a foundation for systematic research on general-purpose agents.

