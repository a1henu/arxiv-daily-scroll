---
layout: default
title: Agentic Diagnostic Reasoning over Telecom and Datacenter Infrastructure
---

# Agentic Diagnostic Reasoning over Telecom and Datacenter Infrastructure
**arXiv**：[2601.07342v1](https://arxiv.org/abs/2601.07342) · [PDF](https://arxiv.org/pdf/2601.07342.pdf)  
**作者**：Nicolas Tacheny  

**一句话要点**：提出基于大语言模型的代理诊断框架，以解决电信与数据中心基础设施的根因分析问题。

**关键词**：代理诊断框架, 大语言模型, 根因分析, 模型上下文协议, 基础设施管理

## 3 点简述
- 核心问题：传统根因分析方法依赖硬编码图遍历或规则引擎，维护成本高且与模型紧耦合。
- 方法要点：利用大语言模型通过模型上下文协议工具进行逐步调查，自主导航基础设施模型。
- 实验或效果：未知，但框架为自主事件解决和变更影响缓解奠定基础。

## 摘要（原文）

> Large-scale telecom and datacenter infrastructures rely on multi-layered service and resource models, where failures propagate across physical and logical components and affect multiple customers. Traditional approaches to root cause analysis(RCA) rely on hard-coded graph traversal algorithms or rule-based correlation engines, which are costly to maintain and tightly coupled to the infrastructure model.
>   In this work, we introduce an agentic diagnostic framework where a Large Language Model (LLM) performs step-wise investigation using a constrained tool space exposed through the Model Context Protocol (MCP). Instead of embedding causal logic or traversal algorithms into the application, the agent autonomously navigates the infrastructure model by invoking tools for service lookup, dependency retrieval, structured and unstructured data, and event analysis, and impact discovery. We define an investigation protocol that structures the agent's reasoning and ensures grounding, reproducibility, and safe handling of missing or ambiguous information.
>   This work lays the foundation for autonomous incident resolution and change impact mitigation. Future systems will not only diagnose and remediate infrastructure failures, but also predict the impact of planned changes on services and customers, enabling operators to mitigate risks before executing maintenance operations.

