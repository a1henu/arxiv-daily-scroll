---
layout: default
title: Learning the Value Systems of Agents with Preference-based and Inverse Reinforcement Learning
---

# Learning the Value Systems of Agents with Preference-based and Inverse Reinforcement Learning
**arXiv**：[2602.04518v1](https://arxiv.org/abs/2602.04518) · [PDF](https://arxiv.org/pdf/2602.04518.pdf)  
**作者**：Andrés Holgado-Sánchez, Holger Billhardt, Alberto Fernández, Sascha Ossowski  

**一句话要点**：提出基于偏好学习和逆强化学习的方法，以自动学习自主软件代理的价值系统。

**关键词**：价值系统学习, 偏好学习, 逆强化学习, 多目标马尔可夫决策过程, 自主软件代理, 伦理对齐

## 3 点简述
- 核心问题：在开放计算机系统中，确保自主代理的协议符合伦理原则和不同价值系统，但人工指定价值系统难以扩展。
- 方法要点：基于多目标马尔可夫决策过程，形式化价值系统学习问题，并设计偏好学习和逆强化学习算法来推断价值基础函数。
- 实验或效果：通过两个模拟用例进行说明和评估，验证方法的可行性。

## 摘要（原文）

> Agreement Technologies refer to open computer systems in which autonomous software agents interact with one another, typically on behalf of humans, in order to come to mutually acceptable agreements. With the advance of AI systems in recent years, it has become apparent that such agreements, in order to be acceptable to the involved parties, must remain aligned with ethical principles and moral values. However, this is notoriously difficult to ensure, especially as different human users (and their software agents) may hold different value systems, i.e. they may differently weigh the importance of individual moral values. Furthermore, it is often hard to specify the precise meaning of a value in a particular context in a computational manner. Methods to estimate value systems based on human-engineered specifications, e.g. based on value surveys, are limited in scale due to the need for intense human moderation. In this article, we propose a novel method to automatically \emph{learn} value systems from observations and human demonstrations. In particular, we propose a formal model of the \emph{value system learning} problem, its instantiation to sequential decision-making domains based on multi-objective Markov decision processes, as well as tailored preference-based and inverse reinforcement learning algorithms to infer value grounding functions and value systems. The approach is illustrated and evaluated by two simulated use cases.

