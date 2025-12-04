---
layout: default
title: Reason-Plan-ReAct: A Reasoner-Planner Supervising a ReAct Executor for Complex Enterprise Tasks
---

# Reason-Plan-ReAct: A Reasoner-Planner Supervising a ReAct Executor for Complex Enterprise Tasks
**arXiv**：[2512.03560v1](https://arxiv.org/abs/2512.03560) · [PDF](https://arxiv.org/pdf/2512.03560.pdf)  
**作者**：Gianni Molinari, Fabio Ciravegna  

**一句话要点**：提出RP-ReAct多智能体架构以解决企业复杂任务中的规划执行不稳定与上下文窗口限制问题

**关键词**：多智能体架构, 规划执行解耦, 上下文管理, 企业任务自动化, 推理模型评估, ReAct执行器

## 3 点简述
- 核心问题：单智能体架构导致轨迹不稳定，本地模型上下文窗口小易溢出，影响企业复杂任务处理
- 方法要点：引入Reasoner Planner Agent进行战略规划，Proxy-Execution Agent执行ReAct交互，并采用上下文保存策略管理大输出
- 实验或效果：在ToolQA基准上评估，使用六种开放权重推理模型，显示性能优于基线，增强泛化能力与稳定性

## 摘要（原文）

> Despite recent advances, autonomous agents often struggle to solve complex tasks in enterprise domains that require coordinating multiple tools and processing diverse data sources. This struggle is driven by two main limitations. First, single-agent architectures enforce a monolithic plan-execute loop, which directly causes trajectory instability. Second, the requirement to use local open-weight models for data privacy introduces smaller context windows leading to the rapid consumption of context from large tool outputs. To solve this problem we introduce RP-ReAct (Reasoner Planner-ReAct), a novel multi-agent approach that fundamentally decouples strategic planning from low-level execution to achieve superior reliability and efficiency. RP-ReAct consists of a Reasoner Planner Agent (RPA), responsible for planning each sub-step, continuously analysing the execution results using the strong reasoning capabilities of a Large Reasoning Model, and one or multiple Proxy-Execution Agent (PEA) that translates sub-steps into concrete tool interactions using a ReAct approach. Crucially, we incorporate a context-saving strategy within the PEA to mitigate context window overflow by managing large tool outputs via external storage and on-demand access. We evaluate RP-ReAct, on the challenging, multi-domain ToolQA benchmark using a diverse set of six open-weight reasoning models. Our empirical results show that RP-ReAct achieves superior performance and improved generalization ability over state-of-the-art baselines when addressing diverse complex tasks across the evaluated domains. Furthermore we establish the enhanced robustness and stability of our approach across different model scales, paving the way for effective and deployable agentic solutions for enterprises.

