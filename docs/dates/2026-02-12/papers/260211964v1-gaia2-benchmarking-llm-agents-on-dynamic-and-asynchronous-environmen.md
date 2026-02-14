---
layout: default
title: Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments
---

# Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments
**arXiv**：[2602.11964v1](https://arxiv.org/abs/2602.11964) · [PDF](https://arxiv.org/pdf/2602.11964.pdf)  
**作者**：Romain Froger, Pierre Andrews, Matteo Bettini, Amar Budhiraja, Ricardo Silveira Cabral, Virginie Do, Emilien Garreau, Jean-Baptiste Gaya, Hugo Laurençon, Maxime Lecanu, Kunal Malkan, Dheeraj Mekala, Pierre Ménard, Gerard Moreno-Torres Bertran, Ulyana Piterbarg, Mikhail Plekhanov, Mathieu Rita, Andrey Rusakov, Vladislav Vorotilov, Mengjue Wang, Ian Yu, Amine Benhalloum, Grégoire Mialon, Thomas Scialom  

**一句话要点**：提出Gaia2基准以评估LLM代理在动态异步环境中的性能

**关键词**：LLM代理评估, 动态异步环境, 动作级验证, 强化学习基准, 开源框架

## 3 点简述
- 核心问题：现有基准多为静态或同步，缺乏真实异步环境下的代理评估
- 方法要点：引入动态异步场景，配备动作级验证器，支持强化学习奖励
- 实验或效果：评估显示模型在推理、效率、鲁棒性间存在权衡，开源模型Kimi-K2表现领先

## 摘要（原文）

> We introduce Gaia2, a benchmark for evaluating large language model agents in realistic, asynchronous environments. Unlike prior static or synchronous evaluations, Gaia2 introduces scenarios where environments evolve independently of agent actions, requiring agents to operate under temporal constraints, adapt to noisy and dynamic events, resolve ambiguity, and collaborate with other agents. Each scenario is paired with a write-action verifier, enabling fine-grained, action-level evaluation and making Gaia2 directly usable for reinforcement learning from verifiable rewards. Our evaluation of state-of-the-art proprietary and open-source models shows that no model dominates across capabilities: GPT-5 (high) reaches the strongest overall score of 42% pass@1 but fails on time-sensitive tasks, Claude-4 Sonnet trades accuracy and speed for cost, Kimi-K2 leads among open-source models with 21% pass@1. These results highlight fundamental trade-offs between reasoning, efficiency, robustness, and expose challenges in closing the "sim2real" gap. Gaia2 is built on a consumer environment with the open-source Agents Research Environments platform and designed to be easy to extend. By releasing Gaia2 alongside the foundational ARE framework, we aim to provide the community with a flexible infrastructure for developing, benchmarking, and training the next generation of practical agent systems.

