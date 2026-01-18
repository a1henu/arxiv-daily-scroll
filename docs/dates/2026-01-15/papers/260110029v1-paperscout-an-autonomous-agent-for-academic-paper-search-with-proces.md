---
layout: default
title: PaperScout: An Autonomous Agent for Academic Paper Search with Process-Aware Sequence-Level Policy Optimization
---

# PaperScout: An Autonomous Agent for Academic Paper Search with Process-Aware Sequence-Level Policy Optimization
**arXiv**：[2601.10029v1](https://arxiv.org/abs/2601.10029) · [PDF](https://arxiv.org/pdf/2601.10029.pdf)  
**作者**：Tingyue Pan, Jie Ouyang, Mingyue Cheng, Qingchuan Li, Zirui Liu, Mingfan Pan, Shuo Yu, Qi Liu  

**一句话要点**：提出PaperScout自主代理，通过序列级策略优化解决学术论文搜索中的动态决策问题。

**关键词**：学术论文搜索, 自主代理, 序列决策, 策略优化, 过程感知

## 3 点简述
- 核心问题：现有学术论文搜索方法依赖刚性工作流，难以处理复杂条件查询。
- 方法要点：将搜索建模为序列决策过程，引入PSPO方法进行过程感知的序列级策略优化。
- 实验或效果：在合成和真实基准测试中，PaperScout在召回率和相关性上显著优于基线方法。

## 摘要（原文）

> Academic paper search is a fundamental task in scientific research, yet most existing approaches rely on rigid, predefined workflows that struggle with complex, conditional queries. To address this limitation, we propose PaperScout, an autonomous agent that reformulates paper search as a sequential decision-making process. Unlike static workflows, PaperScout dynamically decides whether, when, and how to invoke search and expand tools based on accumulated retrieval context. However, training such agents presents a fundamental challenge: standard reinforcement learning methods, typically designed for single-turn tasks, suffer from a granularity mismatch when applied to multi-turn agentic tasks, where token-level optimization diverges from the granularity of sequence-level interactions, leading to noisy credit assignment. We introduce Proximal Sequence Policy Optimization (PSPO), a process-aware, sequence-level policy optimization method that aligns optimization with agent-environment interaction. Comprehensive experiments on both synthetic and real-world benchmarks demonstrate that PaperScout significantly outperforms strong workflow-driven and RL baselines in both recall and relevance, validating the effectiveness of our adaptive agentic framework and optimization strategy.

