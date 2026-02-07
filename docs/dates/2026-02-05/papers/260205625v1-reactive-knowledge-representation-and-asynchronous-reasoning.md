---
layout: default
title: Reactive Knowledge Representation and Asynchronous Reasoning
---

# Reactive Knowledge Representation and Asynchronous Reasoning
**arXiv**：[2602.05625v1](https://arxiv.org/abs/2602.05625) · [PDF](https://arxiv.org/pdf/2602.05625.pdf)  
**作者**：Simon Kohaut, Benedict Flade, Julian Eggert, Kristian Kersting, Devendra Singh Dhami  

**一句话要点**：提出Resin语言和Reactive Circuits以解决动态环境中概率推理的计算效率问题

**关键词**：概率推理, 反应式编程, 异步推理, 计算效率, 动态环境, 代数电路

## 3 点简述
- 核心问题：动态环境中概率推理计算成本高，现有方法无法有效处理异步信息流
- 方法要点：结合概率逻辑与反应式编程，通过Reactive Circuits自适应调整推理结构
- 实验或效果：在无人机群模拟中实现数量级加速，减少延迟并支持实时推理

## 摘要（原文）

> Exact inference in complex probabilistic models often incurs prohibitive computational costs. This challenge is particularly acute for autonomous agents in dynamic environments that require frequent, real-time belief updates. Existing methods are often inefficient for ongoing reasoning, as they re-evaluate the entire model upon any change, failing to exploit that real-world information streams have heterogeneous update rates. To address this, we approach the problem from a reactive, asynchronous, probabilistic reasoning perspective. We first introduce Resin (Reactive Signal Inference), a probabilistic programming language that merges probabilistic logic with reactive programming. Furthermore, to provide efficient and exact semantics for Resin, we propose Reactive Circuits (RCs). Formulated as a meta-structure over Algebraic Circuits and asynchronous data streams, RCs are time-dynamic Directed Acyclic Graphs that autonomously adapt themselves based on the volatility of input signals. In high-fidelity drone swarm simulations, our approach achieves several orders of magnitude of speedup over frequency-agnostic inference. We demonstrate that RCs' structural adaptations successfully capture environmental dynamics, significantly reducing latency and facilitating reactive real-time reasoning. By partitioning computations based on the estimated Frequency of Change in the asynchronous inputs, large inference tasks can be decomposed into individually memoized sub-problems. This ensures that only the specific components of a model affected by new information are re-evaluated, drastically reducing redundant computation in streaming contexts.

