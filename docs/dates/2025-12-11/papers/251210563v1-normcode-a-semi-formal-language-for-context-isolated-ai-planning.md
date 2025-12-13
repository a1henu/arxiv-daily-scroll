---
layout: default
title: NormCode: A Semi-Formal Language for Context-Isolated AI Planning
---

# NormCode: A Semi-Formal Language for Context-Isolated AI Planning
**arXiv**：[2512.10563v1](https://arxiv.org/abs/2512.10563) · [PDF](https://arxiv.org/pdf/2512.10563.pdf)  
**作者**：Xin Guan  

**一句话要点**：提出NormCode半形式化语言以解决多步AI工作流中的上下文污染问题

**关键词**：AI规划语言, 上下文隔离, 工作流审计, 语义-句法分离, 半形式化语言

## 3 点简述
- 核心问题：多步LLM工作流中信息累积导致上下文污染，引发幻觉和任务约束丢失
- 方法要点：设计NormCode语言，通过数据隔离和语义-句法操作分离消除跨步污染
- 实验或效果：验证包括加法算法100%准确性和自托管编译器管道，支持审计工作流

## 摘要（原文）

> Multistep workflows that chain large language model (LLM) calls suffer from context pollution: as information accumulates across steps, models hallucinate, confuse intermediate outputs, and lose track of task constraints. We present NormCode, a semiformal language for constructing plans of inferences, structured decompositions where each step operates in data isolation and receives only explicitly passed inputs, which eliminates crossstep contamination by design. NormCode enforces a strict separation between semantic operations (LLMdriven reasoning, nondeterministic) and syntactic operations (deterministic data restructuring), enabling precise cost and reliability tracing. The language exists in three isomorphic formats: .ncds for human authoring, .ncd for machine execution, and .ncn for human verification, supporting progressive formalization from sketch to production. We validate NormCode through two demonstrations: (1) a base X addition algorithm achieving 100 percent accuracy on arbitrary length inputs, and (2) self hosted execution of NormCode's own five phase compiler pipeline. The working orchestrator provides dependency driven scheduling, SQLite backed checkpointing, and loop management, making AI workflows auditable by design and addressing a critical need for transparency in high stakes domains such as legal reasoning, medical decision making, and financial analysis.

