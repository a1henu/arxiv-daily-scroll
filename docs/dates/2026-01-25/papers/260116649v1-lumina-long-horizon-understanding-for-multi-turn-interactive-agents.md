---
layout: default
title: LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents
---

# LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents
**arXiv**：[2601.16649v1](https://arxiv.org/abs/2601.16649) · [PDF](https://arxiv.org/pdf/2601.16649.pdf)  
**作者**：Amin Rakhsha, Thomas Hehn, Pietro Mazzaglia, Fabio Valerio Massoli, Arash Behboodi, Tribhuvanesh Orekondy  

**一句话要点**：提出LUMINA框架以评估多轮交互智能体中关键技能的重要性

**关键词**：多轮交互智能体, 长程理解, 反事实评估, 可控环境, 技能重要性分析

## 3 点简述
- 核心问题：大语言模型在多轮长程智能体任务中表现不佳，需提升规划、状态跟踪等能力
- 方法要点：开发反事实框架，通过完美技能干预测量其对性能的影响
- 实验或效果：在可控环境中测试，发现技能重要性依赖环境和模型特性

## 摘要（原文）

> Large language models can perform well on many isolated tasks, yet they continue to struggle on multi-turn, long-horizon agentic problems that require skills such as planning, state tracking, and long context processing. In this work, we aim to better understand the relative importance of advancing these underlying capabilities for success on such tasks. We develop an oracle counterfactual framework for multi-turn problems that asks: how would an agent perform if it could leverage an oracle to perfectly perform a specific task? The change in the agent's performance due to this oracle assistance allows us to measure the criticality of such oracle skill in the future advancement of AI agents. We introduce a suite of procedurally generated, game-like tasks with tunable complexity. These controlled environments allow us to provide precise oracle interventions, such as perfect planning or flawless state tracking, and make it possible to isolate the contribution of each oracle without confounding effects present in real-world benchmarks. Our results show that while some interventions (e.g., planning) consistently improve performance across settings, the usefulness of other skills is dependent on the properties of the environment and language model. Our work sheds light on the challenges of multi-turn agentic environments to guide the future efforts in the development of AI agents and language models.

