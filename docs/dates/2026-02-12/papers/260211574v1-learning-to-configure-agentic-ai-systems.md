---
layout: default
title: Learning to Configure Agentic AI Systems
---

# Learning to Configure Agentic AI Systems
**arXiv**：[2602.11574v1](https://arxiv.org/abs/2602.11574) · [PDF](https://arxiv.org/pdf/2602.11574.pdf)  
**作者**：Aditya Taparia, Som Sagar, Ransalu Senanayake  

**一句话要点**：提出ARC学习器，通过强化学习动态配置基于LLM的智能体系统，以解决固定模板导致的脆弱性和计算浪费问题。

**关键词**：智能体配置学习, 强化学习策略, 查询级决策, LLM系统优化, 资源动态分配

## 3 点简述
- 核心问题：基于LLM的智能体系统配置通常依赖固定模板或手动启发式，导致脆弱行为和计算浪费。
- 方法要点：将智能体配置建模为查询级决策问题，使用强化学习学习轻量级分层策略，动态调整工作流、工具和提示。
- 实验或效果：在推理和工具增强问答基准上，ARC策略优于基线，任务准确率提升达25%，同时降低令牌和运行时成本。

## 摘要（原文）

> Configuring LLM-based agent systems involves choosing workflows, tools, token budgets, and prompts from a large combinatorial design space, and is typically handled today by fixed large templates or hand-tuned heuristics. This leads to brittle behavior and unnecessary compute, since the same cumbersome configuration is often applied to both easy and hard input queries. We formulate agent configuration as a query-wise decision problem and introduce ARC (Agentic Resource & Configuration learner), which learns a light-weight hierarchical policy using reinforcement learning to dynamically tailor these configurations. Across multiple benchmarks spanning reasoning and tool-augmented question answering, the learned policy consistently outperforms strong hand-designed and other baselines, achieving up to 25% higher task accuracy while also reducing token and runtime costs. These results demonstrate that learning per-query agent configurations is a powerful alternative to "one size fits all" designs.

