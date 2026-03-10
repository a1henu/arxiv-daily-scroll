---
layout: default
title: OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning
---

# OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning
**arXiv**：[2603.08655v1](https://arxiv.org/abs/2603.08655) · [PDF](https://arxiv.org/pdf/2603.08655.pdf)  
**作者**：Krista Opsahl-Ong, Arnav Singhvi, Jasmine Collins, Ivan Zhou, Cindy Wang, Ashutosh Baheti, Owen Oertell, Jacob Portes, Sam Havens, Erich Elsen, Michael Bendersky, Matei Zaharia, Xing Chen  

**一句话要点**：提出OfficeQA Pro基准，用于评估AI代理在异构文档上的端到端接地推理能力。

**关键词**：接地推理, 多文档问答, 异构文档解析, 企业级基准, AI代理评估

## 3 点简述
- 核心问题：评估AI代理在大型异构文档库上的多文档接地推理能力。
- 方法要点：基于美国财政部公报构建包含13.3万页和2600万数值的基准，要求精确解析、检索和分析。
- 实验或效果：前沿LLM在参数知识下准确率低于5%，提供文档后平均准确率为34.1%，结构化表示提升16.1%相对性能。

## 摘要（原文）

> We introduce OfficeQA Pro, a benchmark for evaluating AI agents on grounded, multi-document reasoning over a large and heterogeneous document corpus. The corpus consists of U.S. Treasury Bulletins spanning nearly 100 years, comprising 89,000 pages and over 26 million numerical values. OfficeQA Pro consists of 133 questions that require precise document parsing, retrieval, and analytical reasoning across both unstructured text and tabular data. Frontier LLMs including Claude Opus 4.6, GPT-5.4, and Gemini 3.1 Pro Preview achieve less than 5% accuracy on OfficeQA Pro when relying on parametric knowledge, and less than 12% with additional access to the web. When provided directly with the document corpus, frontier agents still struggle on over half of questions, scoring 34.1% on average. We find that providing agents with a structured document representation produced by Databricks' ai_parse_document yields a 16.1% average relative performance gain across agents. We conduct additional ablations to study the effects of model selection, table representation, retrieval strategy, and test-time scaling on performance. Despite these improvements, significant headroom remains before agents can be considered reliable at enterprise-grade grounded reasoning.

