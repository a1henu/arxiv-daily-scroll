---
layout: default
title: SPD-RAG: Sub-Agent Per Document Retrieval-Augmented Generation
---

# SPD-RAG: Sub-Agent Per Document Retrieval-Augmented Generation
**arXiv**：[2603.08329v1](https://arxiv.org/abs/2603.08329) · [PDF](https://arxiv.org/pdf/2603.08329.pdf)  
**作者**：Yagiz Can Akay, Muhammed Yusuf Kartal, Esra Alparslan, Faruk Ortakoyluoglu, Arda Akpinar  

**一句话要点**：提出SPD-RAG框架以解决多文档问答中证据覆盖不全和长上下文推理不可靠问题。

**关键词**：检索增强生成, 多文档问答, 分层多代理框架, 长上下文处理, 模块化检索管道

## 3 点简述
- 核心问题：标准RAG在多文档问答中证据覆盖不全，长上下文LLM在大规模输入上推理不可靠。
- 方法要点：采用分层多代理框架，每个文档由专用代理处理，协调器分发任务并聚合部分答案。
- 实验或效果：在LOONG基准测试中，SPD-RAG平均得分58.1，优于Normal RAG和Agentic RAG，API成本仅为全上下文基线的38%。

## 摘要（原文）

> Answering complex, real-world queries often requires synthesizing facts scattered across vast document corpora. In these settings, standard retrieval-augmented generation (RAG) pipelines suffer from incomplete evidence coverage, while long-context large language models (LLMs) struggle to reason reliably over massive inputs. We introduce SPD-RAG, a hierarchical multi-agent framework for exhaustive cross-document question answering that decomposes the problem along the document axis. Each document is processed by a dedicated document-level agent operating only on its own content, enabling focused retrieval, while a coordinator dispatches tasks to relevant agents and aggregates their partial answers. Agent outputs are synthesized by merging partial answers through a token-bounded synthesis layer (which supports recursive map-reduce for massive corpora). This document-level specialization with centralized fusion improves scalability and answer quality in heterogeneous multidocument settings while yielding a modular, extensible retrieval pipeline. On the LOONG benchmark (EMNLP 2024) for long-context multi-document QA, SPD-RAG achieves an Avg Score of 58.1 (GPT-5 evaluation), outperforming Normal RAG (33.0) and Agentic RAG (32.8) while using only 38% of the API cost of a full-context baseline (68.0).

