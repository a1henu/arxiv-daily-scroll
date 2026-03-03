---
layout: default
title: GenDB: The Next Generation of Query Processing -- Synthesized, Not Engineered
---

# GenDB: The Next Generation of Query Processing -- Synthesized, Not Engineered
**arXiv**：[2603.02081v1](https://arxiv.org/abs/2603.02081) · [PDF](https://arxiv.org/pdf/2603.02081.pdf)  
**作者**：Jiale Lao, Immanuel Trummer  

**一句话要点**：提出GenDB系统，利用大语言模型合成查询执行代码以替代传统查询处理引擎。

**关键词**：查询处理, 大语言模型, 代码合成, OLAP, 多代理系统

## 3 点简述
- 传统查询处理引擎难以快速适应新技术和用户需求，且扩展成本高。
- GenDB使用大语言模型为每个查询生成针对特定数据、负载和硬件的执行代码。
- 在OLAP工作负载上，GenDB原型相比DuckDB等先进引擎性能显著提升。

## 摘要（原文）

> Traditional query processing relies on engines that are carefully optimized and engineered by many experts. However, new techniques and user requirements evolve rapidly, and existing systems often cannot keep pace. At the same time, these systems are difficult to extend due to their internal complexity, and developing new systems requires substantial engineering effort and cost. In this paper, we argue that recent advances in Large Language Models (LLMs) are starting to shape the next generation of query processing systems.
>   We propose using LLMs to synthesize execution code for each incoming query, instead of continuously building, extending, and maintaining complex query processing engines. As a proof of concept, we present GenDB, an LLM-powered agentic system that generates instance-optimized and customized query execution code tailored to specific data, workloads, and hardware resources.
>   We implemented an early prototype of GenDB that uses Claude Code Agent as the underlying component in the multi-agent system, and we evaluate it on OLAP workloads. We use queries from the well-known TPC-H benchmark and also construct a new benchmark designed to reduce potential data leakage from LLM training data. We compare GenDB with state-of-the-art query engines, including DuckDB, Umbra, MonetDB, ClickHouse, and PostgreSQL. GenDB achieves significantly better performance than these systems. Finally, we discuss the current limitations of GenDB and outline future extensions and related research challenges.

