---
layout: default
title: Discovering High Level Patterns from Simulation Traces
---

# Discovering High Level Patterns from Simulation Traces
**arXiv**：[2602.10009v1](https://arxiv.org/abs/2602.10009) · [PDF](https://arxiv.org/pdf/2602.10009.pdf)  
**作者**：Sean Memery, Kartic Subr  

**一句话要点**：提出自然语言引导方法从仿真日志中发现粗粒度模式以增强物理推理

**关键词**：仿真日志分析, 物理推理增强, 自然语言引导, 模式发现, 奖励程序生成

## 3 点简述
- 问题：语言模型在物理推理任务中因缺乏仿真基础而表现不佳，仿真日志作为上下文可扩展性差
- 方法：通过合成程序将详细仿真日志映射到高层激活模式，如刚体碰撞和稳定支撑
- 效果：在物理基准测试中，该方法使仿真日志更适于自然语言推理，并支持生成奖励程序

## 摘要（原文）

> Artificial intelligence (AI) agents embedded in environments with physics-based interaction face many challenges including reasoning, planning, summarization, and question answering. This problem is exacerbated when a human user wishes to either guide or interact with the agent in natural language. Although the use of Language Models (LMs) is the default choice, as an AI tool, they struggle with tasks involving physics. The LM's capability for physical reasoning is learned from observational data, rather than being grounded in simulation. A common approach is to include simulation traces as context, but this suffers from poor scalability as simulation traces contain larger volumes of fine-grained numerical and semantic data. In this paper, we propose a natural language guided method to discover coarse-grained patterns (e.g., 'rigid-body collision', 'stable support', etc.) from detailed simulation logs. Specifically, we synthesize programs that operate on simulation logs and map them to a series of high level activated patterns. We show, through two physics benchmarks, that this annotated representation of the simulation log is more amenable to natural language reasoning about physical systems. We demonstrate how this method enables LMs to generate effective reward programs from goals specified in natural language, which may be used within the context of planning or supervised learning.

