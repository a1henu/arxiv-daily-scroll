---
layout: default
title: Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents
---

# Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents
**arXiv**：[2601.02314v1](https://arxiv.org/abs/2601.02314) · [PDF](https://arxiv.org/pdf/2601.02314.pdf)  
**作者**：Sourena Khanzadeh  

**一句话要点**：提出Project Ariadne框架，利用结构因果模型审计LLM代理推理的忠实性

**关键词**：结构因果模型, 反事实推理, 忠实性审计, LLM代理, 因果解耦, 可解释人工智能

## 3 点简述
- 核心问题：LLM代理的推理痕迹可能不忠实，仅为事后合理化，而非真实驱动决策。
- 方法要点：基于结构因果模型和反事实逻辑，通过硬干预中间节点测量因果敏感性。
- 实验或效果：发现普遍因果解耦现象，忠实性差距显著，提出Ariadne评分作为新基准。

## 摘要（原文）

> As Large Language Model (LLM) agents are increasingly tasked with high-stakes autonomous decision-making, the transparency of their reasoning processes has become a critical safety concern. While \textit{Chain-of-Thought} (CoT) prompting allows agents to generate human-readable reasoning traces, it remains unclear whether these traces are \textbf{faithful} generative drivers of the model's output or merely \textbf{post-hoc rationalizations}. We introduce \textbf{Project Ariadne}, a novel XAI framework that utilizes Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity of agentic reasoning. Unlike existing interpretability methods that rely on surface-level textual similarity, Project Ariadne performs \textbf{hard interventions} ($do$-calculus) on intermediate reasoning nodes -- systematically inverting logic, negating premises, and reversing factual claims -- to measure the \textbf{Causal Sensitivity} ($φ$) of the terminal answer. Our empirical evaluation of state-of-the-art models reveals a persistent \textit{Faithfulness Gap}. We define and detect a widespread failure mode termed \textbf{Causal Decoupling}, where agents exhibit a violation density ($ρ$) of up to $0.77$ in factual and scientific domains. In these instances, agents arrive at identical conclusions despite contradictory internal logic, proving that their reasoning traces function as "Reasoning Theater" while decision-making is governed by latent parametric priors. Our findings suggest that current agentic architectures are inherently prone to unfaithful explanation, and we propose the Ariadne Score as a new benchmark for aligning stated logic with model action.

