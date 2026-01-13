---
layout: default
title: OpenTinker: Separating Concerns in Agentic Reinforcement Learning
---

# OpenTinker: Separating Concerns in Agentic Reinforcement Learning
**arXiv**：[2601.07376v1](https://arxiv.org/abs/2601.07376) · [PDF](https://arxiv.org/pdf/2601.07376.pdf)  
**作者**：Siqi Zhu, Jiaxuan You  

**一句话要点**：提出OpenTinker框架，通过关注点分离实现大语言模型代理的强化学习基础设施。

**关键词**：强化学习基础设施, 大语言模型代理, 关注点分离, 可组合组件, 集中式调度, 多代理训练

## 3 点简述
- 核心问题：传统端到端强化学习管道在代理学习系统中存在耦合度高、难以扩展的问题。
- 方法要点：将系统分解为轻量级可组合组件，引入集中式调度器管理训练和推理工作负载。
- 实验或效果：通过实际用例展示框架在代理学习场景中的有效性，支持多代理训练扩展。

## 摘要（原文）

> We introduce OpenTinker, an infrastructure for reinforcement learning (RL) of large language model (LLM) agents built around a separation of concerns across algorithm design, execution, and agent-environment interaction. Rather than relying on monolithic, end-to-end RL pipelines, OpenTinker decomposes agentic learning systems into lightweight, composable components with clearly defined abstraction boundaries. Users specify agents, environments, and interaction protocols, while inference and training are delegated to a managed execution runtime. OpenTinker introduces a centralized scheduler for managing training and inference workloads, including LoRA-based and full-parameter RL, supervised fine-tuning, and inference, over shared resources. We further discuss design principles for extending OpenTinker to multi-agent training. Finally, we present a set of RL use cases that demonstrate the effectiveness of the framework in practical agentic learning scenarios.

