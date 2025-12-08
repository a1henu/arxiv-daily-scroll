---
layout: default
title: CureAgent: A Training-Free Executor-Analyst Framework for Clinical Reasoning
---

# CureAgent: A Training-Free Executor-Analyst Framework for Clinical Reasoning
**arXiv**：[2512.05576v1](https://arxiv.org/abs/2512.05576) · [PDF](https://arxiv.org/pdf/2512.05576.pdf)  
**作者**：Ting-Ting Xie, Yixin Zhang  

**一句话要点**：提出Executor-Analyst框架以解决临床推理中的上下文利用失败问题

**关键词**：临床推理, 模块化架构, 训练免费方法, 上下文利用, 分层集成, 工具执行

## 3 点简述
- 核心问题：现有临床代理在检索生物医学证据后，难以基于信息进行诊断，存在上下文利用失败。
- 方法要点：采用模块化架构，将工具执行的语法精度与临床推理的语义鲁棒性解耦，结合分层集成策略。
- 实验或效果：在CURE-Bench上实现先进性能，无需端到端微调，并揭示上下文扩展和工具集扩展的缩放见解。

## 摘要（原文）

> Current clinical agent built on small LLMs, such as TxAgent suffer from a \textit{Context Utilization Failure}, where models successfully retrieve biomedical evidence due to supervised finetuning but fail to ground their diagnosis in that information. In this work, we propose the Executor-Analyst Framework, a modular architecture that decouples the syntactic precision of tool execution from the semantic robustness of clinical reasoning. By orchestrating specialized TxAgents (Executors) with long-context foundation models (Analysts), we mitigate the reasoning deficits observed in monolithic models. Beyond simple modularity, we demonstrate that a Stratified Ensemble strategy significantly outperforms global pooling by preserving evidentiary diversity, effectively addressing the information bottleneck. Furthermore, our stress tests reveal critical scaling insights: (1) a \textit{Context-Performance Paradox}, where extending reasoning contexts beyond 12k tokens introduces noise that degrades accuracy; and (2) the \textit{Curse of Dimensionality} in action spaces, where expanding toolsets necessitates hierarchical retrieval strategies. Crucially, our approach underscores the potential of training-free architectural engineering, achieving state-of-the-art performance on CURE-Bench without the need for expensive end-to-end finetuning. This provides a scalable, agile foundation for the next generation of trustworthy AI-driven therapeutics. Code has been released on https://github.com/June01/CureAgent.

