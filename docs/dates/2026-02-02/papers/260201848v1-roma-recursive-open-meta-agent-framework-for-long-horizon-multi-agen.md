---
layout: default
title: ROMA: Recursive Open Meta-Agent Framework for Long-Horizon Multi-Agent Systems
---

# ROMA: Recursive Open Meta-Agent Framework for Long-Horizon Multi-Agent Systems
**arXiv**：[2602.01848v1](https://arxiv.org/abs/2602.01848) · [PDF](https://arxiv.org/pdf/2602.01848.pdf)  
**作者**：Salaheddin Alzu'bi, Baran Nama, Arda Kaz, Anushri Eswaran, Weiyuan Chen, Sarvesh Khetan, Rishab Bala, Tu Vu, Sewoong Oh  

**一句话要点**：提出ROMA框架以解决长视野多智能体系统中的推理深度扩展与上下文管理问题

**关键词**：多智能体系统, 递归任务分解, 上下文管理, 模块化框架, 长视野推理, 提示优化

## 3 点简述
- 当前智能体框架在长视野任务中表现不佳，面临推理深度增加时的脆弱性、上下文窗口限制和调试困难。
- ROMA通过递归任务分解和结构化聚合，支持并行执行和上下文控制，采用模块化角色设计实现透明层次化执行。
- 结合GEPA+提示搜索，在SEAL-0和EQ-Bench基准上实现领先性能，提升准确性和匹配闭源模型能力。

## 摘要（原文）

> Current agentic frameworks underperform on long-horizon tasks. As reasoning depth increases, sequential orchestration becomes brittle, context windows impose hard limits that degrade performance, and opaque execution traces make failures difficult to localize or debug. We introduce ROMA (Recursive Open Meta-Agents), a domain-agnostic framework that addresses these limitations through recursive task decomposition and structured aggregation. ROMA decomposes goals into dependency-aware subtask trees that can be executed in parallel, while aggregation compresses and validates intermediate results to control context growth. Our framework standardizes agent construction around four modular roles --Atomizer (which decides whether a task should be decomposed), Planner, Executor, and Aggregator -- which cleanly separate orchestration from model selection and enable transparent, hierarchical execution traces. This design supports heterogeneous multi-agent systems that mix models and tools according to cost, latency, and capability. To adapt ROMA to specific tasks without fine-tuning, we further introduce GEPA$+$, an improved Genetic-Pareto prompt proposer that searches over prompts within ROMA's component hierarchy while preserving interface contracts. We show that ROMA, combined with GEPA+, delivers leading system-level performance on reasoning and long-form generation benchmarks. On SEAL-0, which evaluates reasoning over conflicting web evidence, ROMA instantiated with GLM-4.6 improves accuracy by 9.9\% over Kimi-Researcher. On EQ-Bench, a long-form writing benchmark, ROMA enables DeepSeek-V3 to match the performance of leading closed-source models such as Claude Sonnet 4.5. Our results demonstrate that recursive, modular agent architectures can scale reasoning depth while remaining interpretable, flexible, and model-agnostic.

