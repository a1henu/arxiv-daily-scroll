---
layout: default
title: SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
---

# SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
**arXiv**：[2512.15374v1](https://arxiv.org/abs/2512.15374) · [PDF](https://arxiv.org/pdf/2512.15374.pdf)  
**作者**：Zehua Pei, Hui-Ling Zhen, Shixiong Kai, Sinno Jialin Pan, Yunhe Wang, Mingxuan Yuan, Bei Yu  

**一句话要点**：提出SCOPE框架，通过提示演化优化LLM代理在动态上下文中的性能。

**关键词**：提示演化, 上下文管理, 在线优化, LLM代理, 双流机制

## 3 点简述
- 核心问题：LLM代理的静态提示无法有效管理动态上下文，导致纠正和增强失败。
- 方法要点：将上下文管理建模为在线优化问题，采用双流机制平衡战术与战略演化。
- 实验或效果：在HLE基准上，任务成功率从14.23%提升至38.64%。

## 摘要（原文）

> Large Language Model (LLM) agents are increasingly deployed in environments that generate massive, dynamic contexts. However, a critical bottleneck remains: while agents have access to this context, their static prompts lack the mechanisms to manage it effectively, leading to recurring Corrective and Enhancement failures. To address this capability gap, we introduce \textbf{SCOPE} (Self-evolving Context Optimization via Prompt Evolution). SCOPE frames context management as an \textit{online optimization} problem, synthesizing guidelines from execution traces to automatically evolve the agent's prompt. We propose a Dual-Stream mechanism that balances tactical specificity (resolving immediate errors) with strategic generality (evolving long-term principles). Furthermore, we introduce Perspective-Driven Exploration to maximize strategy coverage, increasing the likelihood that the agent has the correct strategy for any given task. Experiments on the HLE benchmark show that SCOPE improves task success rates from 14.23\% to 38.64\% without human intervention. We make our code publicly available at https://github.com/JarvisPei/SCOPE.

