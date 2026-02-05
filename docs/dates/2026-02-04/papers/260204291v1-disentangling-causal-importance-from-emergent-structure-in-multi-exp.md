---
layout: default
title: Disentangling Causal Importance from Emergent Structure in Multi-Expert Orchestration
---

# Disentangling Causal Importance from Emergent Structure in Multi-Expert Orchestration
**arXiv**：[2602.04291v1](https://arxiv.org/abs/2602.04291) · [PDF](https://arxiv.org/pdf/2602.04291.pdf)  
**作者**：Sudipto Ghosh, Sujoy Nath, Sunny Manchanda, Tanmoy Chakraborty  

**一句话要点**：提出INFORM方法以解耦多专家编排中的因果重要性与交互结构

**关键词**：多专家系统, 编排策略, 因果归因, 交互结构, 可解释性分析

## 3 点简述
- 核心问题：多专家系统编排策略不透明，路由主导与功能必要性脱节
- 方法要点：将编排视为可分析计算，分离交互结构、执行顺序和因果归因
- 实验或效果：在GSM8K等任务上验证，因果重要性与路由频率存在分歧，结构依赖超越准确率

## 摘要（原文）

> Multi-expert systems, where multiple Large Language Models (LLMs) collaborate to solve complex tasks, are increasingly adopted for high-performance reasoning and generation. However, the orchestration policies governing expert interaction and sequencing remain largely opaque. We introduce INFORM, an interpretability analysis that treats orchestration as an explicit, analyzable computation, enabling the decoupling of expert interaction structure, execution order, and causal attribution. We use INFORM to evaluate an orchestrator on GSM8K, HumanEval, and MMLU using a homogeneous consortium of ten instruction-tuned experts drawn from LLaMA-3.1 8B, Qwen-3 8B, and DeepSeek-R1 8B, with controlled decoding-temperature variation, and a secondary heterogeneous consortium spanning 1B-7B parameter models. Across tasks, routing dominance is a poor proxy for functional necessity. We reveal a divergence between relational importance, captured by routing mass and interaction topology, and intrinsic importance, measured via gradient-based causal attribution: frequently selected experts often act as interaction hubs with limited causal influence, while sparsely routed experts can be structurally critical. Orchestration behaviors emerge asynchronously, with expert centralization preceding stable routing confidence and expert ordering remaining non-deterministic. Targeted ablations show that masking intrinsically important experts induces disproportionate collapse in interaction structure compared to masking frequent peers, confirming that INFORM exposes causal and structural dependencies beyond accuracy metrics alone.

