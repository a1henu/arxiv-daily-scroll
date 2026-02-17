---
layout: default
title: Evolutionary System Prompt Learning can Facilitate Reinforcement Learning for LLMs
---

# Evolutionary System Prompt Learning can Facilitate Reinforcement Learning for LLMs
**arXiv**：[2602.14697v1](https://arxiv.org/abs/2602.14697) · [PDF](https://arxiv.org/pdf/2602.14697.pdf)  
**作者**：Lunjun Zhang, Ryan Chen, Bradly C. Stadie  

**一句话要点**：提出进化系统提示学习以联合优化大语言模型的上下文与权重

**关键词**：进化系统提示学习, 强化学习, 大语言模型, 自主改进, 上下文优化, 权重更新

## 3 点简述
- 核心问题：大语言模型自主改进主要依赖上下文更新与权重更新，但两者常分离。
- 方法要点：在强化学习迭代中并行选择多个系统提示进行rollout，结合权重更新与基于LLM的进化提示更新。
- 实验或效果：在推理与代理任务中提升性能，如AIME到BeyondAIME泛化中成功率从38.8%提升至45.1%。

## 摘要（原文）

> Building agentic systems that can autonomously self-improve from experience is a longstanding goal of AI. Large language models (LLMs) today primarily self-improve via two mechanisms: self-reflection for context updates, and reinforcement learning (RL) for weight updates. In this work, we propose Evolutionary System Prompt Learning (E-SPL), a method for jointly improving model contexts and model weights. In each RL iteration, E-SPL selects multiple system prompts and runs rollouts with each in parallel. It applies RL updates to model weights conditioned on each system prompt, and evolutionary updates to the system prompt population via LLM-driven mutation and crossover. Each system prompt has a TrueSkill rating for evolutionary selection, updated from relative performance within each RL iteration batch. E-SPL encourages a natural division between declarative knowledge encoded in prompts and procedural knowledge encoded in weights, resulting in improved performance across reasoning and agentic tasks. For instance, in an easy-to-hard (AIME $\rightarrow$ BeyondAIME) generalization setting, E-SPL improves RL success rate from 38.8% $\rightarrow$ 45.1% while also outperforming reflective prompt evolution (40.0%). Overall, our results show that coupling reinforcement learning with system prompt evolution yields consistent gains in sample efficiency and generalization. Code: https://github.com/LunjunZhang/E-SPL

