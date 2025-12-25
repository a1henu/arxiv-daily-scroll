---
layout: default
title: Policy-Conditioned Policies for Multi-Agent Task Solving
---

# Policy-Conditioned Policies for Multi-Agent Task Solving
**arXiv**：[2512.21024v1](https://arxiv.org/abs/2512.21024) · [PDF](https://arxiv.org/pdf/2512.21024.pdf)  
**作者**：Yue Lin, Shuhui Zhu, Wenhao Li, Ang Li, Dan Qiao, Pascal Poupart, Hongyuan Zha, Baoxiang Wang  

**一句话要点**：提出程序化迭代最佳响应算法，以解决多智能体任务中策略动态适应的表示瓶颈问题。

**关键词**：多智能体强化学习, 程序化策略表示, 大型语言模型, 迭代最佳响应, 游戏理论, 策略适应

## 3 点简述
- 核心问题：深度强化学习中，神经策略作为不透明高维参数向量，难以直接基于对手策略进行动态适应，存在表示瓶颈。
- 方法要点：将策略表示为人类可解释的源代码，利用大型语言模型作为近似解释器，通过文本梯度优化程序化策略，实现程序化迭代最佳响应。
- 实验或效果：在标准协调矩阵游戏和合作性基于等级的觅食环境中，该方法有效解决了多智能体任务。

## 摘要（原文）

> In multi-agent tasks, the central challenge lies in the dynamic adaptation of strategies. However, directly conditioning on opponents' strategies is intractable in the prevalent deep reinforcement learning paradigm due to a fundamental ``representational bottleneck'': neural policies are opaque, high-dimensional parameter vectors that are incomprehensible to other agents. In this work, we propose a paradigm shift that bridges this gap by representing policies as human-interpretable source code and utilizing Large Language Models (LLMs) as approximate interpreters. This programmatic representation allows us to operationalize the game-theoretic concept of \textit{Program Equilibrium}. We reformulate the learning problem by utilizing LLMs to perform optimization directly in the space of programmatic policies. The LLM functions as a point-wise best-response operator that iteratively synthesizes and refines the ego agent's policy code to respond to the opponent's strategy. We formalize this process as \textit{Programmatic Iterated Best Response (PIBR)}, an algorithm where the policy code is optimized by textual gradients, using structured feedback derived from game utility and runtime unit tests. We demonstrate that this approach effectively solves several standard coordination matrix games and a cooperative Level-Based Foraging environment.

