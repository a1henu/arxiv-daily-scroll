---
layout: default
title: The End of Reward Engineering: How LLMs Are Redefining Multi-Agent Coordination
---

# The End of Reward Engineering: How LLMs Are Redefining Multi-Agent Coordination
**arXiv**：[2601.08237v1](https://arxiv.org/abs/2601.08237) · [PDF](https://arxiv.org/pdf/2601.08237.pdf)  
**作者**：Haoran Su, Yandong Sun, Congjia Yu  

**一句话要点**：提出基于大语言模型的语言化奖励规范，以替代多智能体强化学习中的手工奖励工程

**关键词**：多智能体强化学习, 奖励工程, 大语言模型, 语义奖励规范, 动态奖励适应, 语言监督

## 3 点简述
- 核心问题：多智能体强化学习中手工奖励工程因信用分配模糊、环境非平稳和交互复杂性而困难重重
- 方法要点：利用大语言模型从自然语言描述合成奖励函数，并在线动态调整奖励，实现语义化规范
- 实验或效果：基于RLVR等实证，语言监督可作为传统奖励工程的可行替代，提升与人类意图的对齐

## 摘要（原文）

> Reward engineering, the manual specification of reward functions to induce desired agent behavior, remains a fundamental challenge in multi-agent reinforcement learning. This difficulty is amplified by credit assignment ambiguity, environmental non-stationarity, and the combinatorial growth of interaction complexity. We argue that recent advances in large language models (LLMs) point toward a shift from hand-crafted numerical rewards to language-based objective specifications. Prior work has shown that LLMs can synthesize reward functions directly from natural language descriptions (e.g., EUREKA) and adapt reward formulations online with minimal human intervention (e.g., CARD). In parallel, the emerging paradigm of Reinforcement Learning from Verifiable Rewards (RLVR) provides empirical evidence that language-mediated supervision can serve as a viable alternative to traditional reward engineering. We conceptualize this transition along three dimensions: semantic reward specification, dynamic reward adaptation, and improved alignment with human intent, while noting open challenges related to computational overhead, robustness to hallucination, and scalability to large multi-agent systems. We conclude by outlining a research direction in which coordination arises from shared semantic representations rather than explicitly engineered numerical signals.

