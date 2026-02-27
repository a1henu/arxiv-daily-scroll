---
layout: default
title: Agentic AI for Intent-driven Optimization in Cell-free O-RAN
---

# Agentic AI for Intent-driven Optimization in Cell-free O-RAN
**arXiv**：[2602.22539v1](https://arxiv.org/abs/2602.22539) · [PDF](https://arxiv.org/pdf/2602.22539.pdf)  
**作者**：Mohammad Hossein Shokouhi, Vincent W. S. Wong  

**一句话要点**：提出基于智能体AI的意图驱动优化框架，用于无小区O-RAN中的资源管理。

**关键词**：智能体人工智能, 开放无线接入网, 意图驱动优化, 参数高效微调, 深度强化学习, 无小区网络

## 3 点简述
- 核心问题：现有O-RAN中智能体独立处理简单意图，缺乏对复杂意图的协调机制。
- 方法要点：设计多智能体框架，包括监督、用户权重、O-RU管理和监控智能体，采用PEFT方法提升可扩展性。
- 实验或效果：在节能模式下，相比基线方案减少41.93%的活跃O-RU数量，PEFT方法降低92%内存使用。

## 摘要（原文）

> Agentic artificial intelligence (AI) is emerging as a key enabler for autonomous radio access networks (RANs), where multiple large language model (LLM)-based agents reason and collaborate to achieve operator-defined intents. The open RAN (O-RAN) architecture enables the deployment and coordination of such agents. However, most existing works consider simple intents handled by independent agents, while complex intents that require coordination among agents remain unexplored. In this paper, we propose an agentic AI framework for intent translation and optimization in cell-free O-RAN. A supervisor agent translates the operator intents into an optimization objective and minimum rate requirements. Based on this information, a user weighting agent retrieves relevant prior experience from a memory module to determine the user priority weights for precoding. If the intent includes an energy-saving objective, then an open radio unit (O-RU) management agent will also be activated to determine the set of active O-RUs by using a deep reinforcement learning (DRL) algorithm. A monitoring agent measures and monitors the user data rates and coordinates with other agents to guarantee the minimum rate requirements are satisfied. To enhance scalability, we adopt a parameter-efficient fine-tuning (PEFT) method that enables the same underlying LLM to be used for different agents. Simulation results show that the proposed agentic AI framework reduces the number of active O-RUs by 41.93% when compared with three baseline schemes in energy-saving mode. Using the PEFT method, the proposed framework reduces the memory usage by 92% when compared with deploying separate LLM agents.

