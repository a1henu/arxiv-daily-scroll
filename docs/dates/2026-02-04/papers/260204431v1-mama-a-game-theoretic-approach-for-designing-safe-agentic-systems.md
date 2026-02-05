---
layout: default
title: MaMa: A Game-Theoretic Approach for Designing Safe Agentic Systems
---

# MaMa: A Game-Theoretic Approach for Designing Safe Agentic Systems
**arXiv**：[2602.04431v1](https://arxiv.org/abs/2602.04431) · [PDF](https://arxiv.org/pdf/2602.04431.pdf)  
**作者**：Jonathan Nöther, Adish Singla, Goran Radanovic  

**一句话要点**：提出MaMa算法，基于博弈论设计安全的多智能体系统以抵御对抗性攻击

**关键词**：多智能体系统安全, Stackelberg博弈, LLM对抗搜索, 自动化系统设计, 安全泛化

## 3 点简述
- 核心问题：LLM多智能体系统在部分智能体被攻击时存在安全风险，需自动化设计安全系统
- 方法要点：将安全设计建模为Stackelberg安全博弈，使用LLM对抗搜索迭代优化系统设计
- 实验或效果：在多样环境中，MaMa设计的系统能抵御最坏情况攻击，保持任务性能，并泛化到未知攻击

## 摘要（原文）

> LLM-based multi-agent systems have demonstrated impressive capabilities, but they also introduce significant safety risks when individual agents fail or behave adversarially. In this work, we study the automated design of agentic systems that remain safe even when a subset of agents is compromised. We formalize this challenge as a Stackelberg security game between a system designer (the Meta-Agent) and a best-responding Meta-Adversary that selects and compromises a subset of agents to minimize safety. We propose Meta-Adversary-Meta-Agent (MaMa), a novel algorithm for approximately solving this game and automatically designing safe agentic systems. Our approach uses LLM-based adversarial search, where the Meta-Agent iteratively proposes system designs and receives feedback based on the strongest attacks discovered by the Meta-Adversary. Empirical evaluations across diverse environments show that systems designed with MaMa consistently defend against worst-case attacks while maintaining performance comparable to systems optimized solely for task success. Moreover, the resulting systems generalize to stronger adversaries, as well as ones with different attack objectives or underlying LLMs, demonstrating robust safety beyond the training setting.

