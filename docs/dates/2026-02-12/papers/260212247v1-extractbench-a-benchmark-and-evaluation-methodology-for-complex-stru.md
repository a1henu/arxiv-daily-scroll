---
layout: default
title: ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction
---

# ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction
**arXiv**：[2602.12247v1](https://arxiv.org/abs/2602.12247) · [PDF](https://arxiv.org/pdf/2602.12247.pdf)  
**作者**：Nick Ferguson, Josh Pennington, Narek Beghian, Aravind Mohan, Douwe Kiela, Sheshansh Agrawal, Thien Hang Nguyen  

**一句话要点**：提出ExtractBench基准与评估框架，解决PDF到JSON结构化提取的端到端评测难题。

**关键词**：PDF到JSON提取, 结构化提取基准, 评估框架, 嵌套提取语义, 企业级模式, LLM评估

## 3 点简述
- 核心问题：缺乏企业级模式广度的PDF到JSON提取端到端基准，以及嵌套提取语义的评估方法。
- 方法要点：开源基准包含35个PDF文档与JSON模式，评估框架将模式作为可执行规范，每个字段声明评分指标。
- 实验或效果：前沿模型在现实模式上不可靠，性能随模式广度急剧下降，369字段财务报告模式上所有模型输出无效。

## 摘要（原文）

> Unstructured documents like PDFs contain valuable structured information, but downstream systems require this data in reliable, standardized formats. LLMs are increasingly deployed to automate this extraction, making accuracy and reliability paramount. However, progress is bottlenecked by two gaps. First, no end-to-end benchmark evaluates PDF-to-JSON extraction under enterprise-scale schema breadth. Second, no principled methodology captures the semantics of nested extraction, where fields demand different notions of correctness (exact match for identifiers, tolerance for quantities, semantic equivalence for names), arrays require alignment, and omission must be distinguished from hallucination. We address both gaps with ExtractBench, an open-source benchmark and evaluation framework for PDF-to-JSON structured extraction. The benchmark pairs 35 PDF documents with JSON Schemas and human-annotated gold labels across economically valuable domains, yielding 12,867 evaluatable fields spanning schema complexities from tens to hundreds of fields. The evaluation framework treats the schema as an executable specification: each field declares its scoring metric. Baseline evaluations reveal that frontier models (GPT-5/5.2, Gemini-3 Flash/Pro, Claude 4.5 Opus/Sonnet) remain unreliable on realistic schemas. Performance degrades sharply with schema breadth, culminating in 0% valid output on a 369-field financial reporting schema across all tested models. We release ExtractBench at https://github.com/ContextualAI/extract-bench.

