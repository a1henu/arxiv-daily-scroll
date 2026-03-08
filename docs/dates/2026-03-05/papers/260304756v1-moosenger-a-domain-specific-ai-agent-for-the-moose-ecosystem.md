---
layout: default
title: MOOSEnger -- a Domain-Specific AI Agent for the MOOSE Ecosystem
---

# MOOSEnger -- a Domain-Specific AI Agent for the MOOSE Ecosystem
**arXiv**：[2603.04756v1](https://arxiv.org/abs/2603.04756) · [PDF](https://arxiv.org/pdf/2603.04756.pdf)  
**作者**：Mengnan Li, Jason Miller, Zachary Prince, Alexander Lindsay, Cody Permann  

**一句话要点**：提出MOOSEnger，一个针对MOOSE生态系统的领域特定AI代理，以解决输入文件设置和调试缓慢的问题。

**关键词**：领域特定AI代理, 检索增强生成, 输入文件解析, MOOSE生态系统, 语法验证, 执行测试

## 3 点简述
- 核心问题：MOOSE模拟环境中的HIT输入文件对象目录庞大、语法严格，导致初始设置和调试耗时。
- 方法要点：结合检索增强生成与确定性解析工具，通过对话工作流将自然语言意图转换为可运行输入。
- 实验或效果：在125个提示基准测试中，执行通过率达0.93，显著优于仅使用LLM的基线（0.08）。

## 摘要（原文）

> MOOSEnger is a tool-enabled AI agent tailored to the Multiphysics Object-Oriented Simulation Environment (MOOSE). MOOSE cases are specified in HIT ".i" input files; the large object catalog and strict syntax make initial setup and debugging slow. MOOSEnger offers a conversational workflow that turns natural-language intent into runnable inputs by combining retrieval-augmented generation over curated docs/examples with deterministic, MOOSE-aware parsing, validation, and execution tools. A core-plus-domain architecture separates reusable agent infrastructure (configuration, registries, tool dispatch, retrieval services, persistence, and evaluation) from a MOOSE plugin that adds HIT-based parsing, syntax-preserving ingestion of input files, and domain-specific utilities for input repair and checking. An input precheck pipeline removes hidden formatting artifacts, fixes malformed HIT structure with a bounded grammar-constrained loop, and resolves invalid object types via similarity search over an application syntax registry. Inputs are then validated and optionally smoke-tested with the MOOSE runtime in the loop via an MCP-backed execution backend (with local fallback), translating solver diagnostics into iterative verify-and-correct updates. Built-in evaluation reports RAG metrics (faithfulness, relevancy, context precision/recall) and end-to-end success by actual execution. On a 125-prompt benchmark spanning diffusion, transient heat conduction, solid mechanics, porous flow, and incompressible Navier--Stokes, MOOSEnger achieves a 0.93 execution pass rate versus 0.08 for an LLM-only baseline.

