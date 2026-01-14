---
layout: default
title: Reliable Graph-RAG for Codebases: AST-Derived Graphs vs LLM-Extracted Knowledge Graphs
---

# Reliable Graph-RAG for Codebases: AST-Derived Graphs vs LLM-Extracted Knowledge Graphs
**arXiv**：[2601.08773v1](https://arxiv.org/abs/2601.08773) · [PDF](https://arxiv.org/pdf/2601.08773.pdf)  
**作者**：Manideep Reddy Chinthareddy  

**一句话要点**：提出基于AST的确定性知识图谱RAG，以提升代码库中多跳架构推理的可靠性。

**关键词**：检索增强生成, 知识图谱, 代码库分析, 多跳推理, AST解析

## 3 点简述
- 核心问题：向量检索在代码库多跳架构推理中易失效，如控制器到服务链。
- 方法要点：比较向量检索、LLM生成知识图谱和AST派生知识图谱三种检索管道。
- 实验或效果：AST派生图谱在索引成本、覆盖率和答案正确性上优于LLM生成图谱。

## 摘要（原文）

> Retrieval-Augmented Generation for software engineering often relies on vector similarity search, which captures topical similarity but can fail on multi-hop architectural reasoning such as controller to service to repository chains, interface-driven wiring, and inheritance. This paper benchmarks three retrieval pipelines on Java codebases (Shopizer, with additional runs on ThingsBoard and OpenMRS Core): (A) vector-only No-Graph RAG, (B) an LLM-generated knowledge graph RAG (LLM-KB), and (C) a deterministic AST-derived knowledge graph RAG (DKB) built with Tree-sitter and bidirectional traversal.
>   Using 15 architecture and code-tracing queries per repository, we measure indexing time, query latency, corpus coverage, cost, and answer correctness. DKB builds its graph in seconds, while LLM-KB requires much longer graph generation. LLM-KB also shows indexing incompleteness: on Shopizer, 377 files are skipped or missed, reducing embedded chunk coverage and graph size compared to DKB. End-to-end cost is modest for DKB relative to the vector-only baseline but much higher for LLM-KB, especially as repository scale increases. Query latency is similar for No-Graph and DKB, while LLM-KB is slower and more variable. On the Shopizer question suite, DKB achieves the highest correctness, LLM-KB is close behind, and the vector-only baseline performs worst on upstream architectural queries and has the highest hallucination risk. Overall, deterministic AST-derived graphs provide more reliable coverage and multi-hop grounding than LLM-extracted graphs at substantially lower indexing cost.

