---
layout: default
title: MedMCP-Calc: Benchmarking LLMs for Realistic Medical Calculator Scenarios via MCP Integration
---

# MedMCP-Calc: Benchmarking LLMs for Realistic Medical Calculator Scenarios via MCP Integration
**arXiv**：[2601.23049v1](https://arxiv.org/abs/2601.23049) · [PDF](https://arxiv.org/pdf/2601.23049.pdf)  
**作者**：Yakun Zhu, Yutong Huang, Shengqian Qin, Zhongzhen Huang, Shaoting Zhang, Xiaofan Zhang  

**一句话要点**：提出MedMCP-Calc基准，通过MCP集成评估LLMs在真实医疗计算器场景中的表现。

**关键词**：医疗计算器基准, 模型上下文协议, 结构化EHR交互, 外部工具检索, 过程级评估, 开源模型优化

## 3 点简述
- 核心问题：现有基准仅关注静态单步计算，忽略真实医疗计算器使用的自适应多阶段过程。
- 方法要点：集成MCP，包含模糊任务描述、结构化EHR数据库交互和外部参考检索。
- 实验或效果：评估23个模型，揭示关键局限，并开发CalcMate模型实现开源最优性能。

## 摘要（原文）

> Medical calculators are fundamental to quantitative, evidence-based clinical practice. However, their real-world use is an adaptive, multi-stage process, requiring proactive EHR data acquisition, scenario-dependent calculator selection, and multi-step computation, whereas current benchmarks focus only on static single-step calculations with explicit instructions. To address these limitations, we introduce MedMCP-Calc, the first benchmark for evaluating LLMs in realistic medical calculator scenarios through Model Context Protocol (MCP) integration. MedMCP-Calc comprises 118 scenario tasks across 4 clinical domains, featuring fuzzy task descriptions mimicking natural queries, structured EHR database interaction, external reference retrieval, and process-level evaluation. Our evaluation of 23 leading models reveals critical limitations: even top performers like Claude Opus 4.5 exhibit substantial gaps, including difficulty selecting appropriate calculators for end-to-end workflows given fuzzy queries, poor performance in iterative SQL-based database interactions, and marked reluctance to leverage external tools for numerical computation. Performance also varies considerably across clinical domains. Building on these findings, we develop CalcMate, a fine-tuned model incorporating scenario planning and tool augmentation, achieving state-of-the-art performance among open-source models. Benchmark and Codes are available in https://github.com/SPIRAL-MED/MedMCP-Calc.

