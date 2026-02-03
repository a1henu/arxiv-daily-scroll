---
layout: default
title: Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction
---

# Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction
**arXiv**：[2602.02455v1](https://arxiv.org/abs/2602.02455) · [PDF](https://arxiv.org/pdf/2602.02455.pdf)  
**作者**：Han Bao, Zheyuan Zhang, Pengcheng Jing, Zhengqing Yuan, Kaiwen Shi, Yanfang Ye  

**一句话要点**：提出Drift-Bench以诊断LLM代理在输入故障下的多轮交互合作失效问题

**关键词**：LLM代理评估, 多轮交互诊断, 输入故障分析, 合作失效分类, 代理安全评估

## 3 点简述
- 核心问题：用户输入违反合作假设（如隐含意图、缺失参数）导致LLM代理执行风险，现有基准无法评估多轮消歧。
- 方法要点：基于通信理论，构建统一合作失效分类，通过角色驱动用户模拟器在状态导向和服务导向环境中进行多轮澄清评估。
- 实验或效果：实验显示输入故障下性能显著下降，澄清效果因用户角色和故障类型而异，连接澄清研究与代理安全评估。

## 摘要（原文）

> As Large Language Models transition to autonomous agents, user inputs frequently violate cooperative assumptions (e.g., implicit intent, missing parameters, false presuppositions, or ambiguous expressions), creating execution risks that text-only evaluations do not capture. Existing benchmarks typically assume well-specified instructions or restrict evaluation to text-only, single-turn clarification, and thus do not measure multi-turn disambiguation under grounded execution risk. We introduce \textbf{Drift-Bench}, the first diagnostic benchmark that evaluates agentic pragmatics under input faults through multi-turn clarification across state-oriented and service-oriented execution environments. Grounded in classical theories of communication, \textbf{Drift-Bench} provides a unified taxonomy of cooperative breakdowns and employs a persona-driven user simulator with the \textbf{Rise} evaluation protocol. Experiments show substantial performance drops under these faults, with clarification effectiveness varying across user personas and fault types. \MethodName bridges clarification research and agent safety evaluation, enabling systematic diagnosis of failures that can lead to unsafe executions.

