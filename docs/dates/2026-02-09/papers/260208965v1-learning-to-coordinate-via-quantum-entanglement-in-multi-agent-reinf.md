---
layout: default
title: Learning to Coordinate via Quantum Entanglement in Multi-Agent Reinforcement Learning
---

# Learning to Coordinate via Quantum Entanglement in Multi-Agent Reinforcement Learning
**arXiv**：[2602.08965v1](https://arxiv.org/abs/2602.08965) · [PDF](https://arxiv.org/pdf/2602.08965.pdf)  
**作者**：John Gardiner, Orlando Romero, Brendan Tivnan, Nicolò Dal Fabbro, George J. Pappas  

**一句话要点**：提出基于量子纠缠的多智能体强化学习框架，以解决无通信下的协调问题。

**关键词**：多智能体强化学习, 量子纠缠, 协调策略, Dec-POMDP, 量子优势

## 3 点简述
- 核心问题：多智能体强化学习中无通信导致协调困难，传统方法依赖共享随机性。
- 方法要点：引入可微分策略参数化，优化量子测量，结合量子协调器与分散局部执行器架构。
- 实验或效果：在单轮游戏中学习量子优势策略，并在Dec-POMDP中展示量子优势策略学习能力。

## 摘要（原文）

> The inability to communicate poses a major challenge to coordination in multi-agent reinforcement learning (MARL). Prior work has explored correlating local policies via shared randomness, sometimes in the form of a correlation device, as a mechanism to assist in decentralized decision-making. In contrast, this work introduces the first framework for training MARL agents to exploit shared quantum entanglement as a coordination resource, which permits a larger class of communication-free correlated policies than shared randomness alone. This is motivated by well-known results in quantum physics which posit that, for certain single-round cooperative games with no communication, shared quantum entanglement enables strategies that outperform those that only use shared randomness. In such cases, we say that there is quantum advantage. Our framework is based on a novel differentiable policy parameterization that enables optimization over quantum measurements, together with a novel policy architecture that decomposes joint policies into a quantum coordinator and decentralized local actors. To illustrate the effectiveness of our proposed method, we first show that we can learn, purely from experience, strategies that attain quantum advantage in single-round games that are treated as black box oracles. We then demonstrate how our machinery can learn policies with quantum advantage in an illustrative multi-agent sequential decision-making problem formulated as a decentralized partially observable Markov decision process (Dec-POMDP).

