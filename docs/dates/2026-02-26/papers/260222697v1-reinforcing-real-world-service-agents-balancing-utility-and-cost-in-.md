---
layout: default
title: Reinforcing Real-world Service Agents: Balancing Utility and Cost in Task-oriented Dialogue
---

# Reinforcing Real-world Service Agents: Balancing Utility and Cost in Task-oriented Dialogue
**arXiv**：[2602.22697v1](https://arxiv.org/abs/2602.22697) · [PDF](https://arxiv.org/pdf/2602.22697.pdf)  
**作者**：Ning Gao, Wei Zhang, Yuqin Dai, Ling Shi, Ziyin Wang, Yujie Wang, Wei He, Jinpeng Wang, Chaozheng Wang  

**一句话要点**：提出InteractCS-RL框架，通过多粒度强化学习平衡任务型对话中的用户效用与成本约束。

**关键词**：任务型对话, 强化学习, 成本约束, 多粒度策略, 帕累托优化, 用户交互框架

## 3 点简述
- 核心问题：现有方法难以在任务型对话中平衡共情沟通与预算感知决策。
- 方法要点：建立用户中心交互框架和成本感知多轮策略优化，结合PID-Lagrangian成本控制器探索帕累托边界。
- 实验或效果：在真实业务场景中显著优于基线，并在多领域基准上验证了鲁棒性。

## 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) has accelerated the transition from conversational chatbots to general agents. However, effectively balancing empathetic communication with budget-aware decision-making remains an open challenge. Since existing methods fail to capture these complex strategic trade-offs, we propose InteractCS-RL, a framework that reframes task-oriented dialogue as a multi-granularity reinforcement learning process. Specifically, we first establish a User-centric Interaction Framework to provide a high-fidelity training gym, enabling agents to dynamically explore diverse strategies with persona-driven users. Then, we introduce Cost-aware Multi-turn Policy Optimization (CMPO) with a hybrid advantage estimation strategy. By integrating generative process credits and employing a PID-Lagrangian cost controller, CMPO effectively guides the policy to explore Pareto boundary between user reward and global cost constraints. Extensive experiments on customized real business scenarios demonstrate that InteractCS-RL significantly outperform other baselines across three evaluation dimensions. Further evaluation on tool-agent-user interaction benchmarks verify InteractCS-RL robustness across diverse domains.

