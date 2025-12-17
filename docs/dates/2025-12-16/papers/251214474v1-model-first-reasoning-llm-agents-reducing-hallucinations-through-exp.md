---
layout: default
title: Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling
---

# Model-First Reasoning LLM Agents: Reducing Hallucinations through Explicit Problem Modeling
**arXiv**：[2512.14474v1](https://arxiv.org/abs/2512.14474) · [PDF](https://arxiv.org/pdf/2512.14474.pdf)  
**作者**：Annu Rana, Gaurav Kumar  

**一句话要点**：提出模型优先推理以解决大语言模型在复杂规划任务中的幻觉问题

**关键词**：大语言模型, 规划任务, 显式建模, 约束满足, 模型优先推理, AI代理

## 3 点简述
- 核心问题：大语言模型在复杂多步规划任务中常违反约束并产生不一致解
- 方法要点：采用两阶段范式，先构建问题的显式模型再生成解决方案
- 实验或效果：在多个规划领域减少约束违反并提升解质量，显式建模是关键

## 摘要（原文）

> Large Language Models (LLMs) often struggle with complex multi-step planning tasks, showing high rates of constraint violations and inconsistent solutions. Existing strategies such as Chain-of-Thought and ReAct rely on implicit state tracking and lack an explicit problem representation. Inspired by classical AI planning, we propose Model-First Reasoning (MFR), a two-phase paradigm in which the LLM first constructs an explicit model of the problem, defining entities, state variables, actions, and constraints, before generating a solution plan. Across multiple planning domains, including medical scheduling, route planning, resource allocation, logic puzzles, and procedural synthesis, MFR reduces constraint violations and improves solution quality compared to Chain-of-Thought and ReAct. Ablation studies show that the explicit modeling phase is critical for these gains. Our results suggest that many LLM planning failures stem from representational deficiencies rather than reasoning limitations, highlighting explicit modeling as a key component for robust and interpretable AI agents. All prompts, evaluation procedures, and task datasets are documented to facilitate reproducibility.

