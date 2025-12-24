---
layout: default
title: Synthesizing Procedural Memory: Challenges and Architectures in Automated Workflow Generation
---

# Synthesizing Procedural Memory: Challenges and Architectures in Automated Workflow Generation
**arXiv**：[2512.20278v1](https://arxiv.org/abs/2512.20278) · [PDF](https://arxiv.org/pdf/2512.20278.pdf)  
**作者**：Nishant Gaurav, Adit Akarsh, Ankit Ranjan, Manoj Bajaj  

**一句话要点**：提出基于假设-探测-编码方法的自动化工作流生成架构，解决跨服务编排中的结构瓶颈问题。

**关键词**：程序记忆合成, 自动化工作流生成, 大语言模型架构, 跨服务编排, 代码技能生成

## 3 点简述
- 核心问题：从零自主合成程序记忆的机制未充分探索，涉及工具发现、验证、分解和扩展瓶颈。
- 方法要点：通过线性状态锚定等方法，将大语言模型从被动工具使用者转变为主动工作流架构师。
- 实验或效果：在Outlook和OneDrive的跨服务编排案例中，展示代理能自主编写稳健的生产级代码技能。

## 摘要（原文）

> While CodeMem establishes executable code as the optimal representation for agentic procedural memory, the mechanism for autonomously synthesizing this memory from a blank slate remains underexplored. This paper operationalizes the transition of Large Language Models from passive tool-users to active workflow architects. Through a high-fidelity case study of a cross-service orchestration task involving Outlook and OneDrive, we identify and address four structural bottlenecks in automated skill generation: the Discovery Gap involving navigation of large tool registries, the Verification Gap regarding grounding tool response structures, the Decomposition Gap which replaces inefficient search with Linear State Anchoring, and the Scaling Gap focused on concurrency and persistence. We demonstrate that by enforcing a scientific methodology of hypothesize, probe, and code, agents can autonomously write robust, production-grade code skills.

