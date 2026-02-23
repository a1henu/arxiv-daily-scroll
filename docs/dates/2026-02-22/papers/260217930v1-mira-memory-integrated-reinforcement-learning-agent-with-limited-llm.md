---
layout: default
title: MIRA: Memory-Integrated Reinforcement Learning Agent with Limited LLM Guidance
---

# MIRA: Memory-Integrated Reinforcement Learning Agent with Limited LLM Guidance
**arXiv**：[2602.17930v1](https://arxiv.org/abs/2602.17930) · [PDF](https://arxiv.org/pdf/2602.17930.pdf)  
**作者**：Narjes Nourzad, Carlee Joe-Wong  

**一句话要点**：提出MIRA，通过结构化记忆图整合LLM指导，以解决稀疏奖励环境中强化学习样本复杂度高的问题。

**关键词**：强化学习, 稀疏奖励, 记忆图, 大语言模型指导, 效用信号, 样本效率

## 3 点简述
- 核心问题：稀疏或延迟奖励环境中，强化学习代理样本复杂度高，依赖LLM监督可能不可靠且扩展性受限。
- 方法要点：构建动态记忆图，存储高回报经验和LLM输出，通过效用信号软调整优势估计，引导早期训练。
- 实验或效果：在稀疏奖励环境中超越基线，达到与频繁LLM监督方法相当的回报，同时显著减少在线LLM查询。

## 摘要（原文）

> Reinforcement learning (RL) agents often suffer from high sample complexity in sparse or delayed reward settings due to limited prior structure. Large language models (LLMs) can provide subgoal decompositions, plausible trajectories, and abstract priors that facilitate early learning. However, heavy reliance on LLM supervision introduces scalability constraints and dependence on potentially unreliable signals. We propose MIRA (Memory-Integrated Reinforcement Learning Agent), which incorporates a structured, evolving memory graph to guide early training. The graph stores decision-relevant information, including trajectory segments and subgoal structures, and is constructed from both the agent's high-return experiences and LLM outputs. This design amortizes LLM queries into a persistent memory rather than requiring continuous real-time supervision. From this memory graph, we derive a utility signal that softly adjusts advantage estimation to influence policy updates without modifying the underlying reward function. As training progresses, the agent's policy gradually surpasses the initial LLM-derived priors, and the utility term decays, preserving standard convergence guarantees. We provide theoretical analysis showing that utility-based shaping improves early-stage learning in sparse-reward environments. Empirically, MIRA outperforms RL baselines and achieves returns comparable to approaches that rely on frequent LLM supervision, while requiring substantially fewer online LLM queries. Project webpage: https://narjesno.github.io/MIRA/

