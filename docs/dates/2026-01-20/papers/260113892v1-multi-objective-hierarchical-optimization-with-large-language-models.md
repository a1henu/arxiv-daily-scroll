---
layout: default
title: Multi-Objective Hierarchical Optimization with Large Language Models
---

# Multi-Objective Hierarchical Optimization with Large Language Models
**arXiv**：[2601.13892v1](https://arxiv.org/abs/2601.13892) · [PDF](https://arxiv.org/pdf/2601.13892.pdf)  
**作者**：Andrej Schwanke, Lyubomir Ivanov, David Salinas, Frank Hutter, Arber Zela  

**一句话要点**：提出基于大语言模型的分层优化方法以解决多目标优化问题

**关键词**：多目标优化, 大语言模型, 分层搜索, 帕累托前沿, 代理模型, 自适应分区

## 3 点简述
- 核心问题：大语言模型在多目标优化中表现不佳，需改进以平衡探索与利用
- 方法要点：采用分层搜索策略，自适应分区输入空间并限制LLM生成到高潜力子空间
- 实验或效果：算法在合成和真实基准测试中优于全局LLM优化器，与标准算法相当

## 摘要（原文）

> Despite their widespread adoption in various domains, especially due to their powerful reasoning capabilities, Large Language Models (LLMs) are not the off-the-shelf choice to drive multi-objective optimization yet. Conventional strategies rank high in benchmarks due to their intrinsic capabilities to handle numerical inputs and careful modelling choices that balance exploration and Pareto-front exploitation, as well as handle multiple (conflicting) objectives. In this paper, we close this gap by leveraging LLMs as surrogate models and candidate samplers inside a structured hierarchical search strategy. By adaptively partitioning the input space into disjoint hyperrectangular regions and ranking them with a composite score function, we restrict the generative process of the LLM to specific, high-potential sub-spaces, hence making the problem easier to solve as the LLM doesn't have to reason about the global structure of the problem, but only locally instead. We show that under standard regularity assumptions, our algorithm generates candidate solutions that converge to the true Pareto set in Hausdorff distance. Empirically, it consistently outperforms the global LLM-based multi-objective optimizer and is on par with standard evolutionary and Bayesian optimization algorithm on synthetic and real-world benchmarks.

