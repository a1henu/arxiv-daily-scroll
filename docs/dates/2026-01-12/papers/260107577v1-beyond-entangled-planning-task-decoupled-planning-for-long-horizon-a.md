---
layout: default
title: Beyond Entangled Planning: Task-Decoupled Planning for Long-Horizon Agents
---

# Beyond Entangled Planning: Task-Decoupled Planning for Long-Horizon Agents
**arXiv**：[2601.07577v1](https://arxiv.org/abs/2601.07577) · [PDF](https://arxiv.org/pdf/2601.07577.pdf)  
**作者**：Yunfan Li, Bingbing Xu, Xueyun Tian, Xiucheng Xu, Huawei Shen  

**一句话要点**：提出任务解耦规划框架，以解决长视野智能体中的上下文纠缠问题。

**关键词**：长视野智能体, 任务解耦规划, 上下文隔离, 有向无环图, 令牌效率

## 3 点简述
- 核心问题：现有规划方法因上下文纠缠导致错误传播和恢复成本高。
- 方法要点：通过监督器分解任务为有向无环图，使用规划器和执行器进行局部推理。
- 实验或效果：在多个基准上超越基线，减少令牌消耗达82%，提升鲁棒性和效率。

## 摘要（原文）

> Recent advances in large language models (LLMs) have enabled agents to autonomously execute complex, long-horizon tasks, yet planning remains a primary bottleneck for reliable task execution. Existing methods typically fall into two paradigms: step-wise planning, which is reactive but often short-sighted; and one-shot planning, which generates a complete plan upfront yet is brittle to execution errors. Crucially, both paradigms suffer from entangled contexts, where the agent must reason over a monolithic history spanning multiple sub-tasks. This entanglement increases cognitive load and lets local errors propagate across otherwise independent decisions, making recovery computationally expensive. To address this, we propose Task-Decoupled Planning (TDP), a training-free framework that replaces entangled reasoning with task decoupling. TDP decomposes tasks into a directed acyclic graph (DAG) of sub-goals via a Supervisor. Using a Planner and Executor with scoped contexts, TDP confines reasoning and replanning to the active sub-task. This isolation prevents error propagation and corrects deviations locally without disrupting the workflow. Results on TravelPlanner, ScienceWorld, and HotpotQA show that TDP outperforms strong baselines while reducing token consumption by up to 82%, demonstrating that sub-task decoupling improves both robustness and efficiency for long-horizon agents.

