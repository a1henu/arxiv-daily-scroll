---
layout: default
title: MCP-Diag: A Deterministic, Protocol-Driven Architecture for AI-Native Network Diagnostics
---

# MCP-Diag: A Deterministic, Protocol-Driven Architecture for AI-Native Network Diagnostics
**arXiv**：[2601.22633v1](https://arxiv.org/abs/2601.22633) · [PDF](https://arxiv.org/pdf/2601.22633.pdf)  
**作者**：Devansh Lodha, Mohit Panchal, Sameer G. Kulkarni  

**一句话要点**：提出MCP-Diag架构，基于模型上下文协议解决LLM在网络诊断中的随机性问题和安全风险。

**关键词**：网络诊断, 模型上下文协议, 确定性翻译, 人机交互授权, 混合神经符号架构, AIOps

## 3 点简述
- 核心问题：LLM在AIOps中面临解析非结构化CLI输出的随机性问题和自主代理shell访问的安全缺口。
- 方法要点：采用混合神经符号架构，通过确定性翻译层将标准工具输出转换为JSON模式，并强制实施协议级人机交互授权循环。
- 实验或效果：初步评估显示，实体提取准确率达100%，执行延迟开销低于0.9%，上下文令牌使用量增加3.7倍。

## 摘要（原文）

> The integration of Large Language Models (LLMs) into network operations (AIOps) is hindered by two fundamental challenges: the stochastic grounding problem, where LLMs struggle to reliably parse unstructured, vendor-specific CLI output, and the security gap of granting autonomous agents shell access. This paper introduces MCP-Diag, a hybrid neuro-symbolic architecture built upon the Model Context Protocol (MCP). We propose a deterministic translation layer that converts raw stdout from canonical utilities (dig, ping, traceroute) into rigorous JSON schemas before AI ingestion. We further introduce a mandatory "Elicitation Loop" that enforces Human-in-the-Loop (HITL) authorization at the protocol level. Our preliminary evaluation demonstrates that MCP-Diag achieving 100% entity extraction accuracy with less than 0.9% execution latency overhead and 3.7x increase in context token usage.

