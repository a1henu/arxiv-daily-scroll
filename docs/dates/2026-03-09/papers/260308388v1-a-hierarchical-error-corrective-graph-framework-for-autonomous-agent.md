---
layout: default
title: A Hierarchical Error-Corrective Graph Framework for Autonomous Agents with LLM-Based Action Generation
---

# A Hierarchical Error-Corrective Graph Framework for Autonomous Agents with LLM-Based Action Generation
**arXiv**：[2603.08388v1](https://arxiv.org/abs/2603.08388) · [PDF](https://arxiv.org/pdf/2603.08388.pdf)  
**作者**：Cong Cao, Jingyao Zhang, Kun Tong  

**一句话要点**：提出分层纠错图框架以增强基于LLM的自主代理在复杂任务中的执行可靠性

**关键词**：自主代理, 分层纠错图, LLM动作生成, 错误分类, 因果图检索, 策略优化

## 3 点简述
- 核心问题：自主代理在动态任务环境中易受负迁移和错误累积影响，导致执行失败。
- 方法要点：通过多维度可转移策略、错误矩阵分类和因果上下文图检索，实现策略优化与错误根因分析。
- 实验或效果：未知，但框架旨在提升策略选择精度、错误纠正能力和任务适应性。

## 摘要（原文）

> We propose a Hierarchical Error-Corrective Graph FrameworkforAutonomousAgentswithLLM-BasedActionGeneration(HECG),whichincorporates three core innovations: (1) Multi-Dimensional Transferable Strategy (MDTS): by integrating task quality metrics (Q), confidence/cost metrics (C), reward metrics (R), and LLM-based semantic reasoning scores (LLM-Score), MDTS achieves multi-dimensional alignment between quantitative performance and semantic context, enabling more precise selection of high-quality candidate strate gies and effectively reducing the risk of negative transfer. (2) Error Matrix Classification (EMC): unlike simple confusion matrices or overall performance metrics, EMC provides structured attribution of task failures by categorizing errors into ten types, such as Strategy Errors (Strategy Whe) and Script Parsing Errors (Script-Parsing-Error), and decomposing them according to severity, typical actions, error descriptions, and recoverability. This allows precise analysis of the root causes of task failures, offering clear guidance for subsequent error correction and strategy optimization rather than relying solely on overall success rates or single performance metrics. (3) Causal-Context Graph Retrieval (CCGR): to enhance agent retrieval capabilities in dynamic task environments, we construct graphs from historical states, actions, and event sequences, where nodes store executed actions, next-step actions, execution states, transferable strategies, and other relevant information, and edges represent causal dependencies such as preconditions for transitions between nodes. CCGR identifies subgraphs most relevant to the current task context, effectively capturing structural relationships beyond vector similarity, allowing agents to fully leverage contextual information, accelerate strategy adaptation, and improve execution reliability in complex, multi-step tasks.

