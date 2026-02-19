---
layout: default
title: Framework of Thoughts: A Foundation Framework for Dynamic and Optimized Reasoning based on Chains, Trees, and Graphs
---

# Framework of Thoughts: A Foundation Framework for Dynamic and Optimized Reasoning based on Chains, Trees, and Graphs
**arXiv**：[2602.16512v1](https://arxiv.org/abs/2602.16512) · [PDF](https://arxiv.org/pdf/2602.16512.pdf)  
**作者**：Felix Fricke, Simon Malberg, Georg Groh  

**一句话要点**：提出Framework of Thoughts以构建和优化动态推理方案，提升大语言模型推理能力。

**关键词**：推理框架, 提示优化, 并行执行, 智能缓存, 大语言模型, 动态推理

## 3 点简述
- 现有推理方案如Chain of Thought缺乏动态适应性，且超参数和提示未优化。
- FoT框架内置超参数调优、提示优化、并行执行和智能缓存功能。
- 实验显示FoT能加速执行、降低成本并提高任务分数，已实现Tree of Thoughts等方案。

## 摘要（原文）

> Prompting schemes such as Chain of Thought, Tree of Thoughts, and Graph of Thoughts can significantly enhance the reasoning capabilities of large language models. However, most existing schemes require users to define static, problem-specific reasoning structures that lack adaptability to dynamic or unseen problem types. Additionally, these schemes are often under-optimized in terms of hyperparameters, prompts, runtime, and prompting cost. To address these limitations, we introduce Framework of Thoughts (FoT)--a general-purpose foundation framework for building and optimizing dynamic reasoning schemes. FoT comes with built-in features for hyperparameter tuning, prompt optimization, parallel execution, and intelligent caching, unlocking the latent performance potential of reasoning schemes. We demonstrate FoT's capabilities by implementing three popular schemes--Tree of Thoughts, Graph of Thoughts, and ProbTree--within FoT. We empirically show that FoT enables significantly faster execution, reduces costs, and achieves better task scores through optimization. We release our codebase to facilitate the development of future dynamic and efficient reasoning schemes.

