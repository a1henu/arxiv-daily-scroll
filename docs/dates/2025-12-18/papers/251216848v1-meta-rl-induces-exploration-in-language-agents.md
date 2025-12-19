---
layout: default
title: Meta-RL Induces Exploration in Language Agents
---

# Meta-RL Induces Exploration in Language Agents
**arXiv**：[2512.16848v1](https://arxiv.org/abs/2512.16848) · [PDF](https://arxiv.org/pdf/2512.16848.pdf)  
**作者**：Yulun Jiang, Liangze Jiang, Damien Teney, Michael Moor, Maria Brbic  

**一句话要点**：提出LaMer框架，通过元强化学习诱导语言智能体在测试时主动探索环境。

**关键词**：元强化学习, 语言智能体, 主动探索, 策略适应, 长时程任务

## 3 点简述
- 强化学习训练的语言智能体在需要主动探索的任务中表现不佳，难以高效适应试错经验。
- LaMer包含跨回合训练框架以鼓励探索和长期奖励优化，以及通过反思进行上下文策略适应。
- 实验显示LaMer在多个环境中性能显著提升，并展现出更好的泛化能力。

## 摘要（原文）

> Reinforcement learning (RL) has enabled the training of large language model (LLM) agents to interact with the environment and to solve multi-turn long-horizon tasks. However, the RL-trained agents often struggle in tasks that require active exploration and fail to efficiently adapt from trial-and-error experiences. In this paper, we present LaMer, a general Meta-RL framework that enables LLM agents to actively explore and learn from the environment feedback at test time. LaMer consists of two key components: (i) a cross-episode training framework to encourage exploration and long-term rewards optimization; and (ii) in-context policy adaptation via reflection, allowing the agent to adapt their policy from task feedback signal without gradient update. Experiments across diverse environments show that LaMer significantly improves performance over RL baselines, with 11%, 14%, and 19% performance gains on Sokoban, MineSweeper and Webshop, respectively. Moreover, LaMer also demonstrates better generalization to more challenging or previously unseen tasks compared to the RL-trained agents. Overall, our results demonstrate that Meta-RL provides a principled approach to induce exploration in language agents, enabling more robust adaptation to novel environments through learned exploration strategies.

