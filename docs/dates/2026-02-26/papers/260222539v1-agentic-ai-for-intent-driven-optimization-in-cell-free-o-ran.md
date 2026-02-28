---
layout: default
title: Agentic AI for Intent-driven Optimization in Cell-free O-RAN
---

# Agentic AI for Intent-driven Optimization in Cell-free O-RAN
**arXiv**：[2602.22539v1](https://arxiv.org/abs/2602.22539) · [PDF](https://arxiv.org/pdf/2602.22539.pdf)  
**作者**：Mohammad Hossein Shokouhi, Vincent W. S. Wong  

**一句话要点**：提出基于代理AI的意图驱动优化框架，用于无小区O-RAN中的资源管理。

**关键词**：代理人工智能, 意图驱动优化, 无小区O-RAN, 深度强化学习, 参数高效微调, 多代理协作

## 3 点简述
- 核心问题：现有代理AI方法难以处理需要多代理协调的复杂意图，在O-RAN中未充分探索。
- 方法要点：设计多代理框架，包括监督代理翻译意图、用户权重代理确定优先级、O-RU管理代理使用DRL节能、监控代理保障速率要求。
- 实验或效果：仿真显示节能模式下活跃O-RU减少41.93%，参数高效微调方法降低内存使用92%。

## 摘要（原文）

> Agentic artificial intelligence (AI) is emerging as a key enabler for autonomous radio access networks (RANs), where multiple large language model (LLM)-based agents reason and collaborate to achieve operator-defined intents. The open RAN (O-RAN) architecture enables the deployment and coordination of such agents. However, most existing works consider simple intents handled by independent agents, while complex intents that require coordination among agents remain unexplored. In this paper, we propose an agentic AI framework for intent translation and optimization in cell-free O-RAN. A supervisor agent translates the operator intents into an optimization objective and minimum rate requirements. Based on this information, a user weighting agent retrieves relevant prior experience from a memory module to determine the user priority weights for precoding. If the intent includes an energy-saving objective, then an open radio unit (O-RU) management agent will also be activated to determine the set of active O-RUs by using a deep reinforcement learning (DRL) algorithm. A monitoring agent measures and monitors the user data rates and coordinates with other agents to guarantee the minimum rate requirements are satisfied. To enhance scalability, we adopt a parameter-efficient fine-tuning (PEFT) method that enables the same underlying LLM to be used for different agents. Simulation results show that the proposed agentic AI framework reduces the number of active O-RUs by 41.93% when compared with three baseline schemes in energy-saving mode. Using the PEFT method, the proposed framework reduces the memory usage by 92% when compared with deploying separate LLM agents.

