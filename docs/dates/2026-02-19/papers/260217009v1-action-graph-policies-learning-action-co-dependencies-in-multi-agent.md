---
layout: default
title: Action-Graph Policies: Learning Action Co-dependencies in Multi-Agent Reinforcement Learning
---

# Action-Graph Policies: Learning Action Co-dependencies in Multi-Agent Reinforcement Learning
**arXiv**：[2602.17009v1](https://arxiv.org/abs/2602.17009) · [PDF](https://arxiv.org/pdf/2602.17009.pdf)  
**作者**：Nikunj Gupta, James Zachary Hare, Jesse Milzman, Rajgopal Kannan, Viktor Prasanna  

**一句话要点**：提出动作图策略以解决多智能体强化学习中动作协调依赖问题

**关键词**：多智能体强化学习, 动作协调, 策略学习, 部分可观测环境, 反协调惩罚

## 3 点简述
- 核心问题：多智能体决策需协调动作以避免冲突并满足全局约束
- 方法要点：构建协调上下文，建模智能体间动作依赖关系，提升策略表达能力
- 实验或效果：在部分可观测和反协调任务中，成功率显著优于基线方法

## 摘要（原文）

> Coordinating actions is the most fundamental form of cooperation in multi-agent reinforcement learning (MARL). Successful decentralized decision-making often depends not only on good individual actions, but on selecting compatible actions across agents to synchronize behavior, avoid conflicts, and satisfy global constraints. In this paper, we propose Action Graph Policies (AGP), that model dependencies among agents' available action choices. It constructs, what we call, \textit{coordination contexts}, that enable agents to condition their decisions on global action dependencies. Theoretically, we show that AGPs induce a strictly more expressive joint policy compared to fully independent policies and can realize coordinated joint actions that are provably more optimal than greedy execution even from centralized value-decomposition methods. Empirically, we show that AGP achieves 80-95\% success on canonical coordination tasks with partial observability and anti-coordination penalties, where other MARL methods reach only 10-25\%. We further demonstrate that AGP consistently outperforms these baselines in diverse multi-agent environments.

