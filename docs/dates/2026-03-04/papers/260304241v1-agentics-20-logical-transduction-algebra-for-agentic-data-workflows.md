---
layout: default
title: Agentics 2.0: Logical Transduction Algebra for Agentic Data Workflows
---

# Agentics 2.0: Logical Transduction Algebra for Agentic Data Workflows
**arXiv**：[2603.04241v1](https://arxiv.org/abs/2603.04241) · [PDF](https://arxiv.org/pdf/2603.04241.pdf)  
**作者**：Alfio Massimiliano Gliozzo, Junkyu Lee, Nahuel Defosse  

**一句话要点**：提出Agentics 2.0框架，通过逻辑转导代数构建可靠、可扩展的代理式数据工作流。

**关键词**：代理式AI, 逻辑转导代数, 数据工作流, 类型安全, 异步Map-Reduce, 语义可靠性

## 3 点简述
- 核心问题：代理式AI从研究原型转向企业部署，需满足可靠性、可扩展性和可观测性等软件质量属性。
- 方法要点：基于逻辑转导代数，将大语言模型推理形式化为类型化语义转换，支持无状态异步并行执行。
- 实验或效果：在DiscoveryBench和Archer等基准测试中实现先进性能，验证了框架的有效性。

## 摘要（原文）

> Agentic AI is rapidly transitioning from research prototypes to enterprise deployments, where requirements extend to meet the software quality attributes of reliability, scalability, and observability beyond plausible text generation. We present Agentics 2.0, a lightweight, Python-native framework for building high-quality, structured, explainable, and type-safe agentic data workflows. At the core of Agentics 2.0, the logical transduction algebra formalizes a large language model inference call as a typed semantic transformation, which we call a transducible function that enforces schema validity and the locality of evidence. The transducible functions compose into larger programs via algebraically grounded operators and execute as stateless asynchronous calls in parallel in asynchronous Map-Reduce programs. The proposed framework provides semantic reliability through strong typing, semantic observability through evidence tracing between slots of the input and output types, and scalability through stateless parallel execution. We instantiate reusable design patterns and evaluate the programs in Agentics 2.0 on challenging benchmarks, including DiscoveryBench for data-driven discovery and Archer for NL-to-SQL semantic parsing, demonstrating state-of-the-art performance.

