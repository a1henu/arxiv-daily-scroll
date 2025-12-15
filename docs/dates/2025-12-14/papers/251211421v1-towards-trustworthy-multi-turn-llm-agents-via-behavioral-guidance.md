---
layout: default
title: Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance
---

# Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance
**arXiv**：[2512.11421v1](https://arxiv.org/abs/2512.11421) · [PDF](https://arxiv.org/pdf/2512.11421.pdf)  
**作者**：Gonca Gürsun  

**一句话要点**：提出基于强化学习形式的多轮LLM代理框架，通过行为指导提升可信度

**关键词**：多轮LLM代理, 行为指导, 强化学习框架, 可验证推理, 约束生成

## 3 点简述
- 核心问题：多轮任务中LLM行为缺乏可靠性和可验证性
- 方法要点：集成任务分析器、推理模块和生成模块，实现行为指导与约束
- 实验或效果：组件协同进化，代理在交互中展现可信行为

## 摘要（原文）

> Large Language Models demonstrate strong reasoning and generation abilities, yet their behavior in multi-turn tasks often lacks reliability and verifiability. We present a task completion framework that enables LLM-based agents to act under explicit behavioral guidance in environments described by reinforcement learning formalisms with defined observation, action, and reward signals.
>   The framework integrates three components: a lightweight task profiler that selects reasoning and generation strategies, a reasoning module that learns verifiable observation - action mappings, and a generation module that enforces constraint-compliant outputs through validation or deterministic synthesis. We show that as the agent interacts with the environment, these components co-evolve, yielding trustworthy behavior.

