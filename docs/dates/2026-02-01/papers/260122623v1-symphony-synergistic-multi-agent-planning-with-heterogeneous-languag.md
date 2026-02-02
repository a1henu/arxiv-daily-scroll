---
layout: default
title: SYMPHONY: Synergistic Multi-agent Planning with Heterogeneous Language Model Assembly
---

# SYMPHONY: Synergistic Multi-agent Planning with Heterogeneous Language Model Assembly
**arXiv**：[2601.22623v1](https://arxiv.org/abs/2601.22623) · [PDF](https://arxiv.org/pdf/2601.22623.pdf)  
**作者**：Wei Zhu, Zhiwen Tang, Kun Yue  

**一句话要点**：提出SYMPHONY多智能体规划框架，通过异构语言模型集成增强复杂任务探索能力。

**关键词**：多智能体规划, 异构语言模型, 蒙特卡洛树搜索, 探索多样性, 复杂问题求解

## 3 点简述
- 现有单智能体框架在MCTS规划中限制探索，导致分支多样性不足和性能次优。
- SYMPHONY集成异构语言模型智能体，利用多样推理模式提升分支多样性和探索效果。
- 实验表明，SYMPHONY在开源和云端LLMs上均优于基线，验证异构多智能体协调的有效性。

## 摘要（原文）

> Recent advancements have increasingly focused on leveraging large language models (LLMs) to construct autonomous agents for complex problem-solving tasks. However, existing approaches predominantly employ a single-agent framework to generate search branches and estimate rewards during Monte Carlo Tree Search (MCTS) planning. This single-agent paradigm inherently limits exploration capabilities, often resulting in insufficient diversity among generated branches and suboptimal planning performance. To overcome these limitations, we propose Synergistic Multi-agent Planning with Heterogeneous langauge model assembly (SYMPHONY), a novel multi-agent planning framework that integrates a pool of heterogeneous language model-based agents. By leveraging diverse reasoning patterns across agents, SYMPHONY enhances rollout diversity and facilitates more effective exploration. Empirical results across multiple benchmark tasks show that SYMPHONY achieves strong performance even when instantiated with open-source LLMs deployable on consumer-grade hardware. When enhanced with cloud-based LLMs accessible via API, SYMPHONY demonstrates further improvements, outperforming existing state-of-the-art baselines and underscoring the effectiveness of heterogeneous multi-agent coordination in planning tasks.

