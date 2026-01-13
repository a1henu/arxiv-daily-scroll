---
layout: default
title: Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models
---

# Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models
**arXiv**：[2601.07372v1](https://arxiv.org/abs/2601.07372) · [PDF](https://arxiv.org/pdf/2601.07372.pdf)  
**作者**：Xin Cheng, Wangding Zeng, Damai Dai, Qinyu Chen, Bingxuan Wang, Zhenda Xie, Kezhao Huang, Xingkai Yu, Zhewen Hao, Yukun Li, Han Zhang, Huishuai Zhang, Dongyan Zhao, Wenfeng Liang  

**一句话要点**：提出条件记忆模块Engram，通过可扩展查找实现大语言模型的新稀疏轴，优化计算与静态存储的权衡。

**关键词**：条件记忆, 稀疏模型, 知识查找, N-gram嵌入, 长上下文检索, 计算效率

## 3 点简述
- 核心问题：Transformer缺乏原生知识查找机制，需通过计算低效模拟检索。
- 方法要点：引入条件记忆作为稀疏轴，基于N-gram嵌入实现O(1)查找，并建立稀疏分配问题以优化计算与存储。
- 实验或效果：在27B参数规模下，Engram超越同参数和FLOPs的MoE基线，提升知识检索、推理及长上下文性能。

## 摘要（原文）

> While Mixture-of-Experts (MoE) scales capacity via conditional computation, Transformers lack a native primitive for knowledge lookup, forcing them to inefficiently simulate retrieval through computation. To address this, we introduce conditional memory as a complementary sparsity axis, instantiated via Engram, a module that modernizes classic $N$-gram embedding for O(1) lookup. By formulating the Sparsity Allocation problem, we uncover a U-shaped scaling law that optimizes the trade-off between neural computation (MoE) and static memory (Engram). Guided by this law, we scale Engram to 27B parameters, achieving superior performance over a strictly iso-parameter and iso-FLOPs MoE baseline. Most notably, while the memory module is expected to aid knowledge retrieval (e.g., MMLU +3.4; CMMLU +4.0), we observe even larger gains in general reasoning (e.g., BBH +5.0; ARC-Challenge +3.7) and code/math domains~(HumanEval +3.0; MATH +2.4). Mechanistic analyses reveal that Engram relieves the backbone's early layers from static reconstruction, effectively deepening the network for complex reasoning. Furthermore, by delegating local dependencies to lookups, it frees up attention capacity for global context, substantially boosting long-context retrieval (e.g., Multi-Query NIAH: 84.2 to 97.0). Finally, Engram establishes infrastructure-aware efficiency: its deterministic addressing enables runtime prefetching from host memory, incurring negligible overhead. We envision conditional memory as an indispensable modeling primitive for next-generation sparse models.

