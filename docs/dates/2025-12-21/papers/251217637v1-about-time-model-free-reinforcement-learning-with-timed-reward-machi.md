---
layout: default
title: About Time: Model-free Reinforcement Learning with Timed Reward Machines
---

# About Time: Model-free Reinforcement Learning with Timed Reward Machines
**arXiv**：[2512.17637v1](https://arxiv.org/abs/2512.17637) · [PDF](https://arxiv.org/pdf/2512.17637.pdf)  
**作者**：Anirban Majumdar, Ritam Raha, Rajarshi Roy, David Parker, Marta Kwiatkowska  

**一句话要点**：提出定时奖励机以增强强化学习在时间敏感应用中的表达能力

**关键词**：定时奖励机, 无模型强化学习, 定时自动机, 反事实想象, 时间约束, 奖励规范

## 3 点简述
- 传统奖励机无法建模精确时间约束，限制其在时间敏感场景的应用
- 扩展奖励机为定时奖励机，通过定时自动机抽象和反事实想象启发式集成到无模型强化学习中
- 实验表明算法能在满足定时约束下学习高奖励策略，并比较不同语义下的性能

## 摘要（原文）

> Reward specification plays a central role in reinforcement learning (RL), guiding the agent's behavior. To express non-Markovian rewards, formalisms such as reward machines have been introduced to capture dependencies on histories. However, traditional reward machines lack the ability to model precise timing constraints, limiting their use in time-sensitive applications. In this paper, we propose timed reward machines (TRMs), which are an extension of reward machines that incorporate timing constraints into the reward structure. TRMs enable more expressive specifications with tunable reward logic, for example, imposing costs for delays and granting rewards for timely actions. We study model-free RL frameworks (i.e., tabular Q-learning) for learning optimal policies with TRMs under digital and real-time semantics. Our algorithms integrate the TRM into learning via abstractions of timed automata, and employ counterfactual-imagining heuristics that exploit the structure of the TRM to improve the search. Experimentally, we demonstrate that our algorithm learns policies that achieve high rewards while satisfying the timing constraints specified by the TRM on popular RL benchmarks. Moreover, we conduct comparative studies of performance under different TRM semantics, along with ablations that highlight the benefits of counterfactual-imagining.

