---
layout: default
title: Reinforcement Learning with Symbolic Reward Machines
---

# Reinforcement Learning with Symbolic Reward Machines
**arXiv**：[2603.03068v1](https://arxiv.org/abs/2603.03068) · [PDF](https://arxiv.org/pdf/2603.03068.pdf)  
**作者**：Thomas Krug, Daniel Neider  

**一句话要点**：提出符号奖励机以解决奖励机依赖手动标签和适用性差的问题

**关键词**：强化学习, 奖励机, 符号表示, 非马尔可夫奖励, 任务表示, 可解释性

## 3 点简述
- 奖励机依赖环境提供的高层标签，需手动设计标签函数，适用性受限
- 符号奖励机直接处理环境观测，通过符号公式作为守卫，无需额外标签
- 在评估中，符号奖励机方法优于基线强化学习，性能与现有奖励机方法相当

## 摘要（原文）

> Reward Machines (RMs) are an established mechanism in Reinforcement Learning (RL) to represent and learn sparse, temporally extended tasks with non-Markovian rewards. RMs rely on high-level information in the form of labels that are emitted by the environment alongside the observation. However, this concept requires manual user input for each environment and task. The user has to create a suitable labeling function that computes the labels. These limitations lead to poor applicability in widely adopted RL frameworks. We propose Symbolic Reward Machines (SRMs) together with the learning algorithms QSRM and LSRM to overcome the limitations of RMs. SRMs consume only the standard output of the environment and process the observation directly through guards that are represented by symbolic formulas. In our evaluation, our SRM methods outperform the baseline RL approaches and generate the same results as the existing RM methods. At the same time, our methods adhere to the widely used environment definition and provide interpretable representations of the task to the user.

