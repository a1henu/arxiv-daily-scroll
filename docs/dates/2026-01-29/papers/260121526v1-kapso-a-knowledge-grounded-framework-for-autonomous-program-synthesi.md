---
layout: default
title: KAPSO: A Knowledge-grounded framework for Autonomous Program Synthesis and Optimization
---

# KAPSO: A Knowledge-grounded framework for Autonomous Program Synthesis and Optimization
**arXiv**：[2601.21526v1](https://arxiv.org/abs/2601.21526) · [PDF](https://arxiv.org/pdf/2601.21526.pdf)  
**作者**：Alireza Nadaf, Alireza Mohammadshahi, Majid Yazdani  

**一句话要点**：提出KAPSO框架，通过迭代合成与优化解决编程代理的长视距失败问题。

**关键词**：程序合成, 自主优化, 知识系统, 实验引擎, 认知记忆, 长视距编程

## 3 点简述
- 核心问题：编程代理常面临长视距失败，如实验状态丢失、调试脆弱和领域知识重用弱。
- 方法要点：集成Git实验引擎、知识系统和认知记忆层，支持迭代代码合成与优化。
- 实验或效果：在MLE-Bench和ALE-Bench上评估，报告端到端性能，代码已开源。

## 摘要（原文）

> We introduce KAPSO, a modular framework for autonomous program synthesis and optimization. Given a natural language goal and an evaluation method, KAPSO iteratively performs ideation, code synthesis and editing, execution, evaluation, and learning to improve a runnable artifact toward measurable objectives. Rather than treating synthesis as the endpoint, KAPSO uses synthesis as an operator within a long-horizon optimization loop, where progress is defined by evaluator outcomes.
>   KAPSO targets long-horizon failures common in coding agents, including lost experimental state, brittle debugging, and weak reuse of domain expertise, by integrating three tightly coupled components. First, a git-native experimentation engine isolates each attempt as a branch, producing reproducible artifacts and preserving provenance across iterations. Second, a knowledge system ingests heterogeneous sources, including repositories, internal playbooks, and curated external resources such as documentation, scientific papers, and web search results, and organizes them into a structured representation that supports retrieval over workflows, implementations, and environment constraints. Third, a cognitive memory layer coordinates retrieval and maintains an episodic store of reusable lessons distilled from experiment traces (run logs, diffs, and evaluator feedback), reducing repeated error modes and accelerating convergence.
>   We evaluated KAPSO on MLE-Bench (Kaggle-style ML competitions) and ALE-Bench (AtCoder heuristic optimization), and report end-to-end performance.
>   Code Available at: https://github.com/Leeroo-AI/kapso

