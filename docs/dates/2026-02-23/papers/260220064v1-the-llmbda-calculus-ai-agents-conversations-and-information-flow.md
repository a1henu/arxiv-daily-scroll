---
layout: default
title: The LLMbda Calculus: AI Agents, Conversations, and Information Flow
---

# The LLMbda Calculus: AI Agents, Conversations, and Information Flow
**arXiv**：[2602.20064v1](https://arxiv.org/abs/2602.20064) · [PDF](https://arxiv.org/pdf/2602.20064.pdf)  
**作者**：Zac Garby, Andrew D. Gordon, David Sands  

**一句话要点**：提出基于lambda演算的形式化模型，以解决AI代理对话中信息流控制与安全漏洞问题。

**关键词**：lambda演算, 信息流控制, AI代理安全, 提示注入, 形式化语义, 非干扰定理

## 3 点简述
- 核心问题：AI代理对话中恶意提示注入导致安全风险，缺乏形式化语义基础。
- 方法要点：扩展无类型按值调用lambda演算，引入动态信息流控制和LLM调用原语。
- 实验或效果：证明终止不敏感非干扰定理，提供完整性、机密性保证，支持防御机制推理。

## 摘要（原文）

> A conversation with a large language model (LLM) is a sequence of prompts and responses, with each response generated from the preceding conversation. AI agents build such conversations automatically: given an initial human prompt, a planner loop interleaves LLM calls with tool invocations and code execution. This tight coupling creates a new and poorly understood attack surface. A malicious prompt injected into a conversation can compromise later reasoning, trigger dangerous tool calls, or distort final outputs. Despite the centrality of such systems, we currently lack a principled semantic foundation for reasoning about their behaviour and safety. We address this gap by introducing an untyped call-by-value lambda calculus enriched with dynamic information-flow control and a small number of primitives for constructing prompt-response conversations. Our language includes a primitive that invokes an LLM: it serializes a value, sends it to the model as a prompt, and parses the response as a new term. This calculus faithfully represents planner loops and their vulnerabilities, including the mechanisms by which prompt injection alters subsequent computation. The semantics explicitly captures conversations, and so supports reasoning about defenses such as quarantined sub-conversations, isolation of generated code, and information-flow restrictions on what may influence an LLM call. A termination-insensitive noninterference theorem establishes integrity and confidentiality guarantees, demonstrating that a formal calculus can provide rigorous foundations for safe agentic programming.

