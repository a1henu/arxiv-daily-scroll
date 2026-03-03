---
layout: default
title: Expanding LLM Agent Boundaries with Strategy-Guided Exploration
---

# Expanding LLM Agent Boundaries with Strategy-Guided Exploration
**arXiv**：[2603.02045v1](https://arxiv.org/abs/2603.02045) · [PDF](https://arxiv.org/pdf/2603.02045.pdf)  
**作者**：Andrew Szot, Michael Kirchhof, Omar Attia, Alexander Toshev  

**一句话要点**：提出策略引导探索以解决LLM智能体在强化学习中的探索挑战

**关键词**：LLM智能体, 强化学习, 策略引导探索, 语言-动作空间, 探索多样性

## 3 点简述
- 核心问题：LLM智能体在语言-动作空间中探索困难，因观察复杂且奖励稀疏。
- 方法要点：通过生成自然语言策略引导探索，从低级动作转向高级策略空间。
- 实验或效果：在UI交互、工具调用、编码和具身智能体环境中，SGE优于基线，提升学习效率和最终性能。

## 摘要（原文）

> Reinforcement learning (RL) has demonstrated notable success in post-training large language models (LLMs) as agents for tasks such as computer use, tool calling, and coding. However, exploration remains a central challenge in RL for LLM agents, especially as they operate in language-action spaces with complex observations and sparse outcome rewards. In this work, we address exploration for LLM agents by leveraging the ability of LLMs to plan and reason in language about the environment to shift exploration from low-level actions to higher-level language strategies. We thus propose Strategy-Guided Exploration (SGE), which first generates a concise natural-language strategy that describes what to do to make progress toward the goal, and then generates environment actions conditioned on that strategy. By exploring in the space of strategies rather than the space of actions, SGE induces structured and diverse exploration that targets different environment outcomes. To increase strategy diversity during RL, SGE introduces mixed-temperature sampling, which explores diverse strategies in parallel, along with a strategy reflection process that grounds strategy generation on the outcomes of previous strategies in the environment. Across UI interaction, tool-calling, coding, and embodied agent environments, SGE consistently outperforms exploration-focused RL baselines, improving both learning efficiency and final performance. We show that SGE enables the agent to learn to solve tasks too difficult for the base model.

