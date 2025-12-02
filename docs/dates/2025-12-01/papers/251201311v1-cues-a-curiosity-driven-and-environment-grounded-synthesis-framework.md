---
layout: default
title: CuES: A Curiosity-driven and Environment-grounded Synthesis Framework for Agentic RL
---

# CuES: A Curiosity-driven and Environment-grounded Synthesis Framework for Agentic RL
**arXiv**：[2512.01311v1](https://arxiv.org/abs/2512.01311) · [PDF](https://arxiv.org/pdf/2512.01311.pdf)  
**作者**：Shinji Mai, Yunpeng Zhai, Ziqian Chen, Cheng Chen, Anni Zou, Shuchang Tao, Zhaoyang Liu, Bolin Ding  

**一句话要点**：提出CuES框架以解决智能体强化学习中任务稀缺问题

**关键词**：智能体强化学习, 任务生成, 好奇心驱动, 环境可供性, 任务稀缺

## 3 点简述
- 核心问题：智能体强化学习在无预定义任务的新环境中面临任务稀缺瓶颈
- 方法要点：基于环境结构与可供性，通过好奇心驱动自主生成多样可执行任务
- 实验效果：在三个代表性环境中生成的任务分布匹配或超越人工数据集，提升下游策略性能

## 摘要（原文）

> Large language model based agents are increasingly deployed in complex, tool augmented environments. While reinforcement learning provides a principled mechanism for such agents to improve through interaction, its effectiveness critically depends on the availability of structured training tasks. In many realistic settings, however, no such tasks exist a challenge we term task scarcity, which has become a key bottleneck for scaling agentic RL. Existing approaches typically assume predefined task collections, an assumption that fails in novel environments where tool semantics and affordances are initially unknown. To address this limitation, we formalize the problem of Task Generation for Agentic RL, where an agent must learn within a given environment that lacks predefined tasks. We propose CuES, a Curiosity driven and Environment grounded Synthesis framework that autonomously generates diverse, executable, and meaningful tasks directly from the environment structure and affordances, without relying on handcrafted seeds or external corpora. CuES drives exploration through intrinsic curiosity, abstracts interaction patterns into reusable task schemas, and refines them through lightweight top down guidance and memory based quality control. Across three representative environments, AppWorld, BFCL, and WebShop, CuES produces task distributions that match or surpass manually curated datasets in both diversity and executability, yielding substantial downstream policy improvements. These results demonstrate that curiosity driven, environment grounded task generation provides a scalable foundation for agents that not only learn how to act, but also learn what to learn. The code is available at https://github.com/modelscope/AgentEvolver/research/CuES.

