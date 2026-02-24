---
layout: default
title: KNIGHT: Knowledge Graph-Driven Multiple-Choice Question Generation with Adaptive Hardness Calibration
---

# KNIGHT: Knowledge Graph-Driven Multiple-Choice Question Generation with Adaptive Hardness Calibration
**arXiv**：[2602.20135v1](https://arxiv.org/abs/2602.20135) · [PDF](https://arxiv.org/pdf/2602.20135.pdf)  
**作者**：Mohammad Amanlou, Erfan Shafiee Moghaddam, Yasaman Amou Jafari, Mahdi Noori, Farhan Farsi, Behnam Bahrak  

**一句话要点**：提出KNIGHT框架，基于知识图谱生成多选问题，以高效评估大语言模型系统。

**关键词**：知识图谱, 多选问题生成, 大语言模型评估, 难度校准, 可重用状态, 多跳推理

## 3 点简述
- 核心问题：评估大语言模型系统时，构建专业数据集耗时耗力，成为瓶颈。
- 方法要点：利用知识图谱作为可重用状态，从外部源生成多选问题，支持难度控制和多跳推理。
- 实验或效果：在历史、生物和数学领域生成数据集，评估显示高质量、高效且与基准排名一致。

## 摘要（原文）

> With the rise of large language models (LLMs), they have become instrumental in applications such as Retrieval-Augmented Generation (RAG). Yet evaluating these systems remains bottlenecked by the time and cost of building specialized assessment datasets. We introduce KNIGHT, an LLM-based, knowledge-graph-driven framework for generating multiple-choice question (MCQ) datasets from external sources. KNIGHT constructs a topic-specific knowledge graph, a structured and parsimonious summary of entities and relations, that can be reused to generate instructor-controlled difficulty levels, including multi-hop questions, without repeatedly re-feeding the full source text. This knowledge graph acts as a compressed, reusable state, making question generation a cheap read over the graph. We instantiate KNIGHT on Wikipedia/Wikidata while keeping the framework domain- and ontology-agnostic. As a case study, KNIGHT produces six MCQ datasets in History, Biology, and Mathematics. We evaluate quality on five criteria: fluency, unambiguity (single correct answer), topic relevance, option uniqueness, and answerability given the provided sources (as a proxy for hallucination). Results show that KNIGHT enables token- and cost-efficient generation from a reusable graph representation, achieves high quality across these criteria, and yields model rankings aligned with MMLU-style benchmarks, while supporting topic-specific and difficulty-controlled evaluation.

