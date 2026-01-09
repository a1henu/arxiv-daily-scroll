---
layout: default
title: SmartSearch: Process Reward-Guided Query Refinement for Search Agents
---

# SmartSearch: Process Reward-Guided Query Refinement for Search Agents
**arXiv**：[2601.04888v1](https://arxiv.org/abs/2601.04888) · [PDF](https://arxiv.org/pdf/2601.04888.pdf)  
**作者**：Tongyu Wen, Guanting Dong, Zhicheng Dou  

**一句话要点**：提出SmartSearch框架，通过过程奖励和查询优化提升基于大语言模型的搜索代理性能。

**关键词**：搜索代理, 查询优化, 过程奖励, 课程学习, 大语言模型

## 3 点简述
- 核心问题：现有搜索代理在推理过程中生成的中间搜索查询质量不佳，影响检索效果和整体性能。
- 方法要点：引入过程奖励机制进行细粒度监督，结合查询优化策略选择性改进低质量查询，并采用三阶段课程学习框架。
- 实验或效果：实验结果显示SmartSearch超越现有基线，在搜索效率和查询质量上均有显著提升。

## 摘要（原文）

> Large language model (LLM)-based search agents have proven promising for addressing knowledge-intensive problems by incorporating information retrieval capabilities. Existing works largely focus on optimizing the reasoning paradigms of search agents, yet the quality of intermediate search queries during reasoning remains overlooked. As a result, the generated queries often remain inaccurate, leading to unexpected retrieval results and ultimately limiting search agents' overall effectiveness. To mitigate this issue, we introduce SmartSearch, a framework built upon two key mechanisms: (1) Process rewards, which provide fine-grained supervision for the quality of each intermediate search query through Dual-Level Credit Assessment. (2) Query refinement, which promotes the optimization of query generation by selectively refining low-quality search queries and regenerating subsequent search rounds based on these refinements. To enable the search agent to progressively internalize the ability to improve query quality under the guidance of process rewards, we design a three-stage curriculum learning framework. This framework guides the agent through a progression from imitation, to alignment, and ultimately to generalization. Experimental results show that SmartSearch consistently surpasses existing baselines, and additional quantitative analyses further confirm its significant gains in both search efficiency and query quality. The code is available at https://github.com/MYVAE/SmartSearch.

