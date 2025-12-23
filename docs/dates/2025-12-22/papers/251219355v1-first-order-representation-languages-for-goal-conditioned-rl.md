---
layout: default
title: First-Order Representation Languages for Goal-Conditioned RL
---

# First-Order Representation Languages for Goal-Conditioned RL
**arXiv**：[2512.19355v1](https://arxiv.org/abs/2512.19355) · [PDF](https://arxiv.org/pdf/2512.19355.pdf)  
**作者**：Simon Ståhlberg, Hector Geffner  

**一句话要点**：提出基于一阶语言的目标条件强化学习方法，通过原子集表示提升大实例泛化策略学习效率

**关键词**：目标条件强化学习, 一阶表示语言, 后见经验重放, 泛化策略学习, 稀疏奖励问题, 自动课程学习

## 3 点简述
- 研究目标条件强化学习中，大训练实例下稀疏奖励导致目标难以通过随机探索达成的问题
- 采用一阶语言表示状态和目标，结合后见经验重放，通过原子子集和提升版本自动构建递增复杂度目标课程
- 实验验证原子子集和提升版本能成功学习泛化策略，展示计算增益、局限性及改进机会

## 摘要（原文）

> First-order relational languages have been used in MDP planning and reinforcement learning (RL) for two main purposes: specifying MDPs in compact form, and representing and learning policies that are general and not tied to specific instances or state spaces. In this work, we instead consider the use of first-order languages in goal-conditioned RL and generalized planning. The question is how to learn goal-conditioned and general policies when the training instances are large and the goal cannot be reached by random exploration alone. The technique of Hindsight Experience Replay (HER) provides an answer to this question: it relabels unsuccessful trajectories as successful ones by replacing the original goal with one that was actually achieved. If the target policy must generalize across states and goals, trajectories that do not reach the original goal states can enable more data- and time-efficient learning. In this work, we show that further performance gains can be achieved when states and goals are represented by sets of atoms. We consider three versions: goals as full states, goals as subsets of the original goals, and goals as lifted versions of these subgoals. The result is that the latter two successfully learn general policies on large planning instances with sparse rewards by automatically creating a curriculum of easier goals of increasing complexity. The experiments illustrate the computational gains of these versions, their limitations, and opportunities for addressing them.

