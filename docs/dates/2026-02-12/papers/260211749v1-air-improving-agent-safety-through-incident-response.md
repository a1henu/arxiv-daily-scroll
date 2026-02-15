---
layout: default
title: AIR: Improving Agent Safety through Incident Response
---

# AIR: Improving Agent Safety through Incident Response
**arXiv**：[2602.11749v1](https://arxiv.org/abs/2602.11749) · [PDF](https://arxiv.org/pdf/2602.11749.pdf)  
**作者**：Zibo Xiao, Jun Sun, Junjie Chen  

**一句话要点**：提出AIR框架以增强LLM代理在自主应用中的事故响应能力

**关键词**：LLM代理安全, 事故响应框架, 自主应用, 语义检测, 规则合成, 安全机制

## 3 点简述
- 核心问题：现有LLM代理安全机制侧重于事前预防，缺乏事故后的响应、遏制和恢复能力。
- 方法要点：AIR定义领域特定语言，集成到代理执行循环中，实现事故检测、遏制、恢复和规则合成。
- 实验或效果：在三种代理类型上评估，检测、修复和根除成功率均超过90%，规则生成效果接近人工编写。

## 摘要（原文）

> Large Language Model (LLM) agents are increasingly deployed in practice across a wide range of autonomous applications. Yet current safety mechanisms for LLM agents focus almost exclusively on preventing failures in advance, providing limited capabilities for responding to, containing, or recovering from incidents after they inevitably arise. In this work, we introduce AIR, the first incident response framework for LLM agent systems. AIR defines a domain-specific language for managing the incident response lifecycle autonomously in LLM agent systems, and integrates it into the agent's execution loop to (1) detect incidents via semantic checks grounded in the current environment state and recent context, (2) guide the agent to execute containment and recovery actions via its tools, and (3) synthesize guardrail rules during eradication to block similar incidents in future executions. We evaluate AIR on three representative agent types. Results show that AIR achieves detection, remediation, and eradication success rates all exceeding 90%. Extensive experiments further confirm the necessity of AIR's key design components, show the timeliness and moderate overhead of AIR, and demonstrate that LLM-generated rules can approach the effectiveness of developer-authored rules across domains. These results show that incident response is both feasible and essential as a first-class mechanism for improving agent safety.

