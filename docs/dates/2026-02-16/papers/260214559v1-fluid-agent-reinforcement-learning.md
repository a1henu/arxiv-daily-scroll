---
layout: default
title: Fluid-Agent Reinforcement Learning
---

# Fluid-Agent Reinforcement Learning
**arXiv**：[2602.14559v1](https://arxiv.org/abs/2602.14559) · [PDF](https://arxiv.org/pdf/2602.14559.pdf)  
**作者**：Shishir Sharma, Doina Precup, Theodore J. Perkins  

**一句话要点**：提出流体智能体强化学习框架，以解决动态智能体数量环境中的多智能体交互问题。

**关键词**：多智能体强化学习, 流体智能体环境, 动态智能体生成, 博弈论, 自适应团队规模

## 3 点简述
- 核心问题：现实世界中智能体数量不固定且未知，现有MARL方法难以处理动态创建智能体的场景。
- 方法要点：基于博弈论提出流体智能体环境框架，允许智能体动态生成其他智能体，支持自适应团队规模调整。
- 实验或效果：在Predator-Prey等基准测试中验证，展示流体环境能解锁固定群体设置外的新策略，动态匹配环境需求。

## 摘要（原文）

> The primary focus of multi-agent reinforcement learning (MARL) has been to study interactions among a fixed number of agents embedded in an environment. However, in the real world, the number of agents is neither fixed nor known a priori. Moreover, an agent can decide to create other agents (for example, a cell may divide, or a company may spin off a division). In this paper, we propose a framework that allows agents to create other agents; we call this a fluid-agent environment. We present game-theoretic solution concepts for fluid-agent games and empirically evaluate the performance of several MARL algorithms within this framework. Our experiments include fluid variants of established benchmarks such as Predator-Prey and Level-Based Foraging, where agents can dynamically spawn, as well as a new environment we introduce that highlights how fluidity can unlock novel solution strategies beyond those observed in fixed-population settings. We demonstrate that this framework yields agent teams that adjust their size dynamically to match environmental demands.

