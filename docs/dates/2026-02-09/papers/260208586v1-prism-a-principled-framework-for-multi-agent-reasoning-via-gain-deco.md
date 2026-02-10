---
layout: default
title: PRISM: A Principled Framework for Multi-Agent Reasoning via Gain Decomposition
---

# PRISM: A Principled Framework for Multi-Agent Reasoning via Gain Decomposition
**arXiv**：[2602.08586v1](https://arxiv.org/abs/2602.08586) · [PDF](https://arxiv.org/pdf/2602.08586.pdf)  
**作者**：Yiming Yang, Zhuoyuan Li, Fanxiang Zeng, Hao Fu, Yue Liu  

**一句话要点**：提出PRISM框架，通过增益分解理论优化多智能体推理，提升大语言模型协作性能。

**关键词**：多智能体推理, 增益分解, 理论框架, 角色多样性, 证据评估, 迭代合成

## 3 点简述
- 核心问题：现有多智能体协作方法缺乏理论指导，性能增益来源不明，难以系统优化。
- 方法要点：引入统一理论框架，将增益分解为探索、信息和聚合三个维度，并设计PRISM框架最大化这些维度。
- 实验或效果：在数学推理、代码生成和函数调用基准测试中实现最优性能，计算效率优于部分维度优化方法。

## 摘要（原文）

> Multi-agent collaboration has emerged as a promising paradigm for enhancing reasoning capabilities of Large Language Models (LLMs). However, existing approaches remain largely heuristic, lacking principled guidance on what drives performance gains and how to systematically optimize multi-agent reasoning. Specifically, it remains unclear why multi-agent collaboration outperforms single-agent reasoning and which design choices contribute most to these gains, making it difficult to build better systems.
>   We address this gap by introducing a unified theoretical framework that decomposes multi-agent reasoning gains into three conceptually independent dimensions: Exploration for diverse solution coverage, Information for high-fidelity feedback, and Aggregation for principled consensus. Through this lens, existing methods can be understood as special cases that optimize only subsets of these dimensions. Building upon this decomposition, a novel framework called PRISM (Propose-Review-Integrate Synthesis for Multi-agent Reasoning) is proposed, which jointly maximizes all three dimensions through role-based diversity, execution-grounded feedback with evidence-based cross-evaluation, and iterative synthesis with closed-loop validation. Extensive experiments across mathematical reasoning, code generation, and function calling benchmarks demonstrate that PRISM achieves state-of-the-art performance with superior compute-efficiency compared to methods optimizing partial dimensions. The theoretical framework provides actionable design principles for future multi-agent reasoning systems.

