---
layout: default
title: Learning to Orchestrate Agents in Natural Language with the Conductor
---

# Learning to Orchestrate Agents in Natural Language with the Conductor
**arXiv**：[2512.04388v1](https://arxiv.org/abs/2512.04388) · [PDF](https://arxiv.org/pdf/2512.04388.pdf)  
**作者**：Stefan Nielsen, Edoardo Cetin, Peter Schwendeman, Qi Sun, Jinglue Xu, Yujin Tang  

**一句话要点**：提出Conductor模型，通过强化学习协调多LLM以提升推理性能

**关键词**：多智能体协调, 强化学习, 提示工程, 语言模型协作, 推理基准

## 3 点简述
- 核心问题：不同LLM专长各异，需有效协调以发挥集体优势
- 方法要点：训练Conductor模型设计通信拓扑和提示工程，优化协作策略
- 实验或效果：在LiveCodeBench和GPQA基准上达到SOTA，适应任意代理池

## 摘要（原文）

> Powerful large language models (LLMs) from different providers have been expensively trained and finetuned to specialize across varying domains. In this work, we introduce a new kind of Conductor model trained with reinforcement learning to automatically discover powerful coordination strategies among LLMs. Our Conductor learns not only to design targeted communication topologies for effective agent-to-agent collaboration, but also to prompt engineer focused instructions to the LLMs to maximally leverage their individual capabilities. We show that, by learning optimal coordination strategies over pools of powerful worker LLMs, a 7B Conductor achieves significant performance gains beyond any individual worker, attaining state-of-the-art results in challenging reasoning benchmarks, such as LiveCodeBench and GPQA. By training with randomized agent pools, our conductor effectively adapts to arbitrary sets of open- and closed-source agents, meeting any user requirements. Furthermore, allowing the Conductor to select itself as a worker gives rise to recursive topologies, elevating performance with a new form of dynamic test-time scaling through online iterative adaptation. More broadly, ours is among the early work demonstrating language model coordination can be unlocked through RL, where powerful coordination strategies emerge naturally in LLMs through pure end-to-end reward maximization.

