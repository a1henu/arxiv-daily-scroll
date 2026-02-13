---
layout: default
title: Learning to Configure Agentic AI Systems
---

# Learning to Configure Agentic AI Systems
**arXiv**：[2602.11574v1](https://arxiv.org/abs/2602.11574) · [PDF](https://arxiv.org/pdf/2602.11574.pdf)  
**作者**：Aditya Taparia, Som Sagar, Ransalu Senanayake  

**一句话要点**：提出ARC以动态配置基于LLM的智能体系统，提升任务准确率并降低计算成本。

**关键词**：智能体配置, 强化学习, 查询级决策, 资源优化, LLM系统

## 3 点简述
- 核心问题：固定配置导致智能体系统在易难查询中行为脆弱且计算冗余。
- 方法要点：将配置视为查询级决策问题，通过强化学习学习轻量级分层策略。
- 实验或效果：在多个基准测试中，ARC比基线方法任务准确率提升高达25%，同时减少令牌和运行时间成本。

## 摘要（原文）

> Configuring LLM-based agent systems involves choosing workflows, tools, token budgets, and prompts from a large combinatorial design space, and is typically handled today by fixed large templates or hand-tuned heuristics. This leads to brittle behavior and unnecessary compute, since the same cumbersome configuration is often applied to both easy and hard input queries. We formulate agent configuration as a query-wise decision problem and introduce ARC (Agentic Resource & Configuration learner), which learns a light-weight hierarchical policy using reinforcement learning to dynamically tailor these configurations. Across multiple benchmarks spanning reasoning and tool-augmented question answering, the learned policy consistently outperforms strong hand-designed and other baselines, achieving up to 25% higher task accuracy while also reducing token and runtime costs. These results demonstrate that learning per-query agent configurations is a powerful alternative to "one size fits all" designs.

