---
layout: default
title: Scaling Text2SQL via LLM-efficient Schema Filtering with Functional Dependency Graph Rerankers
---

# Scaling Text2SQL via LLM-efficient Schema Filtering with Functional Dependency Graph Rerankers
**arXiv**：[2512.16083v1](https://arxiv.org/abs/2512.16083) · [PDF](https://arxiv.org/pdf/2512.16083.pdf)  
**作者**：Thanh Dat Hoang, Thanh Tam Nguyen, Thanh Trung Huynh, Hongzhi Yin, Quoc Viet Hung Nguyen  

**一句话要点**：提出基于功能依赖图重排的LLM高效模式过滤框架，以解决大规模数据库Text2SQL提示过长问题。

**关键词**：Text2SQL, 模式过滤, 功能依赖图, 大语言模型, 提示工程, 数据库查询

## 3 点简述
- 核心问题：现有Text2SQL系统在大型数据库上因模式信息超出LLM上下文限制而失效。
- 方法要点：通过查询感知编码、功能依赖图重排和连通子模式选择，压缩提示并保持结构。
- 实验或效果：在真实数据集上实现高召回率和精度，支持超2.3万列模式，延迟低于1秒。

## 摘要（原文）

> Most modern Text2SQL systems prompt large language models (LLMs) with entire schemas -- mostly column information -- alongside the user's question. While effective on small databases, this approach fails on real-world schemas that exceed LLM context limits, even for commercial models. The recent Spider 2.0 benchmark exemplifies this with hundreds of tables and tens of thousands of columns, where existing systems often break. Current mitigations either rely on costly multi-step prompting pipelines or filter columns by ranking them against user's question independently, ignoring inter-column structure. To scale existing systems, we introduce \toolname, an open-source, LLM-efficient schema filtering framework that compacts Text2SQL prompts by (i) ranking columns with a query-aware LLM encoder enriched with values and metadata, (ii) reranking inter-connected columns via a lightweight graph transformer over functional dependencies, and (iii) selecting a connectivity-preserving sub-schema with a Steiner-tree heuristic. Experiments on real datasets show that \toolname achieves near-perfect recall and higher precision than CodeS, SchemaExP, Qwen rerankers, and embedding retrievers, while maintaining sub-second median latency and scaling to schemas with 23,000+ columns. Our source code is available at https://github.com/thanhdath/grast-sql.

