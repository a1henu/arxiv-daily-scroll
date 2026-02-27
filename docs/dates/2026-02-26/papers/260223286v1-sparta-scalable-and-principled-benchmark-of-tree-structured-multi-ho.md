---
layout: default
title: SPARTA: Scalable and Principled Benchmark of Tree-Structured Multi-hop QA over Text and Tables
---

# SPARTA: Scalable and Principled Benchmark of Tree-Structured Multi-hop QA over Text and Tables
**arXiv**：[2602.23286v1](https://arxiv.org/abs/2602.23286) · [PDF](https://arxiv.org/pdf/2602.23286.pdf)  
**作者**：Sungho Park, Jueun Kim, Wook-Shin Han  

**一句话要点**：提出SPARTA框架以自动生成大规模表格-文本多跳问答基准，提升复杂推理评估能力。

**关键词**：表格-文本问答, 多跳推理, 基准生成, 聚合操作, 跨模态评估

## 3 点简述
- 现有基准规模小、问题浅，缺乏多跳和聚合操作，难以评估复杂推理模型。
- SPARTA通过构建参考事实数据库和合成嵌套查询，自动生成高质量问答对，支持深度多跳和聚合操作。
- 在SPARTA上，当前先进模型性能显著下降，暴露跨模态推理弱点，基准和代码已开源。

## 摘要（原文）

> Real-world Table-Text question answering (QA) tasks require models that can reason across long text and source tables, traversing multiple hops and executing complex operations such as aggregation. Yet existing benchmarks are small, manually curated - and therefore error-prone - and contain shallow questions that seldom demand more than two hops or invoke aggregations, grouping, or other advanced analytical operations expressible in natural-language queries. We present SPARTA, an end-to-end construction framework that automatically generates large-scale Table-Text QA benchmarks with lightweight human validation, requiring only one quarter of the annotation time of HybridQA. The framework first constructs a reference fact database by enriching each source table with grounding tables whose tuples are atomic facts automatically extracted from the accompanying unstructured passages, then synthesizes nested queries whose number of nested predicates matches the desired hop count. To ensure that every SQL statement is executable and that its verbalization yields a fluent, human-sounding question, we propose two novel techniques: provenance-based refinement, which rewrites any syntactically valid query that returns a non-empty result, and realistic-structure enforcement, which confines generation to post-order traversals of the query graph. The resulting pipeline produces thousands of high-fidelity question-answer pairs covering aggregations, grouping, and deep multi-hop reasoning across text and tables. On SPARTA, state-of-the-art models that reach over 70 F1 on HybridQA or over 50 F1 on OTT-QA drop by more than 30 F1 points, exposing fundamental weaknesses in current cross-modal reasoning. Our benchmark, construction code, and baseline models are available at https://github.com/pshlego/SPARTA/tree/main.

