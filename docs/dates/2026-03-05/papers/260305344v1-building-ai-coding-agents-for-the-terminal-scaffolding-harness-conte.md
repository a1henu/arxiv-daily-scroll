---
layout: default
title: Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned
---

# Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned
**arXiv**：[2603.05344v1](https://arxiv.org/abs/2603.05344) · [PDF](https://arxiv.org/pdf/2603.05344.pdf)  
**作者**：Nghi D. Q. Bui  

**一句话要点**：提出OPENDEV终端原生AI编码代理，通过复合系统架构解决长时程开发中的安全与上下文管理问题。

**关键词**：AI编码代理, 终端原生系统, 上下文管理, 复合AI架构, 自主软件工程

## 3 点简述
- 核心问题：终端AI编码代理需应对上下文膨胀和推理退化，确保安全与高效。
- 方法要点：采用复合AI系统架构，包括模型路由、双代理设计、惰性工具发现和自适应上下文压缩。
- 实验或效果：提供开源实现，支持跨会话知识积累和事件驱动提醒，增强自主软件工程基础。

## 摘要（原文）

> The landscape of AI coding assistance is undergoing a fundamental shift from complex IDE plugins to versatile, terminal-native agents. Operating directly where developers manage source control, execute builds, and deploy environments, CLI-based agents offer unprecedented autonomy for long-horizon development tasks. In this paper, we present OPENDEV, an open-source, command-line coding agent engineered specifically for this new paradigm. Effective autonomous assistance requires strict safety controls and highly efficient context management to prevent context bloat and reasoning degradation. OPENDEV overcomes these challenges through a compound AI system architecture with workload-specialized model routing, a dual-agent architecture separating planning from execution, lazy tool discovery, and adaptive context compaction that progressively reduces older observations. Furthermore, it employs an automated memory system to accumulate project-specific knowledge across sessions and counteracts instruction fade-out through event-driven system reminders. By enforcing explicit reasoning phases and prioritizing context efficiency, OPENDEV provides a secure, extensible foundation for terminal-first AI assistance, offering a blueprint for robust autonomous software engineering.

