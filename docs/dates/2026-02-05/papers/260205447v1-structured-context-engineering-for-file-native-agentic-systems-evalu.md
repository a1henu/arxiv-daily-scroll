---
layout: default
title: Structured Context Engineering for File-Native Agentic Systems: Evaluating Schema Accuracy, Format Effectiveness, and Multi-File Navigation at Scale
---

# Structured Context Engineering for File-Native Agentic Systems: Evaluating Schema Accuracy, Format Effectiveness, and Multi-File Navigation at Scale
**arXiv**：[2602.05447v1](https://arxiv.org/abs/2602.05447) · [PDF](https://arxiv.org/pdf/2602.05447.pdf)  
**作者**：Damon McMillan  

**一句话要点**：提出结构化上下文工程方法，评估文件原生智能体在SQL生成中的架构、格式与可扩展性

**关键词**：上下文工程, 文件原生智能体, SQL生成, 结构化数据, 模型评估, 可扩展性

## 3 点简述
- 核心问题：LLM智能体在程序化操作中缺乏结构化上下文设计的实证指导
- 方法要点：通过SQL生成代理，系统研究11个模型、4种格式和不同规模模式下的上下文工程
- 实验或效果：发现模型能力主导性能，架构选择需因模型而异，文件原生智能体可扩展至万表规模

## 摘要（原文）

> Large Language Model agents increasingly operate external systems through programmatic interfaces, yet practitioners lack empirical guidance on how to structure the context these agents consume. Using SQL generation as a proxy for programmatic agent operations, we present a systematic study of context engineering for structured data, comprising 9,649 experiments across 11 models, 4 formats (YAML, Markdown, JSON, Token-Oriented Object Notation [TOON]), and schemas ranging from 10 to 10,000 tables.
>   Our findings challenge common assumptions. First, architecture choice is model-dependent: file-based context retrieval improves accuracy for frontier-tier models (Claude, GPT, Gemini; +2.7%, p=0.029) but shows mixed results for open source models (aggregate -7.7%, p<0.001), with deficits varying substantially by model. Second, format does not significantly affect aggregate accuracy (chi-squared=2.45, p=0.484), though individual models, particularly open source, exhibit format-specific sensitivities. Third, model capability is the dominant factor, with a 21 percentage point accuracy gap between frontier and open source tiers that dwarfs any format or architecture effect. Fourth, file-native agents scale to 10,000 tables through domain-partitioned schemas while maintaining high navigation accuracy. Fifth, file size does not predict runtime efficiency: compact formats can consume significantly more tokens at scale due to format-unfamiliar search patterns.
>   These findings provide practitioners with evidence-based guidance for deploying LLM agents on structured systems, demonstrating that architectural decisions should be tailored to model capability rather than assuming universal best practices.

