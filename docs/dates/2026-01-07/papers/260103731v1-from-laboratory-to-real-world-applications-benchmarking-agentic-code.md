---
layout: default
title: From Laboratory to Real-World Applications: Benchmarking Agentic Code Reasoning at the Repository Level
---

# From Laboratory to Real-World Applications: Benchmarking Agentic Code Reasoning at the Repository Level
**arXiv**：[2601.03731v1](https://arxiv.org/abs/2601.03731) · [PDF](https://arxiv.org/pdf/2601.03731.pdf)  
**作者**：Jia Li, Yuxin Su, Michael R. Lyu  

**一句话要点**：提出RepoReason基准以评估大语言模型在仓库级代码推理中的逻辑一致性

**关键词**：仓库级代码推理, 白盒诊断基准, 溯因断言验证, 执行驱动突变, 动态程序切片, 认知瓶颈分析

## 3 点简述
- 核心问题：现有基准在孤立代码片段与黑盒评估间波动，难以评估仓库级推理的逻辑一致性
- 方法要点：基于溯因断言验证的白盒诊断基准，采用执行驱动突变框架消除记忆化并保持逻辑深度
- 实验或效果：评估前沿模型揭示聚合缺陷，集成宽度是主要认知瓶颈，提供细粒度白盒洞察

## 摘要（原文）

> As large language models (LLMs) evolve into autonomous agents, evaluating repository-level reasoning, the ability to maintain logical consistency across massive, real-world, interdependent file systems, has become critical. Current benchmarks typically fluctuate between isolated code snippets and black-box evaluations. We present RepoReason, a white-box diagnostic benchmark centered on abductive assertion verification. To eliminate memorization while preserving authentic logical depth, we implement an execution-driven mutation framework that utilizes the environment as a semantic oracle to regenerate ground-truth states. Furthermore, we establish a fine-grained diagnostic system using dynamic program slicing, quantifying reasoning via three orthogonal metrics: $ESV$ (reading load), $MCL$ (simulation depth), and $DFI$ (integration width). Comprehensive evaluations of frontier models (e.g., Claude-4.5-Sonnet, DeepSeek-v3.1-Terminus) reveal a prevalent aggregation deficit, where integration width serves as the primary cognitive bottleneck. Our findings provide granular white-box insights for optimizing the next generation of agentic software engineering.

