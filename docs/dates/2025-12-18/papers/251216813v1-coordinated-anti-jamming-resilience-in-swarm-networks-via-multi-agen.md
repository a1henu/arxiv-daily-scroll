---
layout: default
title: Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning
---

# Coordinated Anti-Jamming Resilience in Swarm Networks via Multi-Agent Reinforcement Learning
**arXiv**：[2512.16813v1](https://arxiv.org/abs/2512.16813) · [PDF](https://arxiv.org/pdf/2512.16813.pdf)  
**作者**：Bahman Abolhassani, Tugba Erpek, Kemal Davaslioglu, Yalin E. Sagduyu, Sastry Kompella  

**一句话要点**：提出基于QMIX的多智能体强化学习框架，以增强机器人集群网络在反应式干扰下的通信韧性。

**关键词**：多智能体强化学习, 集群网络, 抗干扰通信, QMIX算法, 反应式干扰

## 3 点简述
- 核心问题：反应式干扰器选择性破坏集群通信，威胁编队完整性和任务成功。
- 方法要点：采用QMIX算法学习集中式但可分解的动作值函数，实现协调去中心化的频率和功率联合选择。
- 实验或效果：仿真显示QMIX快速收敛至接近最优策略，相比基线提高吞吐量并降低干扰发生率。

## 摘要（原文）

> Reactive jammers pose a severe security threat to robotic-swarm networks by selectively disrupting inter-agent communications and undermining formation integrity and mission success. Conventional countermeasures such as fixed power control or static channel hopping are largely ineffective against such adaptive adversaries. This paper presents a multi-agent reinforcement learning (MARL) framework based on the QMIX algorithm to improve the resilience of swarm communications under reactive jamming. We consider a network of multiple transmitter-receiver pairs sharing channels while a reactive jammer with Markovian threshold dynamics senses aggregate power and reacts accordingly. Each agent jointly selects transmit frequency (channel) and power, and QMIX learns a centralized but factorizable action-value function that enables coordinated yet decentralized execution. We benchmark QMIX against a genie-aided optimal policy in a no-channel-reuse setting, and against local Upper Confidence Bound (UCB) and a stateless reactive policy in a more general fading regime with channel reuse enabled. Simulation results show that QMIX rapidly converges to cooperative policies that nearly match the genie-aided bound, while achieving higher throughput and lower jamming incidence than the baselines, thereby demonstrating MARL's effectiveness for securing autonomous swarms in contested environments.

