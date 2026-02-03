---
layout: default
title: Constrained Process Maps for Multi-Agent Generative AI Workflows
---

# Constrained Process Maps for Multi-Agent Generative AI Workflows
**arXiv**：[2602.02034v1](https://arxiv.org/abs/2602.02034) · [PDF](https://arxiv.org/pdf/2602.02034.pdf)  
**作者**：Ananya Joshi, Michael Rudow  

**一句话要点**：提出基于有限时域MDP的多智能体系统，以优化受监管场景下的生成式AI工作流。

**关键词**：多智能体系统, 有限时域MDP, 生成式AI工作流, 合规场景, 不确定性量化, AI安全评估

## 3 点简述
- 问题：单智能体架构难以观察不确定性处理和跨阶段协调，尤其在合规等受监管场景。
- 方法：将多智能体系统形式化为有向无环MDP，每个智能体对应特定角色，量化不确定性并定义状态转移。
- 效果：在AI安全评估案例中，相比单智能体基线，准确率提升达19%，人工审核需求减少达85倍。

## 摘要（原文）

> Large language model (LLM)-based agents are increasingly used to perform complex, multi-step workflows in regulated settings such as compliance and due diligence. However, many agentic architectures rely primarily on prompt engineering of a single agent, making it difficult to observe or compare how models handle uncertainty and coordination across interconnected decision stages and with human oversight. We introduce a multi-agent system formalized as a finite-horizon Markov Decision Process (MDP) with a directed acyclic structure. Each agent corresponds to a specific role or decision stage (e.g., content, business, or legal review in a compliance workflow), with predefined transitions representing task escalation or completion. Epistemic uncertainty is quantified at the agent level using Monte Carlo estimation, while system-level uncertainty is captured by the MDP's termination in either an automated labeled state or a human-review state. We illustrate the approach through a case study in AI safety evaluation for self-harm detection, implemented as a multi-agent compliance system. Results demonstrate improvements over a single-agent baseline, including up to a 19\% increase in accuracy, up to an 85x reduction in required human review, and, in some configurations, reduced processing time.

