---
layout: default
title: World of Workflows: a Benchmark for Bringing World Models to Enterprise Systems
---

# World of Workflows: a Benchmark for Bringing World Models to Enterprise Systems
**arXiv**：[2601.22130v1](https://arxiv.org/abs/2601.22130) · [PDF](https://arxiv.org/pdf/2601.22130.pdf)  
**作者**：Lakshya Gupta, Litao Li, Yizhe Liu, Sriram Ganapathi Subramanian, Kaheer Suleman, Zichen Zhang, Haoye Lu, Sumit Pasupalak  

**一句话要点**：提出World of Workflows基准以评估大语言模型在企业系统中的隐藏工作流建模能力

**关键词**：企业系统基准, 隐藏工作流建模, 大语言模型评估, 世界模型, 级联效应, ServiceNow环境

## 3 点简述
- 核心问题：现有企业基准忽略隐藏工作流和级联效应，导致大语言模型在复杂系统中表现不佳
- 方法要点：基于ServiceNow构建包含4000+业务规则和55个工作流的真实环境，并设计234个任务的基准
- 实验或效果：发现前沿大语言模型存在动态盲区，需基于世界建模来提升企业代理的可靠性

## 摘要（原文）

> Frontier large language models (LLMs) excel as autonomous agents in many domains, yet they remain untested in complex enterprise systems where hidden workflows create cascading effects across interconnected databases. Existing enterprise benchmarks evaluate surface-level agentic task completion similar to general consumer benchmarks, ignoring true challenges in enterprises, such as limited observability, large database state, and hidden workflows with cascading side effects. We introduce World of Workflows (WoW), a realistic ServiceNow-based environment incorporating 4,000+ business rules and 55 active workflows embedded in the system, alongside WoW-bench, a benchmark of 234 tasks evaluating constrained agentic task completion and enterprise dynamics modeling capabilities. We reveal two major takeaways: (1) Frontier LLMs suffer from dynamics blindness, consistently failing to predict the invisible, cascading side effects of their actions, which leads to silent constraint violations, and (2) reliability in opaque systems requires grounded world modeling, where agents must mentally simulate hidden state transitions to bridge the observability gap when high-fidelity feedback is unavailable. For reliable and useful enterprise agents, WoW motivates a new paradigm to explicitly learn system dynamics. We release our GitHub for setting up and evaluating WoW.

