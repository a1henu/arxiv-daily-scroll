---
layout: default
title: Orchestrating Intelligence: Confidence-Aware Routing for Efficient Multi-Agent Collaboration across Multi-Scale Models
---

# Orchestrating Intelligence: Confidence-Aware Routing for Efficient Multi-Agent Collaboration across Multi-Scale Models
**arXiv**：[2601.04861v1](https://arxiv.org/abs/2601.04861) · [PDF](https://arxiv.org/pdf/2601.04861.pdf)  
**作者**：Jingbo Wang, Sendong Zhao, Jiatong Liu, Haochun Wang, Wanting Li, Bing Qin, Ting Liu  

**一句话要点**：提出OI-MAS框架，通过自适应模型选择解决多智能体系统计算效率低的问题。

**关键词**：多智能体系统, 自适应模型选择, 置信感知路由, 计算效率优化, 多尺度语言模型

## 3 点简述
- 核心问题：多智能体系统在复杂推理任务中计算效率低下，现有方法未考虑不同推理阶段的认知需求差异。
- 方法要点：引入状态依赖路由和置信感知机制，动态选择智能体角色和模型规模，减少对大模型的依赖。
- 实验或效果：实验显示OI-MAS在准确率提升最高12.88%的同时，成本降低最高79.78%。

## 摘要（原文）

> While multi-agent systems (MAS) have demonstrated superior performance over single-agent approaches in complex reasoning tasks, they often suffer from significant computational inefficiencies. Existing frameworks typically deploy large language models (LLMs) uniformly across all agent roles, failing to account for the varying cognitive demands of different reasoning stages. We address this inefficiency by proposing OI-MAS framework, a novel multi-agent framework that implements an adaptive model-selection policy across a heterogeneous pool of multi-scale LLMs. Specifically, OI-MAS introduces a state-dependent routing mechanism that dynamically selects agent roles and model scales throughout the reasoning process. In addition, we introduce a confidence-aware mechanism that selects appropriate model scales conditioned on task complexity, thus reducing unnecessary reliance on large-scale models. Experimental results show that OI-MAS consistently outperforms baseline multi-agent systems, improving accuracy by up to 12.88\% while reducing cost by up to 79.78\%.

