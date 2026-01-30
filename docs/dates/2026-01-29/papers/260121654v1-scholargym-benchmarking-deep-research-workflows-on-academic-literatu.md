---
layout: default
title: ScholarGym: Benchmarking Deep Research Workflows on Academic Literature Retrieval
---

# ScholarGym: Benchmarking Deep Research Workflows on Academic Literature Retrieval
**arXiv**：[2601.21654v1](https://arxiv.org/abs/2601.21654) · [PDF](https://arxiv.org/pdf/2601.21654.pdf)  
**作者**：Hao Shen, Hang Yang, Zhouhong Gu  

**一句话要点**：提出ScholarGym以解决深度研究工作流评估中的非确定性问题

**关键词**：学术文献检索, 工作流评估, 模拟环境, 工具增强大模型, 可复现性

## 3 点简述
- 核心问题：依赖实时API导致评估不可复现，影响系统比较
- 方法要点：构建静态学术语料库，解耦工作流组件进行可控分析
- 实验或效果：基于2,536查询测试不同模型，揭示迭代优化中的交互机制

## 摘要（原文）

> Tool-augmented large language models have advanced from single-turn question answering to deep research workflows that iteratively plan queries, invoke external tools, and synthesize information to address complex information needs. Evaluating such workflows presents a fundamental challenge: reliance on live APIs introduces non-determinism, as tool invocations may yield different results across runs due to temporal drift, rate limiting, and evolving backend states. This variance undermines reproducibility and invalidates cross-system comparisons.
>   We present ScholarGym, a simulation environment for reproducible evaluation of deep research workflows on academic literature. The environment decouples workflow components into query planning, tool invocation, and relevance assessment, enabling fine-grained analysis of each stage under controlled conditions. Built on a static corpus of 570K papers with deterministic retrieval, ScholarGym provides 2,536 queries with expert-annotated ground truth. Experiments across diverse backbone models reveal how reasoning capabilities, planning strategies, and selection mechanisms interact over iterative refinement.

