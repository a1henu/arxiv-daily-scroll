---
layout: default
title: EPOCH: An Agentic Protocol for Multi-Round System Optimization
---

# EPOCH: An Agentic Protocol for Multi-Round System Optimization
**arXiv**：[2603.09049v1](https://arxiv.org/abs/2603.09049) · [PDF](https://arxiv.org/pdf/2603.09049.pdf)  
**作者**：Zhanlin Liu, Yitao Li, Munirathnam Srikanth  

**一句话要点**：提出EPOCH协议以统一异构环境中的多轮系统优化流程

**关键词**：多轮系统优化, 自主代理, 工程协议, 异构环境, 基准构建, 迭代自改进

## 3 点简述
- 现有方法多为任务特定优化循环，缺乏统一协议来建立基准和管理多轮自改进
- EPOCH将优化分为基准构建和迭代自改进两阶段，并通过角色约束阶段标准化执行
- 实证研究展示了EPOCH在生产导向自主改进工作流程中的实用性

## 摘要（原文）

> Autonomous agents are increasingly used to improve prompts, code, and machine learning systems through iterative execution and feedback. Yet existing approaches are usually designed as task-specific optimization loops rather than as a unified protocol for establishing baselines and managing tracked multi-round self-improvement. We introduce EPOCH, an engineering protocol for multi-round system optimization in heterogeneous environments. EPOCH organizes optimization into two phases: baseline construction and iterative self-improvement. It further structures each round through role-constrained stages that separate planning, implementation, and evaluation, and standardizes execution through canonical command interfaces and round-level tracking. This design enables coordinated optimization across prompts, model configurations, code, and rule-based components while preserving stability, reproducibility, traceability, and integrity of evaluation. Empirical studies in various tasks illustrate the practicality of EPOCH for production-oriented autonomous improvement workflows.

