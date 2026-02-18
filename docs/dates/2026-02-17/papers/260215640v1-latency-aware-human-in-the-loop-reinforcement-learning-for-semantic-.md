---
layout: default
title: Latency-aware Human-in-the-Loop Reinforcement Learning for Semantic Communications
---

# Latency-aware Human-in-the-Loop Reinforcement Learning for Semantic Communications
**arXiv**：[2602.15640v1](https://arxiv.org/abs/2602.15640) · [PDF](https://arxiv.org/pdf/2602.15640.pdf)  
**作者**：Peizheng Li, Xinyi Lin, Adnan Aijaz  

**一句话要点**：提出时间约束人机交互强化学习框架，以在语义通信中平衡语义保真度与低延迟需求。

**关键词**：语义通信, 人机交互强化学习, 延迟控制, 约束马尔可夫决策过程, 近端策略优化, 无线接入网络

## 3 点简述
- 核心问题：语义通信需在沉浸式和关键安全服务中兼顾语义保真度与严格延迟保证。
- 方法要点：基于约束马尔可夫决策过程，结合人类反馈、语义效用和延迟控制，采用原对偶近端策略优化算法。
- 实验或效果：在点对多点链路模拟中，该框架稳定满足用户时间约束，优于基线调度器，并减少资源消耗波动。

## 摘要（原文）

> Semantic communication promises task-aligned transmission but must reconcile semantic fidelity with stringent latency guarantees in immersive and safety-critical services. This paper introduces a time-constrained human-in-the-loop reinforcement learning (TC-HITL-RL) framework that embeds human feedback, semantic utility, and latency control within a semantic-aware Open radio access network (RAN) architecture. We formulate semantic adaptation driven by human feedback as a constrained Markov decision process (CMDP) whose state captures semantic quality, human preferences, queue slack, and channel dynamics, and solve it via a primal--dual proximal policy optimization algorithm with action shielding and latency-aware reward shaping. The resulting policy preserves PPO-level semantic rewards while tightening the variability of both air-interface and near-real-time RAN intelligent controller processing budgets. Simulations over point-to-multipoint links with heterogeneous deadlines show that TC-HITL-RL consistently meets per-user timing constraints, outperforms baseline schedulers in reward, and stabilizes resource consumption, providing a practical blueprint for latency-aware semantic adaptation.

