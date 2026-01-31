---
layout: default
title: Optimizing Agentic Workflows using Meta-tools
---

# Optimizing Agentic Workflows using Meta-tools
**arXiv**：[2601.22037v1](https://arxiv.org/abs/2601.22037) · [PDF](https://arxiv.org/pdf/2601.22037.pdf)  
**作者**：Sami Abuzakuk, Anne-Marie Kermarrec, Rishi Sharma, Rasmus Moorits Veski, Martijn de Vos  

**一句话要点**：提出Agent Workflow Optimization框架，通过元工具优化代理工作流以减少LLM调用和提升成功率。

**关键词**：代理工作流优化, 元工具, LLM调用减少, 任务成功率提升, 确定性工具, 工作流轨迹分析

## 3 点简述
- 核心问题：代理工作流因多次迭代推理和工具调用导致高成本、延迟和幻觉失败。
- 方法要点：分析工作流轨迹，将重复工具调用序列转换为确定性元工具，减少中间LLM推理步骤。
- 实验效果：在基准测试中，LLM调用减少达11.9%，任务成功率提升达4.2个百分点。

## 摘要（原文）

> Agentic AI enables LLM to dynamically reason, plan, and interact with tools to solve complex tasks. However, agentic workflows often require many iterative reasoning steps and tool invocations, leading to significant operational expense, end-to-end latency and failures due to hallucinations. This work introduces Agent Workflow Optimization (AWO), a framework that identifies and optimizes redundant tool execution patterns to improve the efficiency and robustness of agentic workflows. AWO analyzes existing workflow traces to discover recurring sequences of tool calls and transforms them into meta-tools, which are deterministic, composite tools that bundle multiple agent actions into a single invocation. Meta-tools bypass unnecessary intermediate LLM reasoning steps and reduce operational cost while also shortening execution paths, leading to fewer failures. Experiments on two agentic AI benchmarks show that AWO reduces the number of LLM calls up to 11.9% while also increasing the task success rate by up to 4.2 percent points.

