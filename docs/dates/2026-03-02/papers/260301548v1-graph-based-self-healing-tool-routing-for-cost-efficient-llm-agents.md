---
layout: default
title: Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents
---

# Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents
**arXiv**：[2603.01548v1](https://arxiv.org/abs/2603.01548) · [PDF](https://arxiv.org/pdf/2603.01548.pdf)  
**作者**：Neeraj Bholani  

**一句话要点**：提出基于图的自愈工具路由以解决LLM代理的可靠性-成本权衡问题

**关键词**：LLM代理, 工具路由, 故障容错, 图算法, 成本效率, 确定性恢复

## 3 点简述
- 核心问题：工具使用LLM代理面临可靠性（高成本）与成本（低可靠性）的权衡，尤其在复合工具故障下静态工作流易失效。
- 方法要点：结合并行健康监控器和成本加权工具图，使用Dijkstra算法进行确定性最短路径路由，实现运行时故障容错与自动恢复。
- 实验或效果：在19个场景中，匹配ReAct的正确性，减少93%的控制平面LLM调用，并消除复合故障下的静默失败。

## 摘要（原文）

> Tool-using LLM agents face a reliability-cost tradeoff: routing every decision through the LLM improves correctness but incurs high latency and inference cost, while pre-coded workflow graphs reduce cost but become brittle under unanticipated compound tool failures. We present Self-Healing Router, a fault-tolerant orchestration architecture that treats most agent control-flow decisions as routing rather than reasoning. The system combines (i) parallel health monitors that assign priority scores to runtime conditions such as tool outages and risk signals, and (ii) a cost-weighted tool graph where Dijkstra's algorithm performs deterministic shortest-path routing. When a tool fails mid-execution, its edges are reweighted to infinity and the path is recomputed -- yielding automatic recovery without invoking the LLM. The LLM is reserved exclusively for cases where no feasible path exists, enabling goal demotion or escalation. Prior graph-based tool-use systems (ControlLLM, ToolNet, NaviAgent) focus on tool selection and planning; our contribution is runtime fault tolerance with deterministic recovery and binary observability -- every failure is either a logged reroute or an explicit escalation, never a silent skip. Across 19 scenarios spanning three graph topologies (linear pipeline, dependency DAG, parallel fan-out), Self-Healing Router matches ReAct's correctness while reducing control-plane LLM calls by 93% (9 vs 123 aggregate) and eliminating the silent-failure cases observed in a well-engineered static workflow baseline under compound failures.

