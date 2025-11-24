---
layout: default
title: Designing Domain-Specific Agents via Hierarchical Task Abstraction Mechanism
---

# Designing Domain-Specific Agents via Hierarchical Task Abstraction Mechanism
**arXiv**：[2511.17198v1](https://arxiv.org/abs/2511.17198) · [PDF](https://arxiv.org/pdf/2511.17198.pdf)  
**作者**：Kaiyu Li, Jiayu Wang, Zhi Wang, Hui Qiao, Weizhan Zhang, Deyu Meng, Xiangyong Cao  

**一句话要点**：提出分层任务抽象机制以解决专业领域多步任务规划问题

**关键词**：分层任务抽象, 多代理系统, 地理空间分析, 任务规划, 专业领域代理

## 3 点简述
- 核心问题：通用LLM代理在需要严格工作流的专业领域表现不佳
- 方法要点：基于任务依赖图构建分层多代理系统，确保程序正确性
- 实验或效果：在GeoPlan-bench上，EarthAgent显著优于现有单/多代理系统

## 摘要（原文）

> LLM-driven agents, particularly those using general frameworks like ReAct or human-inspired role-playing, often struggle in specialized domains that necessitate rigorously structured workflows. Fields such as remote sensing, requiring specialized tools (e.g., correction, spectral indices calculation), and multi-step procedures (e.g., numerous intermediate products and optional steps), significantly challenge generalized approaches. To address this gap, we introduce a novel agent design framework centered on a Hierarchical Task Abstraction Mechanism (HTAM). Specifically, HTAM moves beyond emulating social roles, instead structuring multi-agent systems into a logical hierarchy that mirrors the intrinsic task-dependency graph of a given domain. This task-centric architecture thus enforces procedural correctness and decomposes complex problems into sequential layers, where each layer's sub-agents operate on the outputs of the preceding layers. We instantiate this framework as EarthAgent, a multi-agent system tailored for complex geospatial analysis. To evaluate such complex planning capabilities, we build GeoPlan-bench, a comprehensive benchmark of realistic, multi-step geospatial planning tasks. It is accompanied by a suite of carefully designed metrics to evaluate tool selection, path similarity, and logical completeness. Experiments show that EarthAgent substantially outperforms a range of established single- and multi-agent systems. Our work demonstrates that aligning agent architecture with a domain's intrinsic task structure is a critical step toward building robust and reliable specialized autonomous systems.

