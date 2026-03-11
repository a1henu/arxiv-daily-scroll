---
layout: default
title: Real-Time Trust Verification for Safe Agentic Actions using TrustBench
---

# Real-Time Trust Verification for Safe Agentic Actions using TrustBench
**arXiv**：[2603.09157v1](https://arxiv.org/abs/2603.09157) · [PDF](https://arxiv.org/pdf/2603.09157.pdf)  
**作者**：Tavishi Sharma, Vinayak Sharma, Pragya Sharma  

**一句话要点**：提出TrustBench框架，在自主代理执行前进行实时信任验证以预防有害行动。

**关键词**：实时信任验证, 自主代理安全, 多维度基准测试, 领域特定插件, 行动前干预

## 3 点简述
- 核心问题：现有评估框架如AgentBench和TrustLLM无法在代理执行过程中实时阻止有害行动。
- 方法要点：TrustBench采用双模式框架，包括多维度基准测试和行动前安全验证工具包，支持领域特定插件。
- 实验或效果：在多个代理任务中，TrustBench减少有害行动87%，领域特定插件比通用验证多降低35%危害，延迟低于200毫秒。

## 摘要（原文）

> As large language models evolve from conversational assistants to autonomous agents, ensuring trustworthiness requires a fundamental shift from post-hoc evaluation to real-time action verification. Current frameworks like AgentBench evaluate task completion, while TrustLLM and HELM assess output quality after generation. However, none of these prevent harmful actions during agent execution. We present TrustBench, a dual-mode framework that (1) benchmarks trust across multiple dimensions using both traditional metrics and LLM-as-a-Judge evaluations, and (2) provides a toolkit agents invoke before taking actions to verify safety and reliability. Unlike existing approaches, TrustBench intervenes at the critical decision point: after an agent formulates an action but before execution. Domain-specific plugins encode specialized safety requirements for healthcare, finance, and technical domains. Across multiple agentic tasks, TrustBench reduced harmful actions by 87%. Domain-specific plugins outperformed generic verification, achieving 35% greater harm reduction. With sub-200ms latency, TrustBench enables practical real-time trust verification for autonomous agents.

