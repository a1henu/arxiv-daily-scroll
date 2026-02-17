---
layout: default
title: Arbor: A Framework for Reliable Navigation of Critical Conversation Flows
---

# Arbor: A Framework for Reliable Navigation of Critical Conversation Flows
**arXiv**：[2602.14643v1](https://arxiv.org/abs/2602.14643) · [PDF](https://arxiv.org/pdf/2602.14643.pdf)  
**作者**：Luís Silva, Diogo Gonçalves, Catarina Farinha, Clara Matos, Luís Ungaro  

**一句话要点**：提出Arbor框架以解决大语言模型在医疗分诊等关键对话流程中遵循结构化工作流的难题

**关键词**：决策树导航, 大语言模型, 医疗分诊, 结构化工作流, DAG编排, 成本优化

## 3 点简述
- 核心问题：大语言模型在长提示下易出现指令遵循退化，如中间丢失效应和上下文窗口溢出
- 方法要点：将决策树导航分解为节点级任务，基于DAG编排动态检索边并评估转换
- 实验或效果：在10个基础模型上，平均轮次准确率提升29.4%，延迟降低57.1%，成本减少14.4倍

## 摘要（原文）

> Large language models struggle to maintain strict adherence to structured workflows in high-stakes domains such as healthcare triage. Monolithic approaches that encode entire decision structures within a single prompt are prone to instruction-following degradation as prompt length increases, including lost-in-the-middle effects and context window overflow. To address this gap, we present Arbor, a framework that decomposes decision tree navigation into specialized, node-level tasks. Decision trees are standardized into an edge-list representation and stored for dynamic retrieval. At runtime, a directed acyclic graph (DAG)-based orchestration mechanism iteratively retrieves only the outgoing edges of the current node, evaluates valid transitions via a dedicated LLM call, and delegates response generation to a separate inference step. The framework is agnostic to the underlying decision logic and model provider. Evaluated against single-prompt baselines across 10 foundation models using annotated turns from real clinical triage conversations. Arbor improves mean turn accuracy by 29.4 percentage points, reduces per-turn latency by 57.1%, and achieves an average 14.4x reduction in per-turn cost. These results indicate that architectural decomposition reduces dependence on intrinsic model capability, enabling smaller models to match or exceed larger models operating under single-prompt baselines.

