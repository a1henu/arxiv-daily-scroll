---
layout: default
title: TAAF: A Trace Abstraction and Analysis Framework Synergizing Knowledge Graphs and LLMs
---

# TAAF: A Trace Abstraction and Analysis Framework Synergizing Knowledge Graphs and LLMs
**arXiv**：[2601.02632v1](https://arxiv.org/abs/2601.02632) · [PDF](https://arxiv.org/pdf/2601.02632.pdf)  
**作者**：Alireza Ezaz, Ghazal Khodabandeh, Majid Babaei, Naser Ezzati-Jivan  

**一句话要点**：提出TAAF框架，结合知识图谱与LLMs解决大规模执行轨迹分析难题

**关键词**：执行轨迹分析, 知识图谱, 大型语言模型, 时间索引, 自然语言查询, 软件调试

## 3 点简述
- 核心问题：大规模执行轨迹（如OS内核）分析困难，现有工具依赖预定义分析，定制化需手动脚本，易错耗时。
- 方法要点：TAAF通过时间索引知识图谱捕获轨迹实体关系，利用LLM解释子图回答自然语言查询，减少人工检查。
- 实验或效果：基于TraceQA-100基准测试，TAAF提升答案准确率最高31.2%，尤其在多跳和因果推理任务中表现突出。

## 摘要（原文）

> Execution traces are a critical source of information for understanding, debugging, and optimizing complex software systems. However, traces from OS kernels or large-scale applications like Chrome or MySQL are massive and difficult to analyze. Existing tools rely on predefined analyses, and custom insights often require writing domain-specific scripts, which is an error-prone and time-consuming task. This paper introduces TAAF (Trace Abstraction and Analysis Framework), a novel approach that combines time-indexing, knowledge graphs (KGs), and large language models (LLMs) to transform raw trace data into actionable insights. TAAF constructs a time-indexed KG from trace events to capture relationships among entities such as threads, CPUs, and system resources. An LLM then interprets query-specific subgraphs to answer natural-language questions, reducing the need for manual inspection and deep system expertise. To evaluate TAAF, we introduce TraceQA-100, a benchmark of 100 questions grounded in real kernel traces. Experiments across three LLMs and multiple temporal settings show that TAAF improves answer accuracy by up to 31.2%, particularly in multi-hop and causal reasoning tasks. We further analyze where graph-grounded reasoning helps and where limitations remain, offering a foundation for next-generation trace analysis tools.

