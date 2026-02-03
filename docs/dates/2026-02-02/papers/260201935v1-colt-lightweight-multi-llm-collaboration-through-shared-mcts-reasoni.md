---
layout: default
title: COLT: Lightweight Multi-LLM Collaboration through Shared MCTS Reasoning for Model Compilation
---

# COLT: Lightweight Multi-LLM Collaboration through Shared MCTS Reasoning for Model Compilation
**arXiv**：[2602.01935v1](https://arxiv.org/abs/2602.01935) · [PDF](https://arxiv.org/pdf/2602.01935.pdf)  
**作者**：Annabelle Sujun Tang, Christopher Priebe, Lianhui Qin, Hadi Esmaeilzadeh  

**一句话要点**：提出COLT框架，通过共享MCTS实现多LLM协作以优化编译器搜索成本

**关键词**：编译器优化, 多LLM协作, 蒙特卡洛树搜索, 模型选择, 轻量级推理

## 3 点简述
- 核心问题：单一大模型编译器优化成本高，小模型可靠性不足
- 方法要点：在MCTS中共享树结构，实现模型间协作与轻量级推理
- 实验或效果：未知是否匹配或超越单一大模型性能

## 摘要（原文）

> Model serving costs dominate AI systems, making compiler optimization essential for scalable deployment. Recent works show that a large language model (LLM) can guide compiler search by reasoning over program structure and optimization history. However, using a single large model throughout the search is expensive, while smaller models are less reliable when used alone. Thus, this paper seeks to answer whether multi-LLM collaborative reasoning relying primarily on small LLMs can match or exceed the performance of a single large model. As such, we propose a lightweight collaborative multi-LLM framework, dubbed COLT, for compiler optimization that enables coordinated reasoning across multiple models within a single Monte Carlo tree search (MCTS) process. A key contribution is the use of a single shared MCTS tree as the collaboration substrate across LLMs, enabling the reuse of transformation prefixes and cross-model value propagation. Hence, we circumvent both heavy internal reasoning mechanisms and conventional agentic machinery that relies on external planners, multiple concurrent LLMs, databases, external memory/versioning of intermediate results, and controllers by simply endogenizing model selection within the lightweight MCTS optimization loop. Every iteration, the acting LLM proposes a joint action: (compiler transformation, model to be queried next). We also introduce a model-aware tree policy that biases search toward smaller models while preserving exploration, and a course-alteration mechanism that escalates to the largest model when the search exhibits persistent regressions attributable to smaller models.

