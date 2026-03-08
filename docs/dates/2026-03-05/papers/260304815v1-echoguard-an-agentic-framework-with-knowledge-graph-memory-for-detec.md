---
layout: default
title: EchoGuard: An Agentic Framework with Knowledge-Graph Memory for Detecting Manipulative Communication in Longitudinal Dialogue
---

# EchoGuard: An Agentic Framework with Knowledge-Graph Memory for Detecting Manipulative Communication in Longitudinal Dialogue
**arXiv**：[2603.04815v1](https://arxiv.org/abs/2603.04815) · [PDF](https://arxiv.org/pdf/2603.04815.pdf)  
**作者**：Ratna Kandala, Niva Manchanda, Akshata Kishore Moharir, Ananth Kandala  

**一句话要点**：提出EchoGuard框架，利用知识图谱记忆检测纵向对话中的操纵性沟通

**关键词**：知识图谱记忆, 操纵性沟通检测, 纵向对话分析, 代理AI框架, 心理模式识别

## 3 点简述
- 核心问题：现有AI系统缺乏结构化长期记忆，难以识别操纵性沟通如煤气灯效应和情感胁迫
- 方法要点：采用知识图谱作为核心记忆，通过日志-分析-反思循环检测六种心理操纵模式
- 实验或效果：提出理论框架、设计评估策略，旨在验证方法以增强个人自主性和安全性

## 摘要（原文）

> Manipulative communication, such as gaslighting, guilt-tripping, and emotional coercion, is often difficult for individuals to recognize. Existing agentic AI systems lack the structured, longitudinal memory to track these subtle, context-dependent tactics, often failing due to limited context windows and catastrophic forgetting. We introduce EchoGuard, an agentic AI framework that addresses this gap by using a Knowledge Graph (KG) as the agent's core episodic and semantic memory. EchoGuard employs a structured Log-Analyze-Reflect loop: (1) users log interactions, which the agent structures as nodes and edges in a personal, episodic KG (capturing events, emotions, and speakers); (2) the system executes complex graph queries to detect six psychologically-grounded manipulation patterns (stored as a semantic KG); and (3) an LLM generates targeted Socratic prompts grounded by the subgraph of detected patterns, guiding users toward self-discovery. This framework demonstrates how the interplay between agentic architectures and Knowledge Graphs can empower individuals in recognizing manipulative communication while maintaining personal autonomy and safety. We present the theoretical foundation, framework design, a comprehensive evaluation strategy, and a vision to validate this approach.

