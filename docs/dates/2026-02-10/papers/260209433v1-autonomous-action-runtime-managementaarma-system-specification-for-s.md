---
layout: default
title: Autonomous Action Runtime Management(AARM):A System Specification for Securing AI-Driven Actions at Runtime
---

# Autonomous Action Runtime Management(AARM):A System Specification for Securing AI-Driven Actions at Runtime
**arXiv**：[2602.09433v1](https://arxiv.org/abs/2602.09433) · [PDF](https://arxiv.org/pdf/2602.09433.pdf)  
**作者**：Herman Errico  

**一句话要点**：提出AARM规范以在运行时保护AI驱动的自主行动安全

**关键词**：运行时安全, AI自主行动, 威胁模型, 策略执行, 防篡改记录, 互操作性规范

## 3 点简述
- 核心问题：AI自主行动不可逆、高速执行，传统安全范式失效
- 方法要点：定义运行时拦截、上下文积累、策略评估和防篡改记录的规范
- 实验或效果：提出四种实现架构和最小符合要求，确保模型无关和互操作性

## 摘要（原文）

> As artificial intelligence systems evolve from passive assistants into autonomous agents capable of executing consequential actions, the security boundary shifts from model outputs to tool execution. Traditional security paradigms - log aggregation, perimeter defense, and post-hoc forensics - cannot protect systems where AI-driven actions are irreversible, execute at machine speed, and originate from potentially compromised orchestration layers. This paper introduces Autonomous Action Runtime Management (AARM), an open specification for securing AI-driven actions at runtime. AARM defines a runtime security system that intercepts actions before execution, accumulates session context, evaluates against policy and intent alignment, enforces authorization decisions, and records tamper-evident receipts for forensic reconstruction. We formalize a threat model addressing prompt injection, confused deputy attacks, data exfiltration, and intent drift. We introduce an action classification framework distinguishing forbidden, context-dependent deny, and context-dependent allow actions. We propose four implementation architectures - protocol gateway, SDK instrumentation, kernel eBPF, and vendor integration - with distinct trust properties, and specify minimum conformance requirements for AARM-compliant systems. AARM is model-agnostic, framework-agnostic, and vendor-neutral, treating action execution as the stable security boundary. This specification aims to establish industry-wide requirements before proprietary fragmentation forecloses interoperability.

