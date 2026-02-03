---
layout: default
title: Meta Engine: A Unified Semantic Query Engine on Heterogeneous LLM-Based Query Systems
---

# Meta Engine: A Unified Semantic Query Engine on Heterogeneous LLM-Based Query Systems
**arXiv**：[2602.01701v1](https://arxiv.org/abs/2602.01701) · [PDF](https://arxiv.org/pdf/2602.01701.pdf)  
**作者**：Ruyu Li, Tinghui Zhang, Haodi Ma, Daisy Zhe Wang, Yifan Wang  

**一句话要点**：提出Meta Engine统一语义查询引擎，以解决异构LLM查询系统集成与多模态性能权衡问题。

**关键词**：语义查询, 多模态数据, LLM集成, 查询路由, 异构系统, 性能优化

## 3 点简述
- 核心问题：异构LLM语义查询系统API分散，专用系统与通用系统在多模态查询中存在性能权衡。
- 方法要点：设计包含查询解析、操作生成、路由、适配器和结果聚合的五组件架构，集成异构专用系统。
- 实验或效果：评估中Meta Engine性能优于基线，F1分数在多数情况下提高3-6倍，特定数据集达24倍。

## 摘要（原文）

> With the increasingly use of multi-modal data, semantic query has become more and more demanded in data management systems, which is an important way to access and analyze multi-modal data. As unstructured data, most information of multi-modal data (text, image, video, etc) hides in the semantics, which cannot be accessed by the traditional database queries like SQL.
>   Given the power of Large Language Model (LLM) in understanding semantics and processing natural language, in recent years several LLM-based semantic query systems have been proposed, to support semantic querying over unstructured data. However, this rapid growth has produced a fragmented ecosystem. Applications face significant integration challenges due to (1) disparate APIs of different semantic query systems and (2) a fundamental trade-off between specialization and generality. Many semantic query systems are highly specialized, offering state-of-the-art performance within a single modality but struggling with multi-modal data. Conversely, some "all-in-one" systems handle multiple modalities but often exhibit suboptimal performance compared to their specialized counterparts in specific modalities.
>   This paper introduces Meta Engine, a novel "query system on query systems", designed to resolve those aforementioned challenges. Meta Engine is a unified semantic query engine that integrates heterogeneous, specialized LLM-based query systems. Its architecture comprises five key components: (1) a Natural Language (NL) Query Parser, (2) an Operator Generator, (3) a Query Router, (4) a set of Adapters, and (5) a Result Aggregator. In the evaluation, Meta Engine consistently outperforms all baselines, yielding 3-6x higher F1 in most cases and up to 24x on specific datasets.

