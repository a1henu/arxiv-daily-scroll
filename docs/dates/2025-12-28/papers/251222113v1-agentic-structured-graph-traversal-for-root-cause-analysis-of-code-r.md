---
layout: default
title: Agentic Structured Graph Traversal for Root Cause Analysis of Code-related Incidents in Cloud Applications
---

# Agentic Structured Graph Traversal for Root Cause Analysis of Code-related Incidents in Cloud Applications
**arXiv**：[2512.22113v1](https://arxiv.org/abs/2512.22113) · [PDF](https://arxiv.org/pdf/2512.22113.pdf)  
**作者**：Shengkun Cui, Rahul Krishna, Saurabh Jha, Ravishankar K. Iyer  

**一句话要点**：提出PRAXIS以诊断云应用中代码相关事故的根因，通过图结构遍历提升准确性并降低计算成本。

**关键词**：根因分析, 云事故诊断, 图遍历, LLM驱动, 微服务依赖, 代码依赖图

## 3 点简述
- 核心问题：云事故中代码和配置问题为主要根因，导致高额运营损失。
- 方法要点：PRAXIS利用LLM驱动遍历服务依赖图和程序依赖图，定位和解释故障。
- 实验或效果：相比ReAct基线，PRAXIS提升RCA准确性达3.1倍，减少令牌消耗3.8倍。

## 摘要（原文）

> Cloud incidents pose major operational challenges in production, with unresolved production cloud incidents cost on average over $2M per hour. Prior research identifies code- and configuration-related issues as the predominant category of root causes in cloud incidents. This paper introduces PRAXIS, an orchestrator that manages and deploys an agentic workflow for diagnosing code- and configuration-caused cloud incidents. PRAXIS employs an LLM-driven structured traversal over two types of graph: (1) a service dependency graph (SDG) that captures microservice-level dependencies; and (2) a hammock-block program dependence graph (PDG) that captures code-level dependencies for each microservice. Together, these graphs encode microservice- and code-level dependencies and the LLM acts as a traversal policy over these graphs, moving between services and code dependencies to localize and explain failures. Compared to state-of-the-art ReAct baselines, PRAXIS improves RCA accuracy by up to 3.1x while reducing token consumption by 3.8x. PRAXIS is demonstrated on a set of 30 comprehensive real-world incidents that is being compiled into an RCA benchmark.

