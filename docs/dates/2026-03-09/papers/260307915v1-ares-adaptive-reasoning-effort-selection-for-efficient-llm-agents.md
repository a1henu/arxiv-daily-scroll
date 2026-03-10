---
layout: default
title: Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents
---

# Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents
**arXiv**：[2603.07915v1](https://arxiv.org/abs/2603.07915) · [PDF](https://arxiv.org/pdf/2603.07915.pdf)  
**作者**：Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, Shiyu Chang  

**一句话要点**：提出Ares框架以解决多步智能体任务中动态选择推理努力的问题

**关键词**：LLM智能体, 动态推理选择, 成本效率优化, 多步任务, 轻量级路由器

## 3 点简述
- 核心问题：静态推理努力策略在LLM智能体中导致成本高或性能下降
- 方法要点：使用轻量级路由器基于交互历史动态预测每步最低合适推理努力
- 实验或效果：在多种任务上减少推理令牌使用达52.7%，任务成功率下降最小

## 摘要（原文）

> Modern agents powered by thinking LLMs achieve high accuracy through long chain-of-thought reasoning but incur substantial inference costs. While many LLMs now support configurable reasoning levels (e.g., high/medium/low), static strategies are often ineffective: using low-effort modes at every step leads to significant performance degradation, while random selection fails to preserve accuracy or provide meaningful cost reduction. However, agents should reserve high reasoning effort for difficult steps like navigating complex website structures, while using lower-effort modes for simpler steps like opening a target URL. In this paper, we propose Ares, a framework for per-step dynamic reasoning effort selection tailored for multi-step agent tasks. Ares employs a lightweight router to predict the lowest appropriate reasoning level for each step based on the interaction history. To train this router, we develop a data generation pipeline that identifies the minimum reasoning effort required for successful step completion. We then fine-tune the router to predict these levels, enabling plug-and-play integration for any LLM agents. We evaluate Ares on a diverse set of agent tasks, including TAU-Bench for tool use agents, BrowseComp-Plus for deep-research agents, and WebArena for web agents. Experimental results show that Ares reduces reasoning token usage by up to 52.7% compared to fixed high-effort reasoning, while introducing minimal degradation in task success rates.

