---
layout: default
title: Exploring Plan Space through Conversation: An Agentic Framework for LLM-Mediated Explanations in Planning
---

# Exploring Plan Space through Conversation: An Agentic Framework for LLM-Mediated Explanations in Planning
**arXiv**：[2603.02070v1](https://arxiv.org/abs/2603.02070) · [PDF](https://arxiv.org/pdf/2603.02070.pdf)  
**作者**：Guilhem Fouilhé, Rebecca Eifler, Antonin Poché, Sylvie Thiébaux, Nicholas Asher  

**一句话要点**：提出多智能体LLM架构以支持规划中用户交互式解释

**关键词**：规划解释, 多智能体LLM, 交互式系统, 用户研究, 目标冲突

## 3 点简述
- 核心问题：自动化规划需结合人类指导，但现有解释系统缺乏自然交互能力。
- 方法要点：设计框架无关的多智能体LLM架构，实现用户和上下文依赖的交互解释。
- 实验或效果：实例化用于目标冲突解释，用户研究比较LLM交互与模板基线界面。

## 摘要（原文）

> When automating plan generation for a real-world sequential decision problem, the goal is often not to replace the human planner, but to facilitate an iterative reasoning and elicitation process, where the human's role is to guide the AI planner according to their preferences and expertise. In this context, explanations that respond to users' questions are crucial to improve their understanding of potential solutions and increase their trust in the system. To enable natural interaction with such a system, we present a multi-agent Large Language Model (LLM) architecture that is agnostic to the explanation framework and enables user- and context-dependent interactive explanations. We also describe an instantiation of this framework for goal-conflict explanations, which we use to conduct a user study comparing the LLM-powered interaction with a baseline template-based explanation interface.

