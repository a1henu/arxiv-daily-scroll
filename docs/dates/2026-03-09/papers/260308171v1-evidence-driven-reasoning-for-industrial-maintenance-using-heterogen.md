---
layout: default
title: Evidence-Driven Reasoning for Industrial Maintenance Using Heterogeneous Data
---

# Evidence-Driven Reasoning for Industrial Maintenance Using Heterogeneous Data
**arXiv**：[2603.08171v1](https://arxiv.org/abs/2603.08171) · [PDF](https://arxiv.org/pdf/2603.08171.pdf)  
**作者**：Fearghal O'Donncha, Nianjun Zhou, Natalia Martinez, James T Rayfield, Fenno F. Heath, Abigail Langbridge, Roman Vaculin  

**一句话要点**：提出Condition Insight Agent框架，以证据驱动推理解决工业维护中的异构数据决策支持问题。

**关键词**：工业维护决策支持, 异构数据集成, 证据驱动推理, 规则验证, LLM约束应用

## 3 点简述
- 核心问题：工业维护平台数据异构且碎片化，现有分析孤立，难以支持条件决策。
- 方法要点：整合维护语言、操作数据行为抽象和工程故障语义，通过确定性证据构建和规则验证实现推理。
- 实验或效果：生产CMMS部署案例显示，该框架在异构不完整数据下可靠运行，保持人类监督。

## 摘要（原文）

> Industrial maintenance platforms contain rich but fragmented evidence, including free-text work orders, heterogeneous operational sensors or indicators, and structured failure knowledge. These sources are often analyzed in isolation, producing alerts or forecasts that do not support conditional decision-making: given this asset history and behavior, what is happening and what action is warranted? We present Condition Insight Agent, a deployed decision-support framework that integrates maintenance language, behavioral abstractions of operational data, and engineering failure semantics to produce evidence-grounded explanations and advisory actions. The system constrains reasoning through deterministic evidence construction and structured failure knowledge, and applies a rule-based verification loop to suppress unsupported conclusions. Case studies from production CMMS deployments show that this verification-first design operates reliably under heterogeneous and incomplete data while preserving human oversight. Our results demonstrate how constrained LLM-based reasoning can function as a governed decision-support layer for industrial maintenance.

