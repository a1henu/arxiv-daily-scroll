---
layout: default
title: DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching
---

# DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching
**arXiv**：[2602.06039v1](https://arxiv.org/abs/2602.06039) · [PDF](https://arxiv.org/pdf/2602.06039.pdf)  
**作者**：Yuxing Lu, Yucheng Hu, Xukai Zhao, Jiuxin Cao  

**一句话要点**：提出DyTopo框架，通过语义匹配动态重构稀疏有向通信图以提升多智能体推理性能

**关键词**：多智能体系统, 动态拓扑路由, 语义匹配, 大语言模型, 迭代推理, 可解释性

## 3 点简述
- 现有多智能体系统依赖固定通信模式，难以匹配迭代问题求解的阶段需求
- DyTopo在每轮基于管理器目标，通过智能体输出查询与关键描述符进行语义匹配，动态路由私有消息
- 在代码生成和数学推理基准测试中，DyTopo平均提升6.2%，并提供可解释的协调轨迹

## 摘要（原文）

> Multi-agent systems built from prompted large language models can improve multi-round reasoning, yet most existing pipelines rely on fixed, trajectory-wide communication patterns that are poorly matched to the stage-dependent needs of iterative problem solving. We introduce DyTopo, a manager-guided multi-agent framework that reconstructs a sparse directed communication graph at each round. Conditioned on the manager's round goal, each agent outputs lightweight natural-language query (need) and \key (offer) descriptors; DyTopo embeds these descriptors and performs semantic matching, routing private messages only along the induced edges. Across code generation and mathematical reasoning benchmarks and four LLM backbones, DyTopo consistently outperforms over the strongest baseline (avg. +6.2). Beyond accuracy, DyTopo yields an interpretable coordination trace via the evolving graphs, enabling qualitative inspection of how communication pathways reconfigure across rounds.

