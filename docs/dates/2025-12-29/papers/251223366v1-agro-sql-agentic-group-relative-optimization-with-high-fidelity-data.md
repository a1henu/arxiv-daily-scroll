---
layout: default
title: AGRO-SQL: Agentic Group-Relative Optimization with High-Fidelity Data Synthesis
---

# AGRO-SQL: Agentic Group-Relative Optimization with High-Fidelity Data Synthesis
**arXiv**：[2512.23366v1](https://arxiv.org/abs/2512.23366) · [PDF](https://arxiv.org/pdf/2512.23366.pdf)  
**作者**：Cehua Yang, Dongyu Xiao, Junming Lin, Yuyang Song, Hanxu Yan, Shawn Guo, Wei Zhang, Jian Yang, Mingjie Tang, Bryan Dai  

**一句话要点**：提出AGRO-SQL框架，通过数据合成与代理强化学习提升Text-to-SQL系统性能

**关键词**：Text-to-SQL, 数据合成, 代理强化学习, 策略优化, 基准测试

## 3 点简述
- 核心问题：高质量训练数据稀缺和模型在复杂场景中推理能力有限
- 方法要点：采用数据中心迭代工厂合成高保真数据，模型中心引入代理强化学习优化策略
- 实验或效果：在BIRD和Spider基准测试中实现单模型方法的最先进性能

## 摘要（原文）

> The advancement of Text-to-SQL systems is currently hindered by the scarcity of high-quality training data and the limited reasoning capabilities of models in complex scenarios. In this paper, we propose a holistic framework that addresses these issues through a dual-centric approach. From a Data-Centric perspective, we construct an iterative data factory that synthesizes RL-ready data characterized by high correctness and precise semantic-logic alignment, ensured by strict verification. From a Model-Centric perspective, we introduce a novel Agentic Reinforcement Learning framework. This framework employs a Diversity-Aware Cold Start stage to initialize a robust policy, followed by Group Relative Policy Optimization (GRPO) to refine the agent's reasoning via environmental feedback. Extensive experiments on BIRD and Spider benchmarks demonstrate that our synergistic approach achieves state-of-the-art performance among single-model methods.

