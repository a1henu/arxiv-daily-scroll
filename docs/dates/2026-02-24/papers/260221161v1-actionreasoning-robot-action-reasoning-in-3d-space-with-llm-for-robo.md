---
layout: default
title: ActionReasoning: Robot Action Reasoning in 3D Space with LLM for Robotic Brick Stacking
---

# ActionReasoning: Robot Action Reasoning in 3D Space with LLM for Robotic Brick Stacking
**arXiv**：[2602.21161v1](https://arxiv.org/abs/2602.21161) · [PDF](https://arxiv.org/pdf/2602.21161.pdf)  
**作者**：Guangming Wang, Qizhen Ying, Yixiong Jing, Olaf Wysocki, Brian Sheil  

**一句话要点**：提出ActionReasoning框架，利用LLM进行物理推理以解决机器人砖块堆叠中的动作规划问题。

**关键词**：机器人操作, 大语言模型, 物理推理, 动作规划, 砖块堆叠, 多智能体系统

## 3 点简述
- 核心问题：传统机器人系统缺乏泛化能力，数据驱动方法难以处理物理世界的连续动作空间。
- 方法要点：基于多智能体LLM架构，利用物理先验进行显式动作推理，生成物理一致的动作计划。
- 实验或效果：在砖块堆叠案例中实现稳定放置，减少低级编码需求，展示泛化潜力。

## 摘要（原文）

> Classical robotic systems typically rely on custom planners designed for constrained environments. While effective in restricted settings, these systems lack generalization capabilities, limiting the scalability of embodied AI and general-purpose robots. Recent data-driven Vision-Language-Action (VLA) approaches aim to learn policies from large-scale simulation and real-world data. However, the continuous action space of the physical world significantly exceeds the representational capacity of linguistic tokens, making it unclear if scaling data alone can yield general robotic intelligence. To address this gap, we propose ActionReasoning, an LLM-driven framework that performs explicit action reasoning to produce physics-consistent, prior-guided decisions for robotic manipulation. ActionReasoning leverages the physical priors and real-world knowledge already encoded in Large Language Models (LLMs) and structures them within a multi-agent architecture. We instantiate this framework on a tractable case study of brick stacking, where the environment states are assumed to be already accurately measured. The environmental states are then serialized and passed to a multi-agent LLM framework that generates physics-aware action plans. The experiments demonstrate that the proposed multi-agent LLM framework enables stable brick placement while shifting effort from low-level domain-specific coding to high-level tool invocation and prompting, highlighting its potential for broader generalization. This work introduces a promising approach to bridging perception and execution in robotic manipulation by integrating physical reasoning with LLMs.

