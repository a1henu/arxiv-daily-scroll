---
layout: default
title: CUICurate: A GraphRAG-based Framework for Automated Clinical Concept Curation for NLP applications
---

# CUICurate: A GraphRAG-based Framework for Automated Clinical Concept Curation for NLP applications
**arXiv**：[2602.17949v1](https://arxiv.org/abs/2602.17949) · [PDF](https://arxiv.org/pdf/2602.17949.pdf)  
**作者**：Victoria Blake, Mathew Miller, Jamie Novak, Sze-yuan Ooi, Blanca Gallego  

**一句话要点**：提出CUICurate框架，基于GraphRAG自动化构建UMLS临床概念集以支持NLP应用。

**关键词**：临床概念集构建, 知识图谱检索, 大语言模型过滤, UMLS概念标识符, 自动化NLP管道

## 3 点简述
- 临床NLP中，手动构建UMLS概念集耗时且不一致，现有工具支持不足。
- 方法结合知识图谱检索与LLM过滤分类，自动生成候选概念集。
- 实验显示框架能生成更完整概念集，匹配人工精度，且计算成本低。

## 摘要（原文）

> Background: Clinical named entity recognition tools commonly map free text to Unified Medical Language System (UMLS) Concept Unique Identifiers (CUIs). For many downstream tasks, however, the clinically meaningful unit is not a single CUI but a concept set comprising related synonyms, subtypes, and supertypes. Constructing such concept sets is labour-intensive, inconsistently performed, and poorly supported by existing tools, particularly for NLP pipelines that operate directly on UMLS CUIs. Methods We present CUICurate, a Graph-based retrieval-augmented generation (GraphRAG) framework for automated UMLS concept set curation. A UMLS knowledge graph (KG) was constructed and embedded for semantic retrieval. For each target concept, candidate CUIs were retrieved from the KG, followed by large language model (LLM) filtering and classification steps comparing two LLMs (GPT-5 and GPT-5-mini). The framework was evaluated on five lexically heterogeneous clinical concepts against a manually curated benchmark and gold-standard concept sets. Results Across all concepts, CUICurate produced substantially larger and more complete concept sets than the manual benchmarks whilst matching human precision. Comparisons between the two LLMs found that GPT-5-mini achieved higher recall during filtering, while GPT-5 produced classifications that more closely aligned with clinician judgements. Outputs were stable across repeated runs and computationally inexpensive. Conclusions CUICurate offers a scalable and reproducible approach to support UMLS concept set curation that substantially reduces manual effort. By integrating graph-based retrieval with LLM reasoning, the framework produces focused candidate concept sets that can be adapted to clinical NLP pipelines for different phenotyping and analytic requirements.

