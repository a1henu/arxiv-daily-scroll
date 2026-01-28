---
layout: default
title: CASTER: Breaking the Cost-Performance Barrier in Multi-Agent Orchestration via Context-Aware Strategy for Task Efficient Routing
---

# CASTER: Breaking the Cost-Performance Barrier in Multi-Agent Orchestration via Context-Aware Strategy for Task Efficient Routing
**arXiv**：[2601.19793v1](https://arxiv.org/abs/2601.19793) · [PDF](https://arxiv.org/pdf/2601.19793.pdf)  
**作者**：Shanyv Liu, Xuyang Yuan, Tao Chen, Zijun Zhan, Zhu Han, Danyang Zheng, Weishan Zhang, Shaohua Cao  

**一句话要点**：提出CASTER以解决图基多智能体系统中静态模型分配导致的成本效率低下问题

**关键词**：多智能体系统, 动态模型选择, 成本效率优化, 图基工作流, 任务路由

## 3 点简述
- 核心问题：图基多智能体系统在复杂循环工作流中，静态分配强模型导致计算浪费于简单子任务
- 方法要点：采用双信号路由器结合语义嵌入和结构元特征动态估计任务难度，通过冷启动到迭代演化范式自优化
- 实验或效果：在软件工程等领域实验中，CASTER相比强模型基线降低推理成本达72.4%，同时保持成功率

## 摘要（原文）

> Graph-based Multi-Agent Systems (MAS) enable complex cyclic workflows but suffer from inefficient static model allocation, where deploying strong models uniformly wastes computation on trivial sub-tasks. We propose CASTER (Context-Aware Strategy for Task Efficient Routing), a lightweight router for dynamic model selection in graph-based MAS. CASTER employs a Dual-Signal Router that combines semantic embeddings with structural meta-features to estimate task difficulty. During training, the router self-optimizes through a Cold Start to Iterative Evolution paradigm, learning from its own routing failures via on-policy negative feedback. Experiments using LLM-as-a-Judge evaluation across Software Engineering, Data Analysis, Scientific Discovery, and Cybersecurity demonstrate that CASTER reduces inference cost by up to 72.4% compared to strong-model baselines while matching their success rates, and consistently outperforms both heuristic routing and FrugalGPT across all domains.

